"""Bot configuration settings."""

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    BOT_TOKEN: str = Field(..., description="Telegram bot token")
    CUSTOM_EMOJI_ENABLED: bool = Field(
        default=True, 
        description="Enable custom emoji features"
    )
    FALLBACK_ENABLED: bool = Field(
        default=True, 
        description="Enable automatic fallback behavior"
    )
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
"""Bot configuration settings."""

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    BOT_TOKEN: str = Field(..., description="Telegram bot token")
    CUSTOM_EMOJI_ENABLED: bool = Field(
        default=True, 
        description="Enable custom emoji features"
    )
    FALLBACK_ENABLED: bool = Field(
        default=True, 
        description="Enable automatic fallback behavior"
    )
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
