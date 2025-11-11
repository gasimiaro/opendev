import os

def zebu_compare(zebus):
    zebus.sort()
    diff_min = float('inf')
    for i in range(1,len(zebus)):
        if zebus[i] == zebus[i-1]:
            return 0
        else:
            curr_diff = zebus[i] - zebus[i-1]
            diff_min = min(diff_min, curr_diff)           
                        
    return diff_min

zebu_input = []
N =0 
#methode = "0"
#while methode not in ["1","2"]:
#    methode = input("Choisissez la méthode d'entrée (1 pour fichier, 2 pour la console): ")
#    if methode == "1":
#        path = input("Entrez le chemin du fichier: ")
#        clean_path =  os.path.expanduser(path.strip().strip('\'"'))
#        
#        try:
#            with open(clean_path, "r") as f:
#                N = int(f.readline().strip())
#                for line in f :
#                    if line.strip() != "":
#                        zebu_input.append(int(line.strip()))
#            
#        except FileNotFoundError:
#            print(f"Fichier introuvable: {clean_path}")
#            raise
#    elif methode == "2":
#        N = int(input("Entrez le nombre de zebus: "))
#        for _ in range(N):
#            line = int(input().strip())
#            zebu_input.append(line)
#    
#if not zebu_input or  N < 2 :
#    print("Il faut au moins 2 zebus") 
#else:
#    print(zebu_compare(zebu_input))

N = int(input("Entrez le nombre de zebus: "))
for _ in range(N):
    line = int(input().strip())
    zebu_input.append(line)

if not zebu_input or  N < 2 :
    print("Il faut au moins 2 zebus") 
else:
    print(zebu_compare(zebu_input))
