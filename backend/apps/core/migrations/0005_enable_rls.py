"""
Migración para habilitar Row Level Security (RLS) en las tablas de nuam en PostgreSQL.
Cumple con las recomendaciones de seguridad de Supabase (rls_disabled_in_public,
sensitive_columns_exposed) y estándares ISO/IEC 27001 Control A.9 / DevSecOps.
Bloquea el acceso público a través de la API REST automática de PostgREST,
manteniendo acceso total para el backend Django como dueño de la base de datos (BYPASSRLS).
"""

from django.db import migrations


def enable_rls(apps, schema_editor):
    from django.db import connection

    if connection.vendor == 'postgresql':
        tablas = [
            'TB_ROLES',
            'TB_USUARIOS',
            'TB_EMISORES',
            'TB_CERTIFICADOS_DIVIDENDOS',
            'TB_FACTORES_TRIBUTARIOS',
            'TB_AUDIT_LOGS',
        ]
        with connection.cursor() as cursor:
            for tabla in tablas:
                try:
                    cursor.execute(f'ALTER TABLE "{tabla}" ENABLE ROW LEVEL SECURITY;')
                except Exception as e:
                    print(f"Aviso RLS en {tabla}: {e}")


def disable_rls(apps, schema_editor):
    from django.db import connection

    if connection.vendor == 'postgresql':
        tablas = [
            'TB_ROLES',
            'TB_USUARIOS',
            'TB_EMISORES',
            'TB_CERTIFICADOS_DIVIDENDOS',
            'TB_FACTORES_TRIBUTARIOS',
            'TB_AUDIT_LOGS',
        ]
        with connection.cursor() as cursor:
            for tabla in tablas:
                try:
                    cursor.execute(f'ALTER TABLE "{tabla}" DISABLE ROW LEVEL SECURITY;')
                except Exception as e:
                    print(f"Aviso deshabilitar RLS en {tabla}: {e}")


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_sanitize_demo_ruts'),
    ]

    operations = [
        migrations.RunPython(enable_rls, disable_rls),
    ]
