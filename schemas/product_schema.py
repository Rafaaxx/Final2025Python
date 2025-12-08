# En schemas/product_schema.py
from typing import Optional, List, TYPE_CHECKING
from pydantic import Field

from schemas.base_schema import BaseSchema
from schemas.category_schema import CategoryMinimalSchema 
# 🌟 Importa el esquema anidado que acabas de crear
from schemas.review_schema import ReviewNestedSchema 

if TYPE_CHECKING:
    from schemas.category_schema import CategorySchema
    from schemas.order_detail_schema import OrderDetailSchema
    # NOTA: Ya no necesitas importar ReviewSchema completo si solo usas el Nested en este contexto


class ProductSchema(BaseSchema):
    """Schema for Product entity with validations."""

    name: str = Field(..., min_length=1, max_length=200, description="Product name (required)")
    # ... otros campos ...
    
    category: Optional[CategoryMinimalSchema] = None
    
    # 🎯 ¡EL CAMBIO CLAVE ESTÁ AQUÍ!
    # Usar el esquema simplificado (ReviewNestedSchema)
    reviews: Optional[List[ReviewNestedSchema]] = []
    
    order_details: Optional[List['OrderDetailSchema']] = []