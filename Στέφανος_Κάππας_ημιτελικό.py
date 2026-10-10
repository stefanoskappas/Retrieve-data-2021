"""
Γ. Για μια εκτέλεση το σύστημα θα επιλέγει τυχαία ένα ποσοστό Χ% των συνολικών βαθμολογιών ως γνωστές, και 
σύμφωνα με αυτές θα υπολογίζει προβλέψεις για τις υπόλοιπες (100-Χ)% των βαθμολογιών. Για τις προβλέψεις αυτές θα
πρέπει να υπολογίζετε και το μέσο απόλυτο λάθος το οποίο θα είναι η έξοδος του προγράμματος σας. Το σύστημα θα 
επαναλαμβάνει για Τ επαναλήψεις αυτήν την εκτέλεση και θα παίρνει το μέσο λάθος από όλες.
Σχεδιάστε και εκτελέστε πειράματα που θα απαντούν στα παρακάτω: 
1) Πώς επηρεάζει το ποσοστό των γνωστών βαθμολογιών την απόδοση (ακρίβεια) του συστήματος; 
2) Ποια είναι η καλύτερη συνάρτηση ομοιότητας; 
3) Πώς επηρεάζει το Κ την απόδοση (ακρίβεια) του συστήματος;
4) Ποια είναι η καλύτερη μέθοδος πρόβλεψης;
"""
import random
import math
import numpy
number_grid2 =[
    ['', 'HP1', 'HP2', 'HP3', 'TW', 'SW1', 'SW2', 'SW3'],
    ['A', 4.0, 0.0, 0.0, 5.0, 1.0, 0.0, 0.0],
    ['B', 5.0, 5.0, 4.0, 0.0, 0.0, 0.0, 0.0],
    ['C', 0.0, 0.0, 0.0, 2.0, 4.0, 5.0, 0.0],
    ['D', 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 3.0]
]
number_grid =[
    ['Χρήστης hid \ Βιβλίο hid']
]
i = -1
ij = -1
for row in number_grid:
    print(row)
    i = i + 1
    for col in row:
        ij = ij + 1
    j = ij
    ij = -1
print(i, j)
def add_row(i):
    a = "Χρήστης "
    b = str(i + 1)
    a = (a+b)
    number_grid.append([a])
    i = i + 1
def add_col(i, j):
    Α = 0
    for Β in range (0, i):
        for row in number_grid:
            if Α == i + 1:
                break
            if Α == 0:
                aa = 'Βιβλίο '
                bb = str(c+j+1)
                cc = aa+bb
                row.append(cc)
            if Α > 0:
                new = random.randint(1, 100)
                new = new / 10.0
                row.append(new)
            Α = Α + 1
        j = j + c
def select_greek(i, j):
    x = input("Από ποιά γραμμή θέλεις να μηδενίσεις")
    i = input("Μέχρι ποιά γραμμή θέλεις να μηδενίσεις")
    y = input("Από ποιά στήλη θέλεις να μηδενίσεις")
    j = input("Μέχρι ποιά στήλη θέλεις να μηδενίσεις")
    z = input("Τί τιμή θέλεις να βάλεις")
    z = float(z)
    x = int(x)
    y = int(y)
    i = int(i)
    j = int(j)
    for I in range (x, i+1):
        for J in range (y, j+1):
            number_grid[I][J] = z
def select_arabic(i, j):
    x = input("? αuiuιuιΩuϊ ojzlcl jzujuϊ Shjztl bdtl Lo")
    i = input("? αuiuιuιΩuΪ ojzLcl jzujuϊ Shjztl bdtl shuΪd")
    y = input("? djmuιΩuϊtl ojzLcl jzujuϊ jzgoc Shl djo")
    j = input("? ojzLc jzujuϊ Shjztl jzgoΩtl gφ Lo auiuιuιΩuΪ")
    z = input("αΩuιόuϊ djl jzujuϊ Shjztl jΩuιuιιtl Lo")
    z = float(z)
    x = int(x)
    y = int(y)
    i = int(i)
    j = int(j)
    for I in range (x, i+1):
        for J in range (y, j+1):
            number_grid[I][J] = z
def remove_row(i):
    b = input()
    b = int(b)
    if b <= i:
        for b in range(0, b):
            a = number_grid.pop()
def remove_col(i):
    b = input()
    b = int(b)
    if b <= j:
        for b in range(0, b):
            for e in range(0, i+1):
                a = number_grid[e].pop() 
