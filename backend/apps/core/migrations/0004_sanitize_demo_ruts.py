"""
Migración de datos para anonimizar y proteger el RUT personal.
Actualiza cualquier referencia en TB_AUDIT_LOGS y asigna un RUT ficticio válido (14.555.666-7)
o permite la eliminación segura sin violar la clave foránea.
"""

from django.db import migrations


def sanitize_ruts(apps, schema_editor):
    from django.db import connection

    with connection.cursor() as cursor:
        # 1. Reasignar cualquier log que apunte al RUT personal hacia el administrador institucional oficial
        cursor.execute(
            """
            UPDATE "TB_AUDIT_LOGS"
            SET usuario_rut = '11.222.333-4'
            WHERE usuario_rut LIKE '%17.579.395%' OR usuario_rut LIKE '%17579395%';
            """
        )

        # 2. Anonimizar el RUT en TB_USUARIOS asignando un RUT ficticio de prueba
        cursor.execute(
            """
            UPDATE "TB_USUARIOS"
            SET rut = '14.555.666-7'
            WHERE rut LIKE '%17.579.395%' OR rut LIKE '%17579395%';
            """
        )


def reverse_sanitize(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_create_superuser'),
    ]

    operations = [
        migrations.RunPython(sanitize_ruts, reverse_sanitize),
    ]
