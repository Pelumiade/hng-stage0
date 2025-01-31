# HNG Stage 0 Backend Task

This is a simple API that returns basic information including an email address, current datetime, and GitHub repository URL.

## Setup Instructions
1. Clone this repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `uvicorn main:app --reload`

## API Documentation
Endpoint: GET /
Response format:
{
    "email": "pelumifola@gmail.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/Pelumiade/hng-stage0"
}