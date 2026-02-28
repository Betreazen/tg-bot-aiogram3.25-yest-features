"""Post factory service for assembling formatted messages."""

from typing import Optional, Tuple
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.formatting import (
    Text,
    Bold,
    Italic,
    Underline,
    Strikethrough,
    Spoiler,
    Code,
    Pre,
    TextLink,
    BlockQuote,
    CustomEmoji,
    as_list,
    as_section,
)

from config.templates import (
    TEMPLATES,
    TemplateConfig,
    HeadlineFormat,
    ButtonStyle,
)
from services.emoji_registry import emoji_service
from services.button_factory import button_factory
from utils.fallback import fallback_checker


class PostFactory:
    """Factory for assembling formatted post messages."""
    
    def __init__(self):
        self._emoji_service = emoji_service
        self._button_factory = button_factory
    
    def format_headline(
        self, 
        text: str, 
        format_type: HeadlineFormat
    ) -> Text | Bold | Italic:
        """Format headline according to specified format type."""
        match format_type:
            case HeadlineFormat.BOLD:
                return Bold(text)
            case HeadlineFormat.ITALIC:
                return Italic(text)
            case HeadlineFormat.BOLD_ITALIC:
                return Bold(Italic(text))
            case _:
                return Text(text)
    
    def create_template_post(
        self,
        template_key: str,
        use_custom_emoji: bool = True,
        use_button_icons: bool = True,
        use_button_styles: bool = True,
    ) -> Tuple[Text, Optional[InlineKeyboardMarkup]]:
        """
        Create a formatted post from template.
        
        Args:
            template_key: Key of template in TEMPLATES
            use_custom_emoji: Whether to use custom emoji
            use_button_icons: Whether to use button icons
            use_button_styles: Whether to use button styles
            
        Returns:
            Tuple of (formatted content, keyboard or None)
        """
        template = TEMPLATES.get(template_key)
        if not template:
            return Text(f"Шаблон '{template_key}' не найден"), None
        
        return self._build_from_template(
            template,
            use_custom_emoji=use_custom_emoji,
            use_button_icons=use_button_icons,
            use_button_styles=use_button_styles,
        )
    
    def _build_from_template(
        self,
        template: TemplateConfig,
        use_custom_emoji: bool = True,
        use_button_icons: bool = True,
        use_button_styles: bool = True,
    ) -> Tuple[Text, Optional[InlineKeyboardMarkup]]:
        """Build post content and keyboard from template config."""
        self._emoji_service.clear_used_emoji_ids()
        
        # Build headline with emoji if available
        headline_parts = []
        
        # Add emoji before headline if custom emoji enabled
        if use_custom_emoji and template.emoji_keys:
            first_emoji = self._emoji_service.get_custom_emoji_node(
                template.emoji_keys[0],
                force_unicode=not use_custom_emoji
            )
            headline_parts.append(first_emoji)
            headline_parts.append(" ")
        
        headline_parts.append(
            self.format_headline(template.headline, template.headline_format)
        )
        
        # Build body
        body_content = template.body
        
        # Wrap in blockquote if specified
        if template.use_blockquote:
            body_node = BlockQuote(
                body_content,
                expandable=template.expandable_quote
            )
        else:
            body_node = Text(body_content)
        
        # Combine all parts
        content = as_list(
            Text(*headline_parts),
            Text("\n"),
            body_node,
        )
        
        # Create keyboard if buttons defined
        keyboard = None
        if template.buttons:
            keyboard = self._button_factory.create_inline_keyboard_from_configs(
                template.buttons,
                force_no_icons=not use_button_icons,
                force_no_styles=not use_button_styles,
            )
        
        return content, keyboard
    
    # Demo post creators
    def create_basic_post(self) -> Text:
        """Create basic plain text demo post."""
        return Text(
            "Это простой текстовый пост.\n\n"
            "Без форматирования, просто текст.\n"
            "Используется для базовых сообщений."
        )
    
    def create_combined_styles_post(self) -> Text:
        """Create post demonstrating combined text styles."""
        return as_list(
            Bold("Жирный текст"), Text(" и "), Italic("курсив"),
            Text("\n"),
            Underline("Подчёркнутый"), Text(" и "), Strikethrough("зачёркнутый"),
            Text("\n"),
            Bold(Italic("Жирный курсив")), Text(" и "), Bold(Underline("жирный подчёркнутый")),
            Text("\n\n"),
            Spoiler("Это спойлер — нажмите, чтобы раскрыть"),
            Text("\n\n"),
            Text("Inline код: "), Code("print('Hello')"),
        )
    
    def create_quote_post(self) -> Text:
        """Create post with blockquote."""
        return as_list(
            Bold("📝 Цитата дня"),
            Text("\n\n"),
            BlockQuote(
                "Программирование — это искусство говорить другому человеку, "
                "чего ты хочешь от компьютера.\n\n— Дональд Кнут"
            ),
        )
    
    def create_expandable_quote_post(self) -> Text:
        """Create post with expandable blockquote."""
        return as_list(
            Bold("📖 Развёрнутая цитата"),
            Text("\n\n"),
            Text("Нажмите на цитату, чтобы развернуть полный текст:"),
            Text("\n\n"),
            BlockQuote(
                "Любая достаточно развитая технология неотличима от магии.\n\n"
                "Единственный способ делать великую работу — любить то, что делаешь.\n\n"
                "Будущее уже здесь — оно просто неравномерно распределено.\n\n"
                "Простота — это высшая степень изощрённости.",
                expandable=True
            ),
        )
    
    def create_links_post(self) -> Text:
        """Create post with text links."""
        return as_list(
            Bold("🔗 Полезные ссылки"),
            Text("\n\n"),
            Text("• "), TextLink("Telegram Bot API", url="https://core.telegram.org/bots/api"),
            Text("\n"),
            Text("• "), TextLink("aiogram документация", url="https://docs.aiogram.dev/"),
            Text("\n"),
            Text("• "), TextLink("Python официальный сайт", url="https://python.org"),
            Text("\n\n"),
            Italic("Ссылки открываются в браузере"),
        )
    
    def create_code_block_post(self) -> Text:
        """Create post with code block."""
        return as_list(
            Bold("💻 Пример кода"),
            Text("\n\n"),
            Pre(
                '@dp.message(Command("start"))\n'
                'async def start_handler(message: Message):\n'
                '    await message.answer("Hello!")',
                language="python"
            ),
            Text("\n"),
            Italic("Код с подсветкой синтаксиса Python"),
        )
    
    def create_custom_emoji_post(
        self, 
        force_unicode: bool = False
    ) -> Tuple[Text, list[str]]:
        """
        Create post with custom emoji.
        
        Returns:
            Tuple of (formatted content, list of used emoji IDs)
        """
        self._emoji_service.clear_used_emoji_ids()
        
        fire = self._emoji_service.get_custom_emoji_node("fire", force_unicode)
        star = self._emoji_service.get_custom_emoji_node("star", force_unicode)
        rocket = self._emoji_service.get_custom_emoji_node("rocket", force_unicode)
        check = self._emoji_service.get_custom_emoji_node("check", force_unicode)
        sparkles = self._emoji_service.get_custom_emoji_node("sparkles", force_unicode)
        
        content = as_list(
            fire, Text(" "), Bold("Пост с кастомными эмодзи"), Text(" "), fire,
            Text("\n\n"),
            star, Text(" Первый пункт с звездой\n"),
            rocket, Text(" Второй пункт с ракетой\n"),
            check, Text(" Третий пункт с галочкой\n"),
            Text("\n"),
            sparkles, Text(" "), Italic("Магия кастомных эмодзи!"), Text(" "), sparkles,
        )
        
        return content, self._emoji_service.get_used_emoji_ids()
    
    def create_unicode_emoji_post(self) -> Text:
        """Create post with only Unicode emoji."""
        return as_list(
            Text("🔥 "), Bold("Пост с Unicode эмодзи"), Text(" 🔥"),
            Text("\n\n"),
            Text("⭐ Первый пункт с звездой\n"),
            Text("🚀 Второй пункт с ракетой\n"),
            Text("✅ Третий пункт с галочкой\n"),
            Text("\n"),
            Text("✨ "), Italic("Стандартные Unicode эмодзи"), Text(" ✨"),
        )
    
    def create_mixed_emoji_post(
        self, 
        force_unicode: bool = False
    ) -> Tuple[Text, list[str]]:
        """
        Create post with mixed custom and Unicode emoji.
        
        Returns:
            Tuple of (formatted content, list of used emoji IDs)
        """
        self._emoji_service.clear_used_emoji_ids()
        
        fire = self._emoji_service.get_custom_emoji_node("fire", force_unicode)
        gem = self._emoji_service.get_custom_emoji_node("gem", force_unicode)
        
        content = as_list(
            fire, Text(" "), Bold("Смешанный пост"), Text(" 🔥"),
            Text("\n\n"),
            gem, Text(" Кастомный эмодзи + обычный 💎\n"),
            Text("🌟 Обычный + "), self._emoji_service.get_custom_emoji_node("star", force_unicode),
            Text(" кастомный\n"),
            Text("\n"),
            Italic("Комбинация обоих типов эмодзи"),
        )
        
        return content, self._emoji_service.get_used_emoji_ids()
    
    def create_all_styles_demo(self) -> Text:
        """Create comprehensive demo of all text styles."""
        return as_list(
            Bold("🎨 Все стили форматирования"),
            Text("\n\n"),
            
            Text("1️⃣ "), Bold("Жирный (Bold)"), Text("\n"),
            Text("2️⃣ "), Italic("Курсив (Italic)"), Text("\n"),
            Text("3️⃣ "), Underline("Подчёркнутый (Underline)"), Text("\n"),
            Text("4️⃣ "), Strikethrough("Зачёркнутый (Strikethrough)"), Text("\n"),
            Text("5️⃣ "), Spoiler("Спойлер (Spoiler)"), Text("\n"),
            Text("6️⃣ "), Code("Код (Code)"), Text("\n"),
            Text("7️⃣ "), TextLink("Ссылка (TextLink)", url="https://telegram.org"), Text("\n"),
            Text("\n"),
            
            Text("8️⃣ Блок кода:\n"),
            Pre("def hello():\n    return 'world'", language="python"),
            Text("\n"),
            
            Text("9️⃣ Цитата:\n"),
            BlockQuote("Это цитата"),
        )
    
    def get_all_template_keys(self) -> list[str]:
        """Get all available template keys."""
        return list(TEMPLATES.keys())


