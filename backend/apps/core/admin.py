"""
Configuración del Panel Administrativo de Django - nuam Exchange Group
Gestión integral de Roles, Usuarios RBAC, Emisores, Certificados y Logs de Auditoría.
"""

from django.contrib import admin
from django.utils.safestring import mark_safe
from apps.core.models import (
    Rol, Usuario, Emisor, CertificadoDividendo, FactorTributario, LogAuditoria
)

# Logo institucional nuam optimizado en formato Data URI (carga garantizada sin depender de estáticos)
LOGO_NUAM_B64 = (
    "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAANK0lEQVR42u1bW6xkx1Vda1d1973z8k"
    "xwPLZiPiLLEXGCYmQg4Q/EPxKYAUfEGhGcCfkYUIRQgiCMBvESIPgIxIlRiI0xKIBCAOWDiChCAyIPxzgoESBiZLCxE8DzMh7f7lO1"
    "Fx9Vdc7pe6/sHt+2xEdv6ah7bh+dPr3O2muvvasG2MQmNrGJTWxiE5vYxCb+nwQ3EIxCG0A2dN/LirOYdTvxLqPf4RlHzeCuci0j5A"
    "INlgP1tcuLI39/4qErl1/mHnQglr4X2+lq+B5Jt4GgBchhgMERHGYG0DMIOQBlpBezf+L4/bi0doDmZ8KpCL1fSd8WIghy9BNVXlkv"
    "7YALT0j26/Gj6YGDArFfLE5P7jLz+wP1HaAAq99vAMLoV4Z2XwJELCzeOfut7ssvd/14XTfzrvjzUfk8ASRAOcFFAQThELlbf8QYcB"
    "uQP9y9M7wlfnP+CZ5HOiDje5B37p2+0XL68+B6XedwEhABBggEEQAYBAJ0QAJppIgFDL7KF9qqd9b9+PTuSD8vASnDCaiRBg6xv38O"
    "xFQBMWcoBn9PemryOzp3fQ9lr+bXN+dglvzXguN13RxOhyCIgpTLPSlBSP09AoKk6+PxSgDpHKZM6WcowX1AnpUy5HKyimC5k4KiBC"
    "WHouUz6en4oQOCVFL9H6a3Y+7fmxYQAElFYOQFjKXXBCgDKIeQgelijQDNn57eJuHN2QsQHKuXgRo9EQmA17+QoBEkQVDJpWj+rvSf"
    "B2YSEPGGibCtXFnSCfCie5UtgNfUyoAS+s/kIHw1/V0JoIB80ogZWFJJBEUQBKhGWPbMrR8t50SRAqUsReYz6alw/4FAEmbwyogGTCo"
    "3BxHILIxpgOXRawYW6wQIhFEq6cJauQqx0dijmkvjdGMPmwbwWEEKui89FT786BlMXpFa5/q4GkMygCygG0CAaoo1t1oBogPYWSdAvd"
    "AUxtRnpP1O0e46BlAAqQEykgWkqB97S4of0SsASRlC1gBGS6MkaAGoq2AliKNz+vSbrFGDYOg1BUYwAIgsKcaqNRxga3xRzTQKKmmp4"
    "akZkR2KwX80pfi7OoXp9QAUvGiPMqgMDunEoWplAF0BTh2oDlQCkYlpXq2WraQB//N3kJIgA2wKTA4D0xPQ7DVE3K7mJA9OhVXJKZXq"
    "IjX/qOYCWHFMWYjBT6cj0XQu3cfzWKm+5ATGmuYM9aJeU76ZVSNgKtpECHHEoJVrwQqRLpdc9vpkdlxwAWEL2L4ZOPp6YnZCkBfKiGL"
    "NLbW7oSCQ0Kh7lZdPqk+6N/17pM6m+/hBzFfRoHKt+i1WbUcAkSGxFY36xExggqrTJsIaNShuRYYJEKMQp0CcEZNpKa0vPCn81wXHpa"
    "+2HyzQq2EbaRObzR8w68ucBOQEj8Hfka6Ej+osZitp0FCyC0t815EEplbua1XLhJKwmK9ZpM1QPI0BNCAEIkyAWJXj+X8RnvuC4Ity"
    "1RFT6qOsAo3dPdtgB3KGR9OPpMvhYzqNrZfOsb2AqGiOkKtYZ1BZRJKKDyLhIDOBdQIUYwWoaHRhRAOpHRNg5xvCc48CPi9CLhbp1qj"
    "vqW5gWSs4AinBo+ntycPvrQKSEuAOygElwVs1y4AVj6Qi4ioaUVlHrZVBCTTuBakHqoAVp0B3Ebj4qJB3Sm1Xs43c1atpyLix8xWAVE"
    "FyDx/TqVu39++cl90xVFMta6nNYG7pRSARSNUarLMXQwRoAgP6wwL6dGMALAIWCIvA4iJw+THAdyhyxBbtstf7gVRxzAlu8nvS5NkHd"
    "QaH9tyT16Y01ZRqjrqaQ4lQJpQBlv6rnJ9Z9KpbJ0CI5cdXUMbgmDV9qu9D0aXuEnD58aJJZMupUcOm0fBid4ddT0+JHqkf8iv2kM7c"
    "ciihPBGUgZzB3QF4A7oDXxrQ1rp7L0dqSxq61MijGkkYFJPZA9OBwYFIIQIhAmALdZeDK4wI7mlmdwIzSqbUDy+AsS0NKcAv4Qb/yjd"
    "/XO04e7gEq4BQAusIOJcArazz1WkfV81TTUAnEXOutYmQBJdRUaoC0dOtBiwNQcQLgCvj81+wvEeyZYDBIyx23ltJmX0alBDfD3Xnx"
    "3w/r1GuPACPGOOSVKbmyx7PgqRxKklxoIHnt27p1plhEWkoljtk0YtWQdiUdQwC2ZuCLz/pf22xyj4SrQTD0Y4F9uu02ptByCU8dPFD"
    "fn+25R/TeW7c1z/PUWORAdtBd8AaGFza5E9nBLLABlDPQrbWKzeJQwaw6+N36Ewaf1LOpAjk7ZIf42zsXXDwt8JoRxnGZ95Fou3oN2i"
    "3sKdMD8X3+zDMPd1O7cZ6glEu7kl0FCAdzxsAYB9xZGJUFL6PXlbvj1RhEiJEj3VEFS6W6WemHQqjs6VnU/lauM3kof1IhvBPgjrXv"
    "HuuQRgOvNuPZVfVSghtw97HX+68mwFMSck21qklq7FHWcCRIib1WYbFOBgXQIsD+YNUawiKXNMni6BiEvL+Z+GD3cZm9B2Si+jnBnkkg"
    "vPqZ0lJo/HnK8NkxnTx2exml5AWQUgGnpZyrplNHeAe5gz6kGZOv9ttX90GhAMNI2ITgpApyHIQ6BCCM06ul367+OT7UPSjyJ1ksnBX"
    "mcJdpLGNLCYSaaA0Mywv41g3A8W8hYKB3RaSbWOeWTq7itHNx2oVRSwPQNQIUilnESHdCGKqXtao20qtogMW93xMfTh/KzvdRRG/7x6"
    "lW33PMnjYga065A2YniONvImTVD1WQ1F6990VSZpkNlZ6NawUIVYTNIDP1YLAA0C/WmRVWhfo5CmD7Pq3px9NvZPADAXWI7iMdaq2Hk"
    "3L2fdRu560EbB0HXvNmArEwST74pJwAT1AxkIJyvX63ZqPICpKsaE9buWQoc+ZWuRgLaI1liC89dZr+cfrFJPvlOAbJ93brZfBWQcnD"
    "sg4c8I6Y3QB807cWkNKiak0aGcpS7iEHUgbTWsv8pEzjOGJFBabWfPbAtBQUG1B82Xyf/Gn3synbb0aAanrRBvHaZ6TRZrmqzWmdQ89"
    "uEG68s+hjY9LQcogqIi756jPFlasYY59q7NnR9CiKjTVtZm2Vce2cl2Xpnd1PL9w+MgHIXRVNdb6DPLyXcwCxVb0FMDsq3HgnCpM6MKe"
    "+JVFhk5BTHbCtdVXDANSOHgFQYEm1UFnS/t2G+KEO96HeB71kK3MePr2lO9tl/kFsRrJfptFet71rSK/qm3wBzI4Br70L4KS2JE2LvK"
    "ReXnergb6cc+SFAAVVJqnXp35nhQ3AIaxGaT6AbnLk5jMZ9mcRsGUdGq2aeNljU9ij5UVBEeqI2VHgpm8HuAV6px4c+auwNo8JpBEQh"
    "TUCI4tnj6yiPHwuq4CVVFu9Kf6Tp18Mk2Onu2yfnqBOADReyuFQ7rWsU41FSmXMMjsKnPxOwGakdxq3H8xap1GsGsQIyQQE9emk1tXH"
    "MdNGgh2ud5MNwL947vlJ2H576uzCxAuTlPeOSliXlzXenJBGC4kLYHYYuOmthG0ReQGV6iakV8MHyUBOKEYKUUslvRfjMSj1M4vmuM7"
    "gp69enGPywynxsYnD6hC+F+jGlB6UNijLfYvSFgw1OyadfBvB7WoB1i7ShNSnjojYNEdgkNompSWQRiXf9cq2+h25cO3ZZOFU6vDPU8"
    "BaajFpaYvL3uXnVu3KiqpfA2eHhZvfCsTt8jeuP8UEm0JszIgQJxQmKEucQX2lQ/VAapp0gI0u2387/7fM8AMp8clJhvWpluomhP2W/"
    "xqDRuvxWgCzI8DJ7wImh4n5i7J1rs2z3/vH0d4pU9vrwiXNMRVwrNgAiwfbCrz1+cU/uc/uTh2/HhNMqTKlG0CQljZJlTQc6ZJSsQDT"
    "w8BNbxNuuJ3ra1YTk/qqxMIehSURVtMeTlhc9xJgWOCAMfvStccSJvfIeSnkkXD3zWczkhyE2odzep2aA9NDwIk3rXEmHZvGtJSxuvDe"
    "9CaygBQhobjqAmZJN0X8K9YQhx7f+ZuMcC8SXrDUQFJx2WlYMJSX9a9deqS6FYZ5wXlehK+vsYrFvv/qvZCBoEirGwJC21xVt8uUob1"
    "1wJPRti9gTbH15cWnHOHdyOiYZeOyXkAS2Jaal1KubJEJZZ3+0dnRxRPrSzGkqiu9FrE3hGX7YVGnYW8yQ4ApEor2c/zDK5ewxph9pX"
    "ukM/spKzpDLyMNIAvMhDJZRrZtKx6BDggZlhPnXcYH+MBqAw9b1Qa1leNeV0Jdew6j8UapXoxTGAJTIt8/+6PuEbwKcfgr6YML8Be2BA"
    "aH0Tns4OigtquseidOBJPb/+Yc3r39ifzZte4PAmEWS3cBtJmNhqF6Zt9A5oTOwc+5xV+aPjj/K7yKcfir+dy1N8YuuL9vy3Ckd9q2b"
    "AQTeTVn+4xH/MrsU90X1/5/NV44u33rbNLdU2brDrjBcn0rl8noGTDnxWz4x+kt3eM8fz0LvAeLq3dM79iif7cDx93K/9WoLn7BGf9j"
    "OrUv8bPzJ7CJTWxiE5vYxCY2sYlNbGITm9jEJjaxif8D39NTxgiGydQAAAAASUVORK5CYII="
)

# Personalización institucional del encabezado y títulos del Backoffice
admin.site.site_header = mark_safe(
    f'<span style="display:inline-flex;align-items:center;gap:12px;vertical-align:middle;">'
    f'<img src="{LOGO_NUAM_B64}" alt="nuam logo" style="height:36px;width:36px;object-fit:contain;border-radius:6px;box-shadow:0 2px 4px rgba(0,0,0,0.3);" />'
    f'<span style="display:inline-flex;flex-direction:column;text-align:left;line-height:1.15;">'
    f'<span style="font-weight:800;font-size:1.15rem;letter-spacing:-0.02em;color:#f8fafc;">'
    f'nuam <span style="font-size:0.75rem;font-weight:600;color:#94a3b8;letter-spacing:0.05em;">EXCHANGE GROUP</span>'
    f'</span>'
    f'<span style="font-size:0.78rem;font-weight:400;color:#cbd5e1;">'
    f'Mantenedor de Dividendos y Factores Tributarios'
    f'</span>'
    f'</span></span>'
)

admin.site.site_title = "nuam EXCHANGE GROUP — Administración"
admin.site.index_title = "Panel de Gobernanza de Datos y Seguridad RBAC"
admin.site.site_url = "https://proyecto-integrado-caso-nuam.vercel.app"


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('id_rol', 'nombre_rol', 'nivel_acceso', 'descripcion')
    search_fields = ('nombre_rol', 'descripcion')
    ordering = ('nivel_acceso',)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'email', 'id_rol', 'id_corredora', 'estado')
    list_filter = ('id_rol', 'estado', 'id_corredora')
    search_fields = ('rut', 'nombre', 'email', 'id_corredora')
    ordering = ('nombre', 'rut')
    actions = ['activar_usuarios', 'inactivar_usuarios']

    @admin.action(description="Activar cuentas seleccionadas")
    def activar_usuarios(self, request, queryset):
        queryset.update(estado='ACTIVO')

    @admin.action(description="Inactivar cuentas seleccionadas")
    def inactivar_usuarios(self, request, queryset):
        queryset.update(estado='INACTIVO')


@admin.register(Emisor)
class EmisorAdmin(admin.ModelAdmin):
    list_display = ('rut_emisor', 'razon_social', 'pais_origen', 'sector_economico')
    search_fields = ('rut_emisor', 'razon_social')
    list_filter = ('pais_origen', 'sector_economico')


class FactorTributarioInline(admin.TabularInline):
    model = FactorTributario
    extra = 0
    readonly_fields = ('fecha_calculo',)


@admin.register(CertificadoDividendo)
class CertificadoDividendoAdmin(admin.ModelAdmin):
    list_display = ('folio_certificado', 'rut_emisor', 'anio_tributario', 'fecha_pago', 'monto_total_bruto', 'estado_proceso')
    list_filter = ('anio_tributario', 'estado_proceso')
    search_fields = ('folio_certificado', 'rut_emisor__razon_social', 'rut_emisor__rut_emisor')
    inlines = [FactorTributarioInline]


@admin.register(FactorTributario)
class FactorTributarioAdmin(admin.ModelAdmin):
    list_display = ('id_factor', 'folio_certificado', 'factor_afecto', 'factor_exento', 'factor_credito', 'estado_validacion', 'fecha_calculo')
    list_filter = ('estado_validacion',)
    search_fields = ('folio_certificado__folio_certificado',)


@admin.register(LogAuditoria)
class LogAuditoriaAdmin(admin.ModelAdmin):
    list_display = ('id_log', 'accion', 'folio_certificado', 'usuario_rut', 'fecha_hora', 'hash_sha256')
    list_filter = ('accion', 'fecha_hora')
    search_fields = ('id_log', 'folio_certificado__folio_certificado', 'usuario_rut__rut', 'hash_sha256')
    readonly_fields = ('id_log', 'fecha_hora', 'hash_sha256', 'payload_detalle')
