"""
0 : obstaculo
1 : camino libre
2 : meta
"""
MAP = [[1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
       [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 2],
       [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
       [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       ]

"""
Func. para realizar busqueda a ciegas (DFS)
    Args:
       grid:list[list[int]]: Mapa con obstaculos representado en matriz.
       i [int]: Pos. en x
       j [int]: Pos. en y

    Returns:
       list[tuple[int, int]]: Lista con las coordenadas del camino a la meta
"""
def blindSearch(grid:list[list[int]], i:int, j:int) -> list[tuple[int, int]]:

    path = []
    
    def dfs(grid:list[list[int]], i:int, j:int, n:int, m:int) -> bool:
        
        if(i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == -1 or grid[i][j] == 0):
            return False
        
        # si se llego a la meta
        if(grid[i][j] == 2):
            path.append((i, j))
            return True
        
        # Marca la celda como visitada
        grid[i][j] = -1
        # Añade la celda al camino
        path.append((i, j))

        # Explora en las 4 direcciones. Si encuentra la meta, retorna True y detiene la búsqueda
        # arriba, abajo, izquierda, derecha
        if dfs(grid, i-1, j, n, m) or dfs(grid, i+1, j, n, m) or dfs(grid, i, j-1, n, m) or dfs(grid, i, j+1, n, m):
            return True

        path.pop()  # Elimina la celda del camino si no conduce a la meta
        return False

    # tamaños de la matriz
    n = len(grid)
    m = len(grid[0])
    dfs(grid, i, j, n, m)

    return path


path = blindSearch(MAP, 4, 1)
for cord in path:
    print(cord)
