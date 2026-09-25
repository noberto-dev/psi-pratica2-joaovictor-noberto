from typing import List

from sqlalchemy import ForeignKey, Column, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase

from database import Base


class Autor(Base):
    def __init__(self):
        super().__init__()
        __tablename__ = "Autor"
        id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
        nome : Mapped[String] = mapped_column(nullable=False)
        pais : Mapped[String] = mapped_column(nullable=True)
        livros : Mapped[list["Livro"]] = relationship(back_populates="Autor", nullable=False)

class Livro(Base):
    def __init__(self):
        super().__init__()
        __tablename__ = "Livro"
        id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
        titulo : Mapped[String] = mapped_column(nullable=False)
        ano : Mapped[int] = mapped_column(nullable=False)
        autor_id : Mapped[int] =  mapped_column(ForeignKey("Autor.id"), nullable=False)
        autor : Mapped["Autor"] = relationship(back_populates="Livros")


class Base(DeclarativeBase):
    pass


