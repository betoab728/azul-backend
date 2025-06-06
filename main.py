#This file is part of the "Sistema de Gestión de Residuos" project.


from fastapi import FastAPI

from app.api.routes import rol_routes
from app.api.routes.usuario_routes import router as usuario_router

app = FastAPI(title="Sistema de Gestión de Residuos")
app.include_router(rol_routes.router)
app.include_router(usuario_router)

