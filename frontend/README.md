# Módulo Frontend Web (SPA) — nuam EXCHANGE GROUP
## Mantenedor Centralizado de Calificaciones Tributarias y Dividendos

* **Asignatura:** Proyecto Integrado
* **Docente:** Macarena Angulo Olguín
* **Desarrolladores:** Vicente Sagredo, Martín Tapia, Angelo Zamora
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
3. **Loader Flotante Corporativo (`FloatingLoader`):** Ubicado en la cabecera central con el imagotipo oficial de nuam y spinner circular naranja-rojo reactivo a cada petición API.
4. **Hooks Personalizados:**
   * `useIntersection`: Carga y animación suave de tarjetas a medida que entran en la pantalla.
   * `useWindowScroll`: Topbar fijo (*sticky*) con desenfoque dinámico (`backdrop-filter: blur(12px)`) durante el desplazamiento en celulares.
5. **Formulario con Auto-formato de RUT:** Detección de teclado numérico con formateo instantáneo a `XX.XXX.XXX-X` y validación de dígito verificador Módulo 11 (CMF).
6. **Checklist Interactivo de Contraseñas:** Validación visual en tiempo real de políticas reforzadas ISO/IEC 27001 (mayúscula, minúscula, número y símbolo especial).

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
