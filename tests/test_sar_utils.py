from types import SimpleNamespace

import numpy as np
import xarray as xr

from sar_utils import find_items_missing_polarizations, linear_to_db


# --------------------------------------------------
# Polarization validation tests
# --------------------------------------------------

def test_all_items_have_required_polarizations():
    items = [
        SimpleNamespace(
            id="scene_001",
            properties={"sar:polarizations": ["VV", "VH"]},
        ),
        SimpleNamespace(
            id="scene_002",
            properties={"sar:polarizations": ["VH", "VV"]},
        ),
    ]

    result = find_items_missing_polarizations(items)

    assert result == []


def test_item_missing_vh_polarization():
    items = [
        SimpleNamespace(
            id="scene_001",
            properties={"sar:polarizations": ["VV", "VH"]},
        ),
        SimpleNamespace(
            id="scene_002",
            properties={"sar:polarizations": ["VV"]},
        ),
    ]

    result = find_items_missing_polarizations(items)

    assert result == ["scene_002"]


def test_item_with_no_polarizations():
    items = [
        SimpleNamespace(
            id="scene_003",
            properties={},
        )
    ]

    result = find_items_missing_polarizations(items)

    assert result == ["scene_003"]


# --------------------------------------------------
# Backscatter conversion tests
# --------------------------------------------------

def test_linear_to_db_conversion():
    data = xr.DataArray([1.0, 0.1, 0.01])

    result = linear_to_db(data)

    np.testing.assert_allclose(
        result.values,
        [0.0, -10.0, -20.0],
        atol=1e-10,
    )


def test_linear_to_db_masks_invalid_values():
    data = xr.DataArray([0.1, 0.0, -1.0])

    result = linear_to_db(data)

    assert np.isclose(result.values[0], -10.0)
    assert np.isnan(result.values[1])
    assert np.isnan(result.values[2])
