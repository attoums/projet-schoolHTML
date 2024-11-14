
"""
def trouverMaximum(nombres):
    max = nombres[0]
    for i in range(len(nombres)):
        if max < nombres[i]:
            max =  nombres[i]
            
    return max        



def main():
    nombres = [1,3,-4,7,11,20,0,2,5,-3]

    maximum = trouverMaximum(nombres)
    print(f"le maximum de la liste est: {maximum}")

main()    
    
    """

mess = "Bonjour à tous"
for car in mess:
    print(car)