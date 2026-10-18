# Progreso: presentación v2

Objetivo: mejorar `03_presentacion_overleaf/main.tex` con infografías, animaciones dentro del PDF (paquete `animate`) y la historia de la Base Luna como hilo conductor.

- [x] Paso 0: copia de la base en `pasos/paso0_main_base.tex`
- [x] Paso 1: figuras e infografías (analogia, tres_reglas, resultados) (TikZ standalone → `figuras/*.pdf`, fuentes en `fuentes_figuras/`)
- [x] Paso 2: animaciones (anim_carrera 8 cuadros, anim_tickets 8, anim_peso 12; generadas con fuentes_figuras/generar_animaciones.py y compiladas con xelatex) (cuadros en un PDF multipágina → `animaciones/*.pdf`, mostradas con `\animategraphics`)
- [x] Paso 3: diapositivas de la historia: "Una historia para empezar", "La misma idea, en la Gran Biblioteca de la Luna", "Material complementario"
- [x] Paso 4: `main.tex` integrado (30 diapositivas, 53 páginas con capas); compila en ~3,6 s en local; animaciones verificadas dentro del PDF; copia en `pasos/paso4_main_integrado.tex`
- [ ] Paso 5: copiar a la PC

Cómo regenerar figuras: en `fuentes_figuras/`, `python3 generar_animaciones.py` y luego `xelatex <archivo>.tex` (usa TeX Gyre Heros); copiar los PDF a `figuras/` o `animaciones/`.

## Entregables
- `main.tex` + `figuras/` + `animaciones/` → la presentación (compilar con pdfLaTeX).
- `Overleaf_presentacion_v2.zip` → subir en Overleaf con *New Project → Upload Project*.
- `Presentacion_v2_con_animaciones.pdf` → compilado (sin silabeo español porque el entorno no lo tenía; Overleaf sí lo aplica).
- `PROMPTS_CODEX.md` → prompts opcionales para ilustraciones con Codex.

## Notas
- Las animaciones usan el paquete `animate`: se ven en Adobe Acrobat Reader, Okular y PDF-XChange. En Chrome, Edge o la vista previa de Overleaf solo aparece el primer cuadro.
- Se eliminó la diapositiva "El peso a lo largo del tiempo" (capas) y se sustituyó por la animación `anim_peso` (ejemplo P=4, C=8 de la historia).
