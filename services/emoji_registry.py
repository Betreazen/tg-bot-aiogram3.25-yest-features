"""Emoji registry service for managing custom emoji availability and fallbacks."""

from typing import Optional, Tuple, List
from aiogram.utils.formatting import CustomEmoji

from config.emoji_ids import EMOJI_REGISTRY, EmojiEntry
from utils.fallback import fallback_checker


class EmojiRegistryService:
    """Service for managing emoji insertion with fallback support."""
    
    def __init__(self):
        self._registry = EMOJI_REGISTRY
        self._used_emoji_ids: List[str] = []
    
    def get_emoji_entry(self, key: str) -> Optional[EmojiEntry]:
        """Get emoji entry by key."""
        return self._registry.get(key)
    
    def get_emoji(
        self, 
        key: str, 
        force_unicode: bool = False
    ) -> Tuple[str, Optional[str]]:
        """
        Get emoji text and custom_emoji_id.
        
        Returns:
            Tuple of (text, custom_emoji_id or None)
        """
        entry = self._registry.get(key)
        if not entry:
            return ("", None)
        
        if force_unicode or fallback_checker.should_use_fallback():
            return (entry.unicode_fallback, None)
        
        self._used_emoji_ids.append(entry.custom_emoji_id)
        return (entry.unicode_fallback, entry.custom_emoji_id)
    
    def get_custom_emoji_node(
        self, 
        key: str, 
        force_unicode: bool = False
    ) -> CustomEmoji | str:
        """
        Get CustomEmoji formatting node or unicode fallback.
        
        Returns:
            CustomEmoji node for aiogram.utils.formatting or plain string
        """
        entry = self._registry.get(key)
        if not entry:
            return ""
        
        if force_unicode or fallback_checker.should_use_fallback():
            return entry.unicode_fallback
        
        self._used_emoji_ids.append(entry.custom_emoji_id)
        return CustomEmoji(
            entry.unicode_fallback,
            custom_emoji_id=entry.custom_emoji_id
        )
    
    def get_unicode(self, key: str) -> str:
        """Get unicode fallback emoji."""
        entry = self._registry.get(key)
        return entry.unicode_fallback if entry else ""
    
    def get_custom_emoji_id(self, key: str) -> Optional[str]:
        """Get custom emoji ID by key."""
        entry = self._registry.get(key)
        return entry.custom_emoji_id if entry else None
    
    def get_used_emoji_ids(self) -> List[str]:
        """Get list of custom emoji IDs used in current session."""
        return self._used_emoji_ids.copy()
    
    def clear_used_emoji_ids(self) -> None:
        """Clear the list of used emoji IDs."""
        self._used_emoji_ids.clear()
    
    def get_all_keys(self) -> List[str]:
        """Get all available emoji keys."""
        return list(self._registry.keys())
    
    def is_available(self) -> bool:
        """Check if custom emoji feature is available."""
        return fallback_checker.custom_emoji_available


# Global emoji registry service instance
emoji_service = EmojiRegistryService()
