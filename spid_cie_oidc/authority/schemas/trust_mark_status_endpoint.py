
from typing import Optional

from pydantic import BaseModel, HttpUrl, constr, validator


class TrustMarkRequest(BaseModel):
    trust_mark : Optional[constr(regex=r"^[a-zA-Z\_\-0-9]+\.[a-zA-Z\_\-0-9]+\.[a-zA-Z\_\-0-9]+")] # noqa: F722
    sub : Optional[HttpUrl]
    id : Optional[HttpUrl]

    @validator("id", pre=True, always=True)
    def validate_id(cls, id_value, values):
        if (not values.get("trust_mark") and (not values.get("sub") or not id_value)):
            raise ValueError("sub an id must be present if not trust_mark")


class TrustMarkResponse(BaseModel):
    active : bool
