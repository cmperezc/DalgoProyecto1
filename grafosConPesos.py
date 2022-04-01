from collections import deque
import functools


class Grafo(object):
    def __init__(self):
        self.relaciones = {}

    def __str__(self):
        return str(self.relaciones)


class Arista(object):
    def __init__(self, elemento, peso):
        self.elemento = elemento
        self.peso = peso

    def __str__(self):
        return str(self.elemento) + str(self.peso)


def agregar(grafo, elemento):
    grafo.relaciones.update({elemento: []})


def relacionar(grafo, elemento1, elemento2, peso=1):
    relacionarUnilateral(grafo, elemento1, elemento2, peso)
    relacionarUnilateral(grafo, elemento2, elemento1, peso)


def relacionarUnilateral(grafo, origen, destino, peso):
    grafo.relaciones[origen].append(Arista(destino, peso))


def caminoMinimo(grafo, origen, destino):
    etiquetas = {origen: (0, None)}
    dijkstra(grafo, destino, etiquetas, [])
    return construirCamino(etiquetas, origen, destino)


def construirCamino(etiquetas, origen, destino):
    if (origen == destino):
        return [origen]
    return construirCamino(etiquetas, origen, anterior(etiquetas[destino])) + [destino]


def dijkstra(grafo, destino, etiquetas, procesados):
    nodoActual = menorValorNoProcesado(etiquetas, procesados)
    #    print "-----------------------------"
    #    print "Nodo Actual:",nodoActual
    #    print "Procesados",procesados
    #    print "Etiquetas",etiquetas
    if (nodoActual == destino):
        return
    procesados.append(nodoActual)
    for vecino in vecinoNoProcesado(grafo, nodoActual, procesados):
        generarEtiqueta(grafo, vecino, nodoActual, etiquetas)
    dijkstra(grafo, destino, etiquetas, procesados)


def generarEtiqueta(grafo, nodo, anterior, etiquetas):
    etiquetaNodoAnterior = etiquetas[anterior]
    etiquetaPropuesta = peso(grafo, anterior, nodo) + acumulado(etiquetaNodoAnterior), anterior
    if (not (nodo in etiquetas) or acumulado(etiquetaPropuesta) < acumulado(etiquetas[nodo])):
        etiquetas.update({nodo: etiquetaPropuesta})


def aristas(grafo, nodo):
    return grafo.relaciones[nodo]


def vecinoNoProcesado(grafo, nodo, procesados):
    aristasDeVecinosNoProcesados = [x for x in aristas(grafo, nodo) if not x in procesados]
    return [arista.elemento for arista in aristasDeVecinosNoProcesados]


def peso(grafo, nodoOrigen, nodoDestino):
    return functools.reduce(lambda x, y: x if x.elemento == nodoDestino else y, grafo.relaciones[nodoOrigen]).peso


def acumulado(etiqueta):
    return etiqueta[0]


def anterior(etiqueta):
    return etiqueta[1]


def menorValorNoProcesado(etiquetas, procesados):
    etiquetadosSinProcesar = [nodo__ for nodo__ in iter(etiquetas.items()) if not nodo__[0] in procesados]
    return min(etiquetadosSinProcesar, key=lambda __acum___: __acum___[1][0])[0]

a = "11"
b = "12"
c = "13"
d = "21"
e = "22"
f = "23"
g = "31"
h = "32"
ix = "33"
grafo = Grafo()
agregar(grafo, a)
agregar(grafo, b)
agregar(grafo, c)
agregar(grafo, d)
agregar(grafo, e)
agregar(grafo, f)
agregar(grafo, g)
agregar(grafo, h)
agregar(grafo, ix)
relacionar(grafo, a, b, 1)
relacionar(grafo, b, c, 1)
relacionar(grafo, d, e, 1)
relacionar(grafo, b, g, 5)
relacionar(grafo, c, f, 5)
relacionar(grafo, c, d, 2)
relacionar(grafo, d, f, 2)
relacionar(grafo, d, e, 4)
relacionar(grafo, e, h, 1)
relacionar(grafo, e, g, 2)
relacionar(grafo, f, h, 3)
print (caminoMinimo(grafo, a, c))