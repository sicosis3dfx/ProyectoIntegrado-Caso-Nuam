# Módulo Backend REST API — nuam EXCHANGE GROUP
## Mantenedor Centralizado de Calificaciones Tributarias y Dividendos

* **Asignatura:** Proyecto Integrado
* **Docente:** Macarena Angulo Olguín
* **Desarrolladores:** Vicente Sagredo, Martín Tapia, Angelo Zamora
* **Institución:** INACAP — Segundo Semestre 2026

---

### 🏛️ Arquitectura del Servicio y Stack
* **Lenguaje:** Python 3.12 / 3.13
* **Framework:** Django 5.2 LTS + Django REST Framework (DRF)
* **Motor de Base de Datos:** Supabase PostgreSQL 15 (Transacciones ACID en 3FN vía Session Pooler)
* **Auditoría Inmutable:** MongoDB Atlas / Persistencia Híbrida con sellado criptográfico SHA-256
* **Seguridad y Control de Acceso:** JWT (HS256) con decoradores de segregación SoD `@rol_requerido` (ISO 27001 Control A.9) y hash salteado PBKDF2-SHA256 (Ley 21.719).
* **Precisión Aritmética:** Módulo nativo `decimal.Decimal` con política estricta `ROUND_HALF_UP` a 6 decimales (`0.000001`), garantizando cuadre exacto de proporciones a `1.000000` (DJ 1949 / DJ 1922).

---

### 🚪 Compuertas de Negocio BPMN 2.0
1. **Compuerta 1 (Validación Sintáctica):** Intercepción preventiva de archivos CSV con codificación corrupta o columnas ausentes $\to$ `HTTP 400 Bad Request`.
2. **Compuerta 2 (Consistencia Fiscal DJ 1949):** Verificación de cuadre de factores afecto y exento. Ante cualquier desviación (ej: suma = `0.999999`) $\to$ `HTTP 422 Unprocessable Entity` con reporte de discrepancia y reversión atómica de transacción.
3. **Flujo Transaccional:** Registro atómico (`transaction.atomic()`) del emisor, certificado y factores tributarios $\to$ `HTTP 201 Created` con hash SHA-256.

---

### 🧪 Suite de Pruebas Unitarias (ISO/IEC/IEEE 29119)
Comando de ejecución de la suite automatizada:
```bash
python manage.py test apps.core
```
* **Estado:** 12 de 12 pruebas unitarias aprobadas (**100% OK**).
* **Casos cubiertos:** Autenticación MFA, errores sintácticos CSV, discrepancias de cuadre fiscal, consultas multianuales, segregación de cierre de lotes, inmutabilidad SHA-256, detección de manipulación y benchmark de latencia concurrente.

---

### 💻 Comandos de Instalación y Ejecución Local

```bash
# 1. Crear y activar entorno virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1    # PowerShell en Windows
# source .venv/bin/activate     # Linux / macOS

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Aplicar migraciones
python manage.py migrate --fake-initial

# 4. Sembrar datos base oficiales de demostración
python manage.py seed_nuam

# 5. Iniciar servidor REST
python manage.py runserver 8000
```
La API REST responderá en: `http://localhost:8000/api/v1/`

---

### ☁️ Despliegue en la Nube y Consideración de "Cold Start"
* **Plataforma:** Render Web Service (Free Tier)
* **URL de Producción:** [https://proyectointegrado-caso-nuam.onrender.com](https://proyectointegrado-caso-nuam.onrender.com) *(Redirección automática HTTP 302 hacia el frontend en Vercel)*
* **Backoffice Administrativo (Django Admin):** [https://proyectointegrado-caso-nuam.onrender.com/admin/](https://proyectointegrado-caso-nuam.onrender.com/admin/) *(Superusuario: `sicosis3dfx` / `Ponsill@@1`)*
* **Endpoint de Salud / Wake-Up:** `/api/v1/salud/`
* **API REST Endpoints:** `/api/v1/`
* **Nota sobre Suspensión (*Spin-down*):** En el nivel gratuito de Render, el contenedor entra en reposo tras 15 minutos sin tráfico. La primera petición tras horas de inactividad experimentará una latencia de arranque en frío (*cold start*) de 30 a 50 segundos mientras se levanta el runtime y se restablece el pool de conexiones a Supabase y MongoDB. Las peticiones subsecuentes responden con latencias inmediatas (< 50 ms). En producción industrial nuam, se utilizan clústeres reservados con alta disponibilidad permanente (AWS ECS / EKS).