def user_greek(i, j):
    print("Βαθμολογία χρηστών")
    a = 0
    b = 0
    c = 0
    for row in number_grid[1:(i+1)]:
        b = 0
        for col in row:
            if a >= 1:
                if col is '':
                    col = 10.0
                    b = b + col
                b = b + float(col)
            a = a + 1
        c = b / (a - 1)
        print("Ο", row[0], "έχει μέσο score ", c)
        a = 0
def user_arabic(i, j):
    print("ρjdiιuιιk l YLouiuioui")
    a = 0
    b = 0
    c = 0
    for row in number_grid[1:(i+1)]:
        b = 0
        for col in row:
            if a >= 1:
                if col is '':
                    col = 0.0
                    b = b + col
                b = b + float(col)
            a = a + 1
        c = b / (a - 1)
        print("Jl", row[0], "YLdjjz tbuιuιιgϊo auιjzt", c)
        a = 0
def book_greek(i, j):
    print("Βαθμολογία ανά βιβλίο")
    a = 0
    b = 0
    e = 0
    for e in range (1, j+1):
        a = 0
        b = 0
        for row in number_grid:
            if a == 0:
                d = row[e]
            if a >= 1:
                if row[e] is '':
                    row[e] = 0.0
                    b = b + row[e]
                c = int(row[e])
                b = b + c
            a = a + 1
        c = b / (a-1)
        print("Ο", d, "έχει μέσο score ", c)
        c = 0
def book_arabic(i, j):
    print("ΎLiS JSt Ϋljuιuiιc")
    a = 0
    b = 0
    e = 0
    for e in range (1, j+1):
        a = 0
        b = 0
        for row in number_grid:
            if a == 0:
                d = row[e]
            if a >= 1:
                if row[e] is '':
                    row[e] = 0.0
                    b = b + row[e]
                c = int(row[e])
                b = b + c
            a = a + 1
        c = b / (a-1)
        print("Jl", d, "YLdjjz tbuιuιιgϊo auιjzt", c)
        c = 0
def jaccard_greek():
    print("Ποιούς χρήστες θέλεις να συγκρίνεις?")
    a = input()
    b = input()
    a = int(a)
    b = int(b)
    ja = 0
    za = 0
    Λ = 0
    for col in number_grid[a]:
        if ja > 0:
            if col > 0.0:
                za = za + 1
                jb = 0
                zb = 0
                for col in number_grid[b]:
                    if jb > 0:
                        if col > 0.0:
                            zb = zb + 1
                            if jb == ja:
                                Λ = Λ + 1
                    jb = jb + 1
        ja = ja + 1
    U = za + zb - Λ
    jaccard = Λ / U
    print("Η Jaccard ομοιότητα είναι =", jaccard) 
def jaccard_arabic():
    print("? zθuϊuijLoo jzujuϊ djMojzduϊuιuιιk l shl")
    a = input()
    b = input()
    a = int(a)
    b = int(b)
    ja = 0
    za = 0
    Λ = 0
    for col in number_grid[a]:
        if ja > 0:
            if col > 0.0:
                za = za + 1
                jb = 0
                zb = 0
                for col in number_grid[b]:
                    if jb > 0:
                        if col > 0.0:
                            zb = zb + 1
                            if jb == ja:
                                Λ = Λ + 1
                    jb = jb + 1
        ja = ja + 1
    U = za + zb - Λ
    jaccard = Λ / U
    print("Jaccard gφ αuLuιuiιuϊ =", jaccard) 
def kozani_greek():
    print("Ποιούς χρήστες θέλεις να συγκρίνεις?")
    a = input()
    b = input()
    a = int(a)
    b = int(b)
    j = 0
    AA = 0
    BB = 0
    CC = 0
    for col in number_grid[a]:
        if j > 0:
            AA = AA + col*number_grid[b][j]
            bb = col
            BB = BB + bb*bb
            cc = number_grid[b][j]
            CC = CC + cc*cc
        j = j + 1
    cos = AA / (math.sqrt(BB) * math.sqrt(CC))
    print("Η Κοζάνη ομοιότητα είναι", cos)
def kozani_arabic():
    print("? zθuϊuijLoo jzujuϊ djMojzduϊuιuιιk l shl")
    a = input()
    b = input()
    a = int(a)
    b = int(b)
    j = 0
    AA = 0
    BB = 0
    CC = 0
    for col in number_grid[a]:
        if j > 0:
            AA = AA + col*number_grid[b][j]
            bb = col
            BB = BB + bb*bb
            cc = number_grid[b][j]
            CC = CC + cc*cc
        j = j + 1
    cos = AA / (math.sqrt(BB) * math.sqrt(CC))
    print("αuLuιuiιuϊ ShuiljgS =", cos)
