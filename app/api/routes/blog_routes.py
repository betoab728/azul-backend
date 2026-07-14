from fastapi import APIRouter, Depends
from app.api.auth import get_current_user
from app.use_cases.blog.crear_blog_usecase import CrearBlogUseCase
from app.api.dtos.blog_dto import BlogCreateDto, BlogReadDto
from app.dependencies_folder.blog_dependencies import get_crear_blog_use_case


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
