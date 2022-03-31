from Torre import Torre
import networkx as nx

estructura="4 3 4"
energia="2 1 3 0"
portal1="1 2 3 1"
portal2="1 3 4 3"
portal3="2 1 4 2"
portal4="3 2 4 1"
portales=list()
portales.append(portal1)
portales.append(portal2)
portales.append(portal3)
portales.append(portal4)
torre=Torre(estructura,energia,portales)
print(type(torre.energia))
print(torre.portales)
Grafo = nx.Graph()
def crearGrafoBase(estructura):
    x = estructura.split()
    listaX = []
    listaY = []
    listaXY = []
    for i in range(int(x[0])):
        texto = str(i + 1)
        type(texto)
        listaX.append(texto)
    for i in range(int(x[1])):
        texto = str(i + 1)
        listaY.append(texto)
    for i in listaX:
        for y in listaY:
            listaXY.append(i + y)
    for i in listaXY:
        Grafo.add_node(i)
    for i in range(len(listaXY)):
        test = len(listaXY) - 1
        if i < test:
            inicio = listaXY[i]
            final = listaXY[i + 1]
            listaEnergia=torre.energia.replace(" ", "")
            if inicio[0] == final[0]:
                #print("piso"+" "+inicio[0])
                #print(listaEnergia[int(inicio[0])-1])
                Grafo.add_edge(inicio, final, weight=listaEnergia[int(inicio[0])-1])
    nx.draw(Grafo,with_labels=True)
    return Grafo
def crearPortales():
    for i in torre.portales:
        resultado=i.replace(" ", "")
        inicio=resultado[0]+resultado[1]
        fin=resultado[2]+resultado[3]
        Grafo.add_edge(inicio,fin,weight=100)
crearGrafoBase(torre.estructura)
crearPortales()
t=nx.dijkstra_path(Grafo,source="11",target="43",weight=True)
print(t)
print(Grafo)
print(Grafo.edges)
#print(crearGrafoBase(torre.estructura))


