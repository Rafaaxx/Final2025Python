from pydantic import Field

from schemas.base_schema import BaseSchema

# No necesitamos importar ProductSchema aquí para el nested schema

# 🌟 NUEVO ESQUEMA PARA ANIDAMIENTO 🌟
class ReviewNestedSchema(BaseSchema):
    """Product review schema for use within other schemas (e.g., Product)"""

    rating: float = Field(
        ...,
        ge=1.0,
        le=5.0,
        description="Rating from 1 to 5 stars (required)"
    )

    comment: Optional[str] = Field(
        None,
        min_length=10,
        max_length=1000,
        description="Review comment (optional, 10-1000 characters)"
    )
    # Excluimos product_id y product para no mostrar IDs ni causar recursión
    # Solo mostramos el contenido de la reseña.


if TYPE_CHECKING:
    from schemas.product_schema import ProductSchema


class ReviewSchema(BaseSchema):
    """Product review schema with validation (para endpoints CRUD)"""

    # ... (El resto de tus campos originales) ...
    rating: float = Field(...) 
    comment: Optional[str] = Field(...)
    product_id: int = Field(...)
    
    product: Optional['ProductSchema'] = None # ESTE ES NECESARIO PARA EL ENDPOINT DE REVIEW, PERO CAUSA EL CICLO