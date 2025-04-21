from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.account_model import Account
from requests.accounts.create_account_request import CreateAccountRequest
from requests.accounts.login_account_request import LoginAccountRequest 
from responses.accounts.create_account_response import CreateAccountResponse
from repositories.account_repository import create_account
from services.auth_service import hash_password, verify_password, create_access_token
from database import SessionLocal

account_router = APIRouter(prefix="/accounts", tags=["Accounts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@account_router.post("/register", response_model= CreateAccountResponse)
def register(body: CreateAccountRequest, db: Session = Depends(get_db)):
    hash = hash_password(body.password)
    return create_account(db, body, hash)

@account_router.post("/login")
def login(body: LoginAccountRequest, db: Session = Depends(get_db)):
    user: Account = db.query(Account).filter(Account.email == body.email).first()
    if not user or not verify_password(body.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
    
    
     

    
    