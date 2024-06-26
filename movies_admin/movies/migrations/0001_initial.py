import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.RunSQL(
            sql="CREATE SCHEMA IF NOT EXISTS content;",
            reverse_sql="DROP SCHEMA IF EXISTS content CASCADE;",
        ),
        migrations.CreateModel(
            name="Filmwork",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("title", models.TextField(verbose_name="title")),
                ("description", models.TextField(blank=True, verbose_name="description")),
                ("creation_date", models.DateField(blank=True, verbose_name="creation_date")),
                (
                    "rating",
                    models.FloatField(
                        blank=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="rating",
                    ),
                ),
                ("type", models.TextField(choices=[("movie", "Movie"), ("tv_show", "Tv Show")], verbose_name="type")),
            ],
            options={
                "verbose_name": "Кинопроизведение",
                "verbose_name_plural": "Кинопроизведения",
                "db_table": 'content"."film_work',
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("description", models.TextField(blank=True, verbose_name="description")),
            ],
            options={
                "verbose_name": "Жанр",
                "verbose_name_plural": "Жанры",
                "db_table": 'content"."genre',
            },
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("full_name", models.TextField(verbose_name="full_name")),
            ],
            options={
                "verbose_name": "Персона",
                "verbose_name_plural": "Персоны",
                "db_table": 'content"."person',
            },
        ),
        migrations.CreateModel(
            name="PersonFilmwork",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("role", models.TextField(verbose_name="role")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("film_work_id", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="movies.filmwork")),
                ("person_id", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="movies.person")),
            ],
            options={
                "verbose_name": "Роль персоны",
                "verbose_name_plural": "Роли персоны",
                "db_table": 'content"."person_film_work',
            },
        ),
        migrations.AddField(
            model_name="person",
            name="film_works",
            field=models.ManyToManyField(through="movies.PersonFilmwork", to="movies.filmwork"),
        ),
        migrations.CreateModel(
            name="GenreFilmwork",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("film_work_id", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="movies.filmwork")),
                ("genre_id", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="movies.genre")),
            ],
            options={
                "verbose_name": "Жанр фильма",
                "verbose_name_plural": "Жанры фильмa",
                "db_table": 'content"."genre_film_work',
            },
        ),
        migrations.AddField(
            model_name="filmwork",
            name="genres",
            field=models.ManyToManyField(through="movies.GenreFilmwork", to="movies.genre"),
        ),
        migrations.RunSQL(
            sql="CREATE INDEX IF NOT EXISTS film_work_creation_date_idx ON content.film_work(creation_date);",
            reverse_sql="DROP INDEX IF EXISTS film_work_creation_date_idx;",
        ),
        migrations.RunSQL(
            sql=(
                "CREATE UNIQUE INDEX IF NOT EXISTS film_work_person_idx ON"
                " content.person_film_work(film_work_id, person_id, role);"
            ),
            reverse_sql="DROP INDEX IF EXISTS film_work_person_idx;",
        ),
        migrations.RunSQL(
            sql=(
                "CREATE UNIQUE INDEX IF NOT EXISTS film_work_genre_idx ON "
                "content.genre_film_work(film_work_id, genre_id);"
            ),
            reverse_sql="DROP INDEX IF EXISTS film_work_genre_idx;",
        ),
    ]
