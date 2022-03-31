import networkx as nx
from Torre import Torre
Grafo=nx.Graph()
entrada1="4 3 4"
x=entrada1.split()
listaX=[]
listaY=[]
listaXY=[]
for i in range(int(x[0])):
    texto= str(i+1)
    type(texto)
    listaX.append(texto)
for i in range(int(x[1])):
    texto= str(i+1)
    listaY.append(texto)
for i in listaX:
    for y in listaY:
        listaXY.append(i+y)
for i in listaXY:
    Grafo.add_node(i)
for i in range(len(listaXY)):
    test=len(listaXY)-1
    if i<test:
        inicio=listaXY[i]
        final = listaXY[i+1]
        if inicio[0]==final[0]:
            Grafo.add_edge(inicio,final)
print(Grafo)
print(Grafo.edges)
hola ="1 2 3 1"
print(hola.replace(" ", ""))


