"""Text demo handler - /text_demo command."""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.enums import ParseMode

from services.post_factory import post_factory
from keyboards.menu import get_back_button, get_demo_navigation


router = Router(name="text_demo")


@router.message(Command("text_demo"))
async def cmd_text_demo(message: Message) -> None:
    """Handle /text_demo command - send all text formatting demos."""
    # Demo 1: Basic post
    await message.answer(
        "📝 Демо #1: Базовый пост\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_basic_post()
    await message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(next_callback="text:demo:2")
    )


@router.callback_query(F.data == "text:demo:2")
async def text_demo_2(callback: CallbackQuery) -> None:
    """Demo 2: Combined styles."""
    await callback.message.answer(
        "📝 Демо #2: Комбинированные стили\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_combined_styles_post()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(
            prev_callback="text:demo:1",
            next_callback="text:demo:3"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "text:demo:1")
async def text_demo_1(callback: CallbackQuery) -> None:
    """Demo 1: Basic post (from navigation)."""
    await callback.message.answer(
        "📝 Демо #1: Базовый пост\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_basic_post()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(next_callback="text:demo:2")
    )
    await callback.answer()


@router.callback_query(F.data == "text:demo:3")
async def text_demo_3(callback: CallbackQuery) -> None:
    """Demo 3: Quote post."""
    await callback.message.answer(
        "📝 Демо #3: Цитата\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_quote_post()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(
            prev_callback="text:demo:2",
            next_callback="text:demo:4"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "text:demo:4")
async def text_demo_4(callback: CallbackQuery) -> None:
    """Demo 4: Expandable quote."""
    await callback.message.answer(
        "📝 Демо #4: Развёрнутая цитата\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_expandable_quote_post()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(
            prev_callback="text:demo:3",
            next_callback="text:demo:5"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "text:demo:5")
async def text_demo_5(callback: CallbackQuery) -> None:
    """Demo 5: Links post."""
    await callback.message.answer(
        "📝 Демо #5: Ссылки\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_links_post()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(
            prev_callback="text:demo:4",
            next_callback="text:demo:6"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "text:demo:6")
async def text_demo_6(callback: CallbackQuery) -> None:
    """Demo 6: Code block."""
    await callback.message.answer(
        "📝 Демо #6: Блок кода\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_code_block_post()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(
            prev_callback="text:demo:5",
            next_callback="text:demo:7"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "text:demo:7")
async def text_demo_7(callback: CallbackQuery) -> None:
    """Demo 7: Custom emoji in text."""
    await callback.message.answer(
        "📝 Демо #7: Кастомные эмодзи в тексте\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content, emoji_ids = post_factory.create_custom_emoji_post()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(
            prev_callback="text:demo:6",
            next_callback="text:demo:all"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "text:demo:all")
async def text_demo_all(callback: CallbackQuery) -> None:
    """Demo: All styles in one post."""
    await callback.message.answer(
        "📝 Демо: Все стили форматирования\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_all_styles_demo()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(
            prev_callback="text:demo:7",
        )
    )
    await callback.answer("✅ Все демо просмотрены!")
"""Text demo handler - /text_demo command."""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.enums import ParseMode

from services.post_factory import post_factory
from keyboards.menu import get_back_button, get_demo_navigation


router = Router(name="text_demo")


@router.message(Command("text_demo"))
async def cmd_text_demo(message: Message) -> None:
    """Handle /text_demo command - send all text formatting demos."""
    # Demo 1: Basic post
    await message.answer(
        "📝 Демо #1: Базовый пост\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_basic_post()
    await message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(next_callback="text:demo:2")
    )


@router.callback_query(F.data == "text:demo:2")
async def text_demo_2(callback: CallbackQuery) -> None:
    """Demo 2: Combined styles."""
    await callback.message.answer(
        "📝 Демо #2: Комбинированные стили\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_combined_styles_post()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(
            prev_callback="text:demo:1",
            next_callback="text:demo:3"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "text:demo:1")
async def text_demo_1(callback: CallbackQuery) -> None:
    """Demo 1: Basic post (from navigation)."""
    await callback.message.answer(
        "📝 Демо #1: Базовый пост\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_basic_post()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(next_callback="text:demo:2")
    )
    await callback.answer()


@router.callback_query(F.data == "text:demo:3")
async def text_demo_3(callback: CallbackQuery) -> None:
    """Demo 3: Quote post."""
    await callback.message.answer(
        "📝 Демо #3: Цитата\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_quote_post()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(
            prev_callback="text:demo:2",
            next_callback="text:demo:4"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "text:demo:4")
async def text_demo_4(callback: CallbackQuery) -> None:
    """Demo 4: Expandable quote."""
    await callback.message.answer(
        "📝 Демо #4: Развёрнутая цитата\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_expandable_quote_post()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(
            prev_callback="text:demo:3",
            next_callback="text:demo:5"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "text:demo:5")
async def text_demo_5(callback: CallbackQuery) -> None:
    """Demo 5: Links post."""
    await callback.message.answer(
        "📝 Демо #5: Ссылки\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_links_post()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(
            prev_callback="text:demo:4",
            next_callback="text:demo:6"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "text:demo:6")
async def text_demo_6(callback: CallbackQuery) -> None:
    """Demo 6: Code block."""
    await callback.message.answer(
        "📝 Демо #6: Блок кода\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_code_block_post()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(
            prev_callback="text:demo:5",
            next_callback="text:demo:7"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "text:demo:7")
async def text_demo_7(callback: CallbackQuery) -> None:
    """Demo 7: Custom emoji in text."""
    await callback.message.answer(
        "📝 Демо #7: Кастомные эмодзи в тексте\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content, emoji_ids = post_factory.create_custom_emoji_post()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(
            prev_callback="text:demo:6",
            next_callback="text:demo:all"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "text:demo:all")
async def text_demo_all(callback: CallbackQuery) -> None:
    """Demo: All styles in one post."""
    await callback.message.answer(
        "📝 Демо: Все стили форматирования\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_all_styles_demo()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(
            prev_callback="text:demo:7",
        )
    )
    await callback.answer("✅ Все демо просмотрены!")