# Global post factory instance  
post_factory = PostFactory()
"""Post factory service for assembling formatted messages."""

from typing import Optional, Tuple
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.formatting import (
    Text,
    Bold,
    Italic,
    Underline,
    Strikethrough,
    Spoiler,
    Code,
    Pre,
    TextLink,
    BlockQuote,
    CustomEmoji,
    as_list,
    as_section,
)

from config.templates import (
    TEMPLATES,
    TemplateConfig,
    HeadlineFormat,
    ButtonStyle,
)
from services.emoji_registry import emoji_service
from services.button_factory import button_factory
from utils.fallback import fallback_checker


class PostFactory:
    """Factory for assembling formatted post messages."""
    
    def __init__(self):
        self._emoji_service = emoji_service
        self._button_factory = button_factory
    
    def format_headline(
        self, 
        text: str, 
        format_type: HeadlineFormat
    ) -> Text | Bold | Italic:
        """Format headline according to specified format type."""
        match format_type:
            case HeadlineFormat.BOLD:
                return Bold(text)
            case HeadlineFormat.ITALIC:
                return Italic(text)
            case HeadlineFormat.BOLD_ITALIC:
                return Bold(Italic(text))
            case _:
                return Text(text)
    
    def create_template_post(
        self,
        template_key: str,
        use_custom_emoji: bool = True,
        use_button_icons: bool = True,
        use_button_styles: bool = True,
    ) -> Tuple[Text, Optional[InlineKeyboardMarkup]]:
        """
        Create a formatted post from template.
        
        Args:
            template_key: Key of template in TEMPLATES
            use_custom_emoji: Whether to use custom emoji
            use_button_icons: Whether to use button icons
            use_button_styles: Whether to use button styles
            
        Returns:
            Tuple of (formatted content, keyboard or None)
        """
        template = TEMPLATES.get(template_key)
        if not template:
            return Text(f"Шаблон '{template_key}' не найден"), None
        
        return self._build_from_template(
            template,
            use_custom_emoji=use_custom_emoji,
            use_button_icons=use_button_icons,
            use_button_styles=use_button_styles,
        )
    
    def _build_from_template(
        self,
        template: TemplateConfig,
        use_custom_emoji: bool = True,
        use_button_icons: bool = True,
        use_button_styles: bool = True,
    ) -> Tuple[Text, Optional[InlineKeyboardMarkup]]:
        """Build post content and keyboard from template config."""
        self._emoji_service.clear_used_emoji_ids()
        
        # Build headline with emoji if available
        headline_parts = []
        
        # Add emoji before headline if custom emoji enabled
        if use_custom_emoji and template.emoji_keys:
            first_emoji = self._emoji_service.get_custom_emoji_node(
                template.emoji_keys[0],
                force_unicode=not use_custom_emoji
            )
            headline_parts.append(first_emoji)
            headline_parts.append(" ")
        
        headline_parts.append(
            self.format_headline(template.headline, template.headline_format)
        )
        
        # Build body
        body_content = template.body
        
        # Wrap in blockquote if specified
        if template.use_blockquote:
            body_node = BlockQuote(
                body_content,
                expandable=template.expandable_quote
            )
        else:
            body_node = Text(body_content)
        
        # Combine all parts
        content = as_list(
            Text(*headline_parts),
            Text("\n"),
            body_node,
        )
        
        # Create keyboard if buttons defined
        keyboard = None
        if template.buttons:
            keyboard = self._button_factory.create_inline_keyboard_from_configs(
                template.buttons,
                force_no_icons=not use_button_icons,
                force_no_styles=not use_button_styles,
            )
        
        return content, keyboard
    
    # Demo post creators
    def create_basic_post(self) -> Text:
        """Create basic plain text demo post."""
        return Text(
            "Это простой текстовый пост.\n\n"
            "Без форматирования, просто текст.\n"
            "Используется для базовых сообщений."
        )
    
    def create_combined_styles_post(self) -> Text:
        """Create post demonstrating combined text styles."""
        return as_list(
            Bold("Жирный текст"), Text(" и "), Italic("курсив"),
            Text("\n"),
            Underline("Подчёркнутый"), Text(" и "), Strikethrough("зачёркнутый"),
            Text("\n"),
            Bold(Italic("Жирный курсив")), Text(" и "), Bold(Underline("жирный подчёркнутый")),
            Text("\n\n"),
            Spoiler("Это спойлер — нажмите, чтобы раскрыть"),
            Text("\n\n"),
            Text("Inline код: "), Code("print('Hello')"),
        )
    
    def create_quote_post(self) -> Text:
        """Create post with blockquote."""
        return as_list(
            Bold("📝 Цитата дня"),
            Text("\n\n"),
            BlockQuote(
                "Программирование — это искусство говорить другому человеку, "
                "чего ты хочешь от компьютера.\n\n— Дональд Кнут"
            ),
        )
    
    def create_expandable_quote_post(self) -> Text:
        """Create post with expandable blockquote."""
        return as_list(
            Bold("📖 Развёрнутая цитата"),
            Text("\n\n"),
            Text("Нажмите на цитату, чтобы развернуть полный текст:"),
            Text("\n\n"),
            BlockQuote(
                "Любая достаточно развитая технология неотличима от магии.\n\n"
                "Единственный способ делать великую работу — любить то, что делаешь.\n\n"
                "Будущее уже здесь — оно просто неравномерно распределено.\n\n"
                "Простота — это высшая степень изощрённости.",
                expandable=True
            ),
        )
    
    def create_links_post(self) -> Text:
        """Create post with text links."""
        return as_list(
            Bold("🔗 Полезные ссылки"),
            Text("\n\n"),
            Text("• "), TextLink("Telegram Bot API", url="https://core.telegram.org/bots/api"),
            Text("\n"),
            Text("• "), TextLink("aiogram документация", url="https://docs.aiogram.dev/"),
            Text("\n"),
            Text("• "), TextLink("Python официальный сайт", url="https://python.org"),
            Text("\n\n"),
            Italic("Ссылки открываются в браузере"),
        )
    
    def create_code_block_post(self) -> Text:
        """Create post with code block."""
        return as_list(
            Bold("💻 Пример кода"),
            Text("\n\n"),
            Pre(
                '@dp.message(Command("start"))\n'
                'async def start_handler(message: Message):\n'
                '    await message.answer("Hello!")',
                language="python"
            ),
            Text("\n"),
            Italic("Код с подсветкой синтаксиса Python"),
        )
    
    def create_custom_emoji_post(
        self, 
        force_unicode: bool = False
    ) -> Tuple[Text, list[str]]:
        """
        Create post with custom emoji.
        
        Returns:
            Tuple of (formatted content, list of used emoji IDs)
        """
        self._emoji_service.clear_used_emoji_ids()
        
        fire = self._emoji_service.get_custom_emoji_node("fire", force_unicode)
        star = self._emoji_service.get_custom_emoji_node("star", force_unicode)
        rocket = self._emoji_service.get_custom_emoji_node("rocket", force_unicode)
        check = self._emoji_service.get_custom_emoji_node("check", force_unicode)
        sparkles = self._emoji_service.get_custom_emoji_node("sparkles", force_unicode)
        
        content = as_list(
            fire, Text(" "), Bold("Пост с кастомными эмодзи"), Text(" "), fire,
            Text("\n\n"),
            star, Text(" Первый пункт с звездой\n"),
            rocket, Text(" Второй пункт с ракетой\n"),
            check, Text(" Третий пункт с галочкой\n"),
            Text("\n"),
            sparkles, Text(" "), Italic("Магия кастомных эмодзи!"), Text(" "), sparkles,
        )
        
        return content, self._emoji_service.get_used_emoji_ids()
    
    def create_unicode_emoji_post(self) -> Text:
        """Create post with only Unicode emoji."""
        return as_list(
            Text("🔥 "), Bold("Пост с Unicode эмодзи"), Text(" 🔥"),
            Text("\n\n"),
            Text("⭐ Первый пункт с звездой\n"),
            Text("🚀 Второй пункт с ракетой\n"),
            Text("✅ Третий пункт с галочкой\n"),
            Text("\n"),
            Text("✨ "), Italic("Стандартные Unicode эмодзи"), Text(" ✨"),
        )
    
    def create_mixed_emoji_post(
        self, 
        force_unicode: bool = False
    ) -> Tuple[Text, list[str]]:
        """
        Create post with mixed custom and Unicode emoji.
        
        Returns:
            Tuple of (formatted content, list of used emoji IDs)
        """
        self._emoji_service.clear_used_emoji_ids()
        
        fire = self._emoji_service.get_custom_emoji_node("fire", force_unicode)
        gem = self._emoji_service.get_custom_emoji_node("gem", force_unicode)
        
        content = as_list(
            fire, Text(" "), Bold("Смешанный пост"), Text(" 🔥"),
            Text("\n\n"),
            gem, Text(" Кастомный эмодзи + обычный 💎\n"),
            Text("🌟 Обычный + "), self._emoji_service.get_custom_emoji_node("star", force_unicode),
            Text(" кастомный\n"),
            Text("\n"),
            Italic("Комбинация обоих типов эмодзи"),
        )
        
        return content, self._emoji_service.get_used_emoji_ids()
    
    def create_all_styles_demo(self) -> Text:
        """Create comprehensive demo of all text styles."""
        return as_list(
            Bold("🎨 Все стили форматирования"),
            Text("\n\n"),
            
            Text("1️⃣ "), Bold("Жирный (Bold)"), Text("\n"),
            Text("2️⃣ "), Italic("Курсив (Italic)"), Text("\n"),
            Text("3️⃣ "), Underline("Подчёркнутый (Underline)"), Text("\n"),
            Text("4️⃣ "), Strikethrough("Зачёркнутый (Strikethrough)"), Text("\n"),
            Text("5️⃣ "), Spoiler("Спойлер (Spoiler)"), Text("\n"),
            Text("6️⃣ "), Code("Код (Code)"), Text("\n"),
            Text("7️⃣ "), TextLink("Ссылка (TextLink)", url="https://telegram.org"), Text("\n"),
            Text("\n"),
            
            Text("8️⃣ Блок кода:\n"),
            Pre("def hello():\n    return 'world'", language="python"),
            Text("\n"),
            
            Text("9️⃣ Цитата:\n"),
            BlockQuote("Это цитата"),
        )
    
    def get_all_template_keys(self) -> list[str]:
        """Get all available template keys."""
        return list(TEMPLATES.keys())


# Global post factory instance  
post_factory = PostFactory()
