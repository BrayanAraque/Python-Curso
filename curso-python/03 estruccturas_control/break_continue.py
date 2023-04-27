
c = 0

while c < 10:
    c += 1
    print(c)
    if c == 5:
        #print("termina el bucle")
        print("salta a siguiente iteracion")
        #break
        continue
    print("despues de continue")
else:
    print("fin de while")