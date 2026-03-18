from sqlalchemy import select
from database import SessionLocal
from models import User, Child, Walk, Registration

async def get_user_by_tg(tg_id):
    async with SessionLocal() as session:
        res = await session.execute(select(User).where(User.telegram_id==tg_id))
        return res.scalar()

async def create_user(tg_id, name, phone):
    async with SessionLocal() as session:
        user = User(telegram_id=tg_id, name=name, phone=phone)
        session.add(user)
        await session.commit()

async def add_child(user_id, name, age):
    async with SessionLocal() as session:
        c = Child(user_id=user_id, name=name, age=age)
        session.add(c)
        await session.commit()

async def create_walk(title,date,location,max_people):
    async with SessionLocal() as session:
        w = Walk(title=title,date=date,location=location,max_people=max_people)
        session.add(w)
        await session.commit()

async def list_walks():
    async with SessionLocal() as session:
        res = await session.execute(select(Walk))
        return res.scalars().all()

async def register_user(walk_id,user_id,participants,status="confirmed"):
    async with SessionLocal() as session:
        r = Registration(walk_id=walk_id,user_id=user_id,participants=participants,status=status)
        session.add(r)
        await session.commit()

async def get_registrations(walk_id):
    async with SessionLocal() as session:
        res = await session.execute(select(Registration).where(Registration.walk_id==walk_id))
        return res.scalars().all()