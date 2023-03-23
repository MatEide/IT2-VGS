import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 2, 4, 6, 8, 10]

plt.plot(x,y) # Oppretter et plot
plt.show() # viser plottet

# plott funksjnen f(x) = 3*x + 2, med x fra 0 til 5
# utfordring: bruk for løkker

x = [0, 1, 2, 3, 4, 5]
y = []

for i in range(0,6):
    tall = i*3 + 2
    y.append(tall)

# Alternativt 

x = []
y = []

def f(x):
    return 3*x + 2

for i in range (6):
    x.append(i)
    y.append(f(i))

plt.plot(x,y) 
plt.scatter(x,y) # Prikker 
plt.show() 




