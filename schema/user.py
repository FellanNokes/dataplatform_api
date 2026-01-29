from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    password: str
    isEnabled: bool

class UserSchemaResponse(BaseModel):
    username: str