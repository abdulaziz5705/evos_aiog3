from aiogram.fsm.state import StatesGroup, State

class RegisterState(StatesGroup):
    language = State()
    fullname = State()
    phone_number = State()
