# Contexto para continuar este trabajo

Esta carpeta contiene todo lo que Claude creó en una conversación con David (18 de octubre de 2026). Sirve para que otra IA continúe donde se quedó. Todo gira en torno al paper:

> I. G. de Wolff, D. Anderson, G. K. Keller, A. Seletskiy. *A Fast Wait-Free Solution to Read-Reclaim Races in Reference Counting*. Euro-Par 2024, LNCS 14803, pp. 103–118. Código: github.com/ivogabe/wait-free-atomic-shared-pointer (artefacto en Zenodo, doi:10.5281/zenodo.11775182).

El PDF del paper y una explicación detallada (`explicacion-completa.pdf`) están en la carpeta padre (`alvaroproyectofinal`).

## Qué se pidió y qué se hizo, en orden

1. **Novela al estilo de Isaac Asimov** a partir de `explicacion-completa.pdf`, con prólogo, capítulos, epílogo, etc. → `01_novela_estilo_asimov/`.
2. **Versión más sencilla**: sin estilo Asimov, con nombres fáciles de recordar, primero en Markdown y luego en PDF, pensada para leerse como texto (sin tablas ni fórmulas) → `02_historia_sencilla/`.
3. **Plantilla de diapositivas en Overleaf**: vacía, con un solo gráfico en una diapositiva → `04_plantilla_diapositivas/`. Se creó en el Overleaf de David como proyecto "Diapositivas".
4. **Presentación académica del paper con gráficos y animaciones para Overleaf** → `03_presentacion_overleaf/`.
5. **Recomendación de qué experimentos priorizar** → `RECOMENDACION_EXPERIMENTOS.md`.

## 01_novela_estilo_asimov

- `La_Primera_Regla_del_Archivo.pdf` (91 páginas, A5): novela corta en el Archivo Central de Ceres. Personajes: Inés Calderón (matemática), el robot Siete, el comisionado Mendieta, el archivero Beto Arce, la directora Helga Sørensen, el profesor Loew y el robot navegante ANA-3. Incluye las "Tres Reglas del Archivo" (no fundir lo que se lee, nadie espera sin término, no guardar lo que nadie lee), prólogo, 10 capítulos, epílogo, una nota "lo real y lo inventado" y 4 apéndices (diccionario Ceres ↔ paper, algoritmos, cuentas, mapa de secciones del paper a capítulos).
- `fuente_latex/`: fuentes. Se compila con **XeLaTeX** (`main.tex` incluye los demás). Usa la fuente TeX Gyre Pagella. `build.sh` usaba un formato propio con patrones de silabeo español; en Overleaf basta compilar `main.tex` con XeLaTeX y, si falla el idioma, cambiar las líneas de babel por `\usepackage[spanish]{babel}`.

## 02_historia_sencilla

- `El_misterio_del_letrero.md` y `.pdf` (75 páginas, A5). Ocurre en la Gran Biblioteca de la Base Luna. Personajes: la profe Luz, el robot Tito, Pepe (bibliotecario), Doña Rosa (directora, ama las llaves), Don Tomás (viejo sabio), Max (inspector) y Nico (robot piloto de la nave Paloma).
- Equivalencias: libro = objeto, estante = dirección, contador = refcount, trituradora = liberar memoria, letrero = atomic shared pointer, talonario de tickets = peso, zona roja = peso ≤ P, "falta" = *offence*, salida temprana = la condición que lo hace wait-free.
- Al final trae "Lo que es real" (glosario historia → informática) y un "Resumen en diez frases".

## 03_presentacion_overleaf

- `main.tex`: **versión final**, Beamer 16:9, se compila con **pdfLaTeX** y está en español (`babel` con `es-noshorthands`, necesario para que funcionen las animaciones `<...>` de Beamer). Tiene 23 diapositivas y 47 páginas contando las animaciones (capas `\onslide`, `\only`, `\pause`, `\textcolor<n>`).
- Los gráficos están dibujados en **TikZ simple** (macros `\ejes` y `\serie`) y no en pgfplots, para compilar rápido. Los datos se leyeron a ojo de las Figuras 5 (throughput) y 6 (latencia) del paper, así que son aproximados.
- `Presentacion_WaitFree_RC.pdf`: compilación de prueba hecha fuera de Overleaf, sin el paquete babel en español, que no estaba instalado allí.
- `main_version_anterior_pgfplots.tex`: primera versión, con pgfplots y 99 páginas. **Supera el tiempo de compilación del plan gratuito de Overleaf**, por eso se reemplazó.
- Detalles técnicos aprendidos: (1) no anidar `\Call{}` dentro de `\Call{}` en algpseudocode, porque rompe en Beamer; se usa `\textproc{...}(...)`. (2) No usar `\rowcolor` después de `\pause` en tablas. (3) El tiempo de compilación lo domina el número de páginas o capas, no los gráficos.

### Estado en Overleaf (cuenta de David)

- Proyecto "Diapositivas" (plantilla): listo y compilando.
- Proyecto "Presentación - Wait-Free Reference Counting (Euro-Par 2024)": **contiene la versión anterior (pgfplots), que da timeout**. Falta reemplazar su `main.tex` por el de `03_presentacion_overleaf/main.tex` y recompilar. Se puede pegar a mano: seleccionar todo en el editor y pegar el contenido nuevo.

## 04_plantilla_diapositivas

- `main.tex`: Beamer 16:9 con 5 diapositivas vacías y un gráfico de barras de ejemplo (pgfplots) en la tercera.

## Pendientes y siguientes pasos posibles

- Subir la versión final de la presentación al proyecto de Overleaf y comprobar que compila en el plan gratuito.
- Si se quiere más animación sin superar el límite de tiempo, se puede compilar con la opción `handout` para revisar y quitarla al final, o pasar a un plan con más tiempo de compilación.
- Revisar `propuestas-nuevo-paper.md` (carpeta padre) junto con `RECOMENDACION_EXPERIMENTOS.md` para decidir los experimentos del nuevo paper.
