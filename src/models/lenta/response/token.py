from pydantic import BaseModel, Field


class Token(BaseModel):
    head: 'Head' = Field(validation_alias="Head")
    body: 'Body' = Field(validation_alias="Body")


class Head(BaseModel):
    method: str = Field(validation_alias="Method")
    status: str = Field(validation_alias="Status")
    session_token: str = Field(validation_alias="SessionToken")
    server_name: str = Field(validation_alias="ServerName")


class Body(BaseModel):
    session_token: str = Field(validation_alias="SessionToken")
