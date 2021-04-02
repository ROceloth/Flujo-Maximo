N = { 'u': [['u',1,7,4],
            ['u',2,2,2],
            [3,'u',3,2]],
      
      1: [['u',1,7,4],
          [1,4,3,1],
          [1,5,3,3]],
      
      2: [['u',2,2,2],
          [2,4,1,1],
          [2,6,3,1]],
      
      3: [[3,'u',3,2],
          [5,3,3,3],
          [3,6,4,1]],
      
      4: [[1,4,3,1],
          [2,4,1,1],
          [4,'v',5,2]],
      
      5: [[1,5,3,3],
          [5,3,3,3,],
          [5,'v',3,0]],

      6: [[2,6,3,1],
          [3,6,4,1],
          [6,'v',4,2]],

      'v': [[4,'v',5,2],
            [5,'v',3,0],
            [6,'v',4,2]]
    }

"""
u -> u
r -> 1
s -> 3
z -> 2
y -> 4
w -> 5
t -> 6
v -> v
"""

def printNetInc(N:dict):
    """
    Imprime la Network N, la cual esta representada por una lista de incidencias.
    Las incidencias para cada vertice es una lista de los arcos que inciden
    al vertice sea que salgan o vallan hacia el, el orden de las listas
    internas indica el caso de los arcos sindo este de la forma:

    [x,y,c,f] en donde

    x es el primer extremo del arco
    y es el segundo extremo del arco
    por lo tanto describe el arco en direccion (x,y)
    c es la capacidad con la que cuenta el arco (x,y)
    f es el flujo actual que tiene el arco (x,y)
    (por norma f(x,y) <= c(x,y))

    Existiran dos vértices destacdos en la red;
    u -- The source (La fuente)
    v -- The sink (El pozo)
    """
    for v in N:
        print(v, ': ', N[v])

printNetInc(N) #jalo









