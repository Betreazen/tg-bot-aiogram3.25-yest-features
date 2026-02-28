"""
Post Styling Demo Bot - Entry Point

A Telegram bot demonstrating post styling and visual message presentation
capabilities using aiogram 3.25.0.

Features:
- Rich text formatting
- Custom emoji in messages
- Colored buttons (primary/success/danger)
- Buttons with emoji icons
- Fallback mechanisms for unsupported features
"""

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config.settings import settings
from handlers import (
    start_router,
    text_demo_router,
    post_demo_router,
    emoji_demo_router,
    buttons_demo_router,
    builder_router,
)


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)


async def main() -> None:
    """Initialize and start the bot."""
    logger.info("Starting Post Styling Demo Bot...")
    
    # Initialize bot with default properties
    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        )
    )
    
    # Initialize dispatcher with memory storage for FSM
    dp = Dispatcher(storage=MemoryStorage())
    
    # Register routers
    dp.include_router(start_router)
    dp.include_router(text_demo_router)
    dp.include_router(post_demo_router)
    dp.include_router(emoji_demo_router)
    dp.include_router(buttons_demo_router)
    dp.include_router(builder_router)
    
    # Log startup info
    logger.info(f"Custom emoji enabled: {settings.CUSTOM_EMOJI_ENABLED}")
    logger.info(f"Fallback enabled: {settings.FALLBACK_ENABLED}")
    
    # Start polling
    try:
        logger.info("Bot started successfully!")
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        logger.info("Bot stopped.")
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)
