"""Buttons demo handler - /buttons_demo command."""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from services.button_factory import button_factory
from keyboards.menu import get_back_button, get_demo_navigation


router = Router(name="buttons_demo")


@router.message(Command("buttons_demo"))
async def cmd_buttons_demo(message: Message) -> None:
    """Handle /buttons_demo command - show button styles."""
    await message.answer(
        "🔘 Демонстрация кнопок\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Различные стили и типы кнопок.\n"
        "Нажимайте «Далее» для просмотра всех вариантов."
    )
    
    # Demo 1: Unstyled buttons
    await message.answer(
        "📍 Демо #1: Обычные кнопки (без стиля)\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Стандартные inline кнопки без дополнительного оформления.",
        reply_markup=button_factory.create_unstyled_demo()
    )
    await message.answer(
        "👆 Нажмите любую кнопку или перейдите дальше:",
        reply_markup=get_demo_navigation(next_callback="btn:demo:2")
    )


@router.callback_query(F.data == "btn:demo:1")
async def btn_demo_1(callback: CallbackQuery) -> None:
    """Demo 1: Unstyled buttons (from navigation)."""
    await callback.message.answer(
        "📍 Демо #1: Обычные кнопки (без стиля)\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Стандартные inline кнопки без дополнительного оформления.",
        reply_markup=button_factory.create_unstyled_demo()
    )
    await callback.message.answer(
        "👆 Нажмите любую кнопку или перейдите дальше:",
        reply_markup=get_demo_navigation(next_callback="btn:demo:2")
    )
    await callback.answer()


@router.callback_query(F.data == "btn:demo:2")
async def btn_demo_2(callback: CallbackQuery) -> None:
    """Demo 2: Primary (blue) buttons."""
    await callback.message.answer(
        "📍 Демо #2: Primary кнопки (синие)\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🔵 Кнопки со стилем `primary` — основной цвет действия.",
        reply_markup=button_factory.create_primary_demo()
    )
    await callback.message.answer(
        "👆 Primary кнопки для основных действий:",
        reply_markup=get_demo_navigation(
            prev_callback="btn:demo:1",
            next_callback="btn:demo:3"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "btn:demo:3")
async def btn_demo_3(callback: CallbackQuery) -> None:
    """Demo 3: Success (green) buttons."""
    await callback.message.answer(
        "📍 Демо #3: Success кнопки (зелёные)\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🟢 Кнопки со стилем `success` — для подтверждения.",
        reply_markup=button_factory.create_success_demo()
    )
    await callback.message.answer(
        "👆 Success кнопки для позитивных действий:",
        reply_markup=get_demo_navigation(
            prev_callback="btn:demo:2",
            next_callback="btn:demo:4"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "btn:demo:4")
async def btn_demo_4(callback: CallbackQuery) -> None:
    """Demo 4: Danger (red) buttons."""
    await callback.message.answer(
        "📍 Демо #4: Danger кнопки (красные)\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🔴 Кнопки со стилем `danger` — для важных/опасных действий.",
        reply_markup=button_factory.create_danger_demo()
    )
    await callback.message.answer(
        "👆 Danger кнопки для предупреждений:",
        reply_markup=get_demo_navigation(
            prev_callback="btn:demo:3",
            next_callback="btn:demo:5"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "btn:demo:5")
async def btn_demo_5(callback: CallbackQuery) -> None:
    """Demo 5: Buttons with icons."""
    await callback.message.answer(
        "📍 Демо #5: Кнопки с иконками\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Кнопки с `icon_custom_emoji_id` — иконка перед текстом.",
        reply_markup=button_factory.create_icon_demo()
    )
    await callback.message.answer(
        "👆 Кнопки с кастомными иконками-эмодзи:",
        reply_markup=get_demo_navigation(
            prev_callback="btn:demo:4",
            next_callback="btn:demo:6"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "btn:demo:6")
async def btn_demo_6(callback: CallbackQuery) -> None:
    """Demo 6: Combined - icon + color + callback."""
    await callback.message.answer(
        "📍 Демо #6: Комбинация — иконка + цвет + callback\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Полная комбинация всех возможностей для кнопок с callback.",
        reply_markup=button_factory.create_combined_callback_demo()
    )
    await callback.message.answer(
        "👆 Иконка + цвет + callback действие:",
        reply_markup=get_demo_navigation(
            prev_callback="btn:demo:5",
            next_callback="btn:demo:7"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "btn:demo:7")
async def btn_demo_7(callback: CallbackQuery) -> None:
    """Demo 7: Combined - icon + color + URL."""
    await callback.message.answer(
        "📍 Демо #7: Комбинация — иконка + цвет + URL\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Кнопки-ссылки с полным оформлением.",
        reply_markup=button_factory.create_combined_url_demo()
    )
    await callback.message.answer(
        "👆 Иконка + цвет + внешняя ссылка:",
        reply_markup=get_demo_navigation(
            prev_callback="btn:demo:6",
            next_callback="btn:demo:8"
        )
    )
    await callback.answer()


@router.callback_query(F.data == "btn:demo:8")
async def btn_demo_8(callback: CallbackQuery) -> None:
    """Demo 8: Combined - icon + color + switch."""
    await callback.message.answer(
        "📍 Демо #8: Комбинация — иконка + цвет + switch\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Кнопки для inline-запросов с полным оформлением.",
        reply_markup=button_factory.create_combined_switch_demo()
    )
    await callback.message.answer(
        "👆 Иконка + цвет + switch inline query:",
        reply_markup=get_demo_navigation(
            prev_callback="btn:demo:7",
        )
    )
    await callback.answer("✅ Все демо кнопок просмотрены!")


# Handle demo button clicks (just acknowledge)
@router.callback_query(F.data.startswith("demo_"))
async def handle_demo_button(callback: CallbackQuery) -> None:
    """Handle demo button clicks."""
    await callback.answer(f"Нажата кнопка: {callback.data}")


@router.callback_query(F.data.startswith("primary_"))
async def handle_primary_button(callback: CallbackQuery) -> None:
    """Handle primary button clicks."""
    await callback.answer(f"🔵 Primary: {callback.data}")


@router.callback_query(F.data.startswith("success_"))
async def handle_success_button(callback: CallbackQuery) -> None:
    """Handle success button clicks."""
    await callback.answer(f"🟢 Success: {callback.data}")


@router.callback_query(F.data.startswith("danger_"))
async def handle_danger_button(callback: CallbackQuery) -> None:
    """Handle danger button clicks."""
    await callback.answer(f"🔴 Danger: {callback.data}")


@router.callback_query(F.data.startswith("icon_"))
async def handle_icon_button(callback: CallbackQuery) -> None:
    """Handle icon button clicks."""
    await callback.answer(f"✨ Icon: {callback.data}")


@router.callback_query(F.data == "confirm")
async def handle_confirm(callback: CallbackQuery) -> None:
    """Handle confirm button."""
    await callback.answer("✅ Подтверждено!")


@router.callback_query(F.data == "cancel")
async def handle_cancel(callback: CallbackQuery) -> None:
    """Handle cancel button."""
    await callback.answer("❌ Отменено!")
