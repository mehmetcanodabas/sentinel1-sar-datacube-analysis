import numpy as np


def find_items_missing_polarizations(items):
    """Find STAC items that do not contain both VV and VH polarizations."""
    required_polarizations = {"VV", "VH"}

    return [
        item.id
        for item in items
        if not required_polarizations.issubset(
            set(item.properties.get("sar:polarizations", []))
        )
    ]


def linear_to_db(data):
    """Convert positive linear SAR backscatter values to decibels."""
    return 10 * np.log10(data.where(data > 0))
