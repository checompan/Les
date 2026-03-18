from aiogram import Router, types
from aiogram.filters import Command
from config import ADMIN_IDS
from db_utils import create_walk, list_walks
from excel_export import export_registrations
from db_utils import get_registrations

router = Router()

@router.message(Command("create_walk"))
async def create_walk_cmd(message:types.Message):
    if message.from_user.id not in ADMIN_IDS:
        return
    parts = message.text.split("|")
    if len(parts)<5:
        await message.answer("Формат: /create_walk |название|дата|место|макс")
        return
    _,title,date,location,maxp = parts
    await create_walk(title,date,location,int(maxp))
    await message.answer("Прогулка создана")

@router.message(Command("walks"))
async def list_cmd(message:types.Message):
    if message.from_user.id not in ADMIN_IDS:
        return
    walks = await list_walks()
    txt="Прогулки:\n"
    for w in walks:
        txt+=f"{w.id} {w.title} {w.date}\n"
    await message.answer(txt)

@router.message(Command("export"))
async def export_cmd(message:types.Message):
    if message.from_user.id not in ADMIN_IDS:
        return
    parts=message.text.split()
    if len(parts)<2:
        await message.answer("/export WALK_ID")
        return
    walk_id=int(parts[1])
    regs=await get_registrations(walk_id)
    rows=[]
    for r in regs:
        rows.append({
            "walk_id":r.walk_id,
            "user_id":r.user_id,
            "participants":r.participants,
            "status":r.status
        })
    file="export.xlsx"
    export_registrations(rows,file)
    await message.answer_document(types.FSInputFile(file))