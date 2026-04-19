"""Os pontos (x,y) que pertencem à figura H (abaixo) são tais que x≥0, y≥0 e x2+y2≤1.Leia as coordenadas de um único ponto. O programa deve imprimir 1 se estiver dentro de H e 0 se estiver fora"""
#1²+1²==R²
x = float(input("X:"))
y = float(input("Y:"))
dentro = (x<=1 and x>=0) and (y<=1 and y>=0)
print(int(dentro))