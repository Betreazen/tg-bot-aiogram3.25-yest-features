"""Builder step keyboards for interactive post constructor."""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class BuilderKeyboards:
    """Keyboards for the interactive post builder."""
    
    @staticmethod
    def template_selection() -> InlineKeyboardMarkup:
        """Step 1: Select template type."""
        builder = InlineKeyboardBuilder()
        
        builder.row(
            InlineKeyboardButton(
                text="📢 Объявление",
                callback_data="builder:template:announcement"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="🔥 Промо",
                callback_data="builder:template:promo"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="🚀 Обновление",
                callback_data="builder:template:update"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="⚠️ Предупреждение",
                callback_data="builder:template:warning"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="✅ Успех",
                callback_data="builder:template:success"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="❌ Отмена",
                callback_data="builder:cancel"
            )
        )
        
        return builder.as_markup()
    
    @staticmethod
    def headline_format() -> InlineKeyboardMarkup:
        """Step 2: Select headline format."""
        builder = InlineKeyboardBuilder()
        
        builder.row(
            InlineKeyboardButton(
                text="Обычный",
                callback_data="builder:headline:plain"
            ),
            InlineKeyboardButton(
                text="Жирный",
                callback_data="builder:headline:bold"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="Курсив",
                callback_data="builder:headline:italic"
            ),
            InlineKeyboardButton(
                text="Жирный курсив",
                callback_data="builder:headline:bold_italic"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="« Назад",
                callback_data="builder:back:template"
            ),
            InlineKeyboardButton(
                text="❌ Отмена",
                callback_data="builder:cancel"
            )
        )
        
        return builder.as_markup()
    
    @staticmethod
    def custom_emoji() -> InlineKeyboardMarkup:
        """Step 3: Select custom emoji usage."""
        builder = InlineKeyboardBuilder()
        
        builder.row(
            InlineKeyboardButton(
                text="✅ Да, использовать",
                callback_data="builder:emoji:yes"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="❌ Нет, Unicode",
                callback_data="builder:emoji:no"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="« Назад",
                callback_data="builder:back:headline"
            ),
            InlineKeyboardButton(
                text="❌ Отмена",
                callback_data="builder:cancel"
            )
        )
        
        return builder.as_markup()
    
    @staticmethod
    def button_type() -> InlineKeyboardMarkup:
        """Step 4: Select button type."""
        builder = InlineKeyboardBuilder()
        
        builder.row(
            InlineKeyboardButton(
                text="Inline кнопки",
                callback_data="builder:btntype:inline"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="Reply кнопки",
                callback_data="builder:btntype:reply"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="Без кнопок",
                callback_data="builder:btntype:none"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="« Назад",
                callback_data="builder:back:emoji"
            ),
            InlineKeyboardButton(
                text="❌ Отмена",
                callback_data="builder:cancel"
            )
        )
        
        return builder.as_markup()
    
    @staticmethod
    def button_color() -> InlineKeyboardMarkup:
        """Step 5: Select button color/style."""
        builder = InlineKeyboardBuilder()
        
        builder.row(
            InlineKeyboardButton(
                text="🔵 Primary (синий)",
                callback_data="builder:color:primary"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="🟢 Success (зелёный)",
                callback_data="builder:color:success"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="🔴 Danger (красный)",
                callback_data="builder:color:danger"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="⚪ Без цвета",
                callback_data="builder:color:none"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="« Назад",
                callback_data="builder:back:btntype"
            ),
            InlineKeyboardButton(
                text="❌ Отмена",
                callback_data="builder:cancel"
            )
        )
        
        return builder.as_markup()
    
    @staticmethod
    def button_icon() -> InlineKeyboardMarkup:
        """Step 6: Select button icon."""
        builder = InlineKeyboardBuilder()
        
        builder.row(
            InlineKeyboardButton(
                text="✅ Да, добавить иконки",
                callback_data="builder:icon:yes"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="❌ Нет, без иконок",
                callback_data="builder:icon:no"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="« Назад",
                callback_data="builder:back:color"
            ),
            InlineKeyboardButton(
                text="❌ Отмена",
                callback_data="builder:cancel"
            )
        )
        
        return builder.as_markup()
    
    @staticmethod
    def preview_actions() -> InlineKeyboardMarkup:
        """Preview actions keyboard."""
        builder = InlineKeyboardBuilder()
        
        builder.row(
            InlineKeyboardButton(
                text="✏️ Изменить",
                callback_data="builder:edit"
            ),
            InlineKeyboardButton(
                text="🔄 Заново",
                callback_data="builder:restart"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="« В меню",
                callback_data="menu:back"
            )
        )
        
        return builder.as_markup()
    
    @staticmethod
    def skip_button_options() -> InlineKeyboardMarkup:
        """Keyboard when button type is 'none' - skip to preview."""
        builder = InlineKeyboardBuilder()
        
        builder.row(
            InlineKeyboardButton(
                text="✅ Создать превью",
                callback_data="builder:preview"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="« Назад",
                callback_data="builder:back:btntype"
            ),
            InlineKeyboardButton(
                text="❌ Отмена",
                callback_data="builder:cancel"
            )
        )
        
        return builder.as_markup()


