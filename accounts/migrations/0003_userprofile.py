# Generated by Django 5.0.6 on 2024-06-20 09:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='users/profile_pictures')),
                ('cover_pic', models.ImageField(blank=True, null=True, upload_to='user/cover_pic')),
                ('address_line1', models.CharField(blank=True, max_length=50, null=True)),
                ('address_line2', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('pincode', models.CharField(blank=True, max_length=8, null=True)),
                ('latitude', models.CharField(blank=True, max_length=8, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
