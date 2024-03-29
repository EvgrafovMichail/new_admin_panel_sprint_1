from models.db_models import db_model_mapping
from tests.testing_utils import (
    test_tables_content,
    test_tables_size,
)

from settings import (
    SQLITE_PATH,
    DB_CONFIG,
    BATCH_SIZE,
)


def main() -> None:
    test_tables_size(
        DB_CONFIG,
        SQLITE_PATH,
        db_model_mapping,
    )
    test_tables_content(
        DB_CONFIG,
        SQLITE_PATH,
        db_model_mapping,
        BATCH_SIZE,
    )


if __name__ == "__main__":
    main()
