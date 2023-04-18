marsruti=['1) Centrs-3.lînija', '2) 3.lînija- Centrs']
autobusu_numuri=["1) 1.autobuss","2) 8.autobuss","3) 19.autobuss"]
pietura=["1) Tuðíi GP"," 2) 6. lînija"," 3) Zanderu kapi"," 4) 4. lînija"," 5) 3. lînija"," 6) 1. lînija"," 7) Satiksmes iela (Dobeles ðosejâ)"," 8) Mâras iela"," 9) Ozolskvçrs"," 10) Pçtera iela"," 11) Centrs"]
for i in range(2):
    print(marsruti[i])
auto=int(input("Ievadi no dotâs kopas marðuta skaitli, kâ marðruta informâciju vçlies apskatît! - "))
if auto!=1 and  auto!=2:
    while auto!=1 and  auto!=2:
        print("Ievadi, kâdu no pieejamiem skaitïiem!")
        auto=int(input("Ievadi no dotâs kopas marðuta skaitli, kâ marðruta informâciju vçlies apskatît! - "))
if auto==2:
    for i in range(11):
        print(pietura[i])
    piet=int(input("Ievadi no dotâs kopas autobusa numuru, kâ informâciju vçlies apskatît! - "))
    if  piet not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        while piet not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            print("Ievadi, kâdu no pieejamiem skaitïiem!")
            piet=int(input("Ievadi no dotâs kopas autobusa numuru, kâ informâciju vçlies apskatît! - "))
    for i in range(3):
        print(autobusu_numuri[i])
    aun=int(input("Ievadi no dotâs kopas autobusa numuru, kâ informâciju vçlies apskatît! - "))
    if  aun!=1 and aun!=2 and aun!=3:
        while aun!=1 and aun!=2 and aun!=3:
            print("Ievadi, kâdu no pieejamiem skaitïiem!")
            aun=int(input("Ievadi no dotâs kopas autobusa numuru, kâ informâciju vçlies apskatît! - "))
