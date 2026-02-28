"""Post demo handler - /post_demo command."""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from services.post_factory import post_factory
from keyboards.menu import get_template_selection_menu, get_back_button


router = Router(name="post_demo")


@router.message(Command("post_demo"))
async def cmd_post_demo(message: Message) -> None:
    """Handle /post_demo command - show template selection."""
    await message.answer(
        "📋 Готовые шаблоны постов\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Выберите шаблон для просмотра:\n\n"
        "• 📢 Объявление — заголовок + акцент + ссылка\n"
        "• 🔥 Промо — эмодзи + список + CTA кнопки\n"
        "• 🚀 Обновление — цитата + список + кнопка\n"
        "• ⚠️ Предупреждение — красный акцент + danger\n"
        "• ✅ Успех — зелёные акценты + success\n",
        reply_markup=get_template_selection_menu()
    )


@router.callback_query(F.data == "template:announcement")
async def template_announcement(callback: CallbackQuery) -> None:
    """Show announcement template."""
    await callback.message.answer(
        "📢 Шаблон: Объявление\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content, keyboard = post_factory.create_template_post("announcement")
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=keyboard
    )
    await callback.message.answer(
        "👆 Пример поста-объявления с нейтральными кнопками",
        reply_markup=get_back_button("post:back")
    )
    await callback.answer()


@router.callback_query(F.data == "template:promo")
async def template_promo(callback: CallbackQuery) -> None:
    """Show promo template."""
    await callback.message.answer(
        "🔥 Шаблон: Промо\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content, keyboard = post_factory.create_template_post("promo")
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=keyboard
    )
    await callback.message.answer(
        "👆 Пример промо-поста с CTA кнопками",
        reply_markup=get_back_button("post:back")
    )
    await callback.answer()


@router.callback_query(F.data == "template:update")
async def template_update(callback: CallbackQuery) -> None:
    """Show update template."""
    await callback.message.answer(
        "🚀 Шаблон: Обновление\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content, keyboard = post_factory.create_template_post("update")
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=keyboard
    )
    await callback.message.answer(
        "👆 Пример поста об обновлении с цитатой",
        reply_markup=get_back_button("post:back")
    )
    await callback.answer()


@router.callback_query(F.data == "template:warning")
async def template_warning(callback: CallbackQuery) -> None:
    """Show warning template."""
    await callback.message.answer(
        "⚠️ Шаблон: Предупреждение\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content, keyboard = post_factory.create_template_post("warning")
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=keyboard
    )
    await callback.message.answer(
        "👆 Пример предупреждения с красной danger кнопкой",
        reply_markup=get_back_button("post:back")
    )
    await callback.answer()


@router.callback_query(F.data == "template:success")
async def template_success(callback: CallbackQuery) -> None:
    """Show success template."""
    await callback.message.answer(
        "✅ Шаблон: Успех\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content, keyboard = post_factory.create_template_post("success")
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=keyboard
    )
    await callback.message.answer(
        "👆 Пример успешного результата с зелёной success кнопкой",
        reply_markup=get_back_button("post:back")
    )
    await callback.answer()


@router.callback_query(F.data == "post:back")
async def post_back(callback: CallbackQuery) -> None:
    """Back to template selection."""
    await callback.message.edit_text(
        "📋 Готовые шаблоны постов\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Выберите шаблон для просмотра:\n\n"
        "• 📢 Объявление — заголовок + акцент + ссылка\n"
        "• 🔥 Промо — эмодзи + список + CTA кнопки\n"
        "• 🚀 Обновление — цитата + список + кнопка\n"
        "• ⚠️ Предупреждение — красный акцент + danger\n"
        "• ✅ Успех — зелёные акценты + success\n",
        reply_markup=get_template_selection_menu()
    )
    await callback.answer()


# Handle template button clicks (acknowledge only)
@router.callback_query(F.data == "subscribe")
async def handle_subscribe(callback: CallbackQuery) -> None:
    """Handle subscribe button."""
    await callback.answer("🔔 Вы подписались на уведомления!")


@router.callback_query(F.data == "get_promo")
async def handle_get_promo(callback: CallbackQuery) -> None:
    """Handle get promo button."""
    await callback.answer("🎁 Промокод: DEMO2024")


@router.callback_query(F.data == "update_now")
async def handle_update_now(callback: CallbackQuery) -> None:
    """Handle update now button."""
    await callback.answer("🚀 Обновление запущено!")


@router.callback_query(F.data == "check_settings")
async def handle_check_settings(callback: CallbackQuery) -> None:
    """Handle check settings button."""
    await callback.answer("⚙️ Открываем настройки...")


@router.callback_query(F.data == "success_ack")
async def handle_success_ack(callback: CallbackQuery) -> None:
    """Handle success acknowledgement."""
    await callback.answer("👍 Отлично!")


@router.callback_query(F.data == "rate")
async def handle_rate(callback: CallbackQuery) -> None:
    """Handle rate button."""
    await callback.answer("⭐ Спасибо за оценку!")
