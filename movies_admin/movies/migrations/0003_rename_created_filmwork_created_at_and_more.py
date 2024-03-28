import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_filmwork_file_path"),
    ]

    operations = [
        migrations.RenameField(
            model_name="filmwork",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="filmwork",
            old_name="modified",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="genre",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="genre",
            old_name="modified",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="genrefilmwork",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="person",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="person",
            old_name="modified",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="personfilmwork",
            old_name="created",
            new_name="created_at",
        ),
        migrations.AlterField(
            model_name="filmwork",
            name="creation_date",
            field=models.DateField(blank=True, null=True, verbose_name="creation_date"),
        ),
        migrations.AlterField(
            model_name="filmwork",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="filmwork",
            name="rating",
            field=models.FloatField(
                blank=True,
                null=True,
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)],
                verbose_name="rating",
            ),
        ),
        migrations.AlterField(
            model_name="genre",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="description"),
        ),
    ]
