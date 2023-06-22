from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import Item, MainCategory, SecondCategory, Vendor, Brand
from app.models.schemas import ItemSchema, MainCategorySchema, SecondCategorySchema, VendorSchema, BrandSchema


async def get_item_by_id(db: AsyncSession, item_id: int):
    """
    Поиск Item/продукта по id
    :param db:
    :param item_id:
    :return:
    """
    results = await db.execute(select(Item).filter(Item.id == item_id))  # async execute/select
    item_by_id = results.scalars().first()  # async scalars
    return item_by_id


async def get_second_category_by_name(db: AsyncSession, categ_name: str):
    """
    Поиск категории по наименованию
    :param db:
    :param item_id:
    :return:
    """
    results = await db.execute(select(SecondCategory).filter(SecondCategory.name == categ_name))  # async execute/select
    category_by_name = results.scalars().first()  # async scalars
    return category_by_name


async def get_main_category_by_name(db: AsyncSession, categ_name: str):
    """
    Поиск категории по наименованию
    :param db:
    :param item_id:
    :return:
    """
    results = await db.execute(select(MainCategory).filter(MainCategory.name == categ_name))  # async execute/select
    category_by_name = results.scalars().first()  # async scalars
    return category_by_name


async def create_item(db: AsyncSession, item: ItemSchema):
    """
    Создание продукта
    :param db:
    :param item: модель продукта (с валидацией)
    :return: объект созданного продукта со всеми данными
    """
    _item = Item(code=item.code, name=item.name, image=item.image, category=item.category, vendor=item.vendor,
                 brand=item.brand)
    db.add(_item)
    await db.commit()
    await db.refresh(_item)
    return _item


async def remove_item(db: AsyncSession, item_id: int):  # удаление продукта
    _item = get_item_by_id(db=db, item_id=item_id)
    await db.delete(_item)
    await db.commit()


async def update_item(db: AsyncSession, item_id: int, name: str, image: str):
    '''
    Функция обновления Item(продукта в приложении)
    :param db:
    :param item_id:
    :param name:
    :param image:
    :return: возвращает сам item с которым взаимодествовала
    '''
    _item = await get_item_by_id(db=db, item_id=item_id)  # поиск по id Item для обновления

    _item.name = name
    _item.image = image

    await db.commit()
    await db.refresh(_item)
    return _item


async def create_main_category(db: AsyncSession, main_category: MainCategorySchema):
    """Создание Главной категории (в модели более подробно описано)"""
    results = await db.execute(select(MainCategory).filter(MainCategory.name == main_category.name))
    category_by_name = results.scalars().first()
    if category_by_name:
        raise HTTPException(status_code=409, detail="Элемент уже существует")
    _main_category = MainCategory(name=main_category.name)
    db.add(_main_category)
    await db.commit()
    await db.refresh(_main_category)
    return _main_category


async def create_second_category(db: AsyncSession, second_category: SecondCategorySchema):
    """Создание дочерней категории (в модели более подробно описано)"""
    _second_category = SecondCategory(name=second_category.name, main_categ_id=second_category.main_category_id)
    db.add(_second_category)
    await db.commit()
    await db.refresh(_second_category)
    return _second_category


async def create_vendor(db: AsyncSession, vendor: VendorSchema):
    """Создание поставщика (в модели более подробно описано)"""
    _vendor = Vendor(name=vendor.name)
    db.add(_vendor)
    await db.commit()
    await db.refresh(_vendor)
    return _vendor


async def create_brand(db: AsyncSession, brand: BrandSchema):
    """Создание бренда (в модели более подробно описано)"""
    _brand = Brand(name=brand.name)
    db.add(_brand)
    await db.commit()
    await db.refresh(_brand)
    return _brand


async def delete_item_by_id(db: AsyncSession, item_id: int):
    """Удаление продукта по ID"""
    _item = await get_item_by_id(db=db, item_id=item_id)
    await db.delete(_item)
    await db.commit()
    return _item
