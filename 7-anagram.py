def clean(mot):
    mot=mot.lower()
    nouveau_mot = ""
    for lettre in mot:
        if lettre.isalpha():
            nouveau_mot += lettre    
    return nouveau_mot

def anagram(mot1,mot2):
    for lettre in mot1:
        if lettre in mot2:
            mot2=mot2.replace(lettre,"",1)
        else:
            return False       
    return True

premier, deuxieme = input().split(",")
resultat = f"{premier} et {deuxieme} ne sont pas des anagrammes ❌"
if len(clean(premier)) == len(clean(deuxieme)) and anagram(clean(premier),clean(deuxieme)): 
        resultat = f"{premier} et {deuxieme} sont des anagrammes ✅"

print(resultat)