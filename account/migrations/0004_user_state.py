# Generated by Django 4.0 on 2022-02-25 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
