marsruti=['1) 3.līnija- Centrs']
autobusu_numuri=["1) 1.autobuss","2) 8.autobuss","3) 19.autobuss"]
pietura=["1) 3. līnija"," 2) 1. līnija"," 3) Satiksmes iela (Dobeles šosejē)"," 4) Māras iela"," 5) Ozolskvērs"]
pietura_1_1= [6.15, 7.08, 7.37, 8.06, 8.40, 8.51, 9.04, 9.39, 10.11, 11.31, 12.11, 12.51, 13.31, 14.11, 14.26, 15.01, 15.32, 16.26, 16.51, 17.37, 18.13, 18.23, 19.06, 19.35, 20.05, 20.45]
pietura_1_2= [6.16, 7.09, 7.38, 8.07, 8.41, 8.52, 9.05, 9.40, 10.12, 11.32, 12.12, 12.52, 13.32, 14.12, 14.27, 15.02, 15.33, 16.27, 16.52, 17.38, 18.14, 18.24, 19.07, 19.36, 20.06, 20.46]
pietura_1_3= [6.17, 7.12, 7.41, 8.10, 8.43, 8.55, 9.08, 9.42, 10.15, 11.35, 12.15, 12.55, 13.35, 14.15, 14.30, 15.05, 15.35, 16.30, 16.55, 17.41, 18.17, 18.27, 19.09, 19.38, 20.08, 20.48]
pietura_1_4= [6.19, 7.14, 7.29, 7.44, 8.12, 8.45, 8.57, 9.10, 9.44, 10.17, 11.37, 12.17, 12.57, 13.37, 14.17, 14.32, 15.07, 15.37, 16.32, 16.57, 17.43, 18.19, 18.29, 19.11, 19.40, 20.10, 20.50]
pietura_1_5= [6.20, 7.15, 7.32, 7.48, 8.13, 8.46, 8.58, 9.11, 9.45, 10.18, 11.38, 12.18, 12.58, 13.38, 14.18, 14.33, 15.08, 15.38, 16.34, 16.58, 17.44, 18.20, 18.30, 19.12, 19.41, 20.11, 20.51]
pietura_2_1= [5.48, 6.41, 7.01, 8.02, 8.42, 9.12, 9.39, 10.29, 11.07, 12.25, 13.34, 13.40, 14.39, 15.55, 16.26, 17.26, 18.24, 19.29, 20.30, 20.51, 21.54]
pietura_2_2= [5.49, 6.42, 7.02, 8.03, 8.44, 9.13, 9.40, 10.30, 11.08, 12.26, 13.36, 13.41, 14.40, 15.56, 16.27, 17.27, 18.25, 19.30, 20.31, 20.52, 21.55]
pietura_2_3=[5.52, 6.45, 7.05, 8.06, 8.47, 9.16, 9.43, 10.33, 11.11, 12.29, 13.39, 13.44, 14.43, 15.59, 16.31, 17.31, 18.29, 19.33, 20.34, 20.55, 21.58]
pietura_2_4=[5.54, 6.47, 7.07, 8.08, 8.48, 9.18, 9.45, 10.35, 11.13, 12.31, 13.40, 13.46, 14.45, 16.01, 16.33, 17.33, 18.31, 19.35, 20.36, 20.57, 22.00]
pietura_2_5=[5.55, 6.48, 7.08, 8.09, 8.50, 9.19, 9.46, 10.36, 11.14, 12.32, 13.42, 13.47, 14.46, 16.02, 16.35, 17.35, 18.33, 19.36, 20.37, 20.58, 22.01]
pietura_3_1=[7.38, 9.08, 10.34, 12.00, 14.31, 15.57, 17.01, 18.35]
pietura_3_2=[7.40, 9.10, 10.36, 12.02, 14.33, 15.59, 17.02, 18.36]
pietura_3_3=[7.43, 9.13, 10.39, 12.05, 14.36, 16.02, 17.06, 18.40]
pietura_3_4=[7.46, 9.14, 10.40, 12.06, 14.37, 16.04, 17.08, 18.42]
pietura_3_5=[7.49, 9.16, 10.42, 12.08, 14.39, 16.05, 17.09, 18.43]
print(marsruti)
auto=int(input("Ievadi no dotās kopas maršuta skaitli, kā maršruta informāciju vēlies apskatīt! - "))
if auto!=1:
    while auto!=1:
        print("Ievadi, kādu no pieejamiem skaitļiem!")
        auto=int(input("Ievadi no dotās kopas maršuta skaitli, kā maršruta informāciju vēlies apskatīt! - "))
laiks=float(input("Ievadi pašreizējo laiku pēc piemēra: (12.30, 8.60)! - "))
while laiks<0 or laiks>24:
    print("Nepareizi ievadīts laiks")
    laiks=float(input("Ievadi pašreizējo laiku pēc piemēra: (12.30, 8.60)! - "))
