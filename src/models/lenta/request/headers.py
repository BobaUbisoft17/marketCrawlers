from pydantic import BaseModel, ConfigDict, Field


class Headers(BaseModel):
    content_type: str = Field(..., serialization_alias="Content-Type")
    # user_agent: str = Field(..., serialization_alias="User-Agent")

    model_config = ConfigDict(serialize_by_alias=True)

