# Generated by Django 4.0.5 on 2022-07-01 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_book_ownerid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(default='default-book-cover.png', upload_to='book-cover'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_location',
            field=models.CharField(choices=[('Home', 'Home'), ('Office', 'Office'), ('Into the Matrix', 'Into the Matrix')], default='Digital', max_length=20),
        ),
    ]