"""Post demo handler - /post_demo command."""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from services.post_factory import post_factory
from keyboards.menu import get_template_selection_menu, get_back_button


router = Router(name="post_demo")


@router.message(Command("post_demo"))
async def cmd_post_demo(message: Message) -> None:
    """Handle /post_demo command - show template selection."""
    await message.answer(
        "📋 Готовые шаблоны постов\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Выберите шаблон для просмотра:\n\n"
        "• 📢 Объявление — заголовок + акцент + ссылка\n"
        "• 🔥 Промо — эмодзи + список + CTA кнопки\n"
        "• 🚀 Обновление — цитата + список + кнопка\n"
        "• ⚠️ Предупреждение — красный акцент + danger\n"
        "• ✅ Успех — зелёные акценты + success\n",
        reply_markup=get_template_selection_menu()
    )


@router.callback_query(F.data == "template:announcement")
async def template_announcement(callback: CallbackQuery) -> None:
    """Show announcement template."""
    await callback.message.answer(
        "📢 Шаблон: Объявление\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content, keyboard = post_factory.create_template_post("announcement")
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=keyboard
    )
    await callback.message.answer(
        "👆 Пример поста-объявления с нейтральными кнопками",
        reply_markup=get_back_button("post:back")
    )
    await callback.answer()


@router.callback_query(F.data == "template:promo")
async def template_promo(callback: CallbackQuery) -> None:
    """Show promo template."""
    await callback.message.answer(
        "🔥 Шаблон: Промо\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content, keyboard = post_factory.create_template_post("promo")
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=keyboard
    )
    await callback.message.answer(
        "👆 Пример промо-поста с CTA кнопками",
        reply_markup=get_back_button("post:back")
    )
    await callback.answer()


@router.callback_query(F.data == "template:update")
async def template_update(callback: CallbackQuery) -> None:
    """Show update template."""
    await callback.message.answer(
        "🚀 Шаблон: Обновление\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content, keyboard = post_factory.create_template_post("update")
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=keyboard
    )
    await callback.message.answer(
        "👆 Пример поста об обновлении с цитатой",
        reply_markup=get_back_button("post:back")
    )
    await callback.answer()


@router.callback_query(F.data == "template:warning")
async def template_warning(callback: CallbackQuery) -> None:
    """Show warning template."""
    await callback.message.answer(
        "⚠️ Шаблон: Предупреждение\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content, keyboard = post_factory.create_template_post("warning")
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=keyboard
    )
    await callback.message.answer(
        "👆 Пример предупреждения с красной danger кнопкой",
        reply_markup=get_back_button("post:back")
    )
    await callback.answer()


@router.callback_query(F.data == "template:success")
async def template_success(callback: CallbackQuery) -> None:
    """Show success template."""
    await callback.message.answer(
        "✅ Шаблон: Успех\n━━━━━━━━━━━━━━━━━━━━━━"
    )
    content, keyboard = post_factory.create_template_post("success")
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=keyboard
    )
    await callback.message.answer(
        "👆 Пример успешного результата с зелёной success кнопкой",
        reply_markup=get_back_button("post:back")
    )
    await callback.answer()


@router.callback_query(F.data == "post:back")
async def post_back(callback: CallbackQuery) -> None:
    """Back to template selection."""
    await callback.message.edit_text(
        "📋 Готовые шаблоны постов\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Выберите шаблон для просмотра:\n\n"
        "• 📢 Объявление — заголовок + акцент + ссылка\n"
        "• 🔥 Промо — эмодзи + список + CTA кнопки\n"
        "• 🚀 Обновление — цитата + список + кнопка\n"
        "• ⚠️ Предупреждение — красный акцент + danger\n"
        "• ✅ Успех — зелёные акценты + success\n",
        reply_markup=get_template_selection_menu()
    )
    await callback.answer()


# Handle template button clicks (acknowledge only)
@router.callback_query(F.data == "subscribe")
async def handle_subscribe(callback: CallbackQuery) -> None:
    """Handle subscribe button."""
    await callback.answer("🔔 Вы подписались на уведомления!")


@router.callback_query(F.data == "get_promo")
async def handle_get_promo(callback: CallbackQuery) -> None:
    """Handle get promo button."""
    await callback.answer("🎁 Промокод: DEMO2024")


@router.callback_query(F.data == "update_now")
async def handle_update_now(callback: CallbackQuery) -> None:
    """Handle update now button."""
    await callback.answer("🚀 Обновление запущено!")


@router.callback_query(F.data == "check_settings")
async def handle_check_settings(callback: CallbackQuery) -> None:
    """Handle check settings button."""
    await callback.answer("⚙️ Открываем настройки...")


@router.callback_query(F.data == "success_ack")
async def handle_success_ack(callback: CallbackQuery) -> None:
    """Handle success acknowledgement."""
    await callback.answer("👍 Отлично!")


@router.callback_query(F.data == "rate")
async def handle_rate(callback: CallbackQuery) -> None:
    """Handle rate button."""
    await callback.answer("⭐ Спасибо за оценку!")
