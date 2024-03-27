import os

from models.db_models import db_model_mapping
from tests.testing_utils import (
    test_tables_content,
    test_tables_size,
)


def main() -> None:
    path_to_sqlite = os.path.join("db.sqlite")
    assert os.path.exists(path_to_sqlite)

    path_to_postgres = os.path.join("connection_config.json")
    assert os.path.exists(path_to_postgres)

    test_tables_size(
        path_to_postgres,
        path_to_sqlite,
        db_model_mapping,
    )
    test_tables_content(
        path_to_postgres,
        path_to_sqlite,
        db_model_mapping,
    )


if __name__ == "__main__":
    main()
