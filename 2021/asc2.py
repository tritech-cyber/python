#asc2.py cwc #change the range of the lool .  Tru 32,129
# Change the range from (0,35) to (32,???)
for i in range (0,35):
    c = chr(i)
    print("[",i,"=",c,"]",end="")
    if (i % 10 == 0):
        print("\n")
