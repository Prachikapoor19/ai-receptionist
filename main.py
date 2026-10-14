from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Namaste! AI Receptionist chal reha h"}

@app.get("/services")
def services():
    return[
        {"name": "General Checkup", "price": 300},
        {"name": "Dental Cleaning", "price": 800}
    ]
def timing():
    return[
        {"open": "10am"},
        {"close": "7pm"}
    ]