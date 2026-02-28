"""Main menu keyboards."""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_main_menu() -> InlineKeyboardMarkup:
    """Create main navigation menu keyboard."""
    builder = InlineKeyboardBuilder()
    
    builder.row(
        InlineKeyboardButton(
            text="📝 Text",
            callback_data="menu:text"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="😊 Emoji",
            callback_data="menu:emoji"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="🔘 Buttons",
            callback_data="menu:buttons"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="📋 Templates",
            callback_data="menu:templates"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="🛠 Builder",
            callback_data="menu:builder"
        )
    )
    
    return builder.as_markup()


def get_back_button(callback_data: str = "menu:back") -> InlineKeyboardMarkup:
    """Create back button keyboard."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="« Назад в меню", callback_data=callback_data)]
        ]
    )


def get_demo_navigation(
    prev_callback: str | None = None,
    next_callback: str | None = None,
    back_to_menu: bool = True,
) -> InlineKeyboardMarkup:
    """Create navigation keyboard for demo sequences."""
    builder = InlineKeyboardBuilder()
    
    nav_buttons = []
    if prev_callback:
        nav_buttons.append(
            InlineKeyboardButton(text="« Назад", callback_data=prev_callback)
        )
    if next_callback:
        nav_buttons.append(
            InlineKeyboardButton(text="Далее »", callback_data=next_callback)
        )
    
    if nav_buttons:
        builder.row(*nav_buttons)
    
    if back_to_menu:
        builder.row(
            InlineKeyboardButton(text="« В меню", callback_data="menu:back")
        )
    
    return builder.as_markup()


def get_template_selection_menu() -> InlineKeyboardMarkup:
    """Create template selection menu."""
    builder = InlineKeyboardBuilder()
    
    builder.row(
        InlineKeyboardButton(
            text="📢 Объявление",
            callback_data="template:announcement"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="🔥 Промо",
            callback_data="template:promo"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="🚀 Обновление",
            callback_data="template:update"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="⚠️ Предупреждение",
            callback_data="template:warning"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="✅ Успех",
            callback_data="template:success"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="« Назад в меню",
            callback_data="menu:back"
        )
    )
    
    return builder.as_markup()
"""Main menu keyboards."""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_main_menu() -> InlineKeyboardMarkup:
    """Create main navigation menu keyboard."""
    builder = InlineKeyboardBuilder()
    
    builder.row(
        InlineKeyboardButton(
            text="📝 Text",
            callback_data="menu:text"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="😊 Emoji",
            callback_data="menu:emoji"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="🔘 Buttons",
            callback_data="menu:buttons"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="📋 Templates",
            callback_data="menu:templates"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="🛠 Builder",
            callback_data="menu:builder"
        )
    )
    
    return builder.as_markup()


def get_back_button(callback_data: str = "menu:back") -> InlineKeyboardMarkup:
    """Create back button keyboard."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="« Назад в меню", callback_data=callback_data)]
        ]
    )


def get_demo_navigation(
    prev_callback: str | None = None,
    next_callback: str | None = None,
    back_to_menu: bool = True,
) -> InlineKeyboardMarkup:
    """Create navigation keyboard for demo sequences."""
    builder = InlineKeyboardBuilder()
    
    nav_buttons = []
    if prev_callback:
        nav_buttons.append(
            InlineKeyboardButton(text="« Назад", callback_data=prev_callback)
        )
    if next_callback:
        nav_buttons.append(
            InlineKeyboardButton(text="Далее »", callback_data=next_callback)
        )
    
    if nav_buttons:
        builder.row(*nav_buttons)
    
    if back_to_menu:
        builder.row(
            InlineKeyboardButton(text="« В меню", callback_data="menu:back")
        )
    
    return builder.as_markup()


def get_template_selection_menu() -> InlineKeyboardMarkup:
    """Create template selection menu."""
    builder = InlineKeyboardBuilder()
    
    builder.row(
        InlineKeyboardButton(
            text="📢 Объявление",
            callback_data="template:announcement"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="🔥 Промо",
            callback_data="template:promo"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="🚀 Обновление",
            callback_data="template:update"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="⚠️ Предупреждение",
            callback_data="template:warning"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="✅ Успех",
            callback_data="template:success"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="« Назад в меню",
            callback_data="menu:back"
        )
    )
    
    return builder.as_markup()
