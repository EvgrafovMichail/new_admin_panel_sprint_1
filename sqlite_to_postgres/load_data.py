import os

from db_tools.save_load_utils import transfer_data
from models.db_models import db_model_mapping


def main() -> None:
    path_to_sqlite = os.path.join("db.sqlite")
    assert os.path.exists(path_to_sqlite)

    path_to_postgres = os.path.join("connection_config.json")
    assert os.path.exists(path_to_postgres)

    transfer_data(
        path_to_postgres,
        path_to_sqlite,
        db_model_mapping,
    )


if __name__ == "__main__":
    main()
