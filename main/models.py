import sqlalchemy
from sqlalchemy import DateTime, func, ForeignKey

from main.constants import UserStatus
from main.database import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("full_name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("language", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("chat_id", sqlalchemy.BigInteger, unique=True, nullable=False),
    sqlalchemy.Column("phone_number", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("status", sqlalchemy.Enum(UserStatus), default=UserStatus.active, nullable=False),
    sqlalchemy.Column('created_at', DateTime(timezone=True), server_default=func.now(), nullable=False),
    sqlalchemy.Column('updated_at', DateTime(timezone=True), onupdate=func.now(), nullable=False)
)

Category = sqlalchemy.Table(
    "categories",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=True),
)



Products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("category_id", sqlalchemy.Integer,ForeignKey("categories.id"), nullable=False),

)