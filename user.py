from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from db_utils import get_user_by_tg, create_user, list_walks, register_user

router = Router()

contact_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Отправить телефон",request_contact=True)]],
    resize_keyboard=True
)

@router.message(Command("start"))
async def start(message:types.Message):
    u = await get_user_by_tg(message.from_user.id)
    if u:
        await message.answer("Вы уже зарегистрированы.")
    else:
        await message.answer("Отправьте номер телефона",reply_markup=contact_kb)

@router.message(lambda m:m.contact is not None)
async def save_contact(message:types.Message):
    phone=message.contact.phone_number
    name=message.from_user.full_name
    await create_user(message.from_user.id,name,phone)
    await message.answer("Регистрация завершена")

@router.message(Command("walks"))
async def walks(message:types.Message):
    walks=await list_walks()
    txt="Доступные прогулки:\n"
    for w in walks:
        txt+=f"/join_{w.id} {w.title} {w.date}\n"
    await message.answer(txt)

@router.message(lambda m:m.text.startswith("/join_"))
async def join(message:types.Message):
    walk_id=int(message.text.split("_")[1])
    await register_user(walk_id,message.from_user.id,"1 adult")
    await message.answer("Вы записаны на прогулку")