# Importamos las siguientes bibliotecas que permiten hacer graficar las rutas usando grafos
import networkx as nx
import matplotlib.pyplot as plt

# con nx.digrahp vamos a crear el grafo
G = nx.DiGraph() 

#Vamos a indicar la cantidad de estaciones o nodos
G.add_node('Chia')
G.add_node('Facatativa')
G.add_node('Zipaquira')
G.add_node('Fusagasuga')
G.add_node('Funza')
G.add_node('Mosquera')
G.add_node('Cajica')
G.add_node('Sibate')


#Indicamos la d istancia entre cada una de las estaciones
G.add_edge('Chia','Facatativa', weight=47)
G.add_edge('Chia','Zipaquira', weight=25)
G.add_edge('Chia','Fusagasuga', weight=101)
G.add_edge('Chia','Funza', weight=26)
G.add_edge('Chia','Madrid', weight=33)
G.add_edge('Chia','Mosquera', weight=28)
G.add_edge('Chia','Cajica', weight=9)
G.add_edge('Chia','Sibate', weight=62)
G.add_edge('Facatativa','Chia', weight=47)
G.add_edge('Facatativa','Zipaquira', weight=67)
G.add_edge('Facatativa','Fusagasuga', weight=89)
G.add_edge('Facatativa','Funza', weight=22)
G.add_edge('Facatativa','Madrid', weight=16)
G.add_edge('Facatativa','Mosquera', weight=20)
G.add_edge('Facatativa','Cajica', weight=53)
G.add_edge('Facatativa','Sibate', weight=53)
G.add_edge('Zipaquira','Chia', weight=21)
G.add_edge('Zipaquira','Facatativa', weight=63)
G.add_edge('Zipaquira','Fusagasuga', weight=119)
G.add_edge('Zipaquira','Funza', weight=46)
G.add_edge('Zipaquira','Madrid', weight=54)
G.add_edge('Zipaquira','Mosquera', weight=49)
G.add_edge('Zipaquira','Cajica', weight=13)
G.add_edge('Zipaquira','Sibate', weight=79)
G.add_edge('Fusagasuga','Chia', weight=100)
G.add_edge('Fusagasuga','Facatativa', weight=87)
G.add_edge('Fusagasuga','Zipaquira', weight=118)
G.add_edge('Fusagasuga','Funza', weight=71)
G.add_edge('Fusagasuga','Madrid', weight=72)
G.add_edge('Fusagasuga','Mosquera', weight=68)
G.add_edge('Fusagasuga','Cajica', weight=103)
G.add_edge('Fusagasuga','Sibate', weight=34)
G.add_edge('Funza','Chia', weight=26)
G.add_edge('Funza','Facatativa', weight=21)
G.add_edge('Funza','Zipaquira', weight=50)
G.add_edge('Funza','Fusagasuga', weight=72)
G.add_edge('Funza','Madrid', weight=7)
G.add_edge('Funza','Mosquera', weight=3)
G.add_edge('Funza','Cajica', weight=34)
G.add_edge('Funza','Sibate', weight=35)
G.add_edge('Madrid','Chia', weight=33)
G.add_edge('Madrid','Facatativa', weight=15)
G.add_edge('Madrid','Zipaquira', weight=59)
G.add_edge('Madrid','Fusagasuga', weight=74)
G.add_edge('Madrid','Funza', weight=7)
G.add_edge('Madrid','Mosquera', weight=5)
G.add_edge('Madrid','Cajica', weight=45)
G.add_edge('Madrid','Sibate', weight=37)
G.add_edge('Mosquera','Chia', weight=29)
G.add_edge('Mosquera','Facatativa', weight=19)
G.add_edge('Mosquera','Zipaquira', weight=52)
G.add_edge('Mosquera','Fusagasuga', weight=69)
G.add_edge('Mosquera','Funza', weight=3)
G.add_edge('Mosquera','Madrid', weight=4)
G.add_edge('Mosquera','Cajica', weight=36)
G.add_edge('Mosquera','Sibate', weight=33)
G.add_edge('Cajica','Chia', weight=8)
G.add_edge('Cajica','Facatativa', weight=53)
G.add_edge('Cajica','Zipaquira', weight=15)
G.add_edge('Cajica','Fusagasuga', weight=104)
G.add_edge('Cajica','Funza', weight=33)
G.add_edge('Cajica','Madrid', weight=40)
G.add_edge('Cajica','Mosquera', weight=36)
G.add_edge('Cajica','Sibate', weight=65)
G.add_edge('Sibate','Chia', weight=62)
G.add_edge('Sibate','Facatativa', weight=52)
G.add_edge('Sibate','Zipaquira', weight=80)
G.add_edge('Sibate','Fusagasuga', weight=34)
G.add_edge('Sibate','Funza', weight=36)
G.add_edge('Sibate','Madrid', weight=37)
G.add_edge('Sibate','Mosquera', weight=33)
G.add_edge('Sibate','Cajica', weight=65)


#Con esta información podemos ver las estaciones que tenemos disponibles.
for Estaciones in G.nodes:
    print(f"Estación: {Estaciones}")

#Para determinar cual es la mejor ruta, es necesario conocer la estación de origen y la estación de destino:
Origen = str(input("Ingrese la estación de Origen: "))
Destino = str(input("Ingrese la estación de Destino: "))

#Identificamos las estaciones y las distancias entre ellas:
Etiquetas ={(u, v): G[u][v]['weight'] for u, v in G.edges()}

#Con esta expresión de la biblioteca de nx creamos el gráfico:
pos = nx.spring_layout(G)

#La biblioteca nx evalúa con ésta expresión el algoritmo de Dijkstra para determinar la mejor ruta
Ruta = nx.dijkstra_path(G, Origen, Destino)

#Se muestra la ruta encontrada en el algoritmo de Dijsktra
print(f"""La mejor ruta desde: "{Origen}" hasta "{Destino}" es: """)
for i, parada in enumerate (Ruta):
    print(f"""Estacion: "{parada}" """)
    if i < len (Ruta) -1:
        ProximaParada = Ruta [i+1]
        print(f" - Distancia: {G[parada][ProximaParada]['weight']} m")

#Mostramos el gráfico con las funciones de la biblioteca networkx

#Ruta
Nodos =[(Ruta[i], Ruta[i+1]) for i in range(len(Ruta)-1)]
nx.draw_networkx_edges(G, pos, edgelist=Nodos, width=5, edge_color='Red')

#Marcamos las estaciones, las distancias con sus respectivos nombres
nx.draw_networkx_nodes(G, pos, node_color='Gray')
nx.draw_networkx_edges(G, pos, edge_color='Gray')
nx.draw_networkx_edge_labels(G, pos, edge_labels=Etiquetas, font_size=8)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight=4)


#Visualizar el gráfico
plt.show()