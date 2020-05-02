polynomial = input("Type in a Polynomial :- ")
polynomial
if '+' in polynomial:
    print(len(polynomial.split('+')))
else:
    print("Polynomial has 1 term")
