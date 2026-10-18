# Qué experimentos priorizar

Recomendación para un paper que reproduzca o extienda *A Fast Wait-Free Solution to Read-Reclaim Races in Reference Counting* (Euro-Par 2024). Ordenado por impacto.

## 1. Imprescindible: demostrar el resultado principal

- **Throughput frente a número de hilos con baja contención** (por ejemplo n = 10 pilas, u = 1 % de actualizaciones). Es donde el método gana a todos, incluido Anderson: unos 47 frente a 30 Mop/s en el paper. Es el argumento central.
- **Latencia de `load` con contención alta** (p = 56 hilos). Muestra la ventaja de ser wait-free: unos 1,14 µs frente a 2,58 µs (Anderson) y unos 100 µs (libstdc++, con candados). Conviene reportar también los percentiles altos (99 %), no solo la mediana, porque ahí se ve la garantía.

## 2. Importante: ser honesto con los límites

- **Una sola pila con contención alta** (n = 1). Gana Anderson, porque cada lectura escribe en la misma palabra atómica. Mostrarlo da credibilidad y explica cuándo usar cada método.
- **Barrido del porcentaje de actualizaciones** (u = 1, 10 y 50 %). Muestra cómo el compare-and-swap, que es solo lock-free, se degrada con muchas escrituras.

## 3. Lo que el paper no tiene y aportaría más

- **Memoria usada a lo largo del tiempo** frente a Anderson y otros esquemas de reclamación diferida (hazard pointers, épocas). El paper afirma "sin sobrecoste de memoria" pero no lo mide, y es su ventaja principal frente a Anderson.
- **Pruebas de corrección por intercalado**: estrés con ThreadSanitizer, o intercalados forzados con un planificador controlado. Deben mostrar que las variantes sin R-1, sin R-2 o sin salida temprana fallan y la propuesta no.
- **Peor caso de recarga**: cuántas iteraciones de `increase_weight` se dan en la práctica frente a la cota P.
- **Sensibilidad a C y P**: 16 bits libres frente a 19, o un C pequeño como el de Folly (C = 8192).

## 4. Secundario, si hay tiempo

- Otras estructuras además de la pila: colas, tablas hash, listas.
- Otras arquitecturas, como ARM con TBI/PAC, o x86 con LA57, donde cambian los bits libres del puntero.
- El coste de los punteros *aliased* con el fallback de 128 bits.

## Si el espacio es limitado

Bloque 1, la pila única del bloque 2 y la medición de memoria del bloque 3. Con eso se cuenta la historia completa: dónde gana el método, dónde pierde y por qué vale la pena.
