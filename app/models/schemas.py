from typing import Optional, TypeVar, Generic
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class ItemSchema(BaseModel):
    code: Optional[str] = Field(..., description="Item product code")
    name: Optional[str] = Field(..., description="Item name")
    image: Optional[str] = None
    category: Optional[int] = Field(..., description="id second category")
    vendor: Optional[int] = Field(..., description="id vendor item")
    brand: Optional[int] = Field(..., description="id brand item")


class BrandSchema(BaseModel):
    name: Optional[str] = Field(...)


class VendorSchema(BaseModel):
    name: Optional[str] = Field(...)


class SecondCategorySchema(BaseModel):
    name: Optional[str] = Field(...)
    main_category_id: Optional[int] = Field(...)


class MainCategorySchema(BaseModel):
    name: Optional[str] = Field(...)


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
