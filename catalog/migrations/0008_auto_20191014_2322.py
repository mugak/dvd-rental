# Generated by Django 2.2.5 on 2019-10-14 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_movieinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movieinstance',
            options={'ordering': ['due_date'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
