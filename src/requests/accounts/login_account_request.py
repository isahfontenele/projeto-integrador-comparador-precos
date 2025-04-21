from pydantic import BaseModel, EmailStr, Field

class LoginAccountRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)