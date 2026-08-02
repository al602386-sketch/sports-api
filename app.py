from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/cricket/live")
def get_cricket_live():
    return {
        "status": "success",
        "sport": "cricket",
        "data": [
            {
                "match": "Bangladesh vs Sri Lanka",
                "score": "168/4 (17.5 Overs)",
                "status": "Live"
            }
        ]
    }

@app.get("/football/live")
def get_football_live():
    return {
        "status": "success",
        "sport": "football",
        "data": [
            {
                "match": "Real Madrid vs Barcelona",
                "score": "2 - 1",
                "status": "75th Minute"
            }
        ]
    }