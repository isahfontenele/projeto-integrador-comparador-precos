from pydantic import BaseModel, EmailStr, Field

class CreateAccountRequest(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    password: str = Field(..., min_length=8)