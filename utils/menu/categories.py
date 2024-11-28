from typing import Union

from aiogram import types

from logging_settings import logger
from main.models import  Category
from sqlalchemy.orm import sessionmaker
from main.database import engine
Session = sessionmaker(bind=engine)
session = Session()
async def get_category(name: str) -> Union[dict, None]:
    """Get category data by name"""
    try:
        query = Category.select().where(Category.c.name == name)
        row = session.execute(query).fetchall()
        for rows in row:
            print(rows.name)
            return dict(rows) if row else None
    except Exception as e:
        error_text = f"Error retrieving user with ID {name}: {e}"
        logger.error(error_text)
        return None
