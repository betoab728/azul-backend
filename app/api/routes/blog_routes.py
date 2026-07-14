from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.api.auth import get_current_user
from app.use_cases.blog.crear_blog_usecase import CrearBlogUseCase
from app.use_cases.blog.listar_blogs_usecase import ListarBlogsUseCase
from app.use_cases.blog.actualizar_estado_blog_usecase import ActualizarEstadoBlogUseCase
from app.api.dtos.blog_dto import BlogCreateDto, BlogReadDto, BlogUpdateEstadoDto
from app.dependencies_folder.blog_dependencies import get_crear_blog_use_case, get_listar_blogs_use_case, get_actualizar_estado_blog_use_case


router = APIRouter(
    prefix="/blog",
    tags=["Blog"],
    dependencies=[Depends(get_current_user)]  # 🔒 protegiendo todo este router
)


@router.post("", response_model=BlogReadDto)
async def crear_blog(
    blog_in: BlogCreateDto,
    use_case: CrearBlogUseCase = Depends(get_crear_blog_use_case),
):
    blog = await use_case.execute(
        blog_in.titulo,
        blog_in.contenido,
        blog_in.resumen,
        blog_in.imagen_portada,
        blog_in.autor,
    )
    return BlogReadDto(**blog.__dict__)


@router.get("", response_model=List[BlogReadDto])
async def listar_blogs(
    use_case: ListarBlogsUseCase = Depends(get_listar_blogs_use_case),
):
    blogs = await use_case.execute()
    return [BlogReadDto(**b.__dict__) for b in blogs]


@router.patch("/{id}/estado", response_model=BlogReadDto)
async def actualizar_estado_blog(
    id: int,
    estado_in: BlogUpdateEstadoDto,
    use_case: ActualizarEstadoBlogUseCase = Depends(get_actualizar_estado_blog_use_case),
):
    try:
        blog = await use_case.execute(id, estado_in.estado)
        return BlogReadDto(**blog.__dict__)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
