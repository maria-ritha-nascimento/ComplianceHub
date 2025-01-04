from fastapi import APIRouter, HTTPException
from app.schemas.risk_schema import RiskCreate, RiskResponse

router = APIRouter()

@router.post("/", response_model=RiskResponse)
async def create_risk(risk: RiskCreate):
    # Aqui você conectaria ao banco de dados para criar o risco
    return {"id": 1, "title": risk.title, "description": risk.description}

@router.get("/{risk_id}", response_model=RiskResponse)
async def get_risk(risk_id: int):
    # Exemplo de resposta
    if risk_id == 1:
        return {"id": 1, "title": "Compliance Issue", "description": "Description of the issue"}
    raise HTTPException(status_code=404, detail="Risk not found")
