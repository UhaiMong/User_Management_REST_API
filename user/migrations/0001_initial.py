# Generated by Django 4.2.7 on 2024-08-18 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, max_length=20, null=True)),
                ('mobileNumber', models.CharField(blank=True, max_length=11, null=True)),
                ('profileImage', models.ImageField(blank=True, null=True, upload_to='user/images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Authenticated User',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(default='Bandarban')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.usermodel')),
            ],
        ),
    ]
