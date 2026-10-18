"""Genera los .tex de las animaciones (un tikzpicture por cuadro).

Uso:  python3 generar_animaciones.py   y luego  xelatex anim_*.tex
Cada PDF resultante tiene una página por cuadro; la presentación las
reproduce con \\animategraphics (paquete animate).
"""

HEAD = r"""\documentclass[tikz,border=0pt]{standalone}
\input{estilo}
\renewcommand{\iconscale}{1.6}
\begin{document}
"""
TAIL = r"\end{document}" + "\n"

BB = r"\useasboundingbox[fill=white] (0,0) rectangle (12.8,5.6);"


def escena_comun(letrero_txt, tickets=None):
    s = [BB]
    # salón y estantería
    s.append(r"\node[font=\scriptsize\bfseries, gris] at (2.2,5.35) {Salón};")
    s.append(r"\node[font=\scriptsize\bfseries, gris] at (8.9,5.35) {Estantería};")
    s.append(r"\draw[gris!50, line width=1pt] (7.3,1.25) -- (10.5,1.25);")
    s.append(r"\node[font=\tiny, gris] at (8.0,1.05) {4512};")
    s.append(r"\node[font=\tiny, gris] at (9.8,1.05) {7800};")
    s.append(r"\trituradora{(11.9,1.6)}")
    s.append(r"\node[font=\tiny, gris] at (11.9,0.95) {trituradora};")
    tk = ""
    s.append(r"\letrero{(2.2,4.45)}{Mapa $\to$ %s}{%s}" % (letrero_txt, tk))
    return s


def caption(txt, color="black"):
    return r"\node[font=\small, text width=12.2cm, align=center, text=%s] at (6.4,0.35) {%s};" % (color, txt)


def libro_en(x, y, color, txt, cnt=None, cnt_color="acento"):
    s = [r"\libro{(%s,%s)}{%s}{%s}" % (x, y, color, txt)]
    if cnt is not None:
        s.append(r"\contador{(%s,%s)}{%s}{%s}" % (x + 0.6, y + 0.5, cnt, cnt_color))
    return s


def globo(x, y, txt, color="cLib"):
    return r"\node[draw=%s, fill=white, rounded corners=3pt, font=\tiny\bfseries, text=%s] at (%s,%s) {%s};" % (color, color, x, y, txt)


def carrera():
    frames = []
    pasos = [
        dict(t=0, tito=1.0, letrero="4512", libroA=("8.0", 1), cap="El letrero apunta al mapa (estante 4512). Su contador vale 1: el uno del letrero."),
        dict(t=1, tito=1.0, letrero="4512", libroA=("8.0", 1), globo="4512", cap="\\textbf{1.} Tito lee el letrero: ``estante 4512''. Todavía \\emph{no} se ha anotado en el contador."),
        dict(t=2, tito=3.2, letrero="7800", libroA=("8.0", 1), libroB=True, pepe=True, cap="\\textbf{2.} Mientras Tito camina, Pepe guarda un mapa nuevo en 7800 y cambia el letrero."),
        dict(t=3, tito=4.6, letrero="7800", libroA=("8.0", 0), libroB=True, pepe=True, cap="\\textbf{3.} Pepe resta 1 al mapa viejo: el contador llega a \\textcolor{acento}{\\textbf{0}}."),
        dict(t=4, tito=5.8, letrero="7800", libroA=("trit", None), libroB=True, cap="\\textbf{4.} Para la Biblioteca nadie lo usa: \\textbf{¡a la trituradora!} El estante 4512 queda libre."),
        dict(t=5, tito=6.7, letrero="7800", sopa=1, libroB=True, cap="\\textbf{5.} El estante libre se reutiliza: ahora en 4512 hay una \\textbf{receta de sopa}."),
        dict(t=6, tito=6.8, letrero="7800", sopa=2, libroB=True, boom=True, cap="\\textbf{6.} Tito llega, se anota\\ldots{} en la sopa, y la lee como si fuera el mapa: \\textcolor{acento}{\\textbf{use-after-free}}."),
        dict(t=7, tito=6.8, letrero="7800", sopa=2, libroB=True, boom=True, fin=True, cap="El culpable no es nadie: es el \\textbf{hueco entre dos pasos} (leer el letrero y anotarse)."),
    ]
    for p in pasos:
        s = escena_comun(p["letrero"])
        if p.get("libroB"):
            s += libro_en(9.8, 1.65, "cWil", "B", 1, "cWil")
        la = p.get("libroA")
        if la:
            if la[0] == "trit":
                s.append(r"\libro{(11.9,2.75)}{gris}{A}")
                s.append(r"\draw[->, gris, thick, dashed] (8.4,2.1) to[bend left=20] (11.6,2.4);")
            else:
                cc = "acento" if la[1] == 0 else "cLib"
                s += libro_en(8.0, 1.65, "cLib", "A", la[1], cc)
                s.append(r"\node[font=\scriptsize, cLib] at (8.0,2.4) {mapa};")
        if p.get("sopa"):
            s += libro_en(8.0, 1.65, "cFol", "S", p["sopa"], "cFol")
            s.append(r"\node[font=\scriptsize, cFol!80!black] at (8.0,2.4) {sopa};")
        s.append(r"\robot{(%s,1.95)}{cLib}{Tito}" % p["tito"])
        if p.get("globo"):
            s.append(globo(p["tito"] + 0.3, 3.5, "4512"))
        if p.get("pepe"):
            s.append(r"\persona{(6.3,4.35)}{cWil}{Pepe}")
        else:
            s.append(r"\persona{(6.3,4.35)}{gris}{Pepe}")
        if p.get("boom"):
            s.append(r"\node[star, star points=10, star point ratio=1.6, fill=acento!20, draw=acento, line width=1pt, font=\scriptsize\bfseries, text=acento, inner sep=1pt] at (5.3,2.5) {¡Sopa!};")
        # línea de tiempo
        s.append(r"\draw[gris!60] (0.4,0.85) -- (12.4,0.85);")
        for k in range(8):
            fill = "azul" if k <= p["t"] else "white"
            s.append(r"\draw[azul, fill=%s] (%s,0.85) circle (0.07);" % (fill, 0.4 + k * 12.0 / 7))
        s.append(caption(p["cap"], "acento" if p.get("fin") else "black"))
        frames.append("\\begin{tikzpicture}\n" + "\n".join(s) + "\n\\end{tikzpicture}\n")
    return HEAD + "\n".join(frames) + TAIL


def tickets():
    frames = []
    pasos = [
        dict(t=0, tito=1.0, letrero="4512", tk=5, rcA=5, cap="Con tickets: el letrero trae un talonario de \\textbf{5} y el contador del mapa ya los incluye (5)."),
        dict(t=1, tito=1.0, letrero="4512", tk=4, rcA=5, tito_tk=True, cap="\\textbf{1.} Tito \\textbf{arranca} un ticket: en el mismo movimiento obtiene el estante \\emph{y} su derecho a leer."),
        dict(t=2, tito=3.2, letrero="7800", tk=8, rcA=5, tito_tk=True, pepe=True, pepe_txt="4512 + 4 tickets", libroB=8, cap="\\textbf{2.} Pepe cambia el letrero de golpe (talonario nuevo de 8) y se queda con los \\textbf{4} tickets sobrantes."),
        dict(t=3, tito=4.6, letrero="7800", tk=8, rcA=1, tito_tk=True, pepe=True, libroB=8, cap="\\textbf{3.} Pepe resta solo los 4 sobrantes: el contador queda en \\textbf{1}, que es el ticket de Tito."),
        dict(t=4, tito=6.2, letrero="7800", tk=8, rcA=1, tito_tk=True, libroB=8, ok=True, cap="\\textbf{4.} El mapa sigue vivo mientras Tito tenga su ticket: \\textcolor{verde}{\\textbf{no hay hueco}}."),
        dict(t=5, tito=6.8, letrero="7800", tk=8, rcA=1, tito_tk=True, libroB=8, ok=True, lee=True, cap="\\textbf{5.} Tito llega y lee \\textbf{el mapa correcto}."),
        dict(t=6, tito=6.8, letrero="7800", tk=8, rcA=None, libroB=8, cap="\\textbf{6.} Al terminar devuelve su ticket: el contador llega a 0 y \\emph{ahora sí} va a la trituradora."),
        dict(t=7, tito=6.8, letrero="7800", tk=8, rcA=None, libroB=8, fin=True, cap="Leer y anotarse es \\textbf{un solo paso} (\\emph{fetch-and-add}): el mapa nunca se destruye con un lector en camino."),
    ]
    for p in pasos:
        s = escena_comun(p["letrero"], p["tk"])
        # talonario visual
        s.append(r"\node[font=\scriptsize\bfseries, cFol!80!black, anchor=west] at (%s,3.65) {$\times$%d};" % (0.75 + min(p["tk"], 8) * 0.5, p["tk"]))
        for i in range(min(p["tk"], 8)):
            s.append(r"\ticket{(%s,3.65)}{cFol}" % (0.9 + i * 0.5))
        if p.get("libroB"):
            s += libro_en(9.8, 1.65, "cWil", "B", p["libroB"], "cWil")
        if p["rcA"] is not None:
            cc = "verde" if p["rcA"] == 1 else "cLib"
            s += libro_en(8.0, 1.65, "cLib", "A", p["rcA"], cc)
            s.append(r"\node[font=\scriptsize, cLib] at (8.0,2.4) {mapa};")
        else:
            s.append(r"\libro{(11.9,2.75)}{gris}{A}")
            s.append(r"\draw[->, gris, thick, dashed] (8.4,2.1) to[bend left=20] (11.6,2.4);")
        s.append(r"\robot{(%s,1.95)}{cLib}{Tito}" % p["tito"])
        if p.get("tito_tk"):
            s.append(r"\ticket{(%s,2.15)}{cFol}" % (p["tito"] - 0.75))
            s.append(r"\node[font=\tiny, cFol!80!black] at (%s,2.5) {4512};" % (p["tito"] - 0.75))
        if p.get("pepe"):
            s.append(r"\persona{(6.3,4.35)}{cWil}{Pepe}")
            if p.get("pepe_txt"):
                s.append(globo(7.9, 4.75, p["pepe_txt"], "cWil"))
        else:
            s.append(r"\persona{(6.3,4.35)}{gris}{Pepe}")
        if p.get("lee"):
            s.append(r"\node[circle, fill=verde!20, draw=verde, line width=1pt, font=\scriptsize\bfseries, text=verde] at (5.6,2.5) {\checkmark};")
        s.append(r"\draw[gris!60] (0.4,0.85) -- (12.4,0.85);")
        for k in range(8):
            fill = "azul" if k <= p["t"] else "white"
            s.append(r"\draw[azul, fill=%s] (%s,0.85) circle (0.07);" % (fill, 0.4 + k * 12.0 / 7))
        s.append(caption(p["cap"], "verde!60!black" if p.get("fin") else "black"))
        frames.append("\\begin{tikzpicture}\n" + "\n".join(s) + "\n\\end{tikzpicture}\n")
    return HEAD + "\n".join(frames) + TAIL


