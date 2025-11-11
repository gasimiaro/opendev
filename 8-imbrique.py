def is_valid(chaine):
    pile = []
    imbrik_car = {'(': ')', '{': '}', '[': ']'}
    for car in chaine:
        if car in imbrik_car:
            pile.append(car)
        elif car in imbrik_car.values():
            if not pile or imbrik_car[pile.pop()] != car:
                return False
    return not pile

expression = input("expression : ")
if is_valid(expression):
    print("Expression valide ✅")
else:
    print("Expression invalide ❌")