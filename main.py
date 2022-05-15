with open("morze.txt", "r", encoding="utf8") as f, open("forditott.txt","a", encoding="utf8") as g:
    val = input("Konvertálni vagy fordítani akarsz? [k/f]")
    if val == "k":
        x = input("Adj meg egy szót: ")
        for betu in x:
            for _ in f: #_ = morzekód
                _ = list(_)
                if betu in _:
                    if "\n" not in _:
                        _ = _[2:]
                        _ = "".join(map(str,_))
                        g.writelines(_)
                        g.writelines(" ")

                    else:
                        _ = _[2:-1]
                        _ = "".join(map(str,_))
                        g.writelines(_)
                        g.writelines(" ")

            f.seek(0)
        g.writelines("\n")
    else:
        
        x = list(input("Adj meg egy morze kódot: "))
        
        x = "".join(map(str,x)).split(" ")
        print(len(x))
        
            
        x = x[0]
        for _ in f:
            _ = list(_)
            betu = _[0]
            if "\n" not in _:
                _ = _[2:]
                _ = "".join(map(str,_))
                if x == _:
                    g.writelines(betu)
                    g.writelines(" ")
        
            else:
                _ = _[2:-1]
                _ = "".join(map(str,_))
                if x == _:
                    g.writelines(betu)
                    g.writelines(" ")
        
        g.writelines("\n")
            #f.seek(0)