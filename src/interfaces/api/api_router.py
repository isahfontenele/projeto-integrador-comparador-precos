from fastapi import APIRouter
from fastapi import Depends
from services.auth_service import get_current_user
from models.account_model import Account


api_router = APIRouter()

@api_router.get("/")
def read_root(current_user: Account = Depends(get_current_user)):
    return {
        "health": "OK",
        "user": {
            "id": current_user.id,
            "email": current_user.email
        }
    }