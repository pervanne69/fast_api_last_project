import datetimefrom fastapi_users import schemasfrom pydantic import field_validatorclass SiteRead(schemas.BaseModel):    id: int    name: str    address: strclass SiteCreate(schemas.BaseModel):    name: str    address: str    @field_validator("name")    @classmethod    def validate_name(cls, value: str):        if not (4 <= len(value) <= 10 and isinstance(value, str)):            raise ValueError("Name of site is invalid")        return value    @field_validator("address")    @classmethod    def validate_address(cls, value: str):        if not (10 <= len(value) and isinstance(value, str)):            raise ValueError("Address of site is invalid")        return valueclass SiteDelete(schemas.BaseModel):    name: str    @field_validator("name")    @classmethod    def validate_name(cls, value: str):        if not (4 <= len(value) <= 10 and isinstance(value, str)):            raise ValueError("Name of site is invalid")        return value