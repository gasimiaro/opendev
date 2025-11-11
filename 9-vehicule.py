def point_de_rencontre(xA,vA,xB,vB):
    if vA==vB:
        if xA==xB:
            return f"YES 0.00 {xA:.2f}"
        return "NO"
    t = (xB-xA)/(vA-vB)
    if t>=0 :
        rencontre = xA+vA*t
        return f"YES {abs(t):.2f} {rencontre:.2f}"
    else:
        return "NO"    
    
xA,vA,xB,vB = map(float,input().split())
print(point_de_rencontre(xA,vA,xB,vB))