# AI Development Guide

## Arquitectura

El backend está desarrollado con **FastAPI** siguiendo los principios de **Clean Architecture**.

Todo nuevo módulo debe seguir exactamente la misma estructura existente. No crear nuevas carpetas ni modificar la arquitectura.

---

# Flujo de un endpoint CRUD

La implementación de un endpoint sigue el siguiente orden:

```
Modelo SQLAlchemy
        ↓
Entidad de Dominio
        ↓
Interfaz Repository
        ↓
Repository Implementation
        ↓
Use Case
        ↓
DTO
        ↓
Route
        ↓
Dependency Injection
        ↓
main.py (registro del router)
```

---

# Ejemplo: Crear Usuario

## 1. Modelo (Persistence Layer)

Archivo

```
app/infrastructure/db/models/usuario.py
```

Responsabilidad

- Representa la tabla de PostgreSQL.
- Utiliza SQLModel.
- Define relaciones y Foreign Keys.

Ejemplo

```python
class Usuario(SQLModel, table=True):
```

Este modelo **únicamente interactúa con la base de datos**.

Nunca debe contener lógica de negocio.

---

## 2. Entidad de Dominio

Archivo

```
app/domain/entities/usuario.py
```

Responsabilidad

Representar el objeto de dominio.

No depende de SQLAlchemy.

Ejemplo

```python
class Usuario:
```

Las entidades solamente contienen atributos del negocio.

---

## 3. Repository Interface

Archivo

```
app/domain/interfaces/usuario_repository.py
```

Responsabilidad

Define los métodos que necesita la aplicación.

Ejemplo

```python
class UsuarioRepository(ABC):

    async def create(...)
```

Nunca contiene consultas SQL.

---

## 4. Repository Implementation

Archivo

```
app/infrastructure/repositories/usuario_repository_impl.py
```

Responsabilidad

Implementar la interfaz utilizando SQLModel.

Aquí se realizan:

- select
- insert
- update
- delete

Este archivo convierte entre

```
SQLModel
        ↓
Entidad
```

y viceversa.

---

## 5. Use Case

Archivo

```
app/use_cases/usuario/crear_usuario_usecase.py
```

Responsabilidad

Contiene toda la lógica de negocio.

Ejemplo

```python
hashed_password = bcrypt.hash(clave)
```

El caso de uso nunca conoce SQLModel.

Solo trabaja con entidades e interfaces.

---

## 6. DTO

Archivo

```
app/api/dtos/usuario_dto.py
```

Responsabilidad

Representar la entrada y salida de la API.

Ejemplo

```python
UsuarioCreateDto
UsuarioReadDto
```

---

## 7. Route

Archivo

```
app/api/routes/usuario_routes.py
```

Responsabilidad

Recibir la petición HTTP.

Debe:

- recibir DTO
- inyectar UseCase
- retornar DTO

Nunca implementar lógica de negocio.

---

## 8. Dependency Injection

Todo UseCase debe registrarse en

```
app/dependencies/
```

Las rutas obtienen los casos de uso mediante

```python
Depends(...)
```

---

## 9. Registro del Router

Registrar el router en

```
main.py
```

Si el router no está registrado, el endpoint no aparecerá en Swagger.

---

# Reglas

✔ Mantener Clean Architecture.

✔ No acceder a SQLModel desde UseCases.

✔ No acceder a SQLModel desde Routes.

✔ Toda lógica pertenece al UseCase.

✔ El Repository únicamente accede a la BD.

✔ Las entidades no conocen SQLAlchemy.

✔ Los DTO únicamente representan entrada y salida.

✔ Reutilizar el patrón existente.

✔ No modificar la estructura del proyecto.

---

# Patrón para crear un nuevo módulo

Cuando se implemente un nuevo CRUD crear exactamente:

```
models/
    nuevo.py

entities/
    nuevo.py

interfaces/
    nuevo_repository.py

repositories/
    nuevo_repository_impl.py

use_cases/nuevo/
    crear.py
    listar.py
    actualizar.py
    eliminar.py

api/dtos/
    nuevo_dto.py

api/routes/
    nuevo_routes.py

dependencies/
    nuevo_dependencies.py
```

---

# Convención

Antes de implementar un nuevo módulo, analizar uno existente (Usuarios, Vehículos, Clientes, etc.) y replicar exactamente su estructura.

No crear patrones nuevos.

# Instrucciones para el agente

Antes de generar código:

1. Analiza el módulo CRUD de usuarios existente.
2. Identifica los nombres de carpetas y convenciones.
3. Reutiliza exactamente el mismo patrón.
4. No inventes nuevas arquitecturas.
5. Si falta contexto, solicita únicamente los archivos relacionados con el módulo.
6. Genera únicamente los archivos necesarios para el nuevo CRUD.
7. Mantén consistencia con el estilo del proyecto.