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
QQ = []
QQQ = []
QQQQ = []
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
    x = input("Από ποιά γραμμή θέλεις να τροποποιήσεις; ")
    i = input("Μέχρι ποιά γραμμή θέλεις να τροποποιήσεις; ")
    y = input("Από ποιά στήλη θέλεις να τροποποιήσεις; ")
    j = input("Μέχρι ποιά στήλη θέλεις να τροποποιήσεις; ")
    z = input("Τί τιμή θέλεις να βάλεις; ")
    z = float(z)
    x = int(x)
    y = int(y)
    i = int(i)
    j = int(j)
    for I in range (x, i+1):
        for J in range (y, j+1):
            number_grid[I][J] = z
def select_arabic(i, j):
    x = input("? αlujzΩϊ jzujuϊ Shjztl bdtl Lo ")
    i = input("? αlujzΩϊ jzujuϊ Shjztl bdtl gφ Lo ")
    y = input("? JujzΩϊtl jzujuϊ jzgoc Shl djo ")
    j = input("? αlujzΩϊ jzujuϊ jzgoc Shl shtl ")
    z = input("? αΩuιόuϊ djl jzujuϊ Shjztl jΩuιuιιtl Lo ")
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
    print("Βαθμολογία ανά χρήστη.")
    a = 0
    b = 0
    c = 0
    d = 0
    for row in number_grid[1:(i+1)]:
        b = 0
        for col in row:
            if a >= 1:
                c = col
                if c == 0.0:
                    c = 5.0
                b = b + c
            a = a + 1
        d = b / (a - 1)
        print("Ο", row[0], "έχει μέσο score", d)
        a = 0
def user_arabic(i, j):
    print("pjzdϊuιuιιkl ΫLouιuιοuϊ.")
    a = 0
    b = 0
    c = 0
    d = 0
    for row in number_grid[1:(i+1)]:
        b = 0
        for col in row:
            if a >= 1:
                c = col
                if c == 0.0:
                    c = 5.0
                b = b + c
            a = a + 1
        d = b / (a - 1)
        print("Jl", row[0], "YLdjjz buιuιιgϊo aujzt", c)
        a = 0
def book_greek(i, j):
    print("Βαθμολογία ανά βιβλίο.")
    a = 0
    b = 0
    c = 0
    e = 0
    for e in range (1, j+1):
        a = 0
        b = 0
        for row in number_grid:
            if a == 0:
                d = row[e]
            if a >= 1:
                c = row[e]
                if c == 0.0:
                    c = 5.0
                b = b + c
            a = a + 1
        c = b / (a-1)
        print("Ο", d, "έχει μέσο score", c)
        c = 0
def book_arabic(i, j):
    print("ΎLϊS JSt Ϋljuιuϊιc.")
    a = 0
    b = 0
    c = 0
    e = 0
    for e in range (1, j+1):
        a = 0
        b = 0
        for row in number_grid:
            if a == 0:
                d = row[e]
            if a >= 1:
                c = row[e]
                if c == 0.0:
                    c = 5.0
                b = b + c
            a = a + 1
        c = b / (a-1)
        print("Jl", d, "YLdjjz buιuιιgϊo aujzt", c)
        c = 0
def jaccard_greek():
    print("Ποιούς χρήστες θέλεις να συγκρίνεις;")
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
    print("? pθuϊuijLoo jzujuϊ djMojzduϊuιuιιk l shl")
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
    print("Jaccard gφ αuLuιuϊιuϊtl =", jaccard) 
def kozani_greek():
    print("Ποιούς χρήστες θέλεις να συγκρίνεις;")
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
    print("Η Κοζάνη ομοιότητα είναι =", cos)
def kozani_arabic():
    print("? pθuϊuijLoo jzujuϊ djMojzduϊuιuιιk l shl")
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
    print("αuLuιuϊιο shuiljgS =", cos)
def dice_greek():
    print("Ποιούς χρήστες θέλεις να συγκρίνεις;")
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
    print("? pθuϊuijLoo jzujuϊ djMojzduϊuιuιιk l shl")
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
    print("jzjuitl αuLuιuϊιuϊ =", dice) 
def adjusted_kozani_greek():
    print("Ποιούς χρήστες θέλεις να συγκρίνεις;")
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
    for col in number_grid3[aaa]:
        if jj > 0:
            col = float(col)
            AA = AA + col*number_grid3[bbb][jj]
            bb = col
            BB = BB + bb*bb
            cc = number_grid3[bbb][jj]
            CC = CC + cc*cc
        jj = jj + 1
    FFF = (math.sqrt(BB) * math.sqrt(CC))
    if FFF == 0.0:
        FFF = 1.0
        AA = 0.0
    cos = AA / FFF
    print("Η Αναθεματισμένη Κοζάνη ομοιότητα είναι =", cos)
    stil = input("Θέλεις να δείς τον κανινικοποιημένο πίνακα; ")
    if stil == '1':
        for row in number_grid3:
            print(row)
    stil = input("Θέλεις να καταχωρίσεις τον συντελεστή; ")
    if stil == '1':
        QQ.append(cos)
        bbbb = number_grid[bbb][0]
        QQQ.append(bbbb)
        QQQQ.append(bbb)
        print(QQ)
def adjusted_kozani_arabic():
    print("? pθuϊuijLoo jzujuϊ djMojzduϊuιuιιk l shl")
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
    for col in number_grid3[aaa]:
        if jj > 0:
            col = float(col)
            AA = AA + col*number_grid3[bbb][jj]
            bb = col
            BB = BB + bb*bb
            cc = number_grid3[bbb][jj]
            CC = CC + cc*cc
        jj = jj + 1
    FFF = (math.sqrt(BB) * math.sqrt(CC))
    if FFF == 0.0:
        FFF = 1.0
        AA = 0.0
    cos = AA / FFF
    print("gφ shuiljgS djMΩltl αuιuιuϊιtl =", cos)
    stil = input("? shΩuιuιbtl Jgjzdtl Shjuϊ djl jzujuϊ Jφ ")
    if stil == '1':
        for row in number_grid3:
            print(row)
    stil = input("? jΩuιuιιtl JLdjzl jzujuϊ Jφ ")
    if stil == '1':
        QQ.append(cos)
        bbbb = number_grid[bbb][0]
        QQQ.append(bbbb)
        QQQQ.append(bbb)
        print(QQ)
def predict_1_greek():
    x = input("Ποιά γραμμή θέλεις να επιλέξεις; ")
    y = input("Ποιά στήλη θέλεις να επιλέξεις; ")
    x = int(x)
    y = int(y)
    if number_grid[x][y] == 0.0:
        print(number_grid[x][y])
        print("Πρόβλεψη βαθμολογίας.")
        k = input("Πόσους k γείτονες θέλεις να επιλέξεις; ")
        k = int(k)
        if k >= 1 and k <= 10:
            QQQQQ = []
            QQQQQQ = []
            QQQQQQQ = []
            for a1 in range (0, k):
                a = 0.0
                ia = 1
                for row in QQ:
                    if a <= row:
                        a = row
                        ib = ia-1
                    ia = ia + 1
                QQQQQ.append(QQQQ[ib])
                QQQQQQ.append(QQ[ib])
                QQ.pop(ib)
                QQQ.pop(ib)
                QQQQ.pop(ib)
            for row in QQQQQ:
                aaa = number_grid[row][y]
                QQQQQQQ.append(aaa)
            a = 0
            b = 0
            c = 0
            for row in QQQQQQQ:
                b = row
                c = b + c
                a = a + 1
            d = c / a
            print(d)
            number_grid[x][y] = d
        else:
            a = 0
            b = 0
            c = 0
            e = 0
            for row in number_grid:
                if a != x and a != 0:
                    b = row[y]
                    if b != 0.0:
                        c = c + b
                        e = e + 1
                a = a + 1
            d = c / e
            print(d)
            number_grid[x][y] = d
    else:
        print("Λυπούμαστε, το κελί που ψάχνεις έχει βαθμό.")
def predict_2_greek():
    x = input("Ποιά γραμμή θέλεις να επιλέξεις; ")
    y = input("Ποιά στήλη θέλεις να επιλέξεις; ")
    x = int(x)
    y = int(y)
    if number_grid[x][y] == 0.0:
        print(number_grid[x][y])
        print("Πρόβλεψη βαθμολογίας.")
        k = input("Πόσους k γείτονες θέλεις να επιλέξεις; ")
        k = int(k)
        if k >= 1 and k <= 10:
            QQQQQ = []
            QQQQQQ = []
            QQQQQQQ = []
            for a1 in range (0, k):
                a = 0.0
                ia = 1
                for row in QQ:
                    if a <= row:
                        a = row
                        ib = ia-1
                    ia = ia + 1
                QQQQQ.append(QQQQ[ib])
                QQQQQQ.append(QQ[ib])
                QQ.pop(ib)
                QQQ.pop(ib)
                QQQQ.pop(ib)
            for row in QQQQQ:
                aaa = number_grid[row][y]
                QQQQQQQ.append(aaa)
            a = 0
            b = 0
            c = 0
            e = 0
            f = 0
            for row in QQQQQQQ:
                b = row
                c = QQQQQQ[a]
                d = b*c
                e = e + d
                f = f + c
                a = a + 1
            g = e / f
            print(g)
            number_grid[x][y] = g
        else:
            print("Παρακαλώ επιλέξτε το k μεταξύ του 1 και του 10.")
    else:
        print("Λυπούμαστε, το κελί που ψάχνεις έχει βαθμό.")
def predict_1_arabic():
    x = input("? jLϊduϊ djl jzujuϊ bd Shl ")
    y = input("? jLϊduϊ djl jzujuϊ jzgoc Shl ")
    x = int(x)
    y = int(y)
    if number_grid[x][y] == 0.0:
        print(number_grid[x][y])
        print("αduιuϊuιtl τθoguϊ.")
        k = input("djl jzujuϊ Shjztl djljudtl jzjzc pS ? ojLϊdϊ ")
        k = int(k)
        if k >= 1 and k <= 10:
            QQQQQ = []
            QQQQQQ = []
            QQQQQQQ = []
            for a1 in range (0, k):
                a = 0.0
                ia = 1
                for row in QQ:
                    if a <= row:
                        a = row
                        ib = ia-1
                    ia = ia + 1
                QQQQQ.append(QQQQ[ib])
                QQQQQQ.append(QQ[ib])
                QQ.pop(ib)
                QQQ.pop(ib)
                QQQQ.pop(ib)
            for row in QQQQQ:
                aaa = number_grid[row][y]
                QQQQQQQ.append(aaa)
            a = 0
            b = 0
            c = 0
            for row in QQQQQQQ:
                b = row
                c = b + c
                a = a + 1
            d = c / a
            print(d)
            number_grid[x][y] = d
        else:
            a = 0
            b = 0
            c = 0
            e = 0
            for row in number_grid:
                if a != x and a != 0:
                    b = row[y]
                    if b != 0.0:
                        c = c + b
                        e = e + 1
                a = a + 1
            d = c / e
            print(d)
            number_grid[x][y] = d
    else:
        print("Lθic Ϋduιuϊ shuϊtl αuldtl , ljjzc adjjz shlc ShgϊduΪ.")
