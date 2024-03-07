from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    validates,
)


class Base(DeclarativeBase):
    pass


class RoleCategory(Base):
    __tablename__ = "role_categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    uri: Mapped[str] = mapped_column(String(50), unique=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str] = mapped_column(String(2000), default="")

    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey("role_categories.id"))
    parent: Mapped[Optional["RoleCategory"]] = relationship(remote_side=[id])
    children: Mapped[List["RoleCategory"]] = relationship()


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    uri: Mapped[str] = mapped_column(String(50), unique=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    role_category_id: Mapped[RoleCategory] = mapped_column(
        ForeignKey("role_categories.id")
    )
