from fastapi_users import schemasclass AchievementRead(schemas.BaseModel):    id: int    name: str    description: str    picture_name: strclass AchievementCreate(schemas.BaseModel):    name: str    description: str    email: str    password: strclass AchievementDelete(schemas.BaseModel):    id: int    name: str