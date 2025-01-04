from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.risk_schema import RiskCreate, RiskResponse
from app.services.risk_service import create_risk, get_risk_by_id
from app.config import get_db
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

router = APIRouter()

@router.post("/", response_model=RiskResponse)
async def create_risk_endpoint(risk: RiskCreate, db: Session = Depends(get_db)):
    return create_risk(db, risk)

@router.get("/{risk_id}", response_model=RiskResponse)
async def get_risk_endpoint(risk_id: int, db: Session = Depends(get_db)):
    db_risk = get_risk_by_id(db, risk_id)
    if not db_risk:
        raise HTTPException(status_code=404, detail="Risk not found")
    return db_risk

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Decodifique o token e valide
    pass

@router.post("/", response_model=RiskResponse)
async def create_risk_endpoint(risk: RiskCreate, db: Session = Depends(get_db), token: str = Depends(get_current_user)):
    return create_risk(db, risk)
