# File: handlers.py
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode
import keyboards
import data


# Create a router for these handlers
schedule_router = Router()

@schedule_router.message(Command("start", "help", "помощь", "расписание", "старт"))
async def handle_start(message: Message) -> None:
    """Handles /start and /help commands, showing the class selection keyboard."""
    available_classes = data.get_classes()

    await message.answer(
        "<b>🏫 Выберите ваш класс:</b>", parse_mode="HTML",
        reply_markup=keyboards.create_class_keyboard(available_classes)
    )

@schedule_router.message(Command("timetable", "звонок", "звонки", "расписаниезвонков"))
async def handle_timetable(message: Message) -> None:
   """Handles /timetable command, showing the class selection keyboard."""
   await message.answer_photo(photo="https://dl.dropboxusercontent.com/scl/fi/1ojes57pfj12z6kcskqcg/48dLu9DTZUk.jpeg?rlkey=ola2fwdsyyx5yrzlyc2qvl93u&st=zoyt55ow&dl=0",
                                          parse_mode="HTML",
        caption="<b>🕒 Расписание звонков в школе:</b>\n\n"
    )

        
    
@schedule_router.callback_query(F.data.startswith(keyboards.CALLBACK_PREFIX_CLASS))
async def process_class_selection(callback: CallbackQuery) -> None:
    """Handles the selection of a class from the inline keyboard."""
    try:
        class_name = callback.data.split(keyboards.CALLBACK_PREFIX_CLASS)[1]
    except IndexError:
        pass

    schedule_data = data.get_schedule_for_class(class_name)

    if not schedule_data:
        await callback.answer(
            "⛔️ Расписание для этого класса пока недоступно!",
            show_alert=True
        )
        return

    schedule_text = data.format_schedule_text(class_name, schedule_data)
    available_classes = data.get_classes() # Get classes again for the keyboard

    try:
        await callback.message.edit_text(
            text=schedule_text,
            reply_markup=keyboards.create_class_keyboard(available_classes),
            parse_mode=ParseMode.HTML
        )
    except Exception as e:
        # Log the error in a real application
        print(f"Error editing message: {e}")
        # Try sending a new message if editing fails (e.g., message too old)
        await callback.message.answer(
            text=schedule_text,
            reply_markup=keyboards.create_class_keyboard(available_classes),
            parse_mode=ParseMode.HTML
        )

    await callback.answer() # Acknowledge the callback query
