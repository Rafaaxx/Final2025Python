"""Product schema for request/response validation."""
from typing import Optional, List, TYPE_CHECKING
from pydantic import Field

from schemas.base_schema import BaseSchema
from schemas.category_schema import CategoryMinimalSchema 
from schemas.review_schema import ReviewNestedSchema 

if TYPE_CHECKING:
    from schemas.category_schema import CategorySchema
    from schemas.order_detail_schema import OrderDetailSchema


class ProductSchema(BaseSchema):
    """Schema for Product entity with validations."""

    name: str = Field(..., min_length=1, max_length=200, description="Product name (required)")
    
    # 🎯 CORRECCIÓN CLAVE: Usar Optional[] para permitir NULL de la base de datos
    # Si antes andaba, es porque estos campos eran permisivos o ya venían pre-convertidos
    price: Optional[float] = Field(None, gt=0, description="Product price (must be greater than 0, or None)")
    stock: int = Field(default=0, ge=0, description="Product stock quantity (must be >= 0)")

    category_id: Optional[int] = Field(None, description="Category ID reference (or None)")

    category: Optional[CategoryMinimalSchema] = None 
    
    # Solución de recursión: sigue usando ReviewNestedSchema
    reviews: Optional[List[ReviewNestedSchema]] = []
    
    order_details: Optional[List['OrderDetailSchema']] = []