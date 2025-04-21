from fastapi import FastAPI
from interfaces.api.routes import routes 

app = FastAPI()

app.include_router(routes)