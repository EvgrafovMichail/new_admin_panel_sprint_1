import contextlib
import random
import uuid
import json

from argparse import Namespace
from datetime import datetime
from typing import Union

import psycopg2

from faker import Faker
from psycopg2.extras import execute_batch


def parse_arguments(
    args: Namespace
) -> tuple[dict, int, int]:
    path_to_config = args.config_path

    with open(path_to_config, "r") as file:
        connection_config = json.load(file)

    if (person_amount := args.amount) <= 0:
        raise ValueError("person amount should be natural number")

    if (page_size := args.size) <= 0:
        raise ValueError("page_size should be natural number")

    return connection_config, person_amount, page_size


def fill_persons_tables(
    connection_config: dict[str, Union[str, int]],
    person_amount: int,
    page_size: int
) -> None:
    date_curr = datetime.utcnow()
    fake = Faker()

    with (
        contextlib.closing(psycopg2.connect(**connection_config)) as connection,
        connection.cursor() as cursor
    ):
        persons_ids = [str(uuid.uuid4()) for _ in range(person_amount)]
        data = [(pk, fake.last_name(), date_curr, date_curr) for pk in persons_ids]

        query = "INSERT INTO person (id, full_name, created, modified) VALUES (%s, %s, %s, %s)"
        execute_batch(cursor, query, data, page_size=page_size)
        connection.commit()

        person_film_work_data = []
        roles = ["actor", "producer", "director"]

        cursor.execute("SELECT id FROM film_work")
        film_works_ids = [data[0] for data in cursor.fetchall()]

        for film_work_id in film_works_ids:
            for person_id in random.sample(persons_ids, 5):
                role = random.choice(roles)
                person_film_work_data.append(
                    (
                        str(uuid.uuid4()),
                        film_work_id,
                        person_id,
                        role,
                        date_curr,
                    ),
                )

        query = (
            "INSERT INTO person_film_work (id, film_work_id,"
            " person_id, role, created) VALUES (%s, %s, %s, %s, %s)"
        )
        execute_batch(cursor, query, person_film_work_data, page_size=page_size)
        connection.commit()
