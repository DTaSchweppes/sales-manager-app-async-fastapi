from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Base
import operations
from config import SessionLocal, engine
from models.schemas import ItemSchema, VendorSchema, BrandSchema, MainCategorySchema, SecondCategorySchema, Response

router = APIRouter()


async def get_db():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all) # в async подходе
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()


@router.post('/items',status_code=201)
async def create_item_service(request: ItemSchema, db: AsyncSession = Depends(get_db)):
    result = await operations.create_item(db, item=request)
    return Response(status="Ok",
                    code="201",
                    message="Item created successfully",
                    result=result).dict(exclude_none=True)


@router.post('/main_categories',status_code=201)
async def create_main_category_service(request: MainCategorySchema, db: AsyncSession = Depends(get_db)):
    result = await operations.create_main_category(db, main_category=request)
    if result == False:
        raise HTTPException(status_code=409, detail="Item already exists")
    return Response(status="Ok",
                    code="201",
                    message="Main category created successfully",
                    result=result.name).dict(exclude_none=True)


@router.post('/second_categories',status_code=201)
async def create_second_category_service(request: SecondCategorySchema, db: AsyncSession = Depends(get_db)):
    result = await operations.create_second_category(db, second_category=request)
    return Response(status="Ok",
                    code="201",
                    message="Second category created successfully",
                    result=result).dict(exclude_none=True)


@router.post('/brands',status_code=201)
async def create_brand_service(request: BrandSchema, db: AsyncSession = Depends(get_db)):
    result = await operations.create_brand(db, brand=request)
    return Response(status="Ok",
                    code="201",
                    message="Brand created successfully",
                    result=result).dict(exclude_none=True)


@router.post('/vendors',status_code=201)
async def create_vendor_service(request: VendorSchema, db: AsyncSession = Depends(get_db)):
    result = await operations.create_vendor(db, vendor=request)
    return Response(status="Ok",
                    code="201",
                    message="Vendor created successfully",
                    result=result).dict(exclude_none=True)


@router.get('/items')
async def get_item_service(id: int, db: AsyncSession = Depends(get_db)):
    result = await operations.get_item_by_id(db, id)
    return Response(status="Ok",
                    code="200",
                    message="Get item",
                    result=result).dict(exclude_none=True)


@router.delete("/items")
async def delete_item_service(id: int, db: AsyncSession = Depends(get_db)):
    result = await operations.delete_item_by_id(db, id)
    return Response(status="Ok",
                    code="200",
                    message="Get item",
                    result=result).dict(exclude_none=True)


@router.patch("/items")
async def update_item_service(id: int, name, img, db: AsyncSession = Depends(get_db)):
    """
    Тут для наглядности без Валидации запроса
    :param id: id обновляемого продукта
    :param name: наименование обновляемого продукта
    :param img: изображение обновляемого продукта
    :param db:
    :return:
    """
    result = await operations.update_item(db, id, name, img)
    return Response(status="Ok",
                    code="200",
                    message="Get item",
                    result=result).dict(exclude_none=True)

@router.get('/main_categories')
async def get_name_main_category(name:str, db: AsyncSession = Depends(get_db)):
    result = await operations.get_main_category_by_name(db, name)
    return Response(status="Ok",
                    code="200",
                    message="Get item",
                    result=result.name).dict(exclude_none=True)
