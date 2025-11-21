from fastapi import FastAPI, HTTPException, Query, Depends
from pydantic import BaseModel, validator
from datetime import datetime
import re
import difflib
from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# --- Baza danych ---
engine = create_engine("sqlite:///animals.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class AnimalDB(Base):
    __tablename__ = "animals"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Walidacja danych ---
class Animal(BaseModel):
    name: str

    @validator("name")
    def check_name(cls, v):
        if len(v) < 2:
            raise ValueError("za krótkie")
        if len(v) > 30:
            raise ValueError("za długie")
        if v.endswith(" "):
            raise ValueError("kończy się spacją")
        if not re.fullmatch(r"[A-Za-z\-]+", v):
            raise ValueError("niedozwolone znaki")
        return v

# --- FastAPI ---
app = FastAPI()

@app.get("/")
def list_animals(sort: str | None = None, frm: str | None = Query(None, alias="from"), to: str | None = None, db: Session = Depends(get_db)):
    q = db.query(AnimalDB)

    if frm:
        q = q.filter(func.date(AnimalDB.created_at) >= frm)
    if to:
        q = q.filter(func.date(AnimalDB.created_at) <= to)

    if sort:
        if sort == "name":
            q = q.order_by(AnimalDB.name.asc())
        elif sort == "-name":
            q = q.order_by(AnimalDB.name.desc())
        else:
            raise HTTPException(400, "InvalidSortParameter")

    animals = q.all()
    return animals

@app.get("/animals/{id}")
def get_animal(id: int, db: Session = Depends(get_db)):
    animal = db.query(AnimalDB).filter_by(id=id).first()
    if not animal:
        raise HTTPException(404, "AnimalNotFound")
    return animal

@app.post("/animals")
def create_animal(data: Animal, db: Session = Depends(get_db)):
    exists = db.query(AnimalDB).filter(func.lower(AnimalDB.name) == data.name.lower()).first()
    if exists:
        raise HTTPException(400, "DuplicateName")

    new_animal = AnimalDB(name=data.name)
    db.add(new_animal)
    db.commit()
    db.refresh(new_animal)
    return new_animal

@app.put("/animals/{id}")
def update_animal(id: int, data: Animal, db: Session = Depends(get_db)):
    animal = db.query(AnimalDB).filter_by(id=id).first()
    if not animal:
        raise HTTPException(404, "AnimalNotFound")

    exists = db.query(AnimalDB).filter(func.lower(AnimalDB.name) == data.name.lower(), AnimalDB.id != id).first()
    if exists:
        raise HTTPException(400, "DuplicateName")

    animal.name = data.name
    db.commit()
    db.refresh(animal)
    return animal

@app.delete("/animals/{id}")
def delete_animal(id: int, db: Session = Depends(get_db)):
    animal = db.query(AnimalDB).filter_by(id=id).first()
    if not animal:
        raise HTTPException(404, "AnimalNotFound")

    db.delete(animal)
    db.commit()
    return {"message": "deleted"}

@app.get("/animals/search")
def search_animals(name: str, db: Session = Depends(get_db)):
    animals = db.query(AnimalDB).all()

    # dokładne dopasowanie
    sub_results = []
    for a in animals:
        if name.lower() in a.name.lower():
            sub_results.append(a)

    # dopasowanie przybliżone (fuzzy)
    fuzzy_results = []
    for a in animals:
        similarity = difflib.SequenceMatcher(None, name.lower(), a.name.lower()).ratio()
        if similarity > 0.6:
            fuzzy_results.append(a)

    # łączenie wyników i usuwanie duplikatów
    combined_results = {}
    for a in sub_results:
        combined_results[a.id] = a
    for a in fuzzy_results:
        combined_results[a.id] = a

    final_results = []
    for a_id in combined_results:
        final_results.append(combined_results[a_id])

    if not final_results:
        raise HTTPException(404, "SearchNotFound")

    return final_results
