"""
Β. Το πρόγραμμα σας θα πρέπει να υλοποιεί ένα σύστημα collaborative filtering αντικειμένουαντικειμένου. Για την
ομοιότητα θα πρέπει να υλοποιήσετε τέσσερις διαφορετικές συναρτήσεις ομοιότητας, Jaccard, Dice, cosine και 
adjusted cosine. Για την πρόβλεψη του βαθμού θα χρησιμοποιείται η τεχνική των Κ-κοντινότερων γειτόνων και είτε ο
μέσος όρος είτε ο σταθμισμένος μέσος όρος των βαθμολογιών. 
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
    x = int(x)
    y = int(y)
    i = int(i)
    j = int(j)
    for I in range (x, i+1):
        for J in range (y, j+1):
            number_grid[I][J] = 0.0
def select_arabic(i, j):
    x = input("? αuiuιuιΩuϊ ojzlcl jzujuϊ Υshjztl bdtl Lo")
    i = input("? αuiuιuιΩuΪ ojzLcl jzujuϊ Yshjztl bdtl shuΪd")
    y = input("? djmuιΩuϊtl ojzLcl jzujuϊ jzgoc Yshl djo")
    j = input("? ojzLc jzujuϊ Yshjztl jzgoΩtl gφ Lo auiuιuιΩuΪ")
    x = int(x)
    y = int(y)
    i = int(i)
    j = int(j)
    for I in range (x, i+1):
        for J in range (y, j+1):
            number_grid[I][J] = 0.0
def remove_row(i):
    b = input()
    b = int(b)
    if b <= i:
        for b in range(0, b):
            a = number_grid.pop()
            print(a)
def remove_col(i):
    b = input()
    b = int(b)
    if b <= j:
        for b in range(0, b):
            for e in range(0, i+1):
                a = number_grid[e].pop()
                print(a)
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
        if list == 'Τέλος':
            print("JoΩt l zguiuiij")
            break
        list = input ("? aόιbgtlu Jωόuϊ djl jzujuϊ l jzLo\n")