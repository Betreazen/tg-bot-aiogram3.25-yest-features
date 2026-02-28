"""Button factory service for creating styled keyboards."""

from typing import Optional, List
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from config.templates import ButtonConfig, ButtonStyle
from config.emoji_ids import BUTTON_ICON_EMOJI
from utils.fallback import fallback_checker


class ButtonFactory:
    """Factory for creating styled inline and reply keyboards."""
    
    STYLE_MAP = {
        ButtonStyle.PRIMARY: "primary",
        ButtonStyle.SUCCESS: "success",
        ButtonStyle.DANGER: "danger",
        ButtonStyle.DEFAULT: None,
    }
    
    def __init__(self):
        self._icons_available = fallback_checker.button_icons_available
    
    def create_inline_button(
        self,
        text: str,
        callback_data: Optional[str] = None,
        url: Optional[str] = None,
        switch_inline_query: Optional[str] = None,
        switch_inline_query_current_chat: Optional[str] = None,
        style: ButtonStyle = ButtonStyle.DEFAULT,
        icon_emoji_key: Optional[str] = None,
        force_no_icon: bool = False,
    ) -> InlineKeyboardButton:
        """
        Create a single inline keyboard button with optional styling.
        
        Args:
            text: Button text
            callback_data: Callback data for the button
            url: URL for the button
            switch_inline_query: Switch inline query
            switch_inline_query_current_chat: Switch inline query in current chat
            style: Button style (primary/success/danger)
            icon_emoji_key: Key from BUTTON_ICON_EMOJI for icon
            force_no_icon: Force button without icon
        """
        # Get icon custom emoji ID if available
        icon_custom_emoji_id = None
        if (
            icon_emoji_key 
            and not force_no_icon 
            and self._icons_available 
            and icon_emoji_key in BUTTON_ICON_EMOJI
        ):
            icon_custom_emoji_id = BUTTON_ICON_EMOJI[icon_emoji_key]
        
        # Get style string
        style_str = self.STYLE_MAP.get(style)
        
        # Build button kwargs
        kwargs = {"text": text}
        
        if callback_data:
            kwargs["callback_data"] = callback_data
        elif url:
            kwargs["url"] = url
        elif switch_inline_query is not None:
            kwargs["switch_inline_query"] = switch_inline_query
        elif switch_inline_query_current_chat is not None:
            kwargs["switch_inline_query_current_chat"] = switch_inline_query_current_chat
        
        # Add optional parameters if supported by aiogram version
        if icon_custom_emoji_id:
            kwargs["icon_custom_emoji_id"] = icon_custom_emoji_id
        
        if style_str:
            kwargs["style"] = style_str
        
        return InlineKeyboardButton(**kwargs)
    
    def create_inline_keyboard(
        self,
        buttons: List[List[InlineKeyboardButton]],
    ) -> InlineKeyboardMarkup:
        """Create inline keyboard from button matrix."""
        return InlineKeyboardMarkup(inline_keyboard=buttons)
    
    def create_inline_keyboard_from_configs(
        self,
        configs: List[ButtonConfig],
        row_width: int = 2,
        force_no_icons: bool = False,
        force_no_styles: bool = False,
    ) -> InlineKeyboardMarkup:
        """
        Create inline keyboard from ButtonConfig list.
        
        Args:
            configs: List of button configurations
            row_width: Number of buttons per row
            force_no_icons: Create buttons without icons
            force_no_styles: Create buttons without styles
        """
        builder = InlineKeyboardBuilder()
        
        for config in configs:
            style = ButtonStyle.DEFAULT if force_no_styles else config.style
            icon_key = None if force_no_icons else config.icon_emoji_key
            
            button = self.create_inline_button(
                text=config.text,
                callback_data=config.callback_data,
                url=config.url,
                style=style,
                icon_emoji_key=icon_key,
            )
            builder.add(button)
        
        builder.adjust(row_width)
        return builder.as_markup()
    
    def create_reply_button(
        self,
        text: str,
    ) -> KeyboardButton:
        """Create a single reply keyboard button."""
        return KeyboardButton(text=text)
    
    def create_reply_keyboard(
        self,
        buttons: List[List[str]],
        resize_keyboard: bool = True,
        one_time_keyboard: bool = False,
        is_persistent: bool = False,
    ) -> ReplyKeyboardMarkup:
        """
        Create reply keyboard from text matrix.
        
        Args:
            buttons: Matrix of button texts
            resize_keyboard: Resize keyboard to optimal size
            one_time_keyboard: Hide keyboard after button press
            is_persistent: Show keyboard persistently
        """
        builder = ReplyKeyboardBuilder()
        
        for row in buttons:
            for text in row:
                builder.add(KeyboardButton(text=text))
            builder.row()
        
        return builder.as_markup(
            resize_keyboard=resize_keyboard,
            one_time_keyboard=one_time_keyboard,
            is_persistent=is_persistent,
        )
    
    # Demo-specific button sets
    def create_unstyled_demo(self) -> InlineKeyboardMarkup:
        """Create demo keyboard with unstyled buttons."""
        return self.create_inline_keyboard([
            [
                InlineKeyboardButton(text="Кнопка 1", callback_data="demo_1"),
                InlineKeyboardButton(text="Кнопка 2", callback_data="demo_2"),
            ],
            [
                InlineKeyboardButton(text="Кнопка 3", callback_data="demo_3"),
            ],
        ])
    
    def create_primary_demo(self) -> InlineKeyboardMarkup:
        """Create demo keyboard with primary (blue) buttons."""
        return self.create_inline_keyboard([
            [
                self.create_inline_button(
                    "Primary 1", callback_data="primary_1", style=ButtonStyle.PRIMARY
                ),
                self.create_inline_button(
                    "Primary 2", callback_data="primary_2", style=ButtonStyle.PRIMARY
                ),
            ],
        ])
    
    def create_success_demo(self) -> InlineKeyboardMarkup:
        """Create demo keyboard with success (green) buttons."""
        return self.create_inline_keyboard([
            [
                self.create_inline_button(
                    "Success 1", callback_data="success_1", style=ButtonStyle.SUCCESS
                ),
                self.create_inline_button(
                    "Success 2", callback_data="success_2", style=ButtonStyle.SUCCESS
                ),
            ],
        ])
    
    def create_danger_demo(self) -> InlineKeyboardMarkup:
        """Create demo keyboard with danger (red) buttons."""
        return self.create_inline_keyboard([
            [
                self.create_inline_button(
                    "Danger 1", callback_data="danger_1", style=ButtonStyle.DANGER
                ),
                self.create_inline_button(
                    "Danger 2", callback_data="danger_2", style=ButtonStyle.DANGER
                ),
            ],
        ])
    
    def create_icon_demo(self) -> InlineKeyboardMarkup:
        """Create demo keyboard with icon buttons."""
        return self.create_inline_keyboard([
            [
                self.create_inline_button(
                    "Звезда", callback_data="icon_star", icon_emoji_key="star"
                ),
                self.create_inline_button(
                    "Ракета", callback_data="icon_rocket", icon_emoji_key="rocket"
                ),
            ],
            [
                self.create_inline_button(
                    "Подарок", callback_data="icon_gift", icon_emoji_key="gift"
                ),
                self.create_inline_button(
                    "Молния", callback_data="icon_lightning", icon_emoji_key="lightning"
                ),
            ],
        ])
    
    def create_combined_callback_demo(self) -> InlineKeyboardMarkup:
        """Create demo with icon + color + callback."""
        return self.create_inline_keyboard([
            [
                self.create_inline_button(
                    "Подтвердить",
                    callback_data="confirm",
                    style=ButtonStyle.SUCCESS,
                    icon_emoji_key="check"
                ),
                self.create_inline_button(
                    "Отменить",
                    callback_data="cancel",
                    style=ButtonStyle.DANGER,
                    icon_emoji_key="warning"
                ),
            ],
        ])
    
    def create_combined_url_demo(self) -> InlineKeyboardMarkup:
        """Create demo with icon + color + URL."""
        return self.create_inline_keyboard([
            [
                self.create_inline_button(
                    "Telegram",
                    url="https://telegram.org",
                    style=ButtonStyle.PRIMARY,
                    icon_emoji_key="star"
                ),
            ],
            [
                self.create_inline_button(
                    "Документация",
                    url="https://core.telegram.org/bots/api",
                    style=ButtonStyle.SUCCESS,
                    icon_emoji_key="rocket"
                ),
            ],
        ])
    
    def create_combined_switch_demo(self) -> InlineKeyboardMarkup:
        """Create demo with icon + color + switch actions."""
        return self.create_inline_keyboard([
            [
                self.create_inline_button(
                    "Поделиться",
                    switch_inline_query="Демо пост",
                    style=ButtonStyle.PRIMARY,
                    icon_emoji_key="sparkles"
                ),
            ],
            [
                self.create_inline_button(
                    "Выбрать здесь",
                    switch_inline_query_current_chat="",
                    style=ButtonStyle.SUCCESS,
                    icon_emoji_key="bell"
                ),
            ],
        ])
    
    def is_icons_available(self) -> bool:
        """Check if button icons are available."""
        return self._icons_available
    
    def refresh_availability(self) -> None:
        """Refresh icon availability status."""
        self._icons_available = fallback_checker.button_icons_available


# Global button factory instance
button_factory = ButtonFactory()
"""Button factory service for creating styled keyboards."""

from typing import Optional, List
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from config.templates import ButtonConfig, ButtonStyle
from config.emoji_ids import BUTTON_ICON_EMOJI
from utils.fallback import fallback_checker


class ButtonFactory:
    """Factory for creating styled inline and reply keyboards."""
    
    STYLE_MAP = {
        ButtonStyle.PRIMARY: "primary",
        ButtonStyle.SUCCESS: "success",
        ButtonStyle.DANGER: "danger",
        ButtonStyle.DEFAULT: None,
    }
    
    def __init__(self):
        self._icons_available = fallback_checker.button_icons_available
    
    def create_inline_button(
        self,
        text: str,
        callback_data: Optional[str] = None,
        url: Optional[str] = None,
        switch_inline_query: Optional[str] = None,
        switch_inline_query_current_chat: Optional[str] = None,
        style: ButtonStyle = ButtonStyle.DEFAULT,
        icon_emoji_key: Optional[str] = None,
        force_no_icon: bool = False,
    ) -> InlineKeyboardButton:
        """
        Create a single inline keyboard button with optional styling.
        
        Args:
            text: Button text
            callback_data: Callback data for the button
            url: URL for the button
            switch_inline_query: Switch inline query
            switch_inline_query_current_chat: Switch inline query in current chat
            style: Button style (primary/success/danger)
            icon_emoji_key: Key from BUTTON_ICON_EMOJI for icon
            force_no_icon: Force button without icon
        """
        # Get icon custom emoji ID if available
        icon_custom_emoji_id = None
        if (
            icon_emoji_key 
            and not force_no_icon 
            and self._icons_available 
            and icon_emoji_key in BUTTON_ICON_EMOJI
        ):
            icon_custom_emoji_id = BUTTON_ICON_EMOJI[icon_emoji_key]
        
        # Get style string
        style_str = self.STYLE_MAP.get(style)
        
        # Build button kwargs
        kwargs = {"text": text}
        
        if callback_data:
            kwargs["callback_data"] = callback_data
        elif url:
            kwargs["url"] = url
        elif switch_inline_query is not None:
            kwargs["switch_inline_query"] = switch_inline_query
        elif switch_inline_query_current_chat is not None:
            kwargs["switch_inline_query_current_chat"] = switch_inline_query_current_chat
        
        # Add optional parameters if supported by aiogram version
        if icon_custom_emoji_id:
            kwargs["icon_custom_emoji_id"] = icon_custom_emoji_id
        
        if style_str:
            kwargs["style"] = style_str
        
        return InlineKeyboardButton(**kwargs)
    
    def create_inline_keyboard(
        self,
        buttons: List[List[InlineKeyboardButton]],
    ) -> InlineKeyboardMarkup:
        """Create inline keyboard from button matrix."""
        return InlineKeyboardMarkup(inline_keyboard=buttons)
    
    def create_inline_keyboard_from_configs(
        self,
        configs: List[ButtonConfig],
        row_width: int = 2,
        force_no_icons: bool = False,
        force_no_styles: bool = False,
    ) -> InlineKeyboardMarkup:
        """
        Create inline keyboard from ButtonConfig list.
        
        Args:
            configs: List of button configurations
            row_width: Number of buttons per row
            force_no_icons: Create buttons without icons
            force_no_styles: Create buttons without styles
        """
        builder = InlineKeyboardBuilder()
        
        for config in configs:
            style = ButtonStyle.DEFAULT if force_no_styles else config.style
            icon_key = None if force_no_icons else config.icon_emoji_key
            
            button = self.create_inline_button(
                text=config.text,
                callback_data=config.callback_data,
                url=config.url,
                style=style,
                icon_emoji_key=icon_key,
            )
            builder.add(button)
        
        builder.adjust(row_width)
        return builder.as_markup()
    
    def create_reply_button(
        self,
        text: str,
    ) -> KeyboardButton:
        """Create a single reply keyboard button."""
        return KeyboardButton(text=text)
    
    def create_reply_keyboard(
        self,
        buttons: List[List[str]],
        resize_keyboard: bool = True,
        one_time_keyboard: bool = False,
        is_persistent: bool = False,
    ) -> ReplyKeyboardMarkup:
        """
        Create reply keyboard from text matrix.
        
        Args:
            buttons: Matrix of button texts
            resize_keyboard: Resize keyboard to optimal size
            one_time_keyboard: Hide keyboard after button press
            is_persistent: Show keyboard persistently
        """
        builder = ReplyKeyboardBuilder()
        
        for row in buttons:
            for text in row:
                builder.add(KeyboardButton(text=text))
            builder.row()
        
        return builder.as_markup(
            resize_keyboard=resize_keyboard,
            one_time_keyboard=one_time_keyboard,
            is_persistent=is_persistent,
        )
    
    # Demo-specific button sets
    def create_unstyled_demo(self) -> InlineKeyboardMarkup:
        """Create demo keyboard with unstyled buttons."""
        return self.create_inline_keyboard([
            [
                InlineKeyboardButton(text="Кнопка 1", callback_data="demo_1"),
                InlineKeyboardButton(text="Кнопка 2", callback_data="demo_2"),
            ],
            [
                InlineKeyboardButton(text="Кнопка 3", callback_data="demo_3"),
            ],
        ])
    
    def create_primary_demo(self) -> InlineKeyboardMarkup:
        """Create demo keyboard with primary (blue) buttons."""
        return self.create_inline_keyboard([
            [
                self.create_inline_button(
                    "Primary 1", callback_data="primary_1", style=ButtonStyle.PRIMARY
                ),
                self.create_inline_button(
                    "Primary 2", callback_data="primary_2", style=ButtonStyle.PRIMARY
                ),
            ],
        ])
    
    def create_success_demo(self) -> InlineKeyboardMarkup:
        """Create demo keyboard with success (green) buttons."""
        return self.create_inline_keyboard([
            [
                self.create_inline_button(
                    "Success 1", callback_data="success_1", style=ButtonStyle.SUCCESS
                ),
                self.create_inline_button(
                    "Success 2", callback_data="success_2", style=ButtonStyle.SUCCESS
                ),
            ],
        ])
    
    def create_danger_demo(self) -> InlineKeyboardMarkup:
        """Create demo keyboard with danger (red) buttons."""
        return self.create_inline_keyboard([
            [
                self.create_inline_button(
                    "Danger 1", callback_data="danger_1", style=ButtonStyle.DANGER
                ),
                self.create_inline_button(
                    "Danger 2", callback_data="danger_2", style=ButtonStyle.DANGER
                ),
            ],
        ])
    
    def create_icon_demo(self) -> InlineKeyboardMarkup:
        """Create demo keyboard with icon buttons."""
        return self.create_inline_keyboard([
            [
                self.create_inline_button(
                    "Звезда", callback_data="icon_star", icon_emoji_key="star"
                ),
                self.create_inline_button(
                    "Ракета", callback_data="icon_rocket", icon_emoji_key="rocket"
                ),
            ],
            [
                self.create_inline_button(
                    "Подарок", callback_data="icon_gift", icon_emoji_key="gift"
                ),
                self.create_inline_button(
                    "Молния", callback_data="icon_lightning", icon_emoji_key="lightning"
                ),
            ],
        ])
    
    def create_combined_callback_demo(self) -> InlineKeyboardMarkup:
        """Create demo with icon + color + callback."""
        return self.create_inline_keyboard([
            [
                self.create_inline_button(
                    "Подтвердить",
                    callback_data="confirm",
                    style=ButtonStyle.SUCCESS,
                    icon_emoji_key="check"
                ),
                self.create_inline_button(
                    "Отменить",
                    callback_data="cancel",
                    style=ButtonStyle.DANGER,
                    icon_emoji_key="warning"
                ),
            ],
        ])
    
    def create_combined_url_demo(self) -> InlineKeyboardMarkup:
        """Create demo with icon + color + URL."""
        return self.create_inline_keyboard([
            [
                self.create_inline_button(
                    "Telegram",
                    url="https://telegram.org",
                    style=ButtonStyle.PRIMARY,
                    icon_emoji_key="star"
                ),
            ],
            [
                self.create_inline_button(
                    "Документация",
                    url="https://core.telegram.org/bots/api",
                    style=ButtonStyle.SUCCESS,
                    icon_emoji_key="rocket"
                ),
            ],
        ])
    
    def create_combined_switch_demo(self) -> InlineKeyboardMarkup:
        """Create demo with icon + color + switch actions."""
        return self.create_inline_keyboard([
            [
                self.create_inline_button(
                    "Поделиться",
                    switch_inline_query="Демо пост",
                    style=ButtonStyle.PRIMARY,
                    icon_emoji_key="sparkles"
                ),
            ],
            [
                self.create_inline_button(
                    "Выбрать здесь",
                    switch_inline_query_current_chat="",
                    style=ButtonStyle.SUCCESS,
                    icon_emoji_key="bell"
                ),
            ],
        ])
    
    def is_icons_available(self) -> bool:
        """Check if button icons are available."""
        return self._icons_available
    
    def refresh_availability(self) -> None:
        """Refresh icon availability status."""
        self._icons_available = fallback_checker.button_icons_available


# Global button factory instance
button_factory = ButtonFactory()
