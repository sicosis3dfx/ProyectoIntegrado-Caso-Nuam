# Módulo Frontend Web (SPA) — nuam EXCHANGE GROUP
## Mantenedor Centralizado de Calificaciones Tributarias y Dividendos

* **Asignatura:** Proyecto Integrado
* **Docente:** Macarena Angulo Olguín
* **Desarrollador Principal Frontend:** Angelo Alberto Zamora Romero
* **Equipo del Proyecto:** Martín Ignacio Tapia Jaramillo (Backend & DB), Vicente Sagredo (QA & Pruebas)
* **Institución:** INACAP — Segundo Semestre 2026

---

### 🚀 Stack Tecnológico y Arquitectura UI
* **Librería UI:** React 19 (Modo estricto, componentes funcionales con hooks tipados)
* **Lenguaje:** TypeScript 5.8 (Tipado estático estricto, cero uso de `any`)
* **Empaquetador y Servidor Dev:** Vite 8 (Hot Module Replacement con compilación < 150 ms)
* **Diseño y Estilos:** CSS nativo modular con variables CSS, paleta institucional oscura (Dark Theme WCAG 2.1 AA) y media queries responsivas.

---

### 📱 Características Principales y Modo Responsivo
1. **Menú Hamburguesa Móvil (☰ / ✕):** Navegación off-canvas deslizante en pantallas `<= 768px` con telón oscuro (*backdrop*).
2. **Vista Dual (Lista vs. Cuadros):** Componente `ViewToggle` para alternar entre tabla tradicional y tarjetas táctiles `CertificateCard`.
3. **Loader Flotante Corporativo (`FloatingLoader`):** Ubicado en la cabecera central con el imagotipo oficial de nuam y spinner circular naranja-rojo reactivo a cada petición API, con envoltura de texto adaptativa en móviles.
4. **Modal Preventivo de Confirmación de Ingesta Masiva:** Intercepta la carga o arrastre de archivos CSV con la estética glassmorphism del `FloatingLoader`. Centrado matemáticamente en pantalla (`max-width: 620px`), muestra los metadatos completos (nombre, formato, tamaño y operador sin recortes) y se adapta de forma 100% responsiva apilando verticalmente los datos y botones de acción en pantallas móviles ($\le 480px$).
5. **Alternancia de Contraseña (Ojo):** Botón con iconos SVG de visibilidad en el login para verificar la clave ingresada sin alterar el espaciado del formulario.
6. **Hooks Personalizados:**
   * `useIntersection`: Carga y animación suave de tarjetas a medida que entran en la pantalla.
   * `useWindowScroll`: Topbar fijo (*sticky*) con desenfoque dinámico (`backdrop-filter: blur(12px)`) durante el desplazamiento en celulares.
7. **Formulario con Auto-formato de RUT:** Detección de teclado numérico con formateo instantáneo a `XX.XXX.XXX-X` y validación de dígito verificador Módulo 11 (CMF).
8. **Checklist Interactivo de Contraseñas:** Validación visual en tiempo real de políticas reforzadas ISO/IEC 27001 (mayúscula, minúscula, número y símbolo especial).
9. **Micro-Footer Institucional (`Footer.tsx`):** Pie de página slim corporativo que sella la plataforma con los entes reguladores (CMF, SMV, SFC), resoluciones SII (DJ 1949/1922), leyes de protección de datos y versión `v3.2.0-LTS`. Con diseño 100% responsivo para móviles.

---

### 💻 Comandos de Ejecución

```bash
# 1. Instalar dependencias
npm install

# 2. Compilar para producción y verificar tipado TypeScript
npm run build

# 3. Iniciar servidor de desarrollo local
npm run dev
```

La aplicación se ejecutará en: `http://localhost:5173/`
*(Apunta automáticamente al backend en Render mediante `frontend/.env`)*.

---

### ☁️ Despliegue en Vercel y Enrutamiento Perimetral
* **URL de Producción:** [https://proyecto-integrado-caso-nuam.vercel.app](https://proyecto-integrado-caso-nuam.vercel.app)
* **Redirección Perimetral (`/admin`):** Configurada en `vercel.json` y `index.html` para que cualquier petición hacia `/admin` o `/admin/` sea redirigida de forma inmediata al panel de administración de Django en Render (`https://proyectointegrado-caso-nuam.onrender.com/admin/`).
* **Reglas SPA:** Todas las demás rutas de navegación se canalizan limpiamente hacia `/index.html` evitando errores 404 en recarga de página.