# Create instance for import
builder_keyboards = BuilderKeyboards()
"""Builder step keyboards for interactive post constructor."""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class BuilderKeyboards:
    """Keyboards for the interactive post builder."""
    
    @staticmethod
    def template_selection() -> InlineKeyboardMarkup:
        """Step 1: Select template type."""
        builder = InlineKeyboardBuilder()
        
        builder.row(
            InlineKeyboardButton(
                text="📢 Объявление",
                callback_data="builder:template:announcement"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="🔥 Промо",
                callback_data="builder:template:promo"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="🚀 Обновление",
                callback_data="builder:template:update"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="⚠️ Предупреждение",
                callback_data="builder:template:warning"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="✅ Успех",
                callback_data="builder:template:success"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="❌ Отмена",
                callback_data="builder:cancel"
            )
        )
        
        return builder.as_markup()
    
    @staticmethod
    def headline_format() -> InlineKeyboardMarkup:
        """Step 2: Select headline format."""
        builder = InlineKeyboardBuilder()
        
        builder.row(
            InlineKeyboardButton(
                text="Обычный",
                callback_data="builder:headline:plain"
            ),
            InlineKeyboardButton(
                text="Жирный",
                callback_data="builder:headline:bold"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="Курсив",
                callback_data="builder:headline:italic"
            ),
            InlineKeyboardButton(
                text="Жирный курсив",
                callback_data="builder:headline:bold_italic"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="« Назад",
                callback_data="builder:back:template"
            ),
            InlineKeyboardButton(
                text="❌ Отмена",
                callback_data="builder:cancel"
            )
        )
        
        return builder.as_markup()
    
    @staticmethod
    def custom_emoji() -> InlineKeyboardMarkup:
        """Step 3: Select custom emoji usage."""
        builder = InlineKeyboardBuilder()
        
        builder.row(
            InlineKeyboardButton(
                text="✅ Да, использовать",
                callback_data="builder:emoji:yes"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="❌ Нет, Unicode",
                callback_data="builder:emoji:no"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="« Назад",
                callback_data="builder:back:headline"
            ),
            InlineKeyboardButton(
                text="❌ Отмена",
                callback_data="builder:cancel"
            )
        )
        
        return builder.as_markup()
    
    @staticmethod
    def button_type() -> InlineKeyboardMarkup:
        """Step 4: Select button type."""
        builder = InlineKeyboardBuilder()
        
        builder.row(
            InlineKeyboardButton(
                text="Inline кнопки",
                callback_data="builder:btntype:inline"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="Reply кнопки",
                callback_data="builder:btntype:reply"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="Без кнопок",
                callback_data="builder:btntype:none"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="« Назад",
                callback_data="builder:back:emoji"
            ),
            InlineKeyboardButton(
                text="❌ Отмена",
                callback_data="builder:cancel"
            )
        )
        
        return builder.as_markup()
    
    @staticmethod
    def button_color() -> InlineKeyboardMarkup:
        """Step 5: Select button color/style."""
        builder = InlineKeyboardBuilder()
        
        builder.row(
            InlineKeyboardButton(
                text="🔵 Primary (синий)",
                callback_data="builder:color:primary"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="🟢 Success (зелёный)",
                callback_data="builder:color:success"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="🔴 Danger (красный)",
                callback_data="builder:color:danger"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="⚪ Без цвета",
                callback_data="builder:color:none"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="« Назад",
                callback_data="builder:back:btntype"
            ),
            InlineKeyboardButton(
                text="❌ Отмена",
                callback_data="builder:cancel"
            )
        )
        
        return builder.as_markup()
    
    @staticmethod
    def button_icon() -> InlineKeyboardMarkup:
        """Step 6: Select button icon."""
        builder = InlineKeyboardBuilder()
        
        builder.row(
            InlineKeyboardButton(
                text="✅ Да, добавить иконки",
                callback_data="builder:icon:yes"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="❌ Нет, без иконок",
                callback_data="builder:icon:no"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="« Назад",
                callback_data="builder:back:color"
            ),
            InlineKeyboardButton(
                text="❌ Отмена",
                callback_data="builder:cancel"
            )
        )
        
        return builder.as_markup()
    
    @staticmethod
    def preview_actions() -> InlineKeyboardMarkup:
        """Preview actions keyboard."""
        builder = InlineKeyboardBuilder()
        
        builder.row(
            InlineKeyboardButton(
                text="✏️ Изменить",
                callback_data="builder:edit"
            ),
            InlineKeyboardButton(
                text="🔄 Заново",
                callback_data="builder:restart"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="« В меню",
                callback_data="menu:back"
            )
        )
        
        return builder.as_markup()
    
    @staticmethod
    def skip_button_options() -> InlineKeyboardMarkup:
        """Keyboard when button type is 'none' - skip to preview."""
        builder = InlineKeyboardBuilder()
        
        builder.row(
            InlineKeyboardButton(
                text="✅ Создать превью",
                callback_data="builder:preview"
            )
        )
        builder.row(
            InlineKeyboardButton(
                text="« Назад",
                callback_data="builder:back:btntype"
            ),
            InlineKeyboardButton(
                text="❌ Отмена",
                callback_data="builder:cancel"
            )
        )
        
        return builder.as_markup()


# Create instance for import
builder_keyboards = BuilderKeyboards()
