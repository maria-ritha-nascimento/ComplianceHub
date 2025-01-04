from fastapi import FastAPI
from app.config import Base, engine

app = FastAPI(
    title="ComplianceHub API",
    description="API para gestão de riscos e conformidade",
    version="1.0.0"
)

# Rotas
from app.routes.risk_routes import router as risk_router

app.include_router(risk_router, prefix="/risks", tags=["Risks"])

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)