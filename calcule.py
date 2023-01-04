def calcul(n1,operator, n2):
    if operator == "+":
        return (print(n1 + n2))
    elif operator == "-":
        return (print(n1 - n2))
    elif operator == "*":
        return (print(n1 * n2))
    elif operator == "/":
        return (print(n1 / n2))
    elif operator == "%":
        return (print(n1 % n2))
calcul(10,"+",20)
calcul(9,"/",20)
calcul(4,"%",3)