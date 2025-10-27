from pydantic import BaseModel, ConfigDict, Field


class Body(BaseModel):
    marketing_partner_key: str = Field(serialization_alias="MarketingPartnerKey")
    method_name: str = Field(serialization_alias="Method")
    device_id: str = Field(serialization_alias="DeviceId")
    session_token: str = Field(serialization_alias="SessionToken")

    model_config = ConfigDict(serialize_by_alias=True)


class Head(BaseModel):
    head: Body = Field(..., serialization_alias="Head")
    
    model_config = ConfigDict(serialize_by_alias=True)


class Body(BaseModel):
    request: Head

