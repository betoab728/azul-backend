from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.use_cases.blog.listar_blogs_publicados_usecase import ListarBlogsPublicadosUseCase
from app.use_cases.blog.obtener_blog_por_slug_usecase import ObtenerBlogPorSlugUseCase
from app.api.dtos.blog_publico_dto import BlogPublicoResumenDto, BlogPublicoDetalleDto
from app.dependencies_folder.blog_dependencies import (
    get_listar_blogs_publicados_use_case,
    get_obtener_blog_por_slug_use_case,
)


router = APIRouter(
    prefix="/blog/publicados",
    tags=["Blog Publico"],
)


@router.get("", response_model=List[BlogPublicoResumenDto])
async def listar_blogs_publicados(
    use_case: ListarBlogsPublicadosUseCase = Depends(get_listar_blogs_publicados_use_case),
):
    blogs = await use_case.execute()
    return [BlogPublicoResumenDto(**b.__dict__) for b in blogs]


@router.get("/{slug}", response_model=BlogPublicoDetalleDto)
async def obtener_blog_por_slug(
    slug: str,
    use_case: ObtenerBlogPorSlugUseCase = Depends(get_obtener_blog_por_slug_use_case),
):
    blog = await use_case.execute(slug)
    if not blog:
        raise HTTPException(status_code=404, detail="Articulo no encontrado")
    return BlogPublicoDetalleDto(**blog.__dict__)
