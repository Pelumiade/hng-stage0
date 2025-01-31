from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import pytz

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/")
async def get_info():
    return {
        "email": "pelumifola@gmail.com",
        "current_datetime": datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/Pelumiade/hng-stage0"
    }