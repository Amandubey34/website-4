# Generated by Django 2.0.1 on 2018-01-08 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0002_membership_tz_count_json'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='membership',
            options={'get_latest_by': 'timestamp'},
        ),
    ]
