"""Start handler - /start, /menu, /help commands."""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.formatting import Text, Bold, as_list

from keyboards.menu import get_main_menu


router = Router(name="start")


WELCOME_TEXT = """
🎨 Добро пожаловать в Post Styling Demo Bot!

Этот бот демонстрирует возможности визуального оформления постов в Telegram:

• Форматирование текста
• Кастомные эмодзи
• Цветные кнопки
• Иконки на кнопках
• Готовые шаблоны постов
• Интерактивный конструктор

Выберите раздел в меню ниже:
"""

HELP_TEXT = """
📚 Справка по командам:

/start — Приветствие и главное меню
/menu — Показать главное меню
/text_demo — Демо форматирования текста
/post_demo — Готовые шаблоны постов
/emoji_demo — Демо эмодзи (Unicode vs Custom)
/buttons_demo — Демо стилей кнопок
/builder — Интерактивный конструктор постов
/help — Эта справка

━━━━━━━━━━━━━━━━━━━━━━

💡 Подсказки:

• Используйте кнопки меню для навигации
• В каждом разделе есть кнопка «Назад»
• Конструктор позволяет собрать пост пошагово

━━━━━━━━━━━━━━━━━━━━━━

⚙️ Технические детали:

Бот использует aiogram 3.25.0 с поддержкой:
• CustomEmoji для кастомных эмодзи
• Button styles (primary/success/danger)
• icon_custom_emoji_id для иконок кнопок
• Fallback механизмы при недоступности функций
"""


@router.message(Command("start"))
async def cmd_start(message: Message) -> None:
    """Handle /start command."""
    await message.answer(
        WELCOME_TEXT,
        reply_markup=get_main_menu()
    )


@router.message(Command("menu"))
async def cmd_menu(message: Message) -> None:
    """Handle /menu command."""
    await message.answer(
        "📋 Главное меню\n\nВыберите раздел:",
        reply_markup=get_main_menu()
    )


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    """Handle /help command."""
    await message.answer(HELP_TEXT)


@router.callback_query(F.data == "menu:back")
async def callback_back_to_menu(callback: CallbackQuery) -> None:
    """Handle back to menu callback."""
    await callback.message.edit_text(
        "📋 Главное меню\n\nВыберите раздел:",
        reply_markup=get_main_menu()
    )
    await callback.answer()


@router.callback_query(F.data == "menu:text")
async def callback_menu_text(callback: CallbackQuery) -> None:
    """Redirect to text demo."""
    await callback.message.answer(
        "📝 Для демонстрации форматирования текста используйте команду /text_demo"
    )
    await callback.answer()


@router.callback_query(F.data == "menu:emoji")
async def callback_menu_emoji(callback: CallbackQuery) -> None:
    """Redirect to emoji demo."""
    await callback.message.answer(
        "😊 Для демонстрации эмодзи используйте команду /emoji_demo"
    )
    await callback.answer()


@router.callback_query(F.data == "menu:buttons")
async def callback_menu_buttons(callback: CallbackQuery) -> None:
    """Redirect to buttons demo."""
    await callback.message.answer(
        "🔘 Для демонстрации кнопок используйте команду /buttons_demo"
    )
    await callback.answer()


@router.callback_query(F.data == "menu:templates")
async def callback_menu_templates(callback: CallbackQuery) -> None:
    """Redirect to post templates."""
    await callback.message.answer(
        "📋 Для демонстрации шаблонов используйте команду /post_demo"
    )
    await callback.answer()


@router.callback_query(F.data == "menu:builder")
async def callback_menu_builder(callback: CallbackQuery) -> None:
    """Redirect to builder."""
    await callback.message.answer(
        "🛠 Для запуска конструктора используйте команду /builder"
    )
    await callback.answer()
