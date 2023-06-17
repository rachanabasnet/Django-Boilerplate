# Generated by Django 4.2.2 on 2023-06-16 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=45, unique=True)),
                ('first_name', models.CharField(max_length=45)),
                ('middle_name', models.CharField(blank=True, max_length=45, null=True)),
                ('last_name', models.CharField(max_length=45)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('last_activity', models.DateTimeField(blank=True, null=True, verbose_name='last activity')),
                ('contact_number', models.CharField(blank=True, max_length=14, null=True)),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_cover', to='common.file')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('profile_picture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='common.file')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('-updated_at',),
                'abstract': False,
            },
        ),
    ]
