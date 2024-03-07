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

    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey("role_categories.id"))
    parent: Mapped[Optional["RoleCategory"]] = relationship(remote_side=[id])
    children: Mapped[List["RoleCategory"]] = relationship()

    def __repr__(self) -> str:
        return f"<RoleCategory[{self.id}] {self.name}>"


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    uri: Mapped[str] = mapped_column(String(50), unique=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str] = mapped_column(String(2000), default="")

    role_category_id: Mapped[str] = mapped_column(ForeignKey("role_categories.id"))
    role_category: Mapped[RoleCategory] = relationship()

    def __repr__(self) -> str:
        return f"<Role[{self.id}] {self.name}>"


class Delegation(Base):
    __tablename__ = "delegations"

    id: Mapped[int] = mapped_column(primary_key=True)
