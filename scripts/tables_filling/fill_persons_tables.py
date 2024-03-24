import argparse

from utils import (
    parse_arguments,
    fill_persons_tables,
)


parser = argparse.ArgumentParser(
    description=(
        "This program will help you to create fake"
        " records to person and person_film_work tables"
    )
)
parser.add_argument(
    "config_path",
    type=str,
    help="path to json file with data base connection config",
)
parser.add_argument(
    "--amount",
    type=int,
    default=100000,
    help="amount of records to create",
)
parser.add_argument(
    "--size",
    type=int,
    default=5000,
    help="postgresql page size",
)


if __name__ == "__main__":
    args = parser.parse_args()
    connection_config, person_amount, page_size = parse_arguments(args)
    fill_persons_tables(connection_config, person_amount, page_size)
