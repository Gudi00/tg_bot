from models import async_session
# from app.database.models import Category, Item
from models import User, something_new
from sqlalchemy import select


async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def save_something_new(tg_id, fact):
    async with async_session() as session:
        session.add(something_new(tg_id=tg_id, fact=fact))
        await session.commit()


async def save_user(tg_id, tg_user_first_name,
                    user_first_name, tg_user_last_name,
                    user_last_name, phone_number,
                    extended_information, time):
    async with async_session() as session:
        session.add(User())
        await session.commit()

# async def get_categories():
#     async with async_session() as session:
#         return await session.scalars(select(Category))
#
#
# async def get_category_item(category_id):
#     async with async_session() as session:
#         return await session.scalars(select(Item).where(Item.category == category_id))
#
#
# async def get_item(item_id):
#     async with async_session() as session:
#         return await session.scalar(select(Item).where(Item.id == item_id))
