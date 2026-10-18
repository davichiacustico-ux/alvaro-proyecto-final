# Prompts para generar ilustraciones con Codex (opcional)

Las infografías y animaciones de esta versión ya están hechas con código (TikZ). Si quieres ilustraciones adicionales generadas por Codex, pídele que las cree como **SVG o PNG con código** (Python con matplotlib/PIL, o SVG escrito a mano) y que las guarde en `figuras/`. Cada prompt indica dónde encaja en `main.tex`.

Estilo común para todas: fondo blanco, plano, sin texto en inglés, paleta azul `#1F3A5F`, rojo `#C0392B`, naranja `#FF7F0E`, verde `#2E8B57`, amarillo `#F6C343`. Formato 16:9 o 4:3, sin logotipos ni personajes de marcas.

## 1. Portada: la Gran Biblioteca de la Base Luna
> Genera con Python (matplotlib o PIL) una ilustración plana 1600×900 de una biblioteca futurista dentro de una cúpula lunar: estanterías curvas, un letrero luminoso con 64 lucecitas (16 naranjas a la izquierda y 48 amarillas), un pequeño robot lector y la Tierra visible por una ventana. Guarda `figuras/ilustracion_portada.png`.

Uso: en la diapositiva de título, `\titlegraphic{\includegraphics[width=0.35\linewidth]{figuras/ilustracion_portada}}` antes de `\begin{document}`.

## 2. Personajes de la historia
> Dibuja en SVG tres personajes planos, sencillos y amables: "Tito" (robot lector, azul `#1F77B4`), "Pepe" (bibliotecario, verde `#2CA02C`) y "la profe Luz" (científica con tiza, morado `#9467BD`). Cada uno de 400×400, guardados como `figuras/tito.svg`, `figuras/pepe.svg`, `figuras/luz.svg`, y también convertidos a PDF.

Uso: en "Una historia para empezar" y en "La misma idea, en la Gran Biblioteca de la Luna".

## 3. Infografía de la palabra de 64 bits
> Crea una infografía horizontal de 64 casillas: 16 naranjas etiquetadas "peso (tickets)", 45 amarillas "dirección del objeto" y 3 grises "alineación". Encima, una flecha que muestre que un fetch-and-add de −2^48 resta un ticket sin tocar la dirección. Guarda `figuras/palabra64.pdf`.

Uso: puede sustituir el dibujo de la diapositiva "Empaquetar puntero y peso en una palabra".

## 4. Póster resumen (una página)
> Diseña un póster A3 vertical que resuma el artículo con la analogía de la Biblioteca de la Luna: problema (receta de sopa), solución (talonario de tickets), garantía (zona roja + salida temprana) y resultados (47 Mop/s, 1,14 µs, 0 basura). Guarda `figuras/poster_resumen.pdf`.

Uso: material para repartir, o como última diapositiva de respaldo.
