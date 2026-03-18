Telegram Walk Bot

Functions
- User registration with phone
- Walk creation (admin)
- Join walk
- Participant storage
- Excel export
- SQLite database

Commands

User:
/start
/walks

Admin:
/create_walk |title|date|location|max_people
/walks
/export WALK_ID

Run

pip install -r requirements.txt
cp .env.example .env
python init_db.py
python bot.py