#This file is part of the "Sistema de Gestión de Residuos" project.


from fastapi import FastAPI

from app.api.routes import rol_routes
from app.api.routes.usuario_routes import router as usuario_router
from app.api.routes.clasificacion_routes import router as clasificacion_router
from app.api.routes.tipo_residuo_routes import router as tipo_residuo_router
from app.api.routes.auth_routes import router as auth_router
from app.api.routes.unidad_medida_routes import router as unidad_medida_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Sistema de Gestión de Residuos")
app.include_router(auth_router) 
app.include_router(rol_routes.router)
app.include_router(usuario_router)
app.include_router(clasificacion_router)
app.include_router(tipo_residuo_router)
app.include_router(unidad_medida_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
