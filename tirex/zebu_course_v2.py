import os

def zebu_compare(zebus):
    n = zebus[0]
    zebus = zebus[1:n+1]
    zebus.sort()
    diff_min = zebus[-1]
    for i in range(1,n):
        if zebus[i] == zebus[i-1]:
            return 0
        else:
            curr_diff = zebus[i] - zebus[i-1]
            diff_min = min(diff_min, curr_diff)           
                        
    return diff_min

zebu_input = []
methode = input("Choisissez la méthode d'entrée (1 pour fichier, 2 pour la console): ")
if methode == "1":
    filename = input("Entrez le chemin du fichier: ")
    clean_path =  os.path.expanduser(filename.strip().strip('\'"'))
    
    try:
        with open(clean_path, "r") as f:
            zebu_input = list(map(int,f.readline().split()))
            
    except FileNotFoundError:
        print(f"Fichier introuvable: {clean_path}")
        raise
elif methode == "2":
    zebu_input = list(map(int, input("Entrez les nombres : ").split()))
if not zebu_input or  zebu_input[0] < 2 :
    print("Il faut au moins 2 zebus") 
else:
    print(zebu_compare(zebu_input))


