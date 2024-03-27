from typing import Any

from psycopg2.extras import DictCursor

from db_tools.save_load_utils import (
    connect_to_postgresql,
    connect_to_sqlite,
)


def convert_content_to_str(_dict: dict[Any, Any]) -> dict[Any, str]:
    for key in _dict:
        _dict[key] = str(_dict[key])

    return _dict


def test_tables_size(
    path_to_postgres: str,
    path_to_sqlite: str,
    db_model_mapping: dict[str, type],
) -> None:
    with (
        connect_to_postgresql(path_to_postgres) as connection_postgres,
        connect_to_sqlite(path_to_sqlite) as connection_sqlite,
    ):
        cursor_postgres = connection_postgres.cursor()
        cursor_sqlite = connection_sqlite.cursor()

        for table_name in db_model_mapping:
            select_statement = f"SELECT * from {table_name}"

            cursor_postgres.execute(select_statement)
            data_postgres = cursor_postgres.fetchall()

            cursor_sqlite.execute(select_statement)
            data_sqlite = cursor_sqlite.fetchall()

            assert len(data_postgres) == len(data_sqlite), table_name


def test_tables_content(
    path_to_postgres: str,
    path_to_sqlite: str,
    db_model_mapping: dict[str, type],
) -> None:
    with (
        connect_to_postgresql(path_to_postgres) as connection_postgres,
        connect_to_sqlite(path_to_sqlite) as connection_sqlite,
    ):
        cursor_postgres = connection_postgres.cursor(cursor_factory=DictCursor)
        cursor_sqlite = connection_sqlite.cursor()

        for table_name, model in db_model_mapping.items():
            select_statement = f"SELECT * from {table_name}"

            cursor_postgres.execute(select_statement)
            data_postgres = [model(**convert_content_to_str(dict(record))) for record in cursor_postgres.fetchall()]

            cursor_sqlite.execute(select_statement)
            data_sqlite = [model(**convert_content_to_str(dict(record))) for record in cursor_sqlite.fetchall()]

            assert data_postgres == data_sqlite, table_name
