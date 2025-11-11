def transform_fait_maison(matrice,n):
    temmp_mat =[[0 for _ in range(n)] for __ in range(n)]
    moov = ["R","D","L","U"]
    moov_pos =0
    x,y =0,0
    total_case = n*n
    while total_case >0:
        if total_case == 1 and n%2 != 0:   #traitement cas impaire
            temmp_mat[x][y] == matrice[x][y]
        else:
            temmp_mat[x][y] == (((matrice[x-1] if total_case<n*n else 0)*2) +  (matrice[x+1] if total_case>1 else 0)*3)/5
        total_case -= 1
            
            
    
    