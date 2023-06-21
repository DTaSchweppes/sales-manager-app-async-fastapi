from sqlalchemy import Column, Integer, String, ForeignKey
from app.config import Base
from sqlalchemy.orm import relationship, mapped_column


class Brand(Base):
    """
    модель Бренда (у каждого товара/продукта обязательна!)
    """
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    item = relationship("Item", back_populates="brand_rlshp")


class Vendor(Base):
    """
    наименование поставщика (у каждого товара/продукта обязательно!)
    """
    __tablename__ = 'vendors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    item = relationship("Item", back_populates="vendor_rlshp")


class MainCategory(Base):
    """
    Главный/1ый раздел в иерархии (Сантехника/Труба) (Сантехника - главный)
    """
    __tablename__ = "main_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    main_category = relationship("SecondCategory", back_populates="main_categ")  #


class SecondCategory(Base):
    """
    Дочерний раздел в иерархии (Сантехника/Труба) (Труба - дочерний)
    """
    __tablename__ = "second_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    main_categ_id = mapped_column(Integer, ForeignKey('main_categories.id'))

    item = relationship("Item", back_populates="second_category")
    main_categ = relationship("MainCategory", back_populates="main_category")  #


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String)
    name = Column(String)
    image = Column(String)
    category = mapped_column(Integer, ForeignKey('second_categories.id'))
    vendor = mapped_column(Integer, ForeignKey('vendors.id'))
    brand = mapped_column(Integer, ForeignKey('brands.id'))

    second_category = relationship("SecondCategory", back_populates="item")
    vendor_rlshp = relationship("Vendor", back_populates="item")
    brand_rlshp = relationship("Brand", back_populates="item")
