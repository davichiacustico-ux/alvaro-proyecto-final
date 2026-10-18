# Material de Estudio y Divulgación: Wait-Free Reference Counting

Repositorio con material divulgativo, narrativo, académico y experimental en torno al paper:

> **I. G. de Wolff, D. Anderson, G. K. Keller, A. Seletskiy.**  
> *A Fast Wait-Free Solution to Read-Reclaim Races in Reference Counting.*  
> Euro-Par 2024, LNCS 14803, pp. 103–118.  
> Código de referencia: [ivogabe/wait-free-atomic-shared-pointer](https://github.com/ivogabe/wait-free-atomic-shared-pointer) (Zenodo DOI: [10.5281/zenodo.11775182](https://doi.org/10.5281/zenodo.11775182)).

---

## 📁 Contenido del Repositorio

- **`01_novela_estilo_asimov/`**: 
  - `La_Primera_Regla_del_Archivo.pdf` (91 páginas, A5): Novela corta ambientada en el Archivo Central de Ceres. Explica de forma narrativa las "Tres Reglas del Archivo", el algoritmo de conteo de referencias wait-free, apéndices y equivalencias técnicas.
  - `fuente_latex/`: Código fuente completo en LaTeX (compilable con XeLaTeX).
- **`02_historia_sencilla/`**: 
  - `El_misterio_del_letrero.md` y `.pdf` (75 páginas, A5): Versión pedagógica y directa ambientada en la Gran Biblioteca de la Base Luna, ideal para lectura continua sin fórmulas complejas.
- **`03_presentacion_overleaf/`**: 
  - `main.tex`: Presentación académica en Beamer (16:9, en español) optimizada para tiempos de compilación en Overleaf con TikZ.
  - `Presentacion_WaitFree_RC.pdf`: PDF compilado de la presentación (23 diapositivas, 47 pantallas con animaciones).
- **`04_plantilla_diapositivas/`**: 
  - Plantilla limpia y mínima en Beamer con ejemplo gráfico para nuevas presentaciones.
- **`05_presentacion_v2/`** (versión más reciente):
  - `Presentacion_v2_con_animaciones.pdf`: 30 diapositivas con infografías y tres animaciones dentro del PDF (la carrera *read-reclaim*, la solución con tickets y la recarga con salida temprana), con los personajes de *El misterio del letrero*. Las animaciones se reproducen en Adobe Acrobat Reader, Okular o PDF-XChange; en navegadores y celulares solo se ve el primer cuadro.
  - `main.tex` + `figuras/` + `animaciones/`: fuente Beamer (pdfLaTeX). `Overleaf_presentacion_v2.zip` se sube a Overleaf con *New Project → Upload Project*.
  - `fuentes_figuras/`: fuentes TikZ de las infografías y `generar_animaciones.py`. `PROGRESO.md` y `pasos/` registran el proceso.
- **`LEEME_CONTEXTO.md`**: Detalle cronológico y contextual del proyecto y consideraciones técnicas de compilación.
- **`RECOMENDACION_EXPERIMENTOS.md`**: Guía y priorización de experimentos y benchmarks basados en el paper original.
