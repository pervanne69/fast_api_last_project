import datetimefrom fastapi_users import schemasclass TicketRead(schemas.BaseModel):    id: int    type: str    event_id: int