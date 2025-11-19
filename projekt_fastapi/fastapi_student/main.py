from fastapi import FastAPI
from pydantic import BaseModel

class Game(BaseModel):
    title: str
    genre: str
    year: int

app = FastAPI()

games = [
    {"id": 1, "title": "Minecraft", "genre": "Sandbox", "year": 2011},
    {"id": 2, "title": "The Witcher 3", "genre": "RPG", "year": 2015},
    {"id": 3, "title": "Cyberpunk 2077", "genre": "RPG", "year": 2020},
    {"id": 4, "title": "Valorant", "genre": "FPS", "year": 2020},
    {"id": 5, "title": "ARK Survival Ascended", "genre": "MMOG", "year": 2023}
]

@app.get("/")
def get_games():
    return games

@app.get("/games/{game_id}")
def get_game(game_id: int):
    for game in games:
        if game["id"] == game_id:
            return game

@app.post("/games")
def create_game(game: Game):
    new_id = max([g["id"] for g in games]) + 1 if games else 1
    game_data = game.dict()
    game_data["id"] = new_id
    games.append(game_data)
    return game_data

@app.put("/games/{game_id}")
def update_game(game_id: int, game: Game):
    for index, existing_game in enumerate(games):
        if existing_game["id"] == game_id:
            updated = game.dict()
            updated["id"] = game_id
            games[index] = updated
            return updated

@app.delete("/games/{game_id}")
def delete_game(game_id: int):
    for index, game in enumerate(games):
        if game["id"] == game_id:
            removed = games.pop(index)
            return removed
