G = {
    "a":["c"],
    "b":["c","e"],
    "c":["a","b","d","e"],
    "d":["c"],
    "e":["c","b"],
    "f":[],
}

entrada= input()



if a in G.keys():
  len(G[entrada])
else:
  print("El vertice no existe en el grafo")

