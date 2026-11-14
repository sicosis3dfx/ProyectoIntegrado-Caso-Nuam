# Respaldo Integral de Proyecto y Guía Maestra — Evaluación 3
## Mantenedor Centralizado de Calificaciones Tributarias y Dividendos
### nuam EXCHANGE GROUP (Holding Bursátil Regional Chile · Perú · Colombia)

---

### 📋 Ficha Técnica Académica
* **Institución Educativa:** INACAP — Sede Renca
* **Carrera:** Ingeniería en Informática
* **Asignatura:** Proyecto Integrado
* **Docente Guía:** Macarena Angulo Olguín
* **Equipo de Desarrollo:**
  * **Angelo Alberto Zamora Romero** *(Arquitectura de Software, Backend REST, Seguridad Criptográfica y Base de Datos)*
  * **Martín Ignacio Tapia Jaramillo** *(Optimización UI/UX, Componentes React, Hooks de Visibilidad y Vista en Cuadros)*
  * **Vicente Sagredo** *(Diseño de Casos de Prueba, Control de Calidad QA, Protocolo de Validación y Documentación)*
* **Período Académico:** Cuarto Semestre 2026 — Evaluación 3
* **Fecha de Consolidación:** 13 de Noviembre de 2026

---

## 🌐 1. Mapa de Infraestructura Cloud y URLs Oficiales

El ecosistema se encuentra **100% operativo en producción cloud** con persistencia real y no efímera:

| Componente | Proveedor Cloud | URL Oficial | Descripción Técnica |
| :--- | :---: | :--- | :--- |
| **Frontend Web (SPA)** | **Vercel** | [proyecto-integrado-caso-nuam.vercel.app](https://proyecto-integrado-caso-nuam.vercel.app) | React 19 + TypeScript 5.8 + Vite 8. Dark mode, menú hamburguesa móvil, vista dual tabla/tarjetas y auto-formato RUT. |
| **Backend REST API** | **Render** | [proyectointegrado-caso-nuam.onrender.com](https://proyectointegrado-caso-nuam.onrender.com) | Python 3.12 / 3.13 + Django 5.2 + DRF. Endpoints en `/api/v1/`. La raíz `/` redirige automáticamente a Vercel vía HTTP 302. |
| **Backoffice Administrativo** | **Render** | [proyectointegrado-caso-nuam.onrender.com/admin/](https://proyectointegrado-caso-nuam.onrender.com/admin/) | Django Admin personalizado con logo oficial nuam, enlace "Ver el sitio" a Vercel y paleta corporativa Dual Mode (Claro & Oscuro). |
| **Alias Vercel al Backoffice** | **Vercel Edge** | [proyecto-integrado-caso-nuam.vercel.app/admin](https://proyecto-integrado-caso-nuam.vercel.app/admin) | Redirección perimetral automática (`vercel.json` + `index.html`) hacia el panel de administración en Render. |
| **Base de Datos Relacional** | **Supabase** | `aws-0-sa-east-1.pooler.supabase.com` | PostgreSQL 15 en 3FN estricta vía Session Pooler (IPv4). Persistencia real y atómica ACID. |
| **Auditoría Documental** | **MongoDB Atlas** | Cluster Multi-Cloud Inmutable | Almacén de logs con sellado criptográfico SHA-256 e inmutabilidad garantizada. |
| **Endpoint Wake-Up / Salud** | **Render** | [/api/v1/salud/](https://proyectointegrado-caso-nuam.onrender.com/api/v1/salud/) | Endpoint de verificación de estado y reactivación tras reposo del contenedor. |

---

## 🔑 2. Matriz de Credenciales Oficiales de Demostración

### 2.1. Cuentas de Negocio para el Portal Web (Vercel)
Autenticación institucional con validación de rol RBAC, tokens JWT y código MFA de 6 dígitos:

| Rol Institucional | Correo Oficial | RUT Chileno | Contraseña | Código MFA | Privilegios y Alcance Normativo |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Operador Corredora** | `operador@larrainvial.cl` | `12.345.678-9` | `Nuam2026!` | `123456` o `📲 OTP` | Carga masiva CSV y validación DJ 1949. **Cierre fiscal bloqueado (HTTP 403 Forbidden por SoD).** |
| **Auditor nuam** | `auditor@nuam.com` | `9.876.543-2` | `Nuam2026!` | `123456` o `📲 OTP` | Fiscalización regional, verificación SHA-256 y **aprobación/cierre definitivo de lotes fiscales**. Modo lectura en CSV. |
| **Administrador Plataforma** | `admin@nuam.com` | `11.222.333-4` | `Nuam2026!` | `123456` o `📲 OTP` | Control total, matriz RBAC, gestión de usuarios, depuración de pruebas y configuración institucional. |

### 2.2. Cuenta de Superusuario para el Backoffice Técnico (Django Admin)
Para labores de inspección de modelos ORM, tablas físicas y revisión de bases de datos:
* **URL de Acceso Directo:** [https://proyectointegrado-caso-nuam.onrender.com/admin/](https://proyectointegrado-caso-nuam.onrender.com/admin/) *(o vía [Vercel /admin](https://proyecto-integrado-caso-nuam.vercel.app/admin))*
* **Usuario:** `sicosis3dfx`
* **Contraseña:** `Ponsill@@1`
* **Permisos:** Superusuario y Staff con acceso total a las 6 entidades del sistema.

---

## 🏛️ 3. Resumen Consolidado de Todo lo Desarrollado y Optimizado

### 3.1. Modelo Relacional en 3FN y Base de Datos Supabase PostgreSQL
* **6 Tablas Físicas en 3FN:**
  1. `TB_ROLES`: Jerarquía y permisos de acceso RBAC.
  2. `TB_EMISORES`: Sociedades anónimas emisoras bursátiles (`rut_emisor`, `razon_social`, `pais_origen`, `sector_economico`).
  3. `TB_USUARIOS`: Funcionarios institucionales con hash salteado PBKDF2-SHA256, RUT único e institución.
  4. `TB_CERTIFICADOS_DIVIDENDOS`: Certificados matrices (`folio_certificado`, `rut_emisor`, `anio_tributario`, `fecha_pago`, `monto_total_bruto`, `estado_proceso`).
  5. `TB_FACTORES_TRIBUTARIOS`: Desglose con precisión de 6 decimales (`factor_afecto`, `factor_exento`, `factor_credito`, `fecha_calculo`, `estado_validacion`) con eliminación `CASCADE`.
  6. `TB_AUDIT_LOGS`: Bitácora inmutable con `id_log` tipo `uuid` (UUID v4), payload JSON y firma criptográfica SHA-256 con retención `SET NULL`.
* **Blindaje Teórico de 3FN:** Las columnas derivadas (`suma_proporciones` y `es_cuadre_exacto`) **no se almacenan como columnas físicas redundantes** en la base de datos (lo que violaría 3FN por dependencia transitiva entre atributos no clave), sino que se computan dinámicamente en los métodos del modelo (`calcular_suma_factores()` y `es_cuadre_exacto()`).
* **Diagrama Mermaid Dark Mode en GitHub:** Configurado con directivas `%%{init: {"theme": "base", ...}}%%` con paleta corporativa oscura que no encandila ni desentona al visualizarse en GitHub.

### 3.2. Motor de Precisión Aritmética Bancaria (DJ 1949 / DJ 1922)
* **Cero Floats Primitivos:** Prohibición absoluta de tipos de punto flotante binario (IEEE-754). Se utiliza exclusivamente `decimal.Decimal` con política estricta `ROUND_HALF_UP` a 6 decimales (`0.000001`).
* **Regla de Consistencia Fiscal:** $factor\_afecto + factor\_exento$ debe sumar exactamente `1.000000`. Cualquier desviación genera `HTTP 422 Unprocessable Entity` y revierte la transacción atómica.

### 3.3. Compuertas de Negocio BPMN 2.0 en Ingesta CSV
1. **Compuerta 1 (Sintaxis CSV):** Decodificación preventiva (UTF-8 / Latin-1) y validación de cabeceras obligatorias. Si falta alguna columna $\to$ `HTTP 400 Bad Request`.
2. **Compuerta 2 (Consistencia Fiscal):** Verificación matemática fila por fila. Si hay descuadre $\to$ `HTTP 422 Unprocessable Entity` con reporte de discrepancia.
3. **Persistencia Atómica ACID:** Registro transaccional del emisor, certificado y factores con emisión de firma SHA-256 $\to$ `HTTP 201 Created`.

### 3.4. Estándares de Seguridad Internacionales
* **ISO/IEC 27001 Control A.9 (Segregación SoD):** Decoradores REST `@rol_requerido`. El Operador no puede cerrar lotes (`HTTP 403 Forbidden`); solo el Auditor nuam puede sellar el cierre fiscal.
* **Ley N° 21.719 (Protección de Datos Personales):**
  * *Privacy by Design:* Contraseñas salteadas irreversibles con PBKDF2-SHA256 (`write_only: True`).
  * *Derechos ARCO:* Soporte nativo para Rectificación (`PATCH /usuarios/<id>/`) y Supresión/Cancelación (`DELETE /usuarios/<id>/`).
  * *Accountability:* Bitácora inmutable sellada con hash SHA-256 por cada mutación de datos.
  * *Contraseñas Reforzadas:* Validación de 5 directivas (mínimo 8 caracteres, mayúscula, minúscula, número y símbolo especial) con checklist interactivo `PasswordPolicyChecklist` en el frontend.
* **Validación de RUT Chileno (Módulo 11):** Auto-formato en tiempo real (`XX.XXX.XXX-X`), cálculo del dígito verificador y normalización canónica en backend permitiendo login con o sin puntos/guión.

### 3.5. Optimización UI/UX Responsiva y Componentes Modernos
* **Menú Hamburguesa Móvil (☰ / ✕):** Cajón lateral deslizante (*off-canvas drawer*) en dispositivos $\le 768px$ con fondo translúcido (*backdrop*).
* **Vista Dual Lista / Cuadros (`ViewToggle`):** Selector para alternar entre tabla de datos y tarjetas táctiles independientes (`CertificateCard`).
* **Botón de Ojo en Login:** Alternancia dinámica para ver/ocultar contraseña con iconos SVG accesibles y sin desalineación tipográfica.
* **Notificación Flotante Responsiva (`FloatingLoader`):** Ubicada en la parte superior central con imagotipo nuam y spinner circular. Cuenta con envoltura multilínea adaptativa (`white-space: normal`, `word-break: break-word`) para que el texto nunca desborde el banner en pantallas móviles.
* **Modal Preventivo de Confirmación de Ingesta:** Diálogo modal perfectamente centrado en pantalla (`max-width: 620px`, animación `modalFadeInCenter` sin desfaces) con la misma estética de vidrio oscuro y spinner circular del `FloatingLoader`. Intercepta la subida o arrastre de nóminas CSV, presentando los metadatos técnicos completos (nombre de archivo con tooltip, formato, tamaño y nombre íntegro del operador sin truncamiento). En dispositivos móviles ($\le 480px$), los datos se apilan verticalmente y los botones de acción (*"No, Cancelar"* / *"Sí, Ingestar Nómina"*) se extienden al 100% para evitar errores de digitación y garantizar una ergonomía táctil óptima.
* **TopBar Fijo Dinámico:** Utiliza `useWindowScroll` para volverse *sticky* con desenfoque de fondo (`backdrop-filter: blur(12px)`) durante el scroll en celulares.
* **Skeleton Shimmer Loading:** Animación de carga fluida en tablas para una percepción de velocidad instantánea.
* **Micro-Footer Institucional (Slim Footer):** Pie de página corporativo sutil ubicado al fondo de las vistas de la plataforma, que sella el cumplimiento con los entes supervisores del holding (CMF · SMV · SFC), las resoluciones tributarias (DJ 1949/1922 SII), normativas de seguridad (ISO/IEC 27001, Ley 21.719) y versión de producción (`v3.2.0-LTS`). Diseñado con layout flexible y apilado centrado en dispositivos móviles.
* **Limpieza Institucional:** Eliminación de nomenclaturas académicas (`CU-01`, `CU-07`, etc.) sustituidas por terminología bancaria formal.

### 3.6. Backoffice Administrativo Django Personalizado
* **Branding Oficial:** Encabezado con el imagotipo corporativo de nuam servido directamente desde la CDN de Vercel.
* **Dual Mode (Claro & Oscuro):** Paleta corporativa con Azul Marino (`#0f172a`), Azul Pizarra (`#1e293b`) y acentos en Naranja nuam (`#f97316` / `#ea580c`) con alternancia dinámica mediante el toggle ☀️ / 🌙.
* **Enlace Público Unificado:** El botón *"Ver el sitio"* apunta a la aplicación de producción en Vercel.

### 3.7. Enrutamiento y Conectividad Perimetral
* **Render $\to$ Vercel:** La ruta raíz `https://proyectointegrado-caso-nuam.onrender.com/` redirige vía HTTP 302 a `https://proyecto-integrado-caso-nuam.vercel.app`, evitando pantallas de error 404 o interfaces de depuración.
* **Vercel $\to$ Render:** La ruta `https://proyecto-integrado-caso-nuam.vercel.app/admin` redirige mediante `vercel.json` e `index.html` al backoffice Django en Render.
* **Manejo del Cold Start:** Documentación formal que explica que la suspensión por inactividad tras 15 minutos en Render Free Tier es una optimización de cómputo cloud académica, mitigable mediante el endpoint de salud `/api/v1/salud/` 5 minutos antes de la defensa.

---

## 🧪 4. Resultados del Plan de Pruebas ISO/IEC/IEEE 29119

El aseguramiento de calidad del software alcanzó un **100% de conformidad**:

### 4.1. Suite Automatizada de Pruebas Unitarias
Comando de ejecución:
```bash
python manage.py test apps.core
```
* **Resultado:** **12 de 12 pruebas aprobadas (100% OK)** ejecutadas en ~17 segundos sin fallos.
* **Cobertura:** Precisión aritmética a 6 decimales, compuertas BPMN 1 y 2, segregación de funciones SoD (HTTP 403), inmutabilidad SHA-256, detección de anomalías y concurrencia.

### 4.2. Protocolo QA de Benchmark y Latencia (11 Casos Aprobados)
Detallado en [`docs/REPORTE_PRUEBAS_EVALUACION_3.md`](file:///e:/Mis%20Documentos/OneDrive%20-%20INACAP/GitHub/ProyectoIntegrado-Caso-Nuam/docs/REPORTE_PRUEBAS_EVALUACION_3.md):
* `CP-01` (Autenticación MFA): HTTP 200 — `664 ms` ✅
* `CP-02` (Compuerta 1 - Faltan columnas): HTTP 400 — `3.6 ms` ✅
* `CP-03` (Compuerta 2 - Descuadre `0.999999`): HTTP 422 — `355 ms` ✅
* `CP-04` (Ingesta exitosa suma `1.000000`): HTTP 201 — `345 ms` ✅
* `CP-05` (Filtros multianuales 2024-2026): HTTP 200 — `22.7 ms` ✅
* `CP-06` (Cierre fiscal por Auditor nuam): HTTP 200 — `634 ms` ✅
* `CP-07` (Bloqueo SoD: Operador intenta cerrar): HTTP 403 — `1.4 ms` ✅
* `CP-08` (Verificación integridad SHA-256): Estado VÁLIDO — `1.05 ms` ✅
* `CP-09` (Detección de alteración en BD): `ALTERADO_ANOMALÍA` — `543 ms` ✅
* `CP-10` (Gestión exclusiva de usuarios por Admin): HTTP 200/403 — `4.1 ms` ✅
* `CP-11` (Benchmark concurrente): Latencia media `761 ms` (< 2000 ms) ✅

### 4.3. Registro de Discrepancias Detectadas en Iteración Preliminar y Acciones Correctivas (Rúbrica 3.1.6.12)
Para dar cumplimiento estricto al indicador 3.1.6.12 (*"Se identifican y documentan con precisión todas las discrepancias entre los resultados obtenidos y esperados"*), se documentan las desviaciones de la **Iteración 1 (Pre-Release)** y cómo se subsanaron para alcanzar el 100% de conformidad en la **Iteración 2 (Release Final)**:

| ID Discrepancia | Caso Afectado | Resultado Esperado (SLA / Norma) | Resultado Obtenido (Iteración 1) | Análisis de Causa Raíz | Corrección Implementada (Resultado Iteración 2) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **`DISC-01`** | `CP-01` (Login Cloud) | Tiempo de respuesta `< 1000 ms` en autenticación inicial. | Latencia de `38.420 ms` en la primera petición tras 20 min de inactividad. | Suspensión automática del contenedor (*Spin-Down*) en la capa gratuita de Render e inicialización en frío del pool TCP hacia Supabase. | Creación del endpoint ligero de precalentamiento `/api/v1/salud/`, configuración de `CONN_MAX_AGE` con Session Pooler y componente visual `FloatingLoader`. Latencia en caliente reducida a **`664.06 ms`**. |
| **`DISC-02`** | `CP-02` (Ingesta CSV) | Lectura universal de planillas CSV generadas por corredoras. | Excepción `UnicodeDecodeError` al subir archivos exportados desde MS Excel en Windows. | Excel en configuración regional chilena exporta por defecto en codificación `ISO-8859-1 (Latin-1)` o `UTF-8 con BOM`, discrepando del parser `UTF-8` estricto inicial. | Implementación de decodificador adaptativo multicapa (`utf-8-sig` $\to$ `latin-1`) en `csv_ingestion_service.py`, logrando **`3.62 ms`** sin fallos de lectura. |
| **`DISC-03`** | `CP-08` (Hash SHA-256) | Verificación de hash `VÁLIDO` consistente entre motor local y nube. | Falsos positivos de `ALTERADO_ANOMALÍA` al revalidar registros desde PostgreSQL. | El motor JSONB de PostgreSQL reordenaba alfabéticamente las llaves del diccionario al persistir, alterando el string base con el que se calculó el hash original. | Normalización canónica determinista mediante `json.dumps(payload, sort_keys=True, separators=(',', ':'))` antes de firmar y al verificar, alcanzando **100% de precisión en `1.05 ms`**. |

---

## 📁 5. Archivos CSV para Demostración en Vivo (`ejemplos_csv/`)

Para realizar la demostración interactiva ante la docente:
1. **`1_CARGA_VALIDA_EXITOSA.csv`:** Carga exitosa que demuestra el flujo completo, persistencia en Supabase y firma SHA-256 (`HTTP 201 Created`).
2. **`2_ERROR_COMPUERTA2_DESCUADRE_FISCAL.csv`:** Archivo con descuadre tributario (`0.999999` != `1.000000`) que evidencia la intercepción en Compuerta 2 (`HTTP 422 Unprocessable Entity`).
3. **`3_ERROR_COMPUERTA1_SINTAXIS_FALTAN_COLUMNAS.csv`:** Archivo con cabeceras incompletas que muestra la intercepción sintáctica preventiva en Compuerta 1 (`HTTP 400 Bad Request`).

---

## 🛡️ 6. Batería de Respuestas para la Defensa Oral (Rúbrica 3.1.6.14)

### P1: ¿Por qué la suma de factores nunca presenta discrepancias por redondeo?
> **Respuesta:** *"No utilizamos tipos de punto flotante primitivos (`float`). En computación binaria (IEEE-754), números como 0.1 o 0.2 producen decimales periódicos que generan errores acumulativos. En su lugar, utilizamos la clase estándar `decimal.Decimal` con redondeo bancario estricto `ROUND_HALF_UP` a 6 decimales (`0.000001`), garantizando que $factor\_afecto + factor\_exento$ sume con precisión absoluta `1.000000` bajo la normativa DJ 1949 del SII."*

### P2: ¿Cómo garantizan que la base de datos está en Tercera Forma Normal (3FN)?
> **Respuesta:** *"Cumple estrictamente 1FN (atributos atómicos sin colecciones anidadas), 2FN (dependencia funcional completa de las claves primarias) y 3FN (cero dependencias transitivas). Los datos del emisor están desacoplados en `TB_EMISORES` y los roles en `TB_ROLES`. Además, **no almacenamos valores calculados como columnas físicas** (como la suma de proporciones o el booleano de consistencia), ya que almacenar datos derivados introduciría dependencias funcionales entre atributos no clave ($A + B \to C$). Dichas operaciones se computan en memoria mediante los métodos del modelo (`calcular_suma_factores()` y `es_cuadre_exacto()`)."*

### P3: ¿Cómo se implementa la Segregación de Funciones (SoD) bajo ISO 27001?
> **Respuesta:** *"Bajo el estándar ISO/IEC 27001 Control A.9, las facultades operativas y de fiscalización están estrictamente separadas mediante decoradores `@rol_requerido`. Si un Operador de Corredora intenta invocar el endpoint de cierre fiscal (`/cerrar/`), la petición es interceptada a nivel de middleware devolviendo un código `HTTP 403 Forbidden`. La aprobación y cierre de lotes está reservada con exclusividad al Auditor nuam con firma digital autorizada."*

### P4: ¿Cómo comprueban que un registro de auditoría no ha sido alterado?
> **Respuesta:** *"Cada evento emite un hash canónico SHA-256 generado sobre su payload JSON normalizado con claves ordenadas alfabéticamente. Si un usuario o atacante modifica directamente un registro en la base de datos, el algoritmo de verificación recalcula el hash y, al detectar la discrepancia criptográfica, clasifica automáticamente el evento como `ALTERADO_ANOMALÍA`, alertando de inmediato al oficial de cumplimiento de la CMF."*

### P5: ¿Cómo cumple el sistema con la Ley N° 21.719 de Protección de Datos Personales?
> **Respuesta:** *"El sistema implementa el principio de Privacidad desde el Diseño (*Privacy by Design*). Incorpora los Derechos ARCO: rectificación de perfiles (`PATCH /usuarios/<id>/`) y supresión/cancelación de cuentas (`DELETE /usuarios/<id>/`). Además, las contraseñas se almacenan mediante salteado irreversible PBKDF2-SHA256 con flag `write_only: True` para evitar su fuga en las respuestas JSON, y cada mutación queda registrada en la bitácora inmutable bajo el principio de responsabilidad proactiva (*Accountability*)."*

### P6: ¿Por qué la primera petición de inicio de sesión tras horas de inactividad puede tardar unos segundos?
> **Respuesta:** *"Para efectos de la evaluación académica, el backend está alojado en una capa gratuita (*Free Tier*) de Render. Esta modalidad cuenta con una política de optimización energética de suspensión de contenedores (*spin-down*) tras 15 minutos sin tráfico HTTP. Al recibir la primera petición, realiza un arranque en frío (*Cold Start*) inicializando el entorno Python 3.12 / 3.13, el servidor Gunicorn y el pool de conexiones seguras hacia Supabase y MongoDB Atlas (~30-50 segundos). Una vez activo, el sistema responde con latencias ultra-bajas (< 50 ms). En producción industrial en nuam EXCHANGE, la arquitectura se dimensiona sobre clústeres elásticos reservados (AWS ECS Fargate o Kubernetes) con alta disponibilidad permanente."*

---

## 💻 7. Guía Rápida de Ejecución Local para el Equipo

Si algún compañero va a trabajar o revisar el código localmente:

### Paso 1: Sincronizar el Repositorio
```powershell
# En GitHub Desktop: Presionar Fetch origin y luego Pull origin
git pull origin main
```

### Paso 2: Levantar el Backend (Django)
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate --fake-initial
python manage.py seed_nuam
python manage.py runserver 8000
```
*API disponible en:* `http://localhost:8000/api/v1/`  
*Admin disponible en:* `http://localhost:8000/admin/`

### Paso 3: Levantar el Frontend (React + Vite)
```powershell
cd frontend
npm install
npm run dev
```
*App disponible en:* `http://localhost:5173/` *(configurada automáticamente con `frontend/.env`)*.

---
*nuam EXCHANGE GROUP — Proyecto Integrado INACAP 2026. Documento maestro de respaldo para evaluación académica y defensa técnica oral.*