if auto==1:
        print(pietura)
        piet=int(input("Ievadi no dotās kopas autobusa numuru, kā informāciju vēlies apskatīt! - "))
        if piet not in [1, 2, 3, 4, 5]:
            while piet not in [1, 2, 3, 4, 5]:
                print("Ievadi, kādu no pieejamiem skaitļiem!")
                piet=int(input("Ievadi no dotās kopas autobusa numuru, kā informāciju vēlies apskatīt! - "))
        print(autobusu_numuri)
        aun=int(input("Ievadi no dotās kopas autobusa numuru, kā informāciju vēlies apskatīt! - "))
        if aun!=1 and aun!=2 and aun!=3:
            while aun!=1 and aun!=2 and aun!=3:
                print("Ievadi, kādu no pieejamiem skaitļiem!")
                aun=int(input("Ievadi no dotās kopas autobusa numuru, kā informāciju vēlies apskatīt! - "))

def autobusu_atbraukšanas_laiks(piet, aun, laiks):
    autobusu_laiks_atrasts= False
    if piet == 1 and aun == 1:
        print("Autobuss atbraukšanas laika opcijas:")
        for i in range(26):
            if pietura_1_1[i] > laiks:
                print(pietura_1_1[i])
                autobusu_laiks_atrasts= True
    elif piet == 2 and aun == 1:
        print("Autobuss atbraukšanas laika opcijas:")
        for i in range(26):
            if pietura_1_2[i] > laiks:
                print(pietura_1_2[i])
                autobusu_laiks_atrasts= True
    elif piet == 3 and aun == 1:
        print("Autobuss atbraukšanas laika opcijas:")
        for i in range(26):
            if pietura_1_3[i] > laiks:
                print(pietura_1_3[i])
                autobusu_laiks_atrasts= True
    elif piet == 4 and aun == 1:
        print("Autobuss atbraukšanas laika opcijas:")
        for i in range(26):
            if pietura_1_4[i] > laiks:
                print(pietura_1_4[i])
                autobusu_laiks_atrasts= True
    elif piet == 5 and aun == 1:
        print("Autobuss atbraukšanas laika opcijas:")
        for i in range(26):
            if pietura_1_5[i] > laiks:
                print(pietura_1_5[i])
                autobusu_laiks_atrasts= True
    elif piet == 1 and aun == 2:
        print("Autobuss atbraukšanas laika opcijas:")
        for i in range(21):
            if pietura_2_1[i] > laiks:
                print(pietura_2_1[i])
                autobusu_laiks_atrasts= True
    elif piet == 2 and aun == 2:
        print("Autobuss atbraukšanas laika opcijas:")
        for i in range(21):
            if pietura_2_2[i] > laiks:
                print(pietura_2_2[i])
                autobusu_laiks_atrasts= True
    elif piet == 3 and aun == 2:
        print("Autobuss atbraukšanas laika opcijas:")
        for i in range(21):
            if pietura_2_3[i] > laiks:
                print(pietura_2_3[i])
                autobusu_laiks_atrasts= True
    elif piet == 4 and aun == 2:
        print("Autobuss atbraukšanas laika opcijas:")
        for i in range(21):
            if pietura_2_4[i] > laiks:
                print(pietura_2_4[i])
                autobusu_laiks_atrasts= True
    elif piet == 5 and aun == 2:
        print("Autobuss atbraukšanas laika opcijas:")
        for i in range(21):
            if pietura_2_5[i] > laiks:
                print(pietura_2_5[i])
                autobusu_laiks_atrasts= True
    elif piet == 1 and aun == 3:
        print("Autobuss atbraukšanas laika opcijas:")
        for i in range(8):
            if pietura_3_1[i] > laiks:
                print(pietura_3_1[i])
                autobusu_laiks_atrasts= True
    elif piet == 2 and aun == 3:
        print("Autobuss atbraukšanas laika opcijas:")
        for i in range(8):
            if pietura_3_2[i] > laiks:
                print(pietura_3_2[i])
                autobusu_laiks_atrasts= True
    elif piet == 3 and aun == 3:
        print("Autobuss atbraukšanas laika opcijas:")
        for i in range(8):
            if pietura_3_3[i] > laiks:
                print(pietura_3_3[i])
                autobusu_laiks_atrasts= True
    elif piet == 4 and aun == 3:
        print("Autobuss atbraukšanas laika opcijas:")
        for i in range(8):
            if pietura_3_4[i] > laiks:
                print(pietura_3_4[i])
                autobusu_laiks_atrasts= True
    elif piet == 5 and aun == 3:
        print("Autobuss atbraukšanas laika opcijas:")
        for i in range(8):
            if pietura_3_5[i] > laiks:
                print(pietura_3_5[i])
                autobusu_laiks_atrasts= True
    if not autobusu_laiks_atrasts:
        print("Piedodiet, neviens autobuss nav pieejams!")

(autobusu_atbraukšanas_laiks(piet, aun, laiks))