"""Builder handler - /builder command with FSM-based post constructor."""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.formatting import Text, Bold, Italic, as_list

from config.templates import (
    TEMPLATES, 
    HeadlineFormat, 
    ButtonStyle,
    ButtonConfig,
)
from services.post_factory import post_factory
from services.button_factory import button_factory
from services.emoji_registry import emoji_service
from keyboards.builder_kb import BuilderKeyboards
from keyboards.menu import get_back_button


router = Router(name="builder")


class BuilderStates(StatesGroup):
    """FSM states for the post builder."""
    select_template = State()
    select_headline = State()
    select_emoji = State()
    select_button_type = State()
    select_button_color = State()
    select_button_icon = State()
    preview = State()


@router.message(Command("builder"))
async def cmd_builder(message: Message, state: FSMContext) -> None:
    """Handle /builder command - start the post constructor."""
    await state.clear()
    await state.set_state(BuilderStates.select_template)
    
    await message.answer(
        "🛠 Конструктор постов\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Создайте свой пост пошагово.\n\n"
        "📍 Шаг 1/6: Выберите тип шаблона:",
        reply_markup=BuilderKeyboards.template_selection()
    )


# Step 1: Template selection
@router.callback_query(BuilderStates.select_template, F.data.startswith("builder:template:"))
async def select_template(callback: CallbackQuery, state: FSMContext) -> None:
    """Handle template selection."""
    template_key = callback.data.split(":")[-1]
    await state.update_data(template=template_key)
    await state.set_state(BuilderStates.select_headline)
    
    await callback.message.edit_text(
        f"✅ Выбран шаблон: {TEMPLATES[template_key].name}\n\n"
        "📍 Шаг 2/6: Выберите формат заголовка:",
        reply_markup=BuilderKeyboards.headline_format()
    )
    await callback.answer()


# Step 2: Headline format
@router.callback_query(BuilderStates.select_headline, F.data.startswith("builder:headline:"))
async def select_headline(callback: CallbackQuery, state: FSMContext) -> None:
    """Handle headline format selection."""
    format_key = callback.data.split(":")[-1]
    format_map = {
        "plain": HeadlineFormat.PLAIN,
        "bold": HeadlineFormat.BOLD,
        "italic": HeadlineFormat.ITALIC,
        "bold_italic": HeadlineFormat.BOLD_ITALIC,
    }
    await state.update_data(headline_format=format_map.get(format_key, HeadlineFormat.BOLD))
    await state.set_state(BuilderStates.select_emoji)
    
    format_names = {
        "plain": "Обычный",
        "bold": "Жирный",
        "italic": "Курсив",
        "bold_italic": "Жирный курсив",
    }
    
    await callback.message.edit_text(
        f"✅ Формат заголовка: {format_names.get(format_key, format_key)}\n\n"
        "📍 Шаг 3/6: Использовать кастомные эмодзи?",
        reply_markup=BuilderKeyboards.custom_emoji()
    )
    await callback.answer()


# Step 3: Custom emoji
@router.callback_query(BuilderStates.select_emoji, F.data.startswith("builder:emoji:"))
async def select_emoji(callback: CallbackQuery, state: FSMContext) -> None:
    """Handle custom emoji selection."""
    use_emoji = callback.data.split(":")[-1] == "yes"
    await state.update_data(use_custom_emoji=use_emoji)
    await state.set_state(BuilderStates.select_button_type)
    
    emoji_text = "Да" if use_emoji else "Нет (Unicode)"
    
    await callback.message.edit_text(
        f"✅ Кастомные эмодзи: {emoji_text}\n\n"
        "📍 Шаг 4/6: Выберите тип кнопок:",
        reply_markup=BuilderKeyboards.button_type()
    )
    await callback.answer()


# Step 4: Button type
@router.callback_query(BuilderStates.select_button_type, F.data.startswith("builder:btntype:"))
async def select_button_type(callback: CallbackQuery, state: FSMContext) -> None:
    """Handle button type selection."""
    btn_type = callback.data.split(":")[-1]
    await state.update_data(button_type=btn_type)
    
    type_names = {
        "inline": "Inline кнопки",
        "reply": "Reply кнопки",
        "none": "Без кнопок",
    }
    
    if btn_type == "none":
        # Skip to preview if no buttons
        await state.update_data(button_color=None, button_icon=False)
        await state.set_state(BuilderStates.preview)
        await callback.message.edit_text(
            f"✅ Тип кнопок: {type_names.get(btn_type)}\n\n"
            "📍 Готово! Создаём превью...",
            reply_markup=BuilderKeyboards.skip_button_options()
        )
    else:
        await state.set_state(BuilderStates.select_button_color)
        await callback.message.edit_text(
            f"✅ Тип кнопок: {type_names.get(btn_type)}\n\n"
            "📍 Шаг 5/6: Выберите цвет кнопок:",
            reply_markup=BuilderKeyboards.button_color()
        )
    await callback.answer()


# Step 5: Button color
@router.callback_query(BuilderStates.select_button_color, F.data.startswith("builder:color:"))
async def select_button_color(callback: CallbackQuery, state: FSMContext) -> None:
    """Handle button color selection."""
    color_key = callback.data.split(":")[-1]
    color_map = {
        "primary": ButtonStyle.PRIMARY,
        "success": ButtonStyle.SUCCESS,
        "danger": ButtonStyle.DANGER,
        "none": ButtonStyle.DEFAULT,
    }
    await state.update_data(button_color=color_map.get(color_key, ButtonStyle.DEFAULT))
    await state.set_state(BuilderStates.select_button_icon)
    
    color_names = {
        "primary": "🔵 Primary (синий)",
        "success": "🟢 Success (зелёный)",
        "danger": "🔴 Danger (красный)",
        "none": "⚪ Без цвета",
    }
    
    await callback.message.edit_text(
        f"✅ Цвет кнопок: {color_names.get(color_key)}\n\n"
        "📍 Шаг 6/6: Добавить иконки на кнопки?",
        reply_markup=BuilderKeyboards.button_icon()
    )
    await callback.answer()


# Step 6: Button icon
@router.callback_query(BuilderStates.select_button_icon, F.data.startswith("builder:icon:"))
async def select_button_icon(callback: CallbackQuery, state: FSMContext) -> None:
    """Handle button icon selection."""
    use_icon = callback.data.split(":")[-1] == "yes"
    await state.update_data(button_icon=use_icon)
    await state.set_state(BuilderStates.preview)
    
    icon_text = "Да" if use_icon else "Нет"
    
    await callback.message.edit_text(
        f"✅ Иконки на кнопках: {icon_text}\n\n"
        "🎉 Все параметры выбраны!\n"
        "Создаю превью поста...",
    )
    
    # Generate and send preview
    await generate_preview(callback, state)
    await callback.answer()


@router.callback_query(F.data == "builder:preview")
async def direct_preview(callback: CallbackQuery, state: FSMContext) -> None:
    """Direct preview generation (when skipping button options)."""
    await callback.message.edit_text("🎉 Создаю превью поста...")
    await generate_preview(callback, state)
    await callback.answer()


async def generate_preview(callback: CallbackQuery, state: FSMContext) -> None:
    """Generate and send post preview based on collected data."""
    data = await state.get_data()
    
    template_key = data.get("template", "announcement")
    headline_format = data.get("headline_format", HeadlineFormat.BOLD)
    use_custom_emoji = data.get("use_custom_emoji", True)
    button_type = data.get("button_type", "inline")
    button_color = data.get("button_color", ButtonStyle.DEFAULT)
    button_icon = data.get("button_icon", False)
    
    # Get base template
    template = TEMPLATES.get(template_key)
    if not template:
        await callback.message.answer(
            "❌ Ошибка: шаблон не найден",
            reply_markup=BuilderKeyboards.preview_actions()
        )
        return
    
    # Build configuration summary
    config_summary = (
        "📋 Конфигурация поста:\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        f"• Шаблон: {template.name}\n"
        f"• Заголовок: {headline_format.value}\n"
        f"• Custom emoji: {'Да' if use_custom_emoji else 'Нет'}\n"
        f"• Кнопки: {button_type}\n"
        f"• Цвет кнопок: {button_color.value if button_color else 'Нет'}\n"
        f"• Иконки: {'Да' if button_icon else 'Нет'}\n"
    )
    
    await callback.message.answer(config_summary)
    
    # Generate post
    await callback.message.answer("📍 Превью поста:\n━━━━━━━━━━━━━━━━━━━━━━")
    
    # Create post content
    content, keyboard = post_factory.create_template_post(
        template_key,
        use_custom_emoji=use_custom_emoji,
        use_button_icons=button_icon,
        use_button_styles=button_color != ButtonStyle.DEFAULT if button_color else False,
    )
    
    # Handle no buttons case
    if button_type == "none":
        keyboard = None
    
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=keyboard
    )
    
    # Send actions
    await callback.message.answer(
        "👆 Это превью вашего поста.\n\n"
        "Что дальше?",
        reply_markup=BuilderKeyboards.preview_actions()
    )


# Navigation and control handlers
@router.callback_query(F.data == "builder:cancel")
async def builder_cancel(callback: CallbackQuery, state: FSMContext) -> None:
    """Cancel builder and return to menu."""
    await state.clear()
    await callback.message.edit_text(
        "❌ Конструктор отменён.\n\n"
        "Используйте /builder для нового запуска."
    )
    await callback.answer()


@router.callback_query(F.data == "builder:restart")
async def builder_restart(callback: CallbackQuery, state: FSMContext) -> None:
    """Restart the builder."""
    await state.clear()
    await state.set_state(BuilderStates.select_template)
    
    await callback.message.answer(
        "🔄 Начинаем заново!\n\n"
        "🛠 Конструктор постов\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📍 Шаг 1/6: Выберите тип шаблона:",
        reply_markup=BuilderKeyboards.template_selection()
    )
    await callback.answer()


@router.callback_query(F.data == "builder:edit")
async def builder_edit(callback: CallbackQuery, state: FSMContext) -> None:
    """Edit - restart from beginning."""
    await state.set_state(BuilderStates.select_template)
    
    await callback.message.answer(
        "✏️ Редактирование\n\n"
        "📍 Шаг 1/6: Выберите тип шаблона:",
        reply_markup=BuilderKeyboards.template_selection()
    )
    await callback.answer()


# Back navigation handlers
@router.callback_query(F.data == "builder:back:template")
async def back_to_template(callback: CallbackQuery, state: FSMContext) -> None:
    """Go back to template selection."""
    await state.set_state(BuilderStates.select_template)
    await callback.message.edit_text(
        "📍 Шаг 1/6: Выберите тип шаблона:",
        reply_markup=BuilderKeyboards.template_selection()
    )
    await callback.answer()


@router.callback_query(F.data == "builder:back:headline")
async def back_to_headline(callback: CallbackQuery, state: FSMContext) -> None:
    """Go back to headline format selection."""
    await state.set_state(BuilderStates.select_headline)
    data = await state.get_data()
    template_key = data.get("template", "announcement")
    
    await callback.message.edit_text(
        f"✅ Выбран шаблон: {TEMPLATES[template_key].name}\n\n"
        "📍 Шаг 2/6: Выберите формат заголовка:",
        reply_markup=BuilderKeyboards.headline_format()
    )
    await callback.answer()


@router.callback_query(F.data == "builder:back:emoji")
async def back_to_emoji(callback: CallbackQuery, state: FSMContext) -> None:
    """Go back to emoji selection."""
    await state.set_state(BuilderStates.select_emoji)
    await callback.message.edit_text(
        "📍 Шаг 3/6: Использовать кастомные эмодзи?",
        reply_markup=BuilderKeyboards.custom_emoji()
    )
    await callback.answer()


@router.callback_query(F.data == "builder:back:btntype")
async def back_to_btntype(callback: CallbackQuery, state: FSMContext) -> None:
    """Go back to button type selection."""
    await state.set_state(BuilderStates.select_button_type)
    await callback.message.edit_text(
        "📍 Шаг 4/6: Выберите тип кнопок:",
        reply_markup=BuilderKeyboards.button_type()
    )
    await callback.answer()


@router.callback_query(F.data == "builder:back:color")
async def back_to_color(callback: CallbackQuery, state: FSMContext) -> None:
    """Go back to button color selection."""
    await state.set_state(BuilderStates.select_button_color)
    await callback.message.edit_text(
        "📍 Шаг 5/6: Выберите цвет кнопок:",
        reply_markup=BuilderKeyboards.button_color()
    )
    await callback.answer()
"""Builder handler - /builder command with FSM-based post constructor."""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.formatting import Text, Bold, Italic, as_list

from config.templates import (
    TEMPLATES, 
    HeadlineFormat, 
    ButtonStyle,
    ButtonConfig,
)
from services.post_factory import post_factory
from services.button_factory import button_factory
from services.emoji_registry import emoji_service
from keyboards.builder_kb import BuilderKeyboards
from keyboards.menu import get_back_button


router = Router(name="builder")


class BuilderStates(StatesGroup):
    """FSM states for the post builder."""
    select_template = State()
    select_headline = State()
    select_emoji = State()
    select_button_type = State()
    select_button_color = State()
    select_button_icon = State()
    preview = State()


@router.message(Command("builder"))
async def cmd_builder(message: Message, state: FSMContext) -> None:
    """Handle /builder command - start the post constructor."""
    await state.clear()
    await state.set_state(BuilderStates.select_template)
    
    await message.answer(
        "🛠 Конструктор постов\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Создайте свой пост пошагово.\n\n"
        "📍 Шаг 1/6: Выберите тип шаблона:",
        reply_markup=BuilderKeyboards.template_selection()
    )


# Step 1: Template selection
@router.callback_query(BuilderStates.select_template, F.data.startswith("builder:template:"))
async def select_template(callback: CallbackQuery, state: FSMContext) -> None:
    """Handle template selection."""
    template_key = callback.data.split(":")[-1]
    await state.update_data(template=template_key)
    await state.set_state(BuilderStates.select_headline)
    
    await callback.message.edit_text(
        f"✅ Выбран шаблон: {TEMPLATES[template_key].name}\n\n"
        "📍 Шаг 2/6: Выберите формат заголовка:",
        reply_markup=BuilderKeyboards.headline_format()
    )
    await callback.answer()


# Step 2: Headline format
@router.callback_query(BuilderStates.select_headline, F.data.startswith("builder:headline:"))
async def select_headline(callback: CallbackQuery, state: FSMContext) -> None:
    """Handle headline format selection."""
    format_key = callback.data.split(":")[-1]
    format_map = {
        "plain": HeadlineFormat.PLAIN,
        "bold": HeadlineFormat.BOLD,
        "italic": HeadlineFormat.ITALIC,
        "bold_italic": HeadlineFormat.BOLD_ITALIC,
    }
    await state.update_data(headline_format=format_map.get(format_key, HeadlineFormat.BOLD))
    await state.set_state(BuilderStates.select_emoji)
    
    format_names = {
        "plain": "Обычный",
        "bold": "Жирный",
        "italic": "Курсив",
        "bold_italic": "Жирный курсив",
    }
    
    await callback.message.edit_text(
        f"✅ Формат заголовка: {format_names.get(format_key, format_key)}\n\n"
        "📍 Шаг 3/6: Использовать кастомные эмодзи?",
        reply_markup=BuilderKeyboards.custom_emoji()
    )
    await callback.answer()


# Step 3: Custom emoji
@router.callback_query(BuilderStates.select_emoji, F.data.startswith("builder:emoji:"))
async def select_emoji(callback: CallbackQuery, state: FSMContext) -> None:
    """Handle custom emoji selection."""
    use_emoji = callback.data.split(":")[-1] == "yes"
    await state.update_data(use_custom_emoji=use_emoji)
    await state.set_state(BuilderStates.select_button_type)
    
    emoji_text = "Да" if use_emoji else "Нет (Unicode)"
    
    await callback.message.edit_text(
        f"✅ Кастомные эмодзи: {emoji_text}\n\n"
        "📍 Шаг 4/6: Выберите тип кнопок:",
        reply_markup=BuilderKeyboards.button_type()
    )
    await callback.answer()


