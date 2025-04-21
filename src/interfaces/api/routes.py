from fastapi import APIRouter
from .api_router import api_router 
from .account_router import account_router

routes = APIRouter()
routes.include_router(account_router)
routes.include_router(api_router)