# Generated by Django 4.2.21 on 2025-06-01 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0009_delete_formerpresident'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormerPresident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('tenure', models.CharField(help_text='e.g., 2020-2021', max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='former_presidents/')),
            ],
            options={
                'verbose_name': 'Former President',
                'verbose_name_plural': 'Former Presidents',
                'ordering': ['tenure'],
            },
        ),
    ]
