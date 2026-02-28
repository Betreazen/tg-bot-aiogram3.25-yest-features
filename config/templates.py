"""Post templates configuration."""

from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum


class TemplateType(str, Enum):
    """Available post template types."""
    ANNOUNCEMENT = "announcement"
    PROMO = "promo"
    UPDATE = "update"
    WARNING = "warning"
    SUCCESS = "success"


class ButtonStyle(str, Enum):
    """Available button styles."""
    PRIMARY = "primary"      # Blue
    SUCCESS = "success"      # Green  
    DANGER = "danger"        # Red
    DEFAULT = "default"      # No style


class HeadlineFormat(str, Enum):
    """Available headline formatting options."""
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    BOLD_ITALIC = "bold_italic"


@dataclass
class ButtonConfig:
    """Button configuration for templates."""
    text: str
    callback_data: Optional[str] = None
    url: Optional[str] = None
    style: ButtonStyle = ButtonStyle.DEFAULT
    icon_emoji_key: Optional[str] = None  # Key from EMOJI_REGISTRY


@dataclass
class TemplateConfig:
    """Full post template configuration."""
    name: str
    type: TemplateType
    headline: str
    headline_format: HeadlineFormat = HeadlineFormat.BOLD
    body: str = ""
    emoji_keys: List[str] = field(default_factory=list)
    use_blockquote: bool = False
    expandable_quote: bool = False
    buttons: List[ButtonConfig] = field(default_factory=list)


# Pre-configured post templates
TEMPLATES: dict[str, TemplateConfig] = {
    "announcement": TemplateConfig(
        name="Объявление",
        type=TemplateType.ANNOUNCEMENT,
        headline="📢 Важное объявление",
        headline_format=HeadlineFormat.BOLD,
        body=(
            "Уважаемые пользователи!\n\n"
            "Мы рады сообщить о важных обновлениях в нашем сервисе. "
            "Подробности по ссылке ниже.\n\n"
            "Следите за новостями!"
        ),
        emoji_keys=["bell", "sparkles"],
        buttons=[
            ButtonConfig(
                text="Подробнее",
                url="https://example.com/news",
                style=ButtonStyle.DEFAULT
            ),
            ButtonConfig(
                text="Подписаться",
                callback_data="subscribe",
                style=ButtonStyle.PRIMARY,
                icon_emoji_key="bell"
            ),
        ]
    ),
    
    "promo": TemplateConfig(
        name="Промо",
        type=TemplateType.PROMO,
        headline="🔥 Специальное предложение!",
        headline_format=HeadlineFormat.BOLD_ITALIC,
        body=(
            "Только сегодня:\n\n"
            "• Скидка 50% на все товары\n"
            "• Бесплатная доставка\n"
            "• Подарок при заказе от 1000₽\n\n"
            "Успейте воспользоваться!"
        ),
        emoji_keys=["fire", "gift", "rocket"],
        buttons=[
            ButtonConfig(
                text="🎁 Получить скидку",
                callback_data="get_promo",
                style=ButtonStyle.PRIMARY,
                icon_emoji_key="gift"
            ),
            ButtonConfig(
                text="Каталог",
                url="https://example.com/catalog",
                style=ButtonStyle.DEFAULT
            ),
        ]
    ),
    
    "update": TemplateConfig(
        name="Обновление",
        type=TemplateType.UPDATE,
        headline="🚀 Обновление v2.0",
        headline_format=HeadlineFormat.BOLD,
        body=(
            "Что нового:\n\n"
            "1. Улучшенный интерфейс\n"
            "2. Повышенная производительность\n"
            "3. Новые функции безопасности\n"
            "4. Исправление ошибок"
        ),
        emoji_keys=["rocket", "sparkles"],
        use_blockquote=True,
        expandable_quote=False,
        buttons=[
            ButtonConfig(
                text="Обновить сейчас",
                callback_data="update_now",
                style=ButtonStyle.PRIMARY,
                icon_emoji_key="rocket"
            ),
        ]
    ),
    
    "warning": TemplateConfig(
        name="Предупреждение",
        type=TemplateType.WARNING,
        headline="⚠️ Внимание! Важная информация",
        headline_format=HeadlineFormat.BOLD,
        body=(
            "Обнаружена потенциальная проблема.\n\n"
            "Пожалуйста, проверьте настройки вашего аккаунта "
            "и убедитесь, что все данные актуальны.\n\n"
            "В случае вопросов обратитесь в поддержку."
        ),
        emoji_keys=["warning"],
        use_blockquote=True,
        expandable_quote=True,
        buttons=[
            ButtonConfig(
                text="⚠️ Проверить настройки",
                callback_data="check_settings",
                style=ButtonStyle.DANGER,
                icon_emoji_key="warning"
            ),
            ButtonConfig(
                text="Поддержка",
                url="https://example.com/support",
                style=ButtonStyle.DEFAULT
            ),
        ]
    ),
    
    "success": TemplateConfig(
        name="Успех",
        type=TemplateType.SUCCESS,
        headline="✅ Операция успешно завершена!",
        headline_format=HeadlineFormat.BOLD,
        body=(
            "Поздравляем!\n\n"
            "Ваш запрос был успешно обработан. "
            "Все изменения сохранены и вступили в силу.\n\n"
            "Спасибо за использование нашего сервиса!"
        ),
        emoji_keys=["check", "party", "star"],
        buttons=[
            ButtonConfig(
                text="✅ Отлично!",
                callback_data="success_ack",
                style=ButtonStyle.SUCCESS,
                icon_emoji_key="check"
            ),
            ButtonConfig(
                text="⭐ Оценить",
                callback_data="rate",
                style=ButtonStyle.PRIMARY,
                icon_emoji_key="star"
            ),
        ]
    ),
}