def predict_2_arabic():
    x = input("? jLϊduϊ djl jzujuϊ bd Shl")
    y = input("? jLϊduϊ djl jzujuϊ jzgoc Shl")
    x = int(x)
    y = int(y)
    if number_grid[x][y] == 0.0:
        print(number_grid[x][y])
        print("αduιuϊuιtl τθoguϊ")
        k = input("djl jzujuϊ Shjztl djljudtl jzjzc pS ? ojLϊdϊ")
        k = int(k)
        if k >= 1 and k <= 10:
            QQQQQ = []
            QQQQQQ = []
            QQQQQQQ = []
            for a1 in range (0, k):
                a = 0.0
                ia = 1
                for row in QQ:
                    if a <= row:
                        a = row
                        ib = ia-1
                    ia = ia + 1
                QQQQQ.append(QQQQ[ib])
                QQQQQQ.append(QQ[ib])
                QQ.pop(ib)
                QQQ.pop(ib)
                QQQQ.pop(ib)
            for row in QQQQQ:
                aaa = number_grid[row][y]
                QQQQQQQ.append(aaa)
            a = 0
            b = 0
            c = 0
            e = 0
            f = 0
            for row in QQQQQQQ:
                b = row
                c = QQQQQQ[a]
                d = b*c
                e = e + d
                f = f + c
                a = a + 1
            g = e / f
            print(g)
            number_grid[x][y] = g
        else:
            print("10 g 1 djMu k jzujduϊ cLdjtl")
    else:
        print("Lθic Ϋduιuϊ shuϊtl αuldtl , ljjzc adjjz shlc ShgϊduΪ")
list = input("Ποια γλώσσα θέλεις; Πάτα 1 για ελληνικά ή 2 για αραβικά (αuιuιjΩtl αΏlt)\n")
if list == '1':
    print ("Ελληνικά")
    list = input ("Τί θέλεις να κάνεις με την εργασία;\n")
    while True:
        if list == 'Προσθήκη 1':
            print("Πόσες νέες γραμμές θέλεις να βάλεις;")
            row = input()
            row = int(row)
            for r in range (0, row):
                add_row(i+r)
        if list == 'Προσθήκη 2':
            print("Πόσες νέες στήλες θέλεις να βάλεις;")
            col = input()
            col = int(col)
            for c in range(0, col):
                add_col(i, j)
                j = j
        if list == 'Μηδέν':
            select_greek(i, j)
        if list == 'Αφαίρεση 1':
            print("Πόσες γραμμές θέλεις να σβήσεις;")
            remove_row(i)
        if list == 'Αφαίρεση 2':
            print("Πόσες στήλες θέλεις να σβήσεις;")
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
        if list == 'Πρόβλεψη 1':
            predict_1_greek()
        if list == 'Πρόβλεψη 2':
            predict_2_greek()
        if list == 'Καθαρισμός':
            print("Καθαρισμός.")
            QQ = []
            QQQ = []
            QQQQ = []
        if list == 'Τέλος':
            print("Τέλος εργασίας.")
            break
        list = input ("Τί θέλεις να κάνεις με την εργασία;\n")
if list == '2':
    print ("shujc")
    list = input ("? αόιbgtLι JΩόuϊ djl jzujuϊ ljzLo\n")
    while True:
        if list == 'Προσθήκη 1':
            print("jzujuϊ Shuϊtl ojzujzdtl jbuιuιιΨl jzjzc pS ? LθΩuιόg")
            row = input()
            row = int(row)
            for r in range (0, row):
                add_row(i+r)
        if list == 'Προσθήκη 2':
            print("jzujuϊ shuϊtl ojzujzdtl ojzocΨl jzjzc pS ? LθΩuιόg")
            col = input()
            col = int(col)
            for c in range(0, col):
                add_col(i, j)
                j = j
        j = j
        if list == 'Μηδέν':
            select_arabic(i, j)
        if list == 'Αφαίρεση 1':
            print("? Lθόjzd jzujuϊ shuϊtl jgbuιuιιtl jzjzc pS")
            remove_row(i)
        if list == 'Αφαίρεση 2':
            print("? Lθόjzd jzujuι shuϊtl ojzocΨl jzjzc pS")
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
        if list == 'Πρόβλεψη 1':
            predict_1_arabic()
        if list == 'Πρόβλεψη 2':
            predict_2_arabic()
        if list == 'Καθαρισμός':
            print("YόιbuiuΪ.")
            QQ = []
            QQQ = []
            QQQQ = []
        if list == 'Τέλος':
            print("JoΩtl auLθui.")
            break
        list = input ("? αόιbgtLι JΩόuϊ djl jzujuϊ ljzLo\n")