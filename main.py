#This file is part of the "Sistema de Gestión de Residuos" project.
from fastapi import FastAPI

from app.api.routes import rol_routes
from app.api.routes.usuario_routes import router as usuario_router
from app.api.routes.clasificacion_routes import router as clasificacion_router
from app.api.routes.tipo_residuo_routes import router as tipo_residuo_router
from app.api.routes.auth_routes import router as auth_router
from app.api.routes.unidad_medida_routes import router as unidad_medida_router
from app.api.routes.registro_residuo_routes import router as registro_residuo_router
from app.api.routes.generador_residuo_routes import router as generador_residuo_router
from app.api.routes.ubigeo_routes import router as ubigeo_router
from app.api.routes.embarcacion_routes import router as embarcacion_router
from app.api.routes.tipo_embarcacion_routes import router as tipo_embarcacion_router
from app.api.routes.solicitud_cotizacion_routes import router as solicitud_cotizacion_router
from app.api.routes.estado_solicitud_routes import router as estado_solicitud_router
from app.api.routes.puerto_routes import router as puerto_router
from app.api.routes.detalle_solicitud_routes import router as detalle_solicitud_router
from app.api.routes.cotizacion_routes import router as cotizacion_router
from app.api.routes.files_routes import router as files_router
from app.api.routes.tipo_vehiculo_routes import router as tipo_vehiculo_router
from app.api.routes.vehiculo_routes import router as vehiculo_router
from app.api.routes.orden_traslado_routes import router as orden_traslado_router
from app.api.routes.trazabilidad_routes import router as trazabilidad_router
from app.api.routes.estado_orden_routes import router as estado_orden_router
from app.api.routes.historial_orden_routes import router as historial_orden_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Sistema de Gestión de Residuos")


origins = [
    "https://azulsostenible.es",
    "http://localhost:4200",                 # desarrollo local
    "https://www.azulsostenible.es",
    "https://azul-gestion-residuos.netlify.app"  # producción en Netlify, sin la barra al final
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # <- usar la lista de orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ubigeo_router)
app.include_router(auth_router) 
app.include_router(rol_routes.router)
app.include_router(usuario_router)
app.include_router(clasificacion_router)
app.include_router(tipo_residuo_router)
app.include_router(unidad_medida_router)
app.include_router(registro_residuo_router)
app.include_router(generador_residuo_router)
app.include_router(embarcacion_router)
app.include_router(tipo_embarcacion_router)
app.include_router(solicitud_cotizacion_router)
app.include_router(estado_solicitud_router)
app.include_router(puerto_router)
app.include_router(detalle_solicitud_router)
app.include_router(cotizacion_router)
app.include_router(files_router)
app.include_router(tipo_vehiculo_router)
app.include_router(vehiculo_router)
app.include_router(orden_traslado_router)
app.include_router(trazabilidad_router)
app.include_router(estado_orden_router)
app.include_router(historial_orden_router)




@app.get("/")
def root():
    return {"message": "API del Sistema de Gestión de Residuos funcionando correctamente"}



