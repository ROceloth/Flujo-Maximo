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

def maxF(N:dict): #1
    #E, donde se guardan y registran los vértices etiquetados
    E = {'u': ('-',-1,float('inf')) } 
    L = ['u'] #Lista-cola de procesamiento #2

    #3 scan
    while 'v' not in E:        
        if L: #Fancy mustra que la lista esta vacia
          x = L.pop(0)
          arcs = N[x]
          for a in arcs:
              if a[0] == x: #fordward arc
                  y = a[1]
                  if y not in E and a[3] < a[2]:                  
                      ex = E[x][2]
                      ey = min(ex, (a[2] - a[3]))
                      E[y] = (x,1,ey)
                      L.append(y)
              else: #backward arc
                  y = a[0]
                  if y not in E and a[3] > 0:
                      ex = E[x][2]
                      ey = min(ex, a[3])
                      E[y] = (x,-1,ey)
                      L.append(y)
        else:#4
            break #end

    
    print('E: ', E)
    print('L: ', L)    
    #Actualizar flujo
    #E describe un semipath augmenting desde v

    ev = E['v'][2]
    #print("ev: ", ev)

    v = 'v'
    while v != 'u':
        #print('v: ', v)
        w = E[v][0]
        #print('w: ', w)
        
        if E[v][1] == 1: #fordward arc (w,v)
            #print('fordward')
            arcsw = N[w]
            for i in range(len(arcsw)):
                if N[w][i][1] == v:
                    #print('i: ', i)
                    #print('N[w][i][0]: ', N[w][i][0])
                    #print('antes; N[w][i]: ', N[w][i])
                    N[w][i] = [w,v,N[w][i][2],N[w][i][3] + ev]
                    #print('despues; N[w][i]: ', N[w][i])
                    
                    
            arcsv = N[v]
            for i in range(len(arcsv)):
                if N[v][i][0] == w:
                    #print('i: ', i)
                    #print('N[v][i][0]: ', N[v][i][0])
                    #print('antes; N[v][i]: ', N[v][i])
                    N[v][i] = [w,v,N[v][i][2],N[v][i][3] + ev]
                    #print('despues; N[v][i]: ', N[v][i])
                    
        else: #backward arc (v,w)
            #print('backward')
            arcsw = N[w]
            for i in range(len(arcsw)):
                if N[w][i][0] == v:
                    #print('i: ', i)
                    #print('N[w][i][0]: ', N[w][i][0])
                    #print('antes; N[w][i]: ', N[w][i])
                    N[w][i] = [v,w,N[w][i][2], N[w][i][3] - ev]
                    #print('despues; N[w][i]: ', N[w][i])
            
            arcsv = N[v]
            for i in range(len(arcsv)):
                if N[v][i][1] == w:
                    #print('i:', i)
                    #print('N[v][i][0]: ', N[v][i][0])
                    #print('antes; N[v][i]: ', N[v][i])
                    N[v][i] = [v,w,N[v][i][2], N[v][i][3] - ev]
                    #print('despues; N[v][i]: ', N[v][i])
                    
        v = w
        #A huevo cuidado con variables residuales
        #Los buenos print('Test')
                
    

#Test 1 yeah!
maxF(N)

printNetInc(N)         
                
                
                  








