

## P : Poids maximal du sac
## N : Nombre d'objets
## W : Liste des poids des objets
## V : Liste des valeurs des objets

def knapsack(P,N,W,V) :
    X = [[0 for _ in range(P+1)] for _ in range(N+1)]

    for i in range(1,N+1) :
        for j in range(P+1) :
            if j < W[i-1] :
                X[i][j] = X[i-1][j]
            else :
                X[i][j] = max(X[i-1][j], X[i-1][j-W[i-1]] + V[i-1])
    
    # Recherche des objets sélectionnés
    objets = []
    j = P
    for i in range(N, 0, -1):
        if X[i][j] != X[i-1][j]:
            objets.append(i)
            j -= W[i - 1]

    objets.reverse()
    return X[N][P], objets


if __name__ == "__main__" :
    N = int(input("Nombre d'objets : "))
    P = int(input("Capacité du sac : "))
    W = list(map(int,input("Poids : ").split()))
    V = list(map(int,input("Valeurs : ").split()))

    valeur, objets = knapsack(P,N,W,V)

    print(f"Objets sélectionnés : {objets}\nValeur totale : {valeur}")

