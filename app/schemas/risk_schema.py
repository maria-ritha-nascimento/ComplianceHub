from pydantic import BaseModel

class RiskBase(BaseModel):
    title: str
    description: str

class RiskCreate(RiskBase):
    pass

class RiskResponse(RiskBase):
    id: int

    class Config:
        orm_mode = True
