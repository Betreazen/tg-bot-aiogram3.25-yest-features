"""Emoji demo handler - /emoji_demo command."""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from services.post_factory import post_factory
from utils.fallback import fallback_checker
from keyboards.menu import get_back_button, get_demo_navigation


router = Router(name="emoji_demo")


@router.message(Command("emoji_demo"))
async def cmd_emoji_demo(message: Message) -> None:
    """Handle /emoji_demo command - show emoji comparison."""
    # Header
    await message.answer(
        "😊 Демонстрация эмодзи\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Сравнение Unicode и кастомных эмодзи в постах.\n"
        "Нажмите кнопки для просмотра разных вариантов."
    )
    
    # Demo 1: Unicode only
    await message.answer(
        "📍 Вариант 1: Только Unicode эмодзи\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_unicode_emoji_post()
    await message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(next_callback="emoji:demo:2")
    )


@router.callback_query(F.data == "emoji:demo:1")
async def emoji_demo_1(callback: CallbackQuery) -> None:
    """Demo 1: Unicode only (from navigation)."""
    await callback.message.answer(
        "📍 Вариант 1: Только Unicode эмодзи\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content = post_factory.create_unicode_emoji_post()
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=get_demo_navigation(next_callback="emoji:demo:2")
    )
    await callback.answer()


@router.callback_query(F.data == "emoji:demo:2")
async def emoji_demo_2(callback: CallbackQuery) -> None:
    """Demo 2: Custom emoji."""
    await callback.message.answer(
        "📍 Вариант 2: Кастомные эмодзи\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content, emoji_ids = post_factory.create_custom_emoji_post(force_unicode=False)
    
    # Add technical info
    tech_info = fallback_checker.get_technical_info(emoji_ids)
    
    await callback.message.answer(**content.as_kwargs())
    await callback.message.answer(
        f"```\n{tech_info}\n```",
        parse_mode="MarkdownV2",
        reply_markup=get_demo_navigation(
            prev_callback="emoji:demo:1",
            next_callback="emoji:demo:3"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "emoji:demo:3")
async def emoji_demo_3(callback: CallbackQuery) -> None:
    """Demo 3: Mixed emoji."""
    await callback.message.answer(
        "📍 Вариант 3: Смешанный пост\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content, emoji_ids = post_factory.create_mixed_emoji_post(force_unicode=False)
    
    # Add technical info
    tech_info = fallback_checker.get_technical_info(emoji_ids)
    
    await callback.message.answer(**content.as_kwargs())
    await callback.message.answer(
        f"```\n{tech_info}\n```",
        parse_mode="MarkdownV2",
        reply_markup=get_demo_navigation(
            prev_callback="emoji:demo:2",
            next_callback="emoji:demo:fallback"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "emoji:demo:fallback")
async def emoji_demo_fallback(callback: CallbackQuery) -> None:
    """Demo 4: Fallback demonstration."""
    await callback.message.answer(
        "📍 Вариант 4: Режим Fallback\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Когда кастомные эмодзи недоступны, бот автоматически "
        "использует Unicode эмодзи:"
    )
    
    # Force unicode fallback for demonstration
    content, emoji_ids = post_factory.create_custom_emoji_post(force_unicode=True)
    
    await callback.message.answer(**content.as_kwargs())
    await callback.message.answer(
        "ℹ️ Custom emoji fallback enabled\n\n"
        "В этом режиме все кастомные эмодзи заменяются "
        "на стандартные Unicode символы.",
        reply_markup=get_demo_navigation(
            prev_callback="emoji:demo:3",
        )
    )
    await callback.answer("✅ Все демо эмодзи просмотрены!")