# Template descriptions for builder menu
TEMPLATE_DESCRIPTIONS: dict[str, str] = {
    "announcement": "📢 Объявление — заголовок + акцент + ссылка",
    "promo": "🔥 Промо — эмодзи + список + CTA кнопки",
    "update": "🚀 Обновление — цитата + список + кнопка действия",
    "warning": "⚠️ Предупреждение — красный акцент + danger кнопка",
    "success": "✅ Успех — зелёные акценты + success кнопка",
}
"""Post templates configuration."""

from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum


class TemplateType(str, Enum):
    """Available post template types."""
    ANNOUNCEMENT = "announcement"
    PROMO = "promo"
    UPDATE = "update"
    WARNING = "warning"
    SUCCESS = "success"


class ButtonStyle(str, Enum):
    """Available button styles."""
    PRIMARY = "primary"      # Blue
    SUCCESS = "success"      # Green  
    DANGER = "danger"        # Red
    DEFAULT = "default"      # No style


class HeadlineFormat(str, Enum):
    """Available headline formatting options."""
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    BOLD_ITALIC = "bold_italic"


@dataclass
class ButtonConfig:
    """Button configuration for templates."""
    text: str
    callback_data: Optional[str] = None
    url: Optional[str] = None
    style: ButtonStyle = ButtonStyle.DEFAULT
    icon_emoji_key: Optional[str] = None  # Key from EMOJI_REGISTRY


@dataclass
class TemplateConfig:
    """Full post template configuration."""
    name: str
    type: TemplateType
    headline: str
    headline_format: HeadlineFormat = HeadlineFormat.BOLD
    body: str = ""
    emoji_keys: List[str] = field(default_factory=list)
    use_blockquote: bool = False
    expandable_quote: bool = False
    buttons: List[ButtonConfig] = field(default_factory=list)


