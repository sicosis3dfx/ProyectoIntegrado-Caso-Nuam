"""
Migración de datos para crear el Superusuario oficial de Django Admin.
Permite acceso administrativo directo a /admin/ en Render y Supabase.
"""

from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    user, created = User.objects.get_or_create(
        username='sicosis3dfx',
        defaults={
            'email': 'admin@nuam.com',
            'is_staff': True,
            'is_superuser': True,
            'is_active': True,
            'password': make_password('Ponsill@@1'),
        }
    )
    if not created:
        user.password = make_password('Ponsill@@1')
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()


def reverse_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(username='sicosis3dfx').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_seed_initial_data'),
    ]

    operations = [
        migrations.RunPython(create_superuser, reverse_superuser),
    ]
