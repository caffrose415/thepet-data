from fastapi import FastAPI
from app import routes

app = FastAPI()

app.include_router(routes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)