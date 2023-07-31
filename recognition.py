import matplotlib.pyplot as plt

class recognition:
     def __init__(self):
          pass

     def graph(self,n,x,y,type):

          # se hace n - value por cada valor del arreglo
          x = [value + 1 for value in x]
          y = [n - value for value in y]

          if type == 1:
               plt.plot(x,y, color='r')
          else:
               plt.plot(x,y, color='b')


     def show_graph(self):
          plt.show()


     def analyze(self,a,i,j,n):
          self.is_square(a,i,j,n)
          self.is_triangle(a,i,j,n)
          self.is_triangle_reverse(a,i,j,n)

     def is_square(self,a,i,j,n):

          # si no esta en limite del arreglo
          if i<n-1 and j<n-1:
               # si el digito de la derecha y el de abajo son 1 posiblemente sea un cuadrado
               if a[i][j+1] == 1 and a[i+1][j] == 1:

                    x = []
                    y = []

                    #print("posible_square")
                    # coordenadas de la esquina superior izquierda
                    pointer_i = i
                    pointer_j = j

                    x.append(j)
                    y.append(i)
                    #print("esquina superior izquierda = ["+str(i)+"]["+str(j)+"]")

                    # como va a aumentar la altura se comprueba que la altura sea menor al limite del arreglo
                    # y que el bit sea diferente  0
                    while i<n-1 and a[i][j] != 0:

                         # sigue recorriendo la altura
                         i = i + 1

                         # si el bit de la derecha es igual a 1
                         # asume que es la coordenada de la esquina inferior izquierda
                         if a[i][j+1] == 1:
                              x.append(j)
                              y.append(i)
                              #print("esquina inferior izquierda = ["+str(i)+"]["+str(j)+"]")

                              # como va a aumentar la j se comprueba que la j sea menor al limite del arreglo
                              # y que el bit sea diferente de 0
                              while j<n-1 and a[i][j] != 0:

                                   # sigue recorriendo la j
                                   j = j + 1

                                   # si el bit de la arriba es igual a 1
                                   # asume que es la coordenada de la esquina inferior derecha
                                   if a[i-1][j] == 1:
                                        x.append(j)
                                        y.append(i)
                                        #print("esquina inferior derecha = ["+str(i)+"]["+str(j)+"]")

                                        # como va a compruebar el otro lado la altura no debe ser mayor a la de la esquina superior izquierda
                                        # y que el bit sea diferente de 0
                                        while i>pointer_i and a[i][j] != 0:

                                             # sigue disminuyendo la altura
                                             i = i - 1

                                             # si la altura es igual a la coordenada de la esquina superior izquierda
                                             # asume que es la coordenada de la esquina superior derecha
                                             if i == pointer_i:
                                                  x.append(j)
                                                  y.append(i)
                                                  #print("esquina superior derecha = ["+str(i)+"]["+str(j)+"]")

                                                  # como va a compruebar el otro lado la base no debe ser mayor a la otra base
                                                  # mientras el bit sea diferente de 0
                                                  while j>pointer_j and a[i][j] != 0:
                                                       # sigue disminuyendo la j
                                                       j = j - 1

                                                       # si la altura es igual a la coordenada de la esquina superior derecha
                                                       # comprueba que es un cuadrado completo
                                                       if j == pointer_j:
                                                            x.append(j)
                                                            y.append(i)
                                                            self.graph(n,x,y,1)
                                                            return True
                                                                           
     
     def is_triangle(self,a,i,j,n):

          if j>0 and i<n-1 and j<n-1:
               # es un cuadrado pequeño
               if a[i+1][j-1] == 1 and a[i+1][j+1] == 1 and a[i+1][j] == 1:
                    x = []
                    y = []

                    x.append(j)
                    y.append(i)
                    x.append(j-1)
                    y.append(i+1)
                    x.append(j+1)
                    y.append(i+1)
                    x.append(j)
                    y.append(i)
                    self.graph(n,x,y,2)

               # comprobar triangulo grande
               if a[i+1][j-1] == 1 and a[i+1][j+1] == 1:

                    x = []
                    y = []

                    #print("posible_triangle")
                    # coordenadas de la esquina superior izquierda
                    point_i = i
                    point_j = j

                    x.append(j)
                    y.append(i)
                    #print("esquina superior = ["+str(i)+"]["+str(j)+"]")

                    counter = 0

                    # comienza el recorrido para comprobar todos los lados
                    # como va a aumentar la altura se comprueba que la altura sea menor al limite del arreglo
                    # mientras el bit diferente de 0 y no supere los limites
                    while a[i][j] != 0 and i<n-1 and j>0:

                         # sigue recorriendo el lado derecho del triangulo
                         i = i + 1
                         j = j - 1

                         # si el bit de la derecha es igual a 1
                         # asume que es la coordenada de la esquina inferior izquierda
                         if a[i][j+1] == 1:
                              x.append(j)
                              y.append(i)
                              #print("esquina inferior izquierda = ["+str(i)+"]["+str(j)+"]")

                              # mientras el bit diferente de 0 y no supere los limites
                              while a[i][j] != 0 and j<n-1:
                                   # recorre la j del triangulo
                                   j = j + 1

                                   # si el bit de arriba y a la derecha es igual a 1
                                   # asume que es la coordenada de la esquina inferior izquierda
                                   if a[i-1][j-1] == 1:
                                        # todo triangulo tiene dos triangulos internos en sus esquinas inferiores
                                        counter = counter + 1

                                        if counter == 2:
                                             x.append(j)
                                             y.append(i)
                                             #print("esquina inferior derecha = ["+str(i)+"]["+str(j)+"]")

                                             # mientras el bit diferente de 0 y no supere los limites
                                             while i>point_i and j>point_j and a[i][j] != 0:
                                                  # recorre el lado derecho del triangulo
                                                  i = i - 1
                                                  j = j - 1

                                                  if i == point_i and j == point_j:
                                                       x.append(j)
                                                       y.append(i)
                                                       self.graph(n,x,y,2)
                                                       return True
                                                  

     def is_triangle_reverse(self,a,i,j,n):
          if i>0 and j>0 and i<n-1 and j<n-1:
     
               # es un triangulo pequeño
               if a[i-1][j-1] == 1 and a[i-1][j+1] == 1 and a[i-1][j] == 1:
                    x = []
                    y = []

                    x.append(j)
                    y.append(i)
                    x.append(j-1)
                    y.append(i-1)
                    x.append(j+1)
                    y.append(i-1)
                    x.append(j)
                    y.append(i)
                    self.graph(n,x,y,2)
     
               # comprobar triangulo inverso grande
               if i>1 and j>1 and a[i-1][j-1] == 1 and a[i-1][j+1] == 1:
                    x = []
                    y = []

                    #print("posible_triangle_inverso")
                    # coordenadas de la esquina superior izquierda
                    point_i = i
                    point_j = j

                    x.append(j)
                    y.append(i)
                    #print("esquina superior = ["+str(i)+"]["+str(j)+"]")

                    counter = 0

                    # comienza el recorrido para comprobar todos los lados
                    # mientras el bit diferente de 0 y no supere los limites
                    while i>0 and j>0 and a[i][j] != 0:

                         # sigue recorriendo el lado derecho del triangulo
                         i = i - 1
                         j = j - 1

                         # si el bit de la derecha es igual a 1
                         # asume que es la coordenada de la esquina inferior izquierda
                         if a[i][j] != 0 and a[i][j+1] == 1:
                              x.append(j)
                              y.append(i)
                              #print("esquina inferior izquierda = ["+str(i)+"]["+str(j)+"]")

                              # mientras el bit diferente de 0 y no supere los limites
                              while a[i][j] != 0 and j<n-1:
                                   # recorre la j del triangulo
                                   j = j + 1
                         
                                   # si el bit de abajo y a la izquierda es igual a 1
                                   # asume que es la coordenada de la esquina inferior derecha
                                   if a[i+1][j-1] == 1:
                                        # para ignorar el triangulo interno
                                        counter = counter + 1

                                        if counter == 2:
                                             x.append(j)
                                             y.append(i)
                                             #print("esquina inferior derecha = ["+str(i)+"]["+str(j)+"]")

                                             # mientras no superen los puntos (i,j) y el bit diferente de 0
                                             while i<point_i and j>point_j and a[i][j] != 0:
                                                  # recorre el lado derecho del triangulo
                                                  i = i + 1
                                                  j = j - 1

                                                  if i == point_i and j == point_j:
                                                       x.append(j)
                                                       y.append(i)
                                                       self.graph(n,x,y,2)
                                                       return True