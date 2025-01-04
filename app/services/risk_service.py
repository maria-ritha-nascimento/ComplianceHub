from sqlalchemy.orm import Session
from app.models.risk import Risk
from app.schemas.risk_schema import RiskCreate

def create_risk(db: Session, risk: RiskCreate):
    db_risk = Risk(title=risk.title, description=risk.description)
    db.add(db_risk)
    db.commit()
    db.refresh(db_risk)
    return db_risk

def get_risk_by_id(db: Session, risk_id: int):
    return db.query(Risk).filter(Risk.id == risk_id).first()