# Pre-configured post templates
TEMPLATES: dict[str, TemplateConfig] = {
    "announcement": TemplateConfig(
        name="Объявление",
        type=TemplateType.ANNOUNCEMENT,
        headline="📢 Важное объявление",
        headline_format=HeadlineFormat.BOLD,
        body=(
            "Уважаемые пользователи!\n\n"
            "Мы рады сообщить о важных обновлениях в нашем сервисе. "
            "Подробности по ссылке ниже.\n\n"
            "Следите за новостями!"
        ),
        emoji_keys=["bell", "sparkles"],
        buttons=[
            ButtonConfig(
                text="Подробнее",
                url="https://example.com/news",
                style=ButtonStyle.DEFAULT
            ),
            ButtonConfig(
                text="Подписаться",
                callback_data="subscribe",
                style=ButtonStyle.PRIMARY,
                icon_emoji_key="bell"
            ),
        ]
    ),
    
    "promo": TemplateConfig(
        name="Промо",
        type=TemplateType.PROMO,
        headline="🔥 Специальное предложение!",
        headline_format=HeadlineFormat.BOLD_ITALIC,
        body=(
            "Только сегодня:\n\n"
            "• Скидка 50% на все товары\n"
            "• Бесплатная доставка\n"
            "• Подарок при заказе от 1000₽\n\n"
            "Успейте воспользоваться!"
        ),
        emoji_keys=["fire", "gift", "rocket"],
        buttons=[
            ButtonConfig(
                text="🎁 Получить скидку",
                callback_data="get_promo",
                style=ButtonStyle.PRIMARY,
                icon_emoji_key="gift"
            ),
            ButtonConfig(
                text="Каталог",
                url="https://example.com/catalog",
                style=ButtonStyle.DEFAULT
            ),
        ]
    ),
    
    "update": TemplateConfig(
        name="Обновление",
        type=TemplateType.UPDATE,
        headline="🚀 Обновление v2.0",
        headline_format=HeadlineFormat.BOLD,
        body=(
            "Что нового:\n\n"
            "1. Улучшенный интерфейс\n"
            "2. Повышенная производительность\n"
            "3. Новые функции безопасности\n"
            "4. Исправление ошибок"
        ),
        emoji_keys=["rocket", "sparkles"],
        use_blockquote=True,
        expandable_quote=False,
        buttons=[
            ButtonConfig(
                text="Обновить сейчас",
                callback_data="update_now",
                style=ButtonStyle.PRIMARY,
                icon_emoji_key="rocket"
            ),
        ]
    ),
    
    "warning": TemplateConfig(
        name="Предупреждение",
        type=TemplateType.WARNING,
        headline="⚠️ Внимание! Важная информация",
        headline_format=HeadlineFormat.BOLD,
        body=(
            "Обнаружена потенциальная проблема.\n\n"
            "Пожалуйста, проверьте настройки вашего аккаунта "
            "и убедитесь, что все данные актуальны.\n\n"
            "В случае вопросов обратитесь в поддержку."
        ),
        emoji_keys=["warning"],
        use_blockquote=True,
        expandable_quote=True,
        buttons=[
            ButtonConfig(
                text="⚠️ Проверить настройки",
                callback_data="check_settings",
                style=ButtonStyle.DANGER,
                icon_emoji_key="warning"
            ),
            ButtonConfig(
                text="Поддержка",
                url="https://example.com/support",
                style=ButtonStyle.DEFAULT
            ),
        ]
    ),
    
    "success": TemplateConfig(
        name="Успех",
        type=TemplateType.SUCCESS,
        headline="✅ Операция успешно завершена!",
        headline_format=HeadlineFormat.BOLD,
        body=(
            "Поздравляем!\n\n"
            "Ваш запрос был успешно обработан. "
            "Все изменения сохранены и вступили в силу.\n\n"
            "Спасибо за использование нашего сервиса!"
        ),
        emoji_keys=["check", "party", "star"],
        buttons=[
            ButtonConfig(
                text="✅ Отлично!",
                callback_data="success_ack",
                style=ButtonStyle.SUCCESS,
                icon_emoji_key="check"
            ),
            ButtonConfig(
                text="⭐ Оценить",
                callback_data="rate",
                style=ButtonStyle.PRIMARY,
                icon_emoji_key="star"
            ),
        ]
    ),
}


# Template descriptions for builder menu
TEMPLATE_DESCRIPTIONS: dict[str, str] = {
    "announcement": "📢 Объявление — заголовок + акцент + ссылка",
    "promo": "🔥 Промо — эмодзи + список + CTA кнопки",
    "update": "🚀 Обновление — цитата + список + кнопка действия",
    "warning": "⚠️ Предупреждение — красный акцент + danger кнопка",
    "success": "✅ Успех — зелёные акценты + success кнопка",
}