def peso():
    # Ejemplo del libro: P = 4, C = 8. Eventos: (peso, texto, quién)
    C, P = 8, 4
    ev = [
        (8, "El letrero se cuelga con $C=8$ tickets (y el contador suma 8).", None),
        (7, "Un lector arranca un ticket: el peso baja de uno en uno.", None),
        (6, "Otro lector\\ldots", None),
        (5, "Otro más\\ldots", None),
        (4, "El peso llega a $P=4$: entramos en la \\textcolor{acento}{zona roja}.", None),
        (3, "\\textbf{Tito} arranca en zona roja (\\emph{falta}): aparta 5 en el contador y debe recargar.", "T"),
        (2, "\\textbf{Pepe} también comete una falta: aparta 6 y debe recargar.", "P"),
        (2, "El CAS de Tito falla: ve 2, \\emph{menos} de lo esperado (3) $\\Rightarrow$ reintenta.", "T"),
        (7, "Tito reintenta y su CAS funciona: $2 + 5 = 7$, el peso sale de la zona roja.", "T"),
        (7, "El CAS de Pepe falla y ve 7, \\emph{más} de lo esperado: \\textbf{salida temprana} (devuelve sus 6).", "P"),
        (6, "Los lectores siguen leyendo con un solo \\emph{fetch-and-add}\\ldots", None),
        (6, "Garantía: el peso nunca es negativo y cada recarga termina en $\\le P$ intentos.", None),
    ]
    W, H = 11.0, 3.6
    xs = lambda i: 0.9 + i * (W / (len(ev) - 1))
    ys = lambda w: 1.2 + w * (H / 9.0)
    frames = []
    for k in range(len(ev)):
        s = [BB]
        s.append(r"\fill[acento!10] (0.9,%s) rectangle (%s,%s);" % (ys(0), xs(len(ev) - 1), ys(P)))
        s.append(r"\node[font=\tiny, acento, anchor=south west] at (0.95,%s) {zona roja};" % ys(0))
        s.append(r"\draw[dashed, acento] (0.9,%s) -- (%s,%s) node[right, font=\scriptsize] {$P$};" % (ys(P), xs(len(ev) - 1), ys(P)))
        s.append(r"\draw[dashed, gris] (0.9,%s) -- (%s,%s) node[right, font=\scriptsize] {$C$};" % (ys(C), xs(len(ev) - 1), ys(C)))
        s.append(r"\draw[->] (0.9,%s) -- (0.9,%s) node[above, font=\scriptsize] {peso};" % (ys(0), ys(9.3)))
        s.append(r"\draw[->] (0.9,%s) -- (%s,%s) node[right, font=\scriptsize] {tiempo};" % (ys(0), xs(len(ev) - 1) + 0.6, ys(0)))
        for w in range(0, 9, 2):
            s.append(r"\node[left, font=\tiny] at (0.9,%s) {%d};" % (ys(w), w))
        pts = " -- ".join("(%s,%s)" % (xs(i), ys(ev[i][0])) for i in range(k + 1))
        if k > 0:
            s.append(r"\draw[very thick, cFol] %s;" % pts)
        for i in range(k + 1):
            who = ev[i][2]
            col = {"T": "cLib", "P": "cWil"}.get(who, "cFol")
            s.append(r"\fill[%s] (%s,%s) circle (0.08);" % (col, xs(i), ys(ev[i][0])))
            if who:
                s.append(r"\node[font=\tiny\bfseries, text=%s, above=2pt] at (%s,%s) {%s};" % (col, xs(i), ys(ev[i][0]), "Tito" if who == "T" else "Pepe"))
        s.append(caption(ev[k][1]))
        frames.append("\\begin{tikzpicture}\n" + "\n".join(s) + "\n\\end{tikzpicture}\n")
    return HEAD + "\n".join(frames) + TAIL


if __name__ == "__main__":
    for nombre, fn in [("anim_carrera", carrera), ("anim_tickets", tickets), ("anim_peso", peso)]:
        open(nombre + ".tex", "w", encoding="utf-8").write(fn())
        print("escrito", nombre + ".tex")
