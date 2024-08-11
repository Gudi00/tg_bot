from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    tg_user_first_name: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    user_first_name: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    tg_user_second_name: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    user_second_name: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    phone_number: Mapped[int] = mapped_column(nullable=True, default=None)
    extended_information: Mapped[str] = mapped_column(String(120), nullable=True, default=None)
    time: Mapped[str] = mapped_column(String(30), nullable=True, default=None)
    ban_information: Mapped[int] = mapped_column(default=1)


class Category(Base):
    __tablename__ = 'categories'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    progress: Mapped[int] = mapped_column()


# class Item(Base):
#     __tablename__ = 'items'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(25))
#     description: Mapped[str] = mapped_column(String(120))
#     price: Mapped[int] = mapped_column()
#     category: Mapped[int] = mapped_column(ForeignKey('categories.id'))

class something_new(Base):
    __tablename__ = 'something_new'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    fact: Mapped[str] = mapped_column(String(1000))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
