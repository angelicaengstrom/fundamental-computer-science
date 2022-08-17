x = input("Skriv ett tal: ")
y = input("Skriv ett annat tal: ")

if(x < y):
    m = int(y)
    n = int(x)
else:
    m = int(x)
    n = int(y)

r = m % n

while(r != 0):
    m = n
    n = r
    r = m % n

print("Den största gemensamma nämnaren är " + str(n))