# FUENTE MAESTRA PARA NOTEBOOKLM: PITCH DE VENTA Y CASO NUAM EXCHANGE

## 1. Identificación del Proyecto y Equipo Consultor
* **Proyecto:** Mantenedor Centralizado de Calificaciones Tributarias y Dividendos (DJ 1949 / DJ 1922).
* **Organización Beneficiaria:** nuam EXCHANGE GROUP (Holding bursátil integrado por las Bolsas de Comercio de Santiago de Chile, Lima de Perú y Colombia).
* **Entidad Intermediaria Asociada:** LarrainVial S.A. Corredora de Bolsa.
* **Institución Académica:** Instituto Profesional INACAP — Escuela de Informática y Telecomunicaciones.
* **Asignatura:** Proyecto Integrado de Desarrollo de Software (Evaluación 3).
* **Equipo Consultor y Roles:**
  * **Angelo Alberto Zamora Romero:** Consultor Líder Frontend & UI/UX (React 19 / TypeScript / Vite).
  * **Martín Ignacio Tapia Jaramillo:** Consultor Líder Backend & Arquitectura de Datos (Django 5.2 / PostgreSQL 3FN).
  * **Vicente Sagredo:** Consultor Líder QA, Ciberseguridad & Cumplimiento Normativo (ISO/IEC/IEEE 29119 / ISO 27001).

---

## 2. El Dolor del Negocio y Diagnóstico
* **Problema:** En el mercado bursátil regional, las corredoras calculaban la liquidación tributaria de dividendos corporativos mediante planillas de cálculo tradicionales (MS Excel).
* **Causa Raíz:** Las fórmulas ofimáticas utilizan precisión de coma flotante binaria (IEEE-754 de 64 bits), provocando micro-descuadres acumulativos por redondeo.
* **Impacto:** Un descuadre de apenas $1.000 pesos en una nómina de $1.000.000.000 altera los factores en `0.000001` (suma de `0.999999` en vez de `1.000000`), causando el rechazo automático de la Declaración Jurada 1949 ante el SII, reprocesos de 3 a 5 semanas y multas de hasta 1 UTA por certificado rectificado (Art. 97 N° 1 del Código Tributario).

---

## 3. Propuesta de Valor y Solución Tecnológica
* **Transformación de Negocio:** Reduce el ciclo de calificación y validación tributaria de semanas a **3 segundos**, garantizando un **100% de exactitud matemática**.
* **Motor Algorítmico Fiscal:** Desarrollado en Django con la clase `decimal.Decimal` y redondeo comercial `ROUND_HALF_UP` a 6 decimales (`0.000001`).
* **Dos Compuertas BPMN 2.0:**
  * *Compuerta 1 (Sintaxis):* Validación estructural de 9 columnas obligatorias y sanitización OWASP A03 (CWE-1236) contra inyección de fórmulas CSV.
  * *Compuerta 2 (Fiscal):* Verificación matemática de cuadre de factores. Si la suma difiere de `1.000000`, la transacción se revoca atómicamente y despliega una bandeja visual de discrepancias.
* **Persistencia Híbrida Segura:**
  * *Relacional:* Supabase PostgreSQL en Tercera Forma Normal (3FN), con claves PK/FK, integridad protegida (`models.PROTECT`) y directivas de seguridad **Row Level Security (RLS)**.
  * *NoSQL Documental:* MongoDB Atlas para la colección inmutable `audit_logs`, donde cada evento queda sellado con un hash criptográfico **SHA-256** para auditoría forense ante la CMF.
* **Ciberseguridad ISO/IEC 27001:** Matriz de control RBAC con Segregación de Funciones (SoD) donde el cierre fiscal está estrictamente bloqueado para operadores de corredora (HTTP 403 Forbidden), doble factor de autenticación (MFA de 6 dígitos) y contraseñas salteadas irreversibles con **PBKDF2-SHA256**.

---

## 4. Métricas de Impacto y Retorno de Inversión
* **100% de Exactitud Matemática Fiscal:** Cero descuadres en el Formulario 22 y DJ 1949.
* **0 Multas Tributarias:** Cumplimiento normativo preventivo antes del reporte fiscal.
* **80% de Ahorro en Tiempos de Cierre Anual:** De semanas a segundos.
* **Latencia < 500 ms en Producción Cloud:** Despliegue en Vercel CDN y Render con automatización Keep-Alive 24/7.
* **Protocolo QA ISO 29119:** 13 de 13 pruebas unitarias e integrales aprobadas al 100%.

---

## 5. Ecosistema Operacional en Vivo
* **Web Pública:** https://proyecto-integrado-caso-nuam.vercel.app
* **Servidor API:** https://proyectointegrado-caso-nuam.onrender.com
* **Backoffice Admin:** https://proyectointegrado-caso-nuam.onrender.com/admin/
* **Código Fuente:** https://github.com/sicosis3dfx/ProyectoIntegrado-Caso-Nuam