def dice_greek():
    print("Ποιούς χρήστες θέλεις να συγκρίνεις?")
    a = input()
    b = input()
    a = int(a)
    b = int(b)
    ja = 0
    za = 0
    Λ = 0
    for col in number_grid[a]:
        if ja > 0:
            if col > 0.0:
                za = za + 1
                jb = 0
                zb = 0
                for col in number_grid[b]:
                    if jb > 0:
                        if col > 0.0:
                            zb = zb + 1
                            if jb == ja:
                                Λ = Λ + 1
                    jb = jb + 1
        ja = ja + 1
    U = za + zb - Λ
    dice = 2*Λ / (za + zb)
    print("Η Dice ομοιότητα είναι =", dice) 
def dice_arabic():
    print("? zθuϊuijLoo jzujuϊ djMojzduϊuιuιιk l shl")
    a = input()
    b = input()
    a = int(a)
    b = int(b)
    ja = 0
    za = 0
    Λ = 0
    for col in number_grid[a]:
        if ja > 0:
            if col > 0.0:
                za = za + 1
                jb = 0
                zb = 0
                for col in number_grid[b]:
                    if jb > 0:
                        if col > 0.0:
                            zb = zb + 1
                            if jb == ja:
                                Λ = Λ + 1
                    jb = jb + 1
        ja = ja + 1
    U = za + zb - Λ
    dice = 2*Λ / (za + zb)
    print("jzjuitl αuLuιuiιuϊ =", dice) 
def adjusted_kozani_greek():
    print("Ποιούς χρήστες θέλεις να συγκρίνεις?")
    aaa = input()
    bbb = input()
    aaa = int(aaa)
    bbb = int(bbb)
    ia = 0
    za = 0
    EE = []
    number_grid3 = []
    for row in number_grid:
        ja = 0
        DD = 0.0
        za = 0
        if ia > 0:
            for col in row:
                if ja > 0:
                    DD = DD + col
                    if col > 0.0:
                        za = za + 1
                ja = ja + 1
            if za == 0:
                EE.append(za)
            EE.append(DD/za)
        ia = ia + 1
    ib = 0
    number_grid3.append(number_grid[0])
    for iI in range(0,i):
        a = "Χρήστης "
        b = str(iI + 1)
        a = (a+b)
        number_grid3.append([a])
        iI = iI + 1
    for row in number_grid:
        jb = 0
        DD = 0
        za = 0
        if ib > 0:
            for col in row:
                if jb > 0:
                    if col > 0.0:
                        col = col - EE[ib-1]
                    number_grid3[ib].append(col)
                jb = jb + 1
        ib = ib + 1
    jj = 0
    AA = 0
    BB = 0
    CC = 0
    print(bbb)
    for col in number_grid3[aaa]:
        if jj > 0:
            col = float(col)
            AA = AA + col*number_grid3[bbb][jj]
            bb = col
            BB = BB + bb*bb
            cc = number_grid3[bbb][jj]
            CC = CC + cc*cc
        jj = jj + 1
    cos = AA / (math.sqrt(BB) * math.sqrt(CC))
    print("Η Αναθεματισμένη Κοζάνη ομοιότητα είναι", cos)
    stil = input("Θέλεις να δείς τον κανινικοποιημένο πίνακα?")
    if stil == '1':
        for row in number_grid3:
            print(row)
def adjusted_kozani_arabic():
    print("? zθuϊuijLoo jzujuϊ djMojzduϊuιuιιk l shl")
    aaa = input()
    bbb = input()
    aaa = int(aaa)
    bbb = int(bbb)
    ia = 0
    za = 0
    EE = []
    number_grid3 = []
    for row in number_grid:
        ja = 0
        DD = 0.0
        za = 0
        if ia > 0:
            for col in row:
                if ja > 0:
                    DD = DD + col
                    if col > 0.0:
                        za = za + 1
                ja = ja + 1
            if za == 0:
                EE.append(za)
            EE.append(DD/za)
        ia = ia + 1
    ib = 0
    number_grid3.append(number_grid[0])
    for iI in range(0,i):
        a = "Χρήστης "
        b = str(iI + 1)
        a = (a+b)
        number_grid3.append([a])
        iI = iI + 1
    for row in number_grid:
        jb = 0
        DD = 0
        za = 0
        if ib > 0:
            for col in row:
                if jb > 0:
                    if col > 0.0:
                        col = col - EE[ib-1]
                    number_grid3[ib].append(col)
                jb = jb + 1
        ib = ib + 1
    jj = 0
    AA = 0
    BB = 0
    CC = 0
    print(bbb)
    for col in number_grid3[aaa]:
        if jj > 0:
            col = float(col)
            AA = AA + col*number_grid3[bbb][jj]
            bb = col
            BB = BB + bb*bb
            cc = number_grid3[bbb][jj]
            CC = CC + cc*cc
        jj = jj + 1
    cos = AA / (math.sqrt(BB) * math.sqrt(CC))
    print("gφ shuiljgA djgΩlkl αuιuιuiιtl = ", cos)
    stil = input("?shΩuιuιubtl Jgjzdtl  Shjuϊ djl jzujuϊ Jφ")
    if stil == '1':
        for row in number_grid3:
            print(row)
