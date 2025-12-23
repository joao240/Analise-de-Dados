import pandas as pd
from sqlalchemy import create_engine

def load_to_mysql(
    df: pd.DataFrame,
    user: str,
    host: str,
    port: str,
    database: str,
    table_name: str,
    if_exists: str = "replace"
) -> None:
    """
    Carrega um DataFrame no MySQL usando SQLAlchemy.
    """

    conn_string = (
        f"mysql+pymysql://{user}@{host}:{port}/{database}"
    )

    engine = create_engine(conn_string)

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists=if_exists,
        index=False
    )

    print(f"✅ Dados carregados com sucesso na tabela '{table_name}'")
