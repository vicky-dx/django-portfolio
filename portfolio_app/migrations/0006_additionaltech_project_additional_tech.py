# Generated by Django 5.2.3 on 2025-06-15 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0005_profile_location_profile_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalTech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Additional Technologies',
                'ordering': ['display_order'],
            },
        ),
        migrations.AddField(
            model_name='project',
            name='additional_tech',
            field=models.ManyToManyField(blank=True, to='portfolio_app.additionaltech'),
        ),
    ]
