marsruti=['1) Centrs-3.l�nija', '2) 3.l�nija- Centrs']
autobusu_numuri=["1) 1.autobuss","2) 8.autobuss","3) 19.autobuss"]
pietura=["1) Tu��i GP"," 2) 6. l�nija"," 3) Zanderu kapi"," 4) 4. l�nija"," 5) 3. l�nija"," 6) 1. l�nija"," 7) Satiksmes iela (Dobeles �osej�)"," 8) M�ras iela"," 9) Ozolskv�rs"," 10) P�tera iela"," 11) Centrs"]
for i in range(2):
    print(marsruti[i])
auto=int(input("Ievadi no dot�s kopas mar�uta skaitli, k� mar�ruta inform�ciju v�lies apskat�t! - "))
if auto!=1 and  auto!=2:
    while auto!=1 and  auto!=2:
        print("Ievadi, k�du no pieejamiem skait�iem!")
        auto=int(input("Ievadi no dot�s kopas mar�uta skaitli, k� mar�ruta inform�ciju v�lies apskat�t! - "))
if auto==2:
    for i in range(11):
        print(pietura[i])
    piet=int(input("Ievadi no dot�s kopas autobusa numuru, k� inform�ciju v�lies apskat�t! - "))
    if  piet not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        while piet not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            print("Ievadi, k�du no pieejamiem skait�iem!")
            piet=int(input("Ievadi no dot�s kopas autobusa numuru, k� inform�ciju v�lies apskat�t! - "))
    for i in range(3):
        print(autobusu_numuri[i])
    aun=int(input("Ievadi no dot�s kopas autobusa numuru, k� inform�ciju v�lies apskat�t! - "))
    if  aun!=1 and aun!=2 and aun!=3:
        while aun!=1 and aun!=2 and aun!=3:
            print("Ievadi, k�du no pieejamiem skait�iem!")
            aun=int(input("Ievadi no dot�s kopas autobusa numuru, k� inform�ciju v�lies apskat�t! - "))
