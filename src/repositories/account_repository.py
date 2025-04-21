from models.account_model import Account
from requests.accounts.create_account_request import CreateAccountRequest
from sqlalchemy.orm import Session

def create_account(db: Session, account: CreateAccountRequest, hash: str) -> Account:
    account = Account(name=account.name, email=account.email, hashed_password=hash)
    db.add(account)
    db.commit()
    db.refresh(account)
    return account