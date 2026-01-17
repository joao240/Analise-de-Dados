import pandas as pd

from src.transform import (
    calculation_total_value,
    Addressing_outliers,
    handle_empty_values,
)

def test_calculation_total_value_creates_and_calculates_column():
    df = pd.DataFrame({
        "QUANTITYORDERED": [2, 3],
        "PRICEEACH": [10.0, 5.0],
    })

    out = calculation_total_value(df.copy())

    assert "TOTAL_VALUE" in out.columns
    assert out["TOTAL_VALUE"].tolist() == [20.0, 15.0]


def test_addressing_outliers_removes_extreme_quantity():
    df = pd.DataFrame({
        "QUANTITYORDERED": [10, 11, 9, 10, 12, 11, 10, 9, 10, 9999],
        "PRICEEACH": [100.0] * 10,
    })

    out = Addressing_outliers(df.copy())

    assert 9999 not in out["QUANTITYORDERED"].values
    assert len(out) == 9


def test_handle_empty_values_fills_nans_and_normalizes_text():
    df = pd.DataFrame({
        "PRICEEACH": [10.0, None, 30.0],
        "CITY": ["  São Paulo  ", None, "RIO "],
    })

    out = handle_empty_values(df.copy())

    assert out.loc[1, "PRICEEACH"] == 20.0
    assert out.loc[1, "CITY"] == "unknown"
    assert out.loc[0, "CITY"] == "são paulo"
    assert out.loc[2, "CITY"] == "rio"
