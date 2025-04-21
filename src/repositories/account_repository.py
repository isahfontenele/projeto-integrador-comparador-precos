from models.account_model import Account
from requests.accounts.create_account_request import CreateAccountRequest
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from exceptions.exceptions import DuplicateEmailError, DatabaseError

def create_account(db: Session, account: CreateAccountRequest, hash: str) -> Account:
    existing = db.query(Account).filter(Account.email == account.email).first()

    if existing:
        raise DuplicateEmailError(account.email)
    
    try:
        account = Account(name=account.name, email=account.email, hashed_password=hash)
        db.add(account)
        db.commit()
        db.refresh(account)
        return account
    except SQLAlchemyError:
        db.rollback()
        raise DatabaseError()