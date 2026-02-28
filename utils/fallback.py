"""Fallback detection and handling utilities."""

from dataclasses import dataclass
from config.settings import settings


@dataclass
class FallbackStatus:
    """Status of fallback mechanisms."""
    custom_emoji_available: bool
    button_icons_available: bool
    button_styles_available: bool
    fallback_notice: str = ""


class FallbackChecker:
    """Utility class for checking feature availability and managing fallbacks."""
    
    FALLBACK_NOTICE = "ℹ️ Custom emoji fallback enabled"
    
    def __init__(self):
        self._custom_emoji_available: bool = settings.CUSTOM_EMOJI_ENABLED
        self._button_icons_available: bool = settings.CUSTOM_EMOJI_ENABLED
        self._fallback_enabled: bool = settings.FALLBACK_ENABLED
    
    @property
    def custom_emoji_available(self) -> bool:
        """Check if custom emoji feature is available."""
        return self._custom_emoji_available
    
    @property
    def button_icons_available(self) -> bool:
        """Check if button icons feature is available."""
        return self._button_icons_available
    
    @property
    def button_styles_available(self) -> bool:
        """Button styles are always available (client handles graceful degradation)."""
        return True
    
    @property
    def fallback_enabled(self) -> bool:
        """Check if fallback mode is enabled."""
        return self._fallback_enabled
    
    def set_custom_emoji_available(self, available: bool) -> None:
        """Manually set custom emoji availability."""
        self._custom_emoji_available = available
    
    def set_button_icons_available(self, available: bool) -> None:
        """Manually set button icons availability."""
        self._button_icons_available = available
    
    def get_status(self) -> FallbackStatus:
        """Get current fallback status."""
        notice = ""
        if self._fallback_enabled and not self._custom_emoji_available:
            notice = self.FALLBACK_NOTICE
        
        return FallbackStatus(
            custom_emoji_available=self._custom_emoji_available,
            button_icons_available=self._button_icons_available,
            button_styles_available=True,
            fallback_notice=notice
        )
    
    def should_use_fallback(self) -> bool:
        """Check if fallback should be used for custom emoji."""
        return self._fallback_enabled and not self._custom_emoji_available
    
    def get_technical_info(self, used_emoji_ids: list[str] = None) -> str:
        """Generate technical info block for demo messages."""
        status = self.get_status()
        lines = [
            "─── Техническая информация ───",
            f"Custom emoji: {'✅ Включены' if status.custom_emoji_available else '❌ Fallback'}",
            f"Icon buttons: {'✅ Доступны' if status.button_icons_available else '❌ Недоступны'}",
            f"Button styles: {'✅ Доступны' if status.button_styles_available else '⚠️ Зависит от клиента'}",
        ]
        
        if used_emoji_ids:
            lines.append(f"Использованные emoji ID: {', '.join(used_emoji_ids[:3])}...")
        
        if status.fallback_notice:
            lines.append(f"\n{status.fallback_notice}")
        
        return "\n".join(lines)


# Global fallback checker instance
fallback_checker = FallbackChecker()
"""Fallback detection and handling utilities."""

from dataclasses import dataclass
from config.settings import settings


@dataclass
class FallbackStatus:
    """Status of fallback mechanisms."""
    custom_emoji_available: bool
    button_icons_available: bool
    button_styles_available: bool
    fallback_notice: str = ""


class FallbackChecker:
    """Utility class for checking feature availability and managing fallbacks."""
    
    FALLBACK_NOTICE = "ℹ️ Custom emoji fallback enabled"
    
    def __init__(self):
        self._custom_emoji_available: bool = settings.CUSTOM_EMOJI_ENABLED
        self._button_icons_available: bool = settings.CUSTOM_EMOJI_ENABLED
        self._fallback_enabled: bool = settings.FALLBACK_ENABLED
    
    @property
    def custom_emoji_available(self) -> bool:
        """Check if custom emoji feature is available."""
        return self._custom_emoji_available
    
    @property
    def button_icons_available(self) -> bool:
        """Check if button icons feature is available."""
        return self._button_icons_available
    
    @property
    def button_styles_available(self) -> bool:
        """Button styles are always available (client handles graceful degradation)."""
        return True
    
    @property
    def fallback_enabled(self) -> bool:
        """Check if fallback mode is enabled."""
        return self._fallback_enabled
    
    def set_custom_emoji_available(self, available: bool) -> None:
        """Manually set custom emoji availability."""
        self._custom_emoji_available = available
    
    def set_button_icons_available(self, available: bool) -> None:
        """Manually set button icons availability."""
        self._button_icons_available = available
    
    def get_status(self) -> FallbackStatus:
        """Get current fallback status."""
        notice = ""
        if self._fallback_enabled and not self._custom_emoji_available:
            notice = self.FALLBACK_NOTICE
        
        return FallbackStatus(
            custom_emoji_available=self._custom_emoji_available,
            button_icons_available=self._button_icons_available,
            button_styles_available=True,
            fallback_notice=notice
        )
    
    def should_use_fallback(self) -> bool:
        """Check if fallback should be used for custom emoji."""
        return self._fallback_enabled and not self._custom_emoji_available
    
    def get_technical_info(self, used_emoji_ids: list[str] = None) -> str:
        """Generate technical info block for demo messages."""
        status = self.get_status()
        lines = [
            "─── Техническая информация ───",
            f"Custom emoji: {'✅ Включены' if status.custom_emoji_available else '❌ Fallback'}",
            f"Icon buttons: {'✅ Доступны' if status.button_icons_available else '❌ Недоступны'}",
            f"Button styles: {'✅ Доступны' if status.button_styles_available else '⚠️ Зависит от клиента'}",
        ]
        
        if used_emoji_ids:
            lines.append(f"Использованные emoji ID: {', '.join(used_emoji_ids[:3])}...")
        
        if status.fallback_notice:
            lines.append(f"\n{status.fallback_notice}")
        
        return "\n".join(lines)


# Global fallback checker instance
fallback_checker = FallbackChecker()