# Step 4: Button type
@router.callback_query(BuilderStates.select_button_type, F.data.startswith("builder:btntype:"))
async def select_button_type(callback: CallbackQuery, state: FSMContext) -> None:
    """Handle button type selection."""
    btn_type = callback.data.split(":")[-1]
    await state.update_data(button_type=btn_type)
    
    type_names = {
        "inline": "Inline кнопки",
        "reply": "Reply кнопки",
        "none": "Без кнопок",
    }
    
    if btn_type == "none":
        # Skip to preview if no buttons
        await state.update_data(button_color=None, button_icon=False)
        await state.set_state(BuilderStates.preview)
        await callback.message.edit_text(
            f"✅ Тип кнопок: {type_names.get(btn_type)}\n\n"
            "📍 Готово! Создаём превью...",
            reply_markup=BuilderKeyboards.skip_button_options()
        )
    else:
        await state.set_state(BuilderStates.select_button_color)
        await callback.message.edit_text(
            f"✅ Тип кнопок: {type_names.get(btn_type)}\n\n"
            "📍 Шаг 5/6: Выберите цвет кнопок:",
            reply_markup=BuilderKeyboards.button_color()
        )
    await callback.answer()


# Step 5: Button color
@router.callback_query(BuilderStates.select_button_color, F.data.startswith("builder:color:"))
async def select_button_color(callback: CallbackQuery, state: FSMContext) -> None:
    """Handle button color selection."""
    color_key = callback.data.split(":")[-1]
    color_map = {
        "primary": ButtonStyle.PRIMARY,
        "success": ButtonStyle.SUCCESS,
        "danger": ButtonStyle.DANGER,
        "none": ButtonStyle.DEFAULT,
    }
    await state.update_data(button_color=color_map.get(color_key, ButtonStyle.DEFAULT))
    await state.set_state(BuilderStates.select_button_icon)
    
    color_names = {
        "primary": "🔵 Primary (синий)",
        "success": "🟢 Success (зелёный)",
        "danger": "🔴 Danger (красный)",
        "none": "⚪ Без цвета",
    }
    
    await callback.message.edit_text(
        f"✅ Цвет кнопок: {color_names.get(color_key)}\n\n"
        "📍 Шаг 6/6: Добавить иконки на кнопки?",
        reply_markup=BuilderKeyboards.button_icon()
    )
    await callback.answer()


# Step 6: Button icon
@router.callback_query(BuilderStates.select_button_icon, F.data.startswith("builder:icon:"))
async def select_button_icon(callback: CallbackQuery, state: FSMContext) -> None:
    """Handle button icon selection."""
    use_icon = callback.data.split(":")[-1] == "yes"
    await state.update_data(button_icon=use_icon)
    await state.set_state(BuilderStates.preview)
    
    icon_text = "Да" if use_icon else "Нет"
    
    await callback.message.edit_text(
        f"✅ Иконки на кнопках: {icon_text}\n\n"
        "🎉 Все параметры выбраны!\n"
        "Создаю превью поста...",
    )
    
    # Generate and send preview
    await generate_preview(callback, state)
    await callback.answer()


@router.callback_query(F.data == "builder:preview")
async def direct_preview(callback: CallbackQuery, state: FSMContext) -> None:
    """Direct preview generation (when skipping button options)."""
    await callback.message.edit_text("🎉 Создаю превью поста...")
    await generate_preview(callback, state)
    await callback.answer()


async def generate_preview(callback: CallbackQuery, state: FSMContext) -> None:
    """Generate and send post preview based on collected data."""
    data = await state.get_data()
    
    template_key = data.get("template", "announcement")
    headline_format = data.get("headline_format", HeadlineFormat.BOLD)
    use_custom_emoji = data.get("use_custom_emoji", True)
    button_type = data.get("button_type", "inline")
    button_color = data.get("button_color", ButtonStyle.DEFAULT)
    button_icon = data.get("button_icon", False)
    
    # Get base template
    template = TEMPLATES.get(template_key)
    if not template:
        await callback.message.answer(
            "❌ Ошибка: шаблон не найден",
            reply_markup=BuilderKeyboards.preview_actions()
        )
        return
    
    # Build configuration summary
    config_summary = (
        "📋 Конфигурация поста:\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        f"• Шаблон: {template.name}\n"
        f"• Заголовок: {headline_format.value}\n"
        f"• Custom emoji: {'Да' if use_custom_emoji else 'Нет'}\n"
        f"• Кнопки: {button_type}\n"
        f"• Цвет кнопок: {button_color.value if button_color else 'Нет'}\n"
        f"• Иконки: {'Да' if button_icon else 'Нет'}\n"
    )
    
    await callback.message.answer(config_summary)
    
    # Generate post
    await callback.message.answer("📍 Превью поста:\n━━━━━━━━━━━━━━━━━━━━━━")
    
    # Create post content
    content, keyboard = post_factory.create_template_post(
        template_key,
        use_custom_emoji=use_custom_emoji,
        use_button_icons=button_icon,
        use_button_styles=button_color != ButtonStyle.DEFAULT if button_color else False,
    )
    
    # Handle no buttons case
    if button_type == "none":
        keyboard = None
    
    await callback.message.answer(
        **content.as_kwargs(),
        reply_markup=keyboard
    )
    
    # Send actions
    await callback.message.answer(
        "👆 Это превью вашего поста.\n\n"
        "Что дальше?",
        reply_markup=BuilderKeyboards.preview_actions()
    )


# Navigation and control handlers
@router.callback_query(F.data == "builder:cancel")
async def builder_cancel(callback: CallbackQuery, state: FSMContext) -> None:
    """Cancel builder and return to menu."""
    await state.clear()
    await callback.message.edit_text(
        "❌ Конструктор отменён.\n\n"
        "Используйте /builder для нового запуска."
    )
    await callback.answer()


@router.callback_query(F.data == "builder:restart")
async def builder_restart(callback: CallbackQuery, state: FSMContext) -> None:
    """Restart the builder."""
    await state.clear()
    await state.set_state(BuilderStates.select_template)
    
    await callback.message.answer(
        "🔄 Начинаем заново!\n\n"
        "🛠 Конструктор постов\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📍 Шаг 1/6: Выберите тип шаблона:",
        reply_markup=BuilderKeyboards.template_selection()
    )
    await callback.answer()


@router.callback_query(F.data == "builder:edit")
async def builder_edit(callback: CallbackQuery, state: FSMContext) -> None:
    """Edit - restart from beginning."""
    await state.set_state(BuilderStates.select_template)
    
    await callback.message.answer(
        "✏️ Редактирование\n\n"
        "📍 Шаг 1/6: Выберите тип шаблона:",
        reply_markup=BuilderKeyboards.template_selection()
    )
    await callback.answer()


# Back navigation handlers
@router.callback_query(F.data == "builder:back:template")
async def back_to_template(callback: CallbackQuery, state: FSMContext) -> None:
    """Go back to template selection."""
    await state.set_state(BuilderStates.select_template)
    await callback.message.edit_text(
        "📍 Шаг 1/6: Выберите тип шаблона:",
        reply_markup=BuilderKeyboards.template_selection()
    )
    await callback.answer()


@router.callback_query(F.data == "builder:back:headline")
async def back_to_headline(callback: CallbackQuery, state: FSMContext) -> None:
    """Go back to headline format selection."""
    await state.set_state(BuilderStates.select_headline)
    data = await state.get_data()
    template_key = data.get("template", "announcement")
    
    await callback.message.edit_text(
        f"✅ Выбран шаблон: {TEMPLATES[template_key].name}\n\n"
        "📍 Шаг 2/6: Выберите формат заголовка:",
        reply_markup=BuilderKeyboards.headline_format()
    )
    await callback.answer()


@router.callback_query(F.data == "builder:back:emoji")
async def back_to_emoji(callback: CallbackQuery, state: FSMContext) -> None:
    """Go back to emoji selection."""
    await state.set_state(BuilderStates.select_emoji)
    await callback.message.edit_text(
        "📍 Шаг 3/6: Использовать кастомные эмодзи?",
        reply_markup=BuilderKeyboards.custom_emoji()
    )
    await callback.answer()


@router.callback_query(F.data == "builder:back:btntype")
async def back_to_btntype(callback: CallbackQuery, state: FSMContext) -> None:
    """Go back to button type selection."""
    await state.set_state(BuilderStates.select_button_type)
    await callback.message.edit_text(
        "📍 Шаг 4/6: Выберите тип кнопок:",
        reply_markup=BuilderKeyboards.button_type()
    )
    await callback.answer()


@router.callback_query(F.data == "builder:back:color")
async def back_to_color(callback: CallbackQuery, state: FSMContext) -> None:
    """Go back to button color selection."""
    await state.set_state(BuilderStates.select_button_color)
    await callback.message.edit_text(
        "📍 Шаг 5/6: Выберите цвет кнопок:",
        reply_markup=BuilderKeyboards.button_color()
    )
    await callback.answer()
