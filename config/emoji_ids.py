"""Custom emoji ID registry configuration."""

from dataclasses import dataclass
from typing import Dict


@dataclass
class EmojiEntry:
    """Single emoji entry with custom ID and Unicode fallback."""
    custom_emoji_id: str
    unicode_fallback: str
    description: str = ""


# Registry of custom emoji IDs with their Unicode fallbacks
# These IDs are examples - replace with actual custom emoji IDs from your Telegram Premium account
EMOJI_REGISTRY: Dict[str, EmojiEntry] = {
    # Status indicators
    "fire": EmojiEntry(
        custom_emoji_id="5368324170671202286",
        unicode_fallback="🔥",
        description="Fire emoji for highlights"
    ),
    "check": EmojiEntry(
        custom_emoji_id="5409099013373066849",
        unicode_fallback="✅",
        description="Checkmark for success"
    ),
    "warning": EmojiEntry(
        custom_emoji_id="5413879192267805083",
        unicode_fallback="⚠️",
        description="Warning indicator"
    ),
    "star": EmojiEntry(
        custom_emoji_id="5368324170671202287",
        unicode_fallback="⭐",
        description="Star for ratings/highlights"
    ),
    "rocket": EmojiEntry(
        custom_emoji_id="5368324170671202288",
        unicode_fallback="🚀",
        description="Rocket for launches/updates"
    ),
    "lightning": EmojiEntry(
        custom_emoji_id="5368324170671202289",
        unicode_fallback="⚡",
        description="Lightning for speed/power"
    ),
    "heart": EmojiEntry(
        custom_emoji_id="5368324170671202290",
        unicode_fallback="❤️",
        description="Heart for favorites"
    ),
    "gem": EmojiEntry(
        custom_emoji_id="5368324170671202291",
        unicode_fallback="💎",
        description="Gem for premium/valuable"
    ),
    "party": EmojiEntry(
        custom_emoji_id="5368324170671202292",
        unicode_fallback="🎉",
        description="Party for celebrations"
    ),
    "bell": EmojiEntry(
        custom_emoji_id="5368324170671202293",
        unicode_fallback="🔔",
        description="Bell for notifications"
    ),
    "gift": EmojiEntry(
        custom_emoji_id="5368324170671202294",
        unicode_fallback="🎁",
        description="Gift for offers/rewards"
    ),
    "sparkles": EmojiEntry(
        custom_emoji_id="5368324170671202295",
        unicode_fallback="✨",
        description="Sparkles for magic/new"
    ),
}

# Button icon emoji IDs (subset commonly used for buttons)
BUTTON_ICON_EMOJI: Dict[str, str] = {
    "check": "5409099013373066849",
    "warning": "5413879192267805083",
    "star": "5368324170671202287",
    "rocket": "5368324170671202288",
    "lightning": "5368324170671202289",
    "bell": "5368324170671202293",
    "gift": "5368324170671202294",
    "sparkles": "5368324170671202295",
}
"""Custom emoji ID registry configuration."""

from dataclasses import dataclass
from typing import Dict


@dataclass
class EmojiEntry:
    """Single emoji entry with custom ID and Unicode fallback."""
    custom_emoji_id: str
    unicode_fallback: str
    description: str = ""


# Registry of custom emoji IDs with their Unicode fallbacks
# These IDs are examples - replace with actual custom emoji IDs from your Telegram Premium account
EMOJI_REGISTRY: Dict[str, EmojiEntry] = {
    # Status indicators
    "fire": EmojiEntry(
        custom_emoji_id="5368324170671202286",
        unicode_fallback="🔥",
        description="Fire emoji for highlights"
    ),
    "check": EmojiEntry(
        custom_emoji_id="5409099013373066849",
        unicode_fallback="✅",
        description="Checkmark for success"
    ),
    "warning": EmojiEntry(
        custom_emoji_id="5413879192267805083",
        unicode_fallback="⚠️",
        description="Warning indicator"
    ),
    "star": EmojiEntry(
        custom_emoji_id="5368324170671202287",
        unicode_fallback="⭐",
        description="Star for ratings/highlights"
    ),
    "rocket": EmojiEntry(
        custom_emoji_id="5368324170671202288",
        unicode_fallback="🚀",
        description="Rocket for launches/updates"
    ),
    "lightning": EmojiEntry(
        custom_emoji_id="5368324170671202289",
        unicode_fallback="⚡",
        description="Lightning for speed/power"
    ),
    "heart": EmojiEntry(
        custom_emoji_id="5368324170671202290",
        unicode_fallback="❤️",
        description="Heart for favorites"
    ),
    "gem": EmojiEntry(
        custom_emoji_id="5368324170671202291",
        unicode_fallback="💎",
        description="Gem for premium/valuable"
    ),
    "party": EmojiEntry(
        custom_emoji_id="5368324170671202292",
        unicode_fallback="🎉",
        description="Party for celebrations"
    ),
    "bell": EmojiEntry(
        custom_emoji_id="5368324170671202293",
        unicode_fallback="🔔",
        description="Bell for notifications"
    ),
    "gift": EmojiEntry(
        custom_emoji_id="5368324170671202294",
        unicode_fallback="🎁",
        description="Gift for offers/rewards"
    ),
    "sparkles": EmojiEntry(
        custom_emoji_id="5368324170671202295",
        unicode_fallback="✨",
        description="Sparkles for magic/new"
    ),
}

# Button icon emoji IDs (subset commonly used for buttons)
BUTTON_ICON_EMOJI: Dict[str, str] = {
    "check": "5409099013373066849",
    "warning": "5413879192267805083",
    "star": "5368324170671202287",
    "rocket": "5368324170671202288",
    "lightning": "5368324170671202289",
    "bell": "5368324170671202293",
    "gift": "5368324170671202294",
    "sparkles": "5368324170671202295",
}
