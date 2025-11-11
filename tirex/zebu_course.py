import os

def zebu_compare(zebus):
    clean_zebus = []
    for i in range(1,zebus[0]+1):
        if clean_zebus.count(zebus[i]) == 1:
            return 0
        else:
            clean_zebus.append(zebus[i])

    clean_zebus.sort()
    diff_min = clean_zebus[-1]
    for i in range(1,len(clean_zebus)):
        curr_diff = clean_zebus[i] - clean_zebus[i-1]
        if curr_diff < diff_min:
            diff_min = curr_diff            
                        
    return diff_min

zebu_input = []
methode = input("Choisissez la méthode d'entrée (1 pour fichier, 2 pour la console): ")
if methode == "1":
    filename = input("Entrez le chemin du fichier: ")
    clean_path =  os.path.expanduser(filename.strip().strip('\'"'))
    with open(filename, "r") as f:
        zebu_input = list(map(int,f.readline().split()))
elif methode == "2":
    zebu_input = list(map(int, input("Entrez les nombres : ").split()))
if zebu_input[0] < 2 :
    print("Il faut au moins 2 zebus") 
else:
    print(zebu_compare(zebu_input))


