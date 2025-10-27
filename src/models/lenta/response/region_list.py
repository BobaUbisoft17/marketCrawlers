from pydantic import BaseModel, Field
from datetime import datetime


class RegionList(BaseModel):
    headers: 'Headers' = Field(validation_alias="Head")
    body: 'Body' = Field(validation_alias="Body")


class Headers(BaseModel):
    create_date: datetime = Field(validation_alias="Created")
    method: str = Field(validation_alias="Method")
    status: str = Field(validation_alias="Status")
    server_name: str = Field(validation_alias="ServerName")


class Body(BaseModel):
    cities: list['City'] = Field(validation_alias="Regions")


class City(BaseModel):
    id: int
    name_rus: str = Field(validation_alias="name")
    name_eng: str = Field(validation_alias="slug")
    # Возможно стоит перегнать в числовые типы
    latitude: str = Field(validation_alias="centerLat")
    longitude: str = Field(validation_alias="centerLng")
    
