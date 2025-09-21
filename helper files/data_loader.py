# data_loader.py
"""
Utility functions to load Stranger STATS datasets
from a Google Sheet with multiple sheets.
"""

import pandas as pd
from pathlib import Path

# Put your Google Sheet ID here
DATA_FILE = Path("data/stranger_stats.xlsx")

def load_sheet(sheet_name: str) -> pd.DataFrame:
    """
    Load a single sheet from the Stranger Stats Excel file.

    Args:
        sheet_name (str): The sheet name (e.g. "monster_sightings").

    Returns:
        pd.DataFrame: The data as a pandas DataFrame.
    """
    return pd.read_excel(DATA_FILE, sheet_name=sheet_name)


def load_monster_sightings() -> pd.DataFrame:
    """Load the Monster Sightings sheet."""
    return load_sheet("monster_sightings")


def load_character_stats() -> pd.DataFrame:
    """Load the Character Stats sheet."""
    return load_sheet("character_stats")


def load_upside_down_events() -> pd.DataFrame:
    """Load the Upside Down Events sheet."""
    return load_sheet("upside_down_events")