list = input("Ποια γλώσσα θέλεις? Πάτα 1 για ελληνικά ή 2 για αραβικά (auιuιJΩt l aΏlt)\n")
if list == '1':
    print ("Ελληνικά")
    list = input ("Τί θέλεις να κάνεις με την εργασία?\n")
    while True:
        if list == 'Προσθήκη 1':
            print("Πόσες νέες γραμμές θέλεις να βάλεις?")
            row = input()
            row = int(row)
            for r in range (0, row):
                add_row(i+r)
        if list == 'Προσθήκη 2':
            print("Πόσες νέες στήλες θέλεις να βρείς?")
            col = input()
            col = int(col)
            for c in range(0, col):
                add_col(i, j)
                j = j
        if list == 'Μηδέν':
            select_greek(i, j)
        if list == 'Αφαίρεση 1':
            print("Πόσες γραμμές θέλεις να σβήσεις?")
            remove_row(i)
        if list == 'Αφαίρεση 2':
            print("Πόσες στήλες θέλεις να σβήσεις?")
            remove_col(i)
        if list == 'Εμφάνιση':
            i = -1
            ij = 1
            for row in number_grid:
                print(row)
                i = i + 1
                for col in row:
                    ij = ij + 1
                j = ij
                ij = -1
            if i == 0:
                j = j - 2
            print(i, j)
        if list == 'Χρήστη':
            user_greek(i, j)
        if list == 'Βιβλίο':
            book_greek(i, j)
        if list == 'Jaccard':
            jaccard_greek()
        if list == 'Κοζάνη':
            kozani_greek()
        if list == 'Dice':
            dice_greek()
        if list == 'ΑΚοζάνη':
            adjusted_kozani_greek()
        if list == 'Τέλος':
            print("Τέλος εργασίας")
            break
        list = input ("Τί θέλεις να κάνεις με την εργασία?\n")
if list == '2':
    print ("shujc")
    list = input ("? aόιbgtlu Jωόuϊ djl jzujuϊ l jzLo\n")
    while True:
        if list == 'Προσθήκη 1':
            print("Shuϊt l o jzuιjzdtl jbuιuιιΨl jzjzc zS ? LΘΩuιόg jzuιjui")
            row = input()
            row = int(row)
            for r in range (0, row):
                add_row(i+r)
        if list == 'Προσθήκη 2':
            print("jzuιjuϊ shuϊtl ojzuιjzdtl ojzoc Ψl jzjzc zS ? LθΩuιόg")
            col = input()
            col = int(col)
            for c in range(0, col):
                add_col(i, j)
                j = j
        j = j
        if list == 'Μηδέν':
            select_arabic(i, j)
        if list == 'Αφαίρεση 1':
            print("?Lθόjzd jzuιjuϊ shuϊtl jgbuιuιιtl jzjzc zS")
            remove_row(i)
        if list == 'Αφαίρεση 2':
            print("?Lθόjzd jzuιjuι shuϊtl ojzocΨl jzjzc zS")
            remove_col(i)
        if list == 'Εμφάνιση':
            i = -1
            ij = 1
            for row in number_grid:
                print(row)
                i = i + 1
                for col in row:
                    ij = ij + 1
                j = ij
                ij = -1
            if i == 0:
                j = j - 2
            print(i, j)
        if list == 'Χρήστη':
            user_arabic(i, j)
        if list == 'Βιβλίο':
            book_arabic(i, j)
        if list == 'Jaccard':
            jaccard_arabic()
        if list == 'Κοζάνη':
            kozani_arabic()
        if list == 'Dice':
            dice_arabic()
        if list == 'ΑΚοζάνη':
            adjusted_kozani_arabic()
        if list == 'Τέλος':
            print("JoΩt l zguiuiij")
            break
        list = input ("? aόιbgtlu Jωόuϊ djl jzujuϊ l jzLo\n")