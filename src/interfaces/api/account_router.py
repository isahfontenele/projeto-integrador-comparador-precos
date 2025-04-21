from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.account_model import Account
from requests.accounts.create_account_request import CreateAccountRequest
from responses.accounts.create_account_response import CreateAccountResponse
from repositories.account_repository import create_account
from services.account_service import hash_password
from database import SessionLocal

account_router = APIRouter(prefix="/accounts", tags=["Accounts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@account_router.post("/", response_model= CreateAccountResponse)
def register(body: CreateAccountRequest, db: Session = Depends(get_db)):
    hash = hash_password(body.password)
    new_account = create_account(db, body, hash)
    return new_account
    
     

    
    