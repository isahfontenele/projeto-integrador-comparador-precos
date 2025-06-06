from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from interfaces.api.routes import routes 
from exceptions.exceptions import AppError
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.exception_handler(AppError)
async def handle_app_error(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.message},
    )

@app.exception_handler(Exception)
async def handle_generic_exception(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"Erro interno inesperado:": exc.message},
    )

app.include_router(routes)

