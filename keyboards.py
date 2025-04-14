# File: keyboards.py
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Define callback data prefixes for better organization
CALLBACK_PREFIX_CLASS = "class_"

def create_class_keyboard(classes: list[str]) -> InlineKeyboardMarkup:
    """Creates an inline keyboard with buttons for each class."""
    builder = InlineKeyboardBuilder()
    for class_name in classes:
        builder.button(text=class_name, callback_data=f"{CALLBACK_PREFIX_CLASS}{class_name}")
    builder.adjust(3)  # Adjust layout: 3 buttons per row
    return builder.as_markup()

