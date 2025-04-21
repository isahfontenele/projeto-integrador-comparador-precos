from database import Base, engine
from models.account_model import Account

Base.metadata.create_all(bind=engine)