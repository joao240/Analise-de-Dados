from src.extract import extract_data, missing_values, validate_and_convert_types
from src.transform import calculation_total_value, Addressing_outliers, handle_empty_values
from src.load import load_to_mysql

def main():
    # EXTRACT
    df = extract_data()
    missing_values(df)
    df = validate_and_convert_types(df)

    # TRANSFORM
    df = calculation_total_value(df)
    df = Addressing_outliers(df)
    df = handle_empty_values(df)

    # LOAD (MySQL)
    load_to_mysql(
        df=df,
        user="root",
        host="localhost",
        port="3306",
        database="analiseDados",
        table_name="sales",
        if_exists="replace"
    )

if __name__ == "__main__":
    main()
