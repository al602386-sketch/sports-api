import time
from functools import lru_cache
from fastapi import FastAPI

# FastAPI অ্যাপ ইনিশিয়ালাইজ করা
app = FastAPI(
    title="Sports Pulse Live API",
    description="Real-time multi-sport scores and updates API with high-performance caching.",
    version="1.1.0"
)

# ---------------------------------------------------------
# ক্যাশিং ফাংশন (৫ সেকেন্ড পর পর ডাটা রিফ্রেশ হবে)
# ---------------------------------------------------------
@lru_cache(maxsize=128)
def fetch_sports_data_cached(sport_name: str, time_key: int):
    # বিভিন্ন খেলার ডেমো ডাটা (এখানে আপনার আসল স্ক্র্যাপিং বা থার্ড-পার্টি API লজিক বসবে)
    sports_database = {
        "cricket": {
            "sport": "Cricket",
            "matches": [
                {"match_id": "c1", "team_1": "Bangladesh", "team_2": "India", "score": "165/4 (18.2 Overs)", "status": "Live"}
            ]
        },
        "football": {
            "sport": "Football",
            "matches": [
                {"match_id": "f1", "team_1": "Brazil", "team_2": "Argentina", "score": "2 - 1", "status": "78'"}
            ]
        },
        "tennis": {
            "sport": "Tennis",
            "matches": [
                {"match_id": "t1", "player_1": "Djokovic", "player_2": "Alcaraz", "score": "6-4, 3-2", "status": "Set 2"}
            ]
        },
        "basketball": {
            "sport": "Basketball",
            "matches": [
                {"match_id": "b1", "team_1": "Lakers", "team_2": "Warriors", "score": "102 - 98", "status": "Q4 02:15"}
            ]
        },
        "badminton": {
            "sport": "Badminton",
            "matches": [
                {"match_id": "bm1", "player_1": "Axelsen", "player_2": "Loh Kean Yew", "score": "21-18, 15-12", "status": "Game 2"}
            ]
        }
    }
    
    return {
        "status": "success",
        "data": sports_database.get(sport_name, {"error": "Sport not found"})
    }


# ---------------------------------------------------------
# API Endpoints (সকল খেলার রুট)
# ---------------------------------------------------------

# ১. হোম এন্ডপয়েন্ট (সব লিস্ট দেখাবে)
@app.get("/")
def home():
    return {
        "message": "Welcome to Sports Pulse Live API!",
        "available_endpoints": {
            "cricket": "/cricket/live",
            "football": "/football/live",
            "tennis": "/tennis/live",
            "basketball": "/basketball/live",
            "badminton": "/badminton/live",
            "all_sports": "/sports/all"
        }
    }

# ২. ক্রিকেট লাইভ
@app.get("/cricket/live")
def get_cricket():
    time_key = int(time.time() / 5)
    return fetch_sports_data_cached("cricket", time_key)

# ৩. ফুটবল লাইভ
@app.get("/football/live")
def get_football():
    time_key = int(time.time() / 5)
    return fetch_sports_data_cached("football", time_key)

# ৪. টেনিস লাইভ
@app.get("/tennis/live")
def get_tennis():
    time_key = int(time.time() / 5)
    return fetch_sports_data_cached("tennis", time_key)

# ৫. বাস্কেটবল লাইভ
@app.get("/basketball/live")
def get_basketball():
    time_key = int(time.time() / 5)
    return fetch_sports_data_cached("basketball", time_key)

# ৬. ব্যাডমিন্টন লাইভ
@app.get("/badminton/live")
def get_badminton():
    time_key = int(time.time() / 5)
    return fetch_sports_data_cached("badminton", time_key)

# ৭. সব খেলা এক সাথে পাওয়ার জন্য অল-ইন-ওয়ান এন্ডপয়েন্ট
@app.get("/sports/all")
def get_all_sports():
    time_key = int(time.time() / 5)
    return {
        "status": "success",
        "all_live_matches": [
            fetch_sports_data_cached("cricket", time_key)["data"],
            fetch_sports_data_cached("football", time_key)["data"],
            fetch_sports_data_cached("tennis", time_key)["data"],
            fetch_sports_data_cached("basketball", time_key)["data"],
            fetch_sports_data_cached("badminton", time_key)["data"]
        ]
    }
    }
