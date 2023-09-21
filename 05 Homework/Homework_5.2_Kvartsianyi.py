h, w, a, b, c = map(int, input("h, w, a, b, c: ").split())

if (a < h or a < w) and (b < h or b < w): print("Коробка проходить")
        
elif (b < h or b < w) and (c < h or c < w): print("Коробка проходить")

elif (a < h or a < w) and (c < h or c < w): print("Коробка проходить")

else : print("Коробка не проходить")
