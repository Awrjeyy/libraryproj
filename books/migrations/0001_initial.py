# Generated by Django 4.0.5 on 2022-06-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('authorName', models.CharField(max_length=255)),
                ('authorEmail', models.CharField(max_length=255)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('book_condition', models.CharField(choices=[('Physical', 'Phyiscal'), ('Digital', 'Digital')], default='Physical', max_length=20)),
                ('book_location', models.CharField(choices=[('Home', 'Home'), ('Office', 'Office'), ('Into the Matrix', 'into the matrix')], default='Into the Matrix', max_length=20)),
                ('book_cover', models.ImageField(default='default-book-cover.jpg', upload_to='book-cover')),
            ],
        ),
    ]
