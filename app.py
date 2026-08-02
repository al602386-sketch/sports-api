import time
from fastapi import FastAPI

app = FastAPI()


# ডামি ক্যাশ ডাটা ফাংশন (আপনার প্রয়োজন অনুযায়ী পরিবর্তন করতে পারেন)
def fetch_sports_data_cached(sport_name, time_key):
    return {
        "status": "success",
        "sport": sport_name,
        "data": [
            {
                "match": f"Sample {sport_name.capitalize()} Match",
                "status": "Live",
            }
        ],
    }


# ১. ক্রিকেট লাইভ
@app.get("/cricket/live")
def get_cricket():
    time_key = int(time.time() / 5)
    return fetch_sports_data_cached("cricket", time_key)


# ২. ফুটবল লাইভ
@app.get("/football/live")
def get_football():
    time_key = int(time.time() / 5)
    return fetch_sports_data_cached("football", time_key)


# ৩. টেনিস লাইভ
@app.get("/tennis/live")
def get_tennis():
    time_key = int(time.time() / 5)
    return fetch_sports_data_cached("tennis", time_key)


# ৪. বাস্কেটবল লাইভ
@app.get("/basketball/live")
def get_basketball():
    time_key = int(time.time() / 5)
    return fetch_sports_data_cached("basketball", time_key)


# ৫. ব্যাডমিন্টন লাইভ
@app.get("/badminton/live")
def get_badminton():
    time_key = int(time.time() / 5)
    return fetch_sports_data_cached("badminton", time_key)


# ৬. সব খেলা একসাথে পাওয়ার জন্য অল-ইন-ওয়ান এন্ডপয়েন্ট
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
            fetch_sports_data_cached("badminton", time_key)["data"],
        ],
    }
