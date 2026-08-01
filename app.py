from fastapi import FastAPI

# FastAPI অ্যাপ তৈরি
app = FastAPI(title="My Sports API")

# হোম রুট (ওয়েবসাইটের মূল পাতা)
@app.get("/")
def home():
    return {
        "status": "Success",
        "message": "Welcome to Sports Live Score API!"
    }

# লাইভ স্কোর দেখার এন্ডপয়েন্ট (Endpoint)
@app.get("/api/v1/sports/live")
def get_live_scores():
    return {
        "cricket": {
            "match": "Bangladesh vs India",
            "score": "185/4 (18.2 Overs)",
            "status": "Live"
        },
        "football": {
            "match": "Real Madrid vs Barcelona",
            "score": "2 - 1",
            "status": "75th Minute"
        }
    }