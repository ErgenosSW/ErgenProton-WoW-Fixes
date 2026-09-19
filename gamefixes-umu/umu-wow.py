"""Compatibility profile for Battle.net and World of Warcraft."""

from protonfixes import util


def early() -> None:
    """Apply settings required before the Wine session starts."""
    util.set_environment('WINE_SIMULATE_WRITECOPY', '1')
