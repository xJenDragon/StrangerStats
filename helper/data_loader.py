# data_loader.py
"""
Utility functions to load Stranger Stats datasets
from a local Excel file with multiple sheets.
"""

import pandas as pd

def load_sheet(DATA_FILE, sheet_name: str) -> pd.DataFrame:
    """
    Load a single sheet from the Stranger Stats Excel file.

    Args:
        DATA_FILE (str or Path): Path to the Excel file.
        sheet_name (str): The sheet name (e.g. "monster_sightings").

    Returns:
        pd.DataFrame: The data as a pandas DataFrame.
    """
    return pd.read_excel(DATA_FILE, sheet_name=sheet_name)


def load_monster_sightings(DATA_FILE) -> pd.DataFrame:
    """Load the Monster Sightings sheet from the provided Excel file."""
    return load_sheet(DATA_FILE, "monster_sightings")


def load_character_stats(DATA_FILE) -> pd.DataFrame:
    """Load the Character Stats sheet from the provided Excel file."""
    return load_sheet(DATA_FILE, "character_stats")


def load_upside_down_events(DATA_FILE) -> pd.DataFrame:
    """Load the Upside Down Events sheet from the provided Excel file."""
    return load_sheet(DATA_FILE, "upside_down_events")


