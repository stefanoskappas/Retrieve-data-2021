import random
import math
#import numpy
Similarity_value = []
Similarity_index = []
number_grid2 = []
count = 0
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
    name = "Χρήστης "
    b = str(i + 1)
    name = (name + b)
    number_grid.append([name])
    i = i + 1
def add_col(i, j):
    Α = 0
    for Β in range (0, i):
        for row in number_grid:
            if Α == i + 1:
                break
            if Α == 0:
                book = 'Βιβλίο '
                bb = str(c+j+1)
                name = book + bb
                row.append(name)
            if Α > 0:
                new = random.randint(1, 100)
                new = new / 10.0
                row.append(new)
            Α = Α + 1
        j = j + c
def select(i, j, language):
    # Το x σημαίνει γραμμή. Το y σημαίνει στήλη.
    if language == '1':
        x_start = input("Από ποιά γραμμή θέλεις να τροποποιήσεις; ")
        x_finish = input("Μέχρι ποιά γραμμή θέλεις να τροποποιήσεις; ")
        y_start = input("Από ποιά στήλη θέλεις να τροποποιήσεις; ")
        y_finish = input("Μέχρι ποιά στήλη θέλεις να τροποποιήσεις; ")
        value = input("Τί τιμή θέλεις να βάλεις; ")
    if language == '2':
        x_start = input("? αlujzΩϊ jzujuϊ Shjztl bdtl Lo ")
        x_finish = input("? αlujzΩϊ jzujuϊ Shjztl bdtl gφ Lo ")
        y_start = input("? JujzΩϊtl jzujuϊ jzgoc Shl djo ")
        y_finish = input("? αlujzΩϊ jzujuϊ jzgoc Shl shtl ")
        value = input("? αΩuιόuϊ djl jzujuϊ Shjztl jΩuιuιιtl Lo ")
    value = float(value)
    x_start = int(x_start)
    y_start = int(y_start)
    x_finish = int(x_finish)
    y_finish = int(y_finish)
    if (x_start > 0 and x_finish >= x_start and x_finish <= i and y_start > 0 and y_finish >= y_start and y_finish <= j):
        for ROW in range (x_start, x_finish+1):
            for COL in range (y_start, y_finish + 1):
                number_grid[ROW][COL] = value
    else:
        if language == '1':
            print("Παρακαλώ, να επιλέξεις τα στοιχεία εντός των ορίων του πίνακα.")
        if language == '2':
            print("jzgjzd Jdljz jιOLiΩtl jzujzdϊ cLdjtl .Jgjzdtl")
def remove_row(i, language):
    number_of_rows = input()
    number_of_rows = int(number_of_rows)
    if number_of_rows <= i:
        for number_of_rows in range(0, number_of_rows):
            a = number_grid.pop()
    else:
        if language == '1':
            print("Δεν μπορείς να αφαιρέσεις περισσότερους χρήστες από τους υπάρχοντες.")
        if language == '2':
            print("Loo jϊSl dzjuojzdϊuιιo αtl jl JsiSouι Ψ .JΩόtLu jSujzt")
def remove_col(i, language):
    number_of_cols = input()
    number_of_cols = int(number_of_cols)
    if number_of_cols <= j:
        for number_of_cols in range(0, number_of_cols):
            for row in range(0, i+1):
                a = number_grid[row].pop() 
    else:
        if language == '1':
            print("Δεν μπορείς να αφαιρέσεις περισσότερα βιβλία από τα υπάρχοντα.")
        if language == '2':
            print(".Jsujzt Loo jϊSl YuϊS αtl jl JsiSouι Ψ")
def user(i, j, language):
    if language == '1':
        print("Βαθμολογία ανά χρήστη.")
    if language == '2':
        print("pjzdϊuιuιιkl ΫLouιuιοuϊ.")
    index = 0
    sum = 0
    value = 0
    average = 0
    for row in number_grid[1:(i+1)]:
        sum = 0
        for col in row:
            if index >= 1:
                value = col
                if value == 0.0:
                    value = 5.0
                sum = sum + value
            index = index + 1
        average = sum / (index - 1)
        if language == '1':
            print("Ο", row[0], "έχει μέσο score", average)
        if language == '2':
            print("Jl", row[0], "YLdjjz buιuιιgϊo aujzt", average)
        index = 0
def book(i, j, language):
    if language == '1':
        print("Βαθμολογία ανά βιβλίο.")
    if language == '2':
        print("ΎLϊS JSt Ϋljuιuϊιc.")
    index = 0
    sum = 0
    value = 0
    e = 0
    for e in range (1, j+1):
        index = 0
        sum = 0
        for row in number_grid:
            if index == 0:
                book = row[e]
            if index >= 1:
                value = row[e]
                if value == 0.0:
                    value = 5.0
                sum = sum + value
            index = index + 1
        value = sum / (index-1)
        if language == '1':
            print("Ο", book, "έχει μέσο score", value)
        if language == '2':
            print("Jl", book, "YLdjjz buιuιιgϊo aujzt", value)
        value = 0
def jaccard(user, compare_user, language, list, prin):
    if (user > 0 and user <= i and compare_user > 0 and compare_user <= i):
        j_user = 0
        user_positive = 0
        Λ = 0
        for col in number_grid[user]:
            if j_user > 0:
                if col > 0.0:
                    user_positive = user_positive + 1
                    j_compare_user = 0
                    compare_user_positive = 0
                    for col in number_grid[compare_user]:
                        if j_compare_user > 0:
                            if col > 0.0:
                                compare_user_positive = compare_user_positive + 1
                                if j_compare_user == j_user:
                                    Λ = Λ + 1
                        j_compare_user = j_compare_user + 1
            j_user = j_user + 1
        U = user_positive + compare_user_positive - Λ
        jaccard = Λ / U
        if list == 'Jaccard':
            if language == '1':
                print("Η Jaccard ομοιότητα", user, compare_user, "είναι =", jaccard)
                stil = input("Θέλεις να καταχωρίσεις τον συντελεστή; ")
            if language == '2':
                print("Jaccard gφ", user, compare_user, "αuLuιuϊιuϊtl =", jaccard)
                stil = input("? jΩuιuιιtl JLdjzl jzujuϊ Jφ ")
            if stil == '1':
                Similarity_value.append(jaccard)
                Similarity_index.append(compare_user)
                print(Similarity_value)
        if list == 'Γ':
            Similarity_value.append(jaccard)
            Similarity_index.append(compare_user)
            if prin == '1':
                if language == '1':
                    print("Jaccard ", user, compare_user, "= ", jaccard)
                if language == '2':
                    print("jzjLSLd ", user, compare_user, "= ", jaccard)
    else:
        if language == '1':
            print("Η επιλογή για ομοιότητα χρηστών είναι εκτός ορίων.")
        if language == '2':
            print("τθjLd pjzdϊuιuιιotl αuLuιuϊιuϊ jLuιuϊdl .jzgjzdtl")
def kozani(user, compare_user, language, list, prin):
    if (user > 0 and user <= i and compare_user > 0 and compare_user <= i):
        j_user = 0
        user_x_compareuser = 0
        sum_user = 0
        sum_compareuser = 0
        for col in number_grid[user]:
            if j_user > 0:
                user_x_compareuser = user_x_compareuser + col*number_grid[compare_user][j_user]
                value_user = col
                sum_user = sum_user + value_user * value_user
                value_compare_user = number_grid[compare_user][j_user]
                sum_compareuser = sum_compareuser + value_compare_user * value_compare_user
            j_user = j_user + 1
        cos = user_x_compareuser / (math.sqrt(sum_user) * math.sqrt(sum_compareuser))
        if list == 'Κοζάνη':
            if language == '1':
                print("Η Κοζάνη ομοιότητα", user, compare_user, "είναι =", cos)
                stil = input("Θέλεις να καταχωρίσεις τον συντελεστή; ")
            if language == '2':
                print("αuLuιuϊιο", user, compare_user, "shuiljgS =", cos)
                stil = input("? jΩuιuιιtl JLdjzl jzujuϊ Jφ ")
            if stil == '1':
                Similarity_value.append(cos)
                Similarity_index.append(compare_user)
                print(Similarity_value)
        if list == 'Γ':
            Similarity_value.append(cos)
            Similarity_index.append(compare_user)
            if prin == '1':
                if language == '1':
                    print("Cosine ", user, compare_user, "= ", cos)
                if language == '2':
                    print("pLoϊtl Υuιd ", user, compare_user, "= ", cos)
    else:
        if language == '1':
            print("Η επιλογή για ομοιότητα χρηστών είναι εκτός ορίων.")
        if language == '2':
            print("τθjLd pjzdϊuιuιιotl αuLuιuϊιuϊ jLuιuϊdl .jzgjzdtl")
def dice(user, compare_user, language, list, prin):
    if (user > 0 and user <= i and compare_user > 0 and compare_user <= i):
        j_user = 0
        user_positive = 0
        Λ = 0
        for col in number_grid[user]:
            if j_user > 0:
                if col > 0.0:
                    user_positive = user_positive + 1
                    j_compare_user = 0
                    compare_user_positive = 0
                    for col in number_grid[compare_user]:
                        if j_compare_user > 0:
                            if col > 0.0:
                                compare_user_positive = compare_user_positive + 1
                                if j_compare_user == j_user:
                                    Λ = Λ + 1
                        j_compare_user = j_compare_user + 1
            j_user = j_user + 1
        U = user_positive + compare_user_positive - Λ
        dice = 2*Λ / (user_positive + compare_user_positive)
        if list == 'Dice':
            if language == '1':
                print("Η Dice ομοιότητα", user, compare_user, "είναι =", dice)
                stil = input("Θέλεις να καταχωρίσεις τον συντελεστή; ")
            if language == '2':
                print("jzjuitl", user, compare_user, "αuLuιuϊιuϊ =", dice)
                stil = input("? jΩuιuιιtl JLdjzl jzujuϊ Jφ ")
            if stil == '1':
                Similarity_value.append(dice)
                Similarity_index.append(compare_user)
                print(Similarity_value)
        if list == 'Γ':
            Similarity_value.append(dice)
            Similarity_index.append(compare_user)
            if prin == '1':
                if language == '1':
                    print("Dice ", user, compare_user, "= ", dice)
                if language == '2':
                    print("Jgοu ", user, compare_user, "= ", dice)
    else:
        if language == '1':
            print("Η επιλογή για ομοιότητα χρηστών είναι εκτός ορίων.")
        if language == '2':
            print("τθjLd pjzdϊuιuιιotl αuLuιuϊιuϊ jLuιuϊdl .jzgjzdtl")
def adjusted_kozani(user, compare_user, language, list, prin):
    if (user > 0 and user <= i and compare_user > 0 and compare_user <= i):
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
        user_x_compareuser = 0
        user_sum = 0
        compareuser_sum = 0
        for col in number_grid3[user]:
            if jj > 0:
                col = float(col)
                user_x_compareuser = user_x_compareuser + col*number_grid3[compare_user][jj]
                bb = col
                user_sum = user_sum + bb*bb
                cc = number_grid3[compare_user][jj]
                compareuser_sum = compareuser_sum + cc*cc
            jj = jj + 1
        FFF = (math.sqrt(user_sum) * math.sqrt(compareuser_sum))
        if FFF == 0.0:
            FFF = 1.0
            user_x_compareuser = 0.0
        cos = user_x_compareuser / FFF
        if list == 'ΑΚοζάνη':
            if language == '1':
                print("Η αναθεματισμένη Κοζάνη ομοιότητα", user, compare_user, "είναι =", cos)
                stil = input("Θέλεις να δείς τον κανινικοποιημένο πίνακα; ")
            if language == '2':
                print("gφ shuiljgS djMΩltl", user, compare_user, "αuιuιuϊιtl =", cos)
                stil = input("? shΩuιuιbtl Jgjzdtl Shjuϊ djl jzujuϊ Jφ ")
            if stil == '1':
                for row in number_grid3:
                    print(row)
            if language == '1':
                stil = input("Θέλεις να καταχωρίσεις τον συντελεστή; ")
            if language == '2':
                stil = input("? jΩuιuιιtl JLdjzl jzujuϊ Jφ ")
            if stil == '1':
                Similarity_value.append(cos)
                Similarity_index.append(compare_user)
                print(Similarity_value)
        if list == 'Γ':
            Similarity_value.append(cos)
            Similarity_index.append(compare_user)
            if prin == '1':
                if language == '1':
                    print("adjusted cosine ", user, compare_user, "= ", cos)
                if language == '2':
                    print("JjzΩοtl pLoϊtl Υuιd ", user, compare_user, "= ", cos)
    else:
        if language == '1':
            print("Η επιλογή για ομοιότητα χρηστών είναι εκτός ορίων.")
        if language == '2':
            print("τθjLd pjzdϊuιuιιotl αuLuιuϊιuϊ jLuιuϊdl .jzgjzdtl")
def predict_1(x, y, k, language, list, prin):
    if x > 0 and x <= i and y > 0 and y <= j:
        if number_grid[x][y] == 0.0:
            if list == 'Πρόβλεψη 1':
                if language == '1':
                    k = input("Δώσε μία τιμή k-γειτόνων ")
                if language == '2':
                    k = input("djzljudtl -k aouιϋg bcl")
                k = int(k)
            if k > 0 and k < j:
                search_row = 0
                rest_of_k = k
                sum = 0
                predict_value = 0
                for row in number_grid:
                    if search_row > x and rest_of_k > 0:        
                        if row[y] > 0.0:
                            rest_of_k = rest_of_k - 1
                            sum = sum + row[y]
                    search_row = search_row + 1
                search_row = 0
                for row in number_grid:
                    if search_row > 0 and search_row < x and rest_of_k > 0:
                        if row[y] > 0.0:
                            rest_of_k = rest_of_k - 1
                            sum = sum + row[y]
                    search_row = search_row + 1
                k = k - rest_of_k
                predict_value = sum / k
                if list == 'Γ':
                    if prin == '1':
                        if language == '1':
                            print("\nΠρόβλεψη 1: χρήστη", x, "βιβλίο", y, " =", predict_value)
                        if language == '2':
                            print("\nτθLiotlu guιuiuϊ 1: JoΩϊuιuιιοtl", x, "YLϊS", y, " =", predict_value)
                if list == 'Πρόβλεψη 1':
                    print(predict_value)
                number_grid[x][y] = predict_value
            else:
                if language == '1':
                    print("Λάθως τιμή k")
                if language == '2':
                    print("adιdιΟ juc k aoιϋg")
        else:
            if language == '1':
                print("Λάθος τιμή πίνακα")
            if language == '2':
                print("adιdιΟ juc aϋg gόιΟο aoιϋg")
    else:
        if language == '1':
            print("Όλα λάθος")
        if language == '2':
            print("shbld cshuιuϊί JS")
def predict_2(x, y, k, language, list, prin): 
    if x > 0 and x <= i and y > 0 and y <= j:
        if number_grid[x][y] == 0.0:
            if list == 'Πρόβλεψη 2':
                if language == '1':
                    k = input("Δώσε μία τιμή k-γειτόνων ")
                if language == '2':
                    k = input("djzljudtl -k aouιϋg bcl")
                k = int(k)
            k_limit = 0
            for row in Similarity_value:
                k_limit = k_limit + 1
            if k > 0 and k <= k_limit and k < i:
                k_limit = 0
                for row in Similarity_value:
                    if row <= k:
                        k_limit = k_limit + 1
                if list == 'Πρόβλεψη 2':
                    if language == '1':
                        print("Οι πίνακες ομοιότητας πριν την ταξινόμηση:\n")
                    if language == '2':
                        print("Juϋg auLuιuϊiuϊtl ΫLύggόιΟο υόuιuiιΟϊtl:\n")
                    print(Similarity_value, Similarity_index)
                RANGE = k_limit - 1
                for I in range(i-1):
                    for row in range(0, RANGE-I):
                        if Similarity_value[row] < Similarity_value[row+1]:
                            Similarity_value[row], Similarity_value[row+1] = Similarity_value[row+1], Similarity_value[row]
                            Similarity_index[row], Similarity_index[row+1] = Similarity_index[row+1], Similarity_index[row]                
                if list == 'Πρόβλεψη 2':
                    if language == '1':
                        print("Ταξινομοιμένοι κατά φθίνουσα σειρά πίνακες ομοιότητας:\n")
                    if language == '2':
                        print("Jgljzd shtjLiuϊ Yuιuϊjuϊuι αuιuϊjo αuLuιuϊiuϊtl:\n")
                    print(Similarity_value, Similarity_index)
                predict_value = 0
                rest_of_k = k
                for row in range(0,k):
                    index = Similarity_index[row]
                    if number_grid[index][y] > 0.0:
                        predict_value = predict_value + number_grid[index][y]
                        rest_of_k = rest_of_k - 1
                if list == 'Πρόβλεψη 2':
                    k = k - rest_of_k
                    predict_value = predict_value / k
                    print(predict_value)
                if list == 'Γ':
                    predict_value = predict_value / k
                    if prin == '1':
                        if language == '1':
                            print("\nΠρόβλεψη 2: χρήστη", x, "βιβλίο", y, " =", predict_value)
                        if language == '2':
                            print("\nτθLiotlu guιuiuϊ 2: JoΩϊuιuιιοtl", x, "YLϊS", y, " =", predict_value)
                number_grid[x][y] = predict_value
            else:
                if language == '1':
                    print("Λάθως τιμή k")
                if language == '2':
                    print("adιdιΟ juc k aoιϋg")
        else:
            if language == '1':
                print("Λάθος τιμή πίνακα")
            if language == '2':
                print("adιdιΟ juc aϋg gόιΟο aoιϋg")
    else:
        if language == '1':
            print("Όλα λάθος")
        if language == '2':
            print("shbld cshuιuϊί JS")
def predict_3(x, y, k, language, list, prin): 
    if x > 0 and x <= i and y > 0 and y <= j:
        if number_grid[x][y] == 0.0:
            if list == 'Πρόβλεψη 3':
                if language == '1':
                    k = input("Δώσε μία τιμή k-γειτόνων ")
                if language == '2':
                    k = input("djzljudtl -k aouιϋg bcl")
                k = int(k)
            k_limit = 0
            for row in Similarity_value:
                k_limit = k_limit + 1
            if k > 0 and k <= k_limit and k < i:
                k_limit = 0
                for row in Similarity_value:
                    if row <= k:
                        k_limit = k_limit + 1
                if list == 'Πρόβλεψη 3':
                    if language == '1':
                        print("Οι πίνακες ομοιότητας πριν την ταξινόμηση:\n")
                    if language == '2':
                        print("Juϋg auLuιuϊiuϊtl ΫLύggόιΟο υόuιuiιΟϊtl:\n")
                    print(Similarity_value, Similarity_index)
                RANGE = k_limit - 1
                for I in range(i-1):
                    for row in range(0, RANGE-I):
                        if Similarity_value[row] < Similarity_value[row+1]:
                            Similarity_value[row], Similarity_value[row+1] = Similarity_value[row+1], Similarity_value[row]
                            Similarity_index[row], Similarity_index[row+1] = Similarity_index[row+1], Similarity_index[row]
                if list == 'Πρόβλεψη 3':
                    if language == '1':
                        print("Ταξινομοιμένοι κατά φθίνουσα σειρά πίνακες ομοιότητας:\n")
                    if language == '2':
                        print("Jgljzd shtjLiuϊ Yuιuϊjuϊuι αuιuϊjo αuLuιuϊiuϊtl:\n")
                    print(Similarity_value, Similarity_index)
                predict_value = 0
                similarity_value = 0
                product = 0
                sum_of_product = 0
                sum_of_similarity_value = 0
                for row in range(0,k):
                    index = Similarity_index[row]
                    if number_grid[index][y] > 0.0:
                        predict_value = number_grid[index][y]
                        similarity_value = Similarity_value[row]
                        product = predict_value * similarity_value
                        sum_of_product = sum_of_product + product
                        sum_of_similarity_value = sum_of_similarity_value + similarity_value
                if sum_of_similarity_value == 0:
                    predict_value = 0
                else:
                    predict_value = sum_of_product / sum_of_similarity_value
                if list == 'Πρόβλεψη 3':
                    print(predict_value)
                if list == 'Γ':
                    if prin == '1':
                        if language == '1':
                            print("\nΠρόβλεψη 3: χρήστη", x, "βίβλίο", y, " =", predict_value)
                        if language == '2':
                            print("\nτθLiotlu guιuiuϊ 3: JoΩϊuιuιιοtl", x, "YLϊS", y, " =", predict_value)
                number_grid[x][y] = predict_value
            else:
                if language == '1':
                    print("Λάθως τιμή k")
                if language == '2':
                    print("adιdιΟ juc k aoιϋg")
        else:
            if language == '1':
                print("Λάθος τιμή πίνακα")
            if language == '2':
                print("adιdιΟ juc aϋg gόιΟο aoιϋg")
    else:
        if language == '1':
            print("Όλα λάθος")
        if language == '2':
            print("shbld cshuιuϊί JS")
def gamma(language, count):
    i_grid = [0]
    j_grid = [0]
    number_of_zeros = 1
    if count == 0:
        ia = 0
        ib = 0
        number_grid2.append(number_grid[0])
        for iI in range(0,i):
            a = "Χρήστης "
            b = str(iI + 1)
            a = (a+b)
            number_grid2.append([a])
            iI = iI + 1
        for row in number_grid:
            jb = 0
            DD = 0
            za = 0
            if ib > 0:
                for col in row:
                    if jb > 0:
                        number_grid2[ib].append(col)
                    jb = jb + 1
            ib = ib + 1
    for row in range(1,i+1):
        for col in range(1,j+1):
            if number_grid[row][col] == 0:
                i_grid.append(row)
                j_grid.append(col)
                number_of_zeros = number_of_zeros + 1
            new = random.randint(0, 9)
            if new == 0:
                number_grid[row][col] = new
                i_grid.append(row)
                j_grid.append(col)
                number_of_zeros = number_of_zeros + 1
    if number_of_zeros > 1:
        if language == '1':
            print("Αριθμός αλλαγών =", number_of_zeros-1)
            similarity_key = input("Ποιά μέθοδο ομοιότητας χρηστών θα επιλέξεις ")
            predict_key = input("Ποιά μέθοδο πρόβλεψης βαθμολογιών θα επιλέξεις ")
            k = input("Πόσους k-γείτονες θα επιλέξεις ")
            prin = input("Θέλεις να δείς τις τιμές ομοιότητας και προβλέψεις; ")
        if language == '2':
            print("ΫljuιuιΏuϊtl =", number_of_zeros-1)
            similarity_key = input("pjzdϊuιuιιοtl auLuιuϊiuϊ αοuιjb shl ?jLϊdϊ υόguιuιι ")
            predict_key = input("aduιuϊuitl Ωτθϋggϊ αοuιjb shφ Lo ?LφjLϊdϊuιuιι shϊtl ")
            k = input("υόguιuιι k djzl judtl jzjzv pS ?jLϊdϊ ")
            prin = input("? αuLuιuϊiuϊtl puϋg shjuϊ djzl jzujuϊ Ϋlguιuiuϊtlg ")
        if prin == '1':
            if language == '1':
                print("\nΟι άγνωστες βαθμολογίες βρίσκονται στις παρακάτω γραμμές και στήλες του πίνακα")
            if language == '2':
                print("\nαύgjΩοtl juc ΫLdjjztl ojzocΨlg υόgόιΟtl shύg ojzgdgo Jgjzdtl djzo autLϊtl")
            for row in range(1, number_of_zeros):
                print(i_grid[row], j_grid[row])
            print()
            if language == '1':
                print("Ο πίνακας βαθμολογιών μετά την προσθήκη των άγνωστων βαθμολογιών.")
            if language == '2':
                print("αύgLιΌl jzΩu τθiLϊuitl adgt .atgθdotl ΫLdjjztl")
            for row in number_grid:
                print(row)
            print()
        k = int(k)
        if k > 0 and k < j: 
            for row in range (1, number_of_zeros):
                del Similarity_value[:]
                del Similarity_index[:]
                if i_grid[row] != i_grid[row-1]:
                    for col in range (1, i+1):
                        if col != i_grid[row]:
                            if similarity_key == '1':
                                jaccard(i_grid[row], col, language, list, prin)
                            if similarity_key == '2':
                                kozani(i_grid[row], col, language, list, prin)
                            if similarity_key == '3':
                                dice(i_grid[row], col, language, list, prin)
                            if similarity_key == '4':
                                adjusted_kozani(i_grid[row], col, language, list, prin)
                    if predict_key == '1':
                        predict_1(i_grid[row], j_grid[row], k, language, list, prin)
                    if predict_key == '2':
                        predict_2(i_grid[row], j_grid[row], k, language, list, prin)
                    if predict_key == '3':
                        predict_3(i_grid[row], j_grid[row], k, language, list, prin)
                    i_grid[row] = 0
                    j_grid[row] = 0
                    if prin == '1':
                        print()
                        for col in number_grid:
                            print(col)
                        print()
        else:
            if language == '1':
                print("Λάθος τιμή κ-γειτόνων.")
            if language == '2':
                print(".adιdιΟ juc k jlgdtl aoιϋg")
def delta(language):
    error = 0
    sum = 0
    abs_sum = 0
    file = open('Αποτέλεσμα.csv', 'w')
    if language == '1':
        print("Ο πίνακας βαθμολογιών από τους χρήστες πριν από την τροποποίηση του.")
        file.write("Ο πίνακας βαθμολογιών από τους χρήστες πριν από την τροποποίηση του.\n")
    if language == '2':
        print("Juϋg pjzdϊuιuιιotl υόuιuιιΟuϊ Jgjzd .αlujzΩuϊ")
        file.write("Juϋg pjzdϊuιuιιotl υόuιuιιΟuϊ Jgjzd .αlujzΩuϊ\n")
    for row in number_grid2:
        print(row)
        for col in row:
            COL = str(col)
            file.write(COL)
            file.write(";")
        file.write("\n")
    if language == '1':
        print("\nΟ πίνακας βαθμολογιών μετά την τροποποίηση του.")
        file.write("\nΟ πίνακας βαθμολογιών μετά την τροποποίηση του.\n")
    if language == '2':
        print("\n.LθlujzΩuϊ jzΩu τθiLuϊuitl adgt")
        file.write("\n.LθlujzΩuϊ jzΩu τθiLuϊuitl adgt\n")
    for row in number_grid:
        print(row)
        for col in row:
            COL = str(col)
            file.write(COL)
            file.write(";")
        file.write("\n")
    file.write("")
    print()
    for row in range(1,i+1):
        for col in range(1,j+1):
            if abs(number_grid[row][col] - number_grid2[row][col]) < 0.1 and number_grid[row][col] != number_grid2[row][col]:
                if language == '1':
                    file.write("\nΧρήστης ")
                    file.write(str(row))
                    file.write(";Βιβλίο ")
                    file.write(str(col))
                    file.write(";=")
                    file.write(str(number_grid[row][col] - number_grid2[row][col]))
                    file.write(";Ασήμαντο")
                if language == '2':
                    file.write("\nJoΩϊuιuιιοtl ")
                    file.write(str(row))
                    file.write(";YLϊS ")
                    file.write(str(col))
                    file.write(";=")
                    file.write(str(number_grid[row][col] - number_grid2[row][col]))
                    file.write(";αύgLϊ")
            if abs(number_grid[row][col] - number_grid2[row][col]) >= 0.1:
                error = error + 1
                if language == '1':
                    file.write("\nΧρήστης ")
                    file.write(str(row))
                    file.write(";Βιβλίο ")
                    file.write(str(col))
                    file.write(";=")
                    file.write(str(number_grid[row][col] - number_grid2[row][col]))
                if language == '2':
                    file.write("\nJoΩϊuιuιιοtl ")
                    file.write(str(row))
                    file.write(";YLϊS ")
                    file.write(str(col))
                    file.write(";=")
                    file.write(str(number_grid[row][col] - number_grid2[row][col]))
                sum = sum + number_grid[row][col] - number_grid2[row][col]
                abs_sum = abs_sum + abs(number_grid[row][col] - number_grid2[row][col])
    if error == 0:
        average_error = 0
        average_abs_error = 0
    else:
        average_error = sum / error
        average_abs_error = abs_sum / error
        file.write("\n\n")
    if language == '1':
        print("Ο αριθμός των λανθασμένων προβλέψεων είναι", error)
        file.write("Ο αριθμός των λανθασμένων προβλέψεων είναι = ")
        file.write(str(error))
        print("Το μέσο απόλυτο λάθος των προβλέψεων είναι", average_error)
        file.write("\nΤο μέσο απόλυτο λάθος των προβλέψεων είναι = ")
        file.write(str(average_error))
        print("Το μέσο απόλυτο λάθος κατά απόλυτη τιμή είναι", average_abs_error)
        file.write("\nΤο μέσο απόλυτο λάθος κατά απόλυτη τιμή είναι = ")
        file.write(str(average_abs_error))
    if language == '2':
        print("adudιΟtl juc Ϋlguιuiuϊtt jzjzc gφ", error)
        file.write("adudιΟtl juc Ϋlguιuiuϊtt jzjzc gφ = ")
        file.write(str(error))
        print("Ϋlguιuiuϊtt ϋglbotl Lbdtl buιuιιgϊο gφ", average_error)
        file.write("\nΫlguιuiuϊtt ϋglbotl Lbdtl buιuιιgϊο gφ = ")
        file.write(str(average_error))
        print("shύg ϋglbotl Lbdtl buιuιιgϊο gφ aolbotl aouιοtl", average_abs_error)
        file.write("\nshύg ϋglbotl Lbdtl buιuιιgϊο gφ aolbotl aouιοtl = ")
        file.write(str(average_abs_error))
    file.close()
def compare(list, language):
    if list == 'Jaccard' or list == 'Κοζάνη' or list == 'Dice' or list == 'ΑΚοζάνη':
        if language == '1':
            print("Ποιούς χρήστες θέλεις να συγκρίνεις;")
        if language == '2':
            print("? pθuϊuijLoo jzujuϊ djMojzduϊuιuιιk l shl")
        a = input()
        b = input()
    if list == 'Πρόβλεψη 1' or list == 'Πρόβλεψη 2' or list == 'Πρόβλεψη 3':
        if language == '1':
            a = input("Ποιά γραμμή θέλεις να επιλέξεις; ")
            b = input("Ποιά στήλη θέλεις να επιλέξεις; ")
        if language == '2':
            a = input("? jLϊduϊ djl jzujuϊ bd Shl")
            b = input("? jLϊduϊ djl jzujuϊ jzgoc Shl")
    a = int(a)
    b = int(b)
    if list == 'Jaccard':
        jaccard(a, b, language, list, 0)
    if list == 'Κοζάνη':
        kozani(a, b, language, list, 0)
    if list == 'Dice':
        dice(a, b, language, list, 0)
    if list == 'ΑΚοζάνη':
        adjusted_kozani(a, b, language, list, 0)
    if list == 'Πρόβλεψη 1':
        predict_1(a, b, 0, language, list, 0)
    if list == 'Πρόβλεψη 2':
        predict_2(a, b, 0, language, list, 0)
    if list == 'Πρόβλεψη 3':
        predict_3(a, b, 0, language, list, 0)
language = input("Ποια γλώσσα θέλεις; Πάτα 1 για ελληνικά ή 2 για αραβικά (αuιuιjΩtl αΏlt)\n")
if language == '1':
    print ("Ελληνικά")
    list = input ("Τί θέλεις να κάνεις με την εργασία;\n")
    while True:
        if list == 'Προσθήκη 1':
            iIi = i
            if iIi == 0 and j == 0 or iIi > 0 and j == 0:
                print("Πόσες νέες γραμμές θέλεις να βάλεις; ")
                row = input()
                row = int(row)
                for r in range (0, row):
                    add_row(i+r)
            else:
                print("Δεν μπορείς να προσθέσεις χρήστες στον πίνακα την ώρα που έχει βαθμολογημένα")
                print("βιβλία. Σβήστα τα και μετά πρόσθεσε χρήστες")
        if list == 'Προσθήκη 2':
            if i > 0:
                print("Πόσες νέες στήλες θέλεις να βάλεις;")
                col = input()
                col = int(col)
                for c in range(0, col):
                    add_col(i, j)
                    j = j
            else:
                print("Δεν μπορείς να προσθέσεις βιβλία όταν δεν υπάρχουν χρήστες.")
        if list == 'Μηδέν':
            select(i, j, language)
        if list == 'Αφαίρεση 1':
            print("Πόσες γραμμές θέλεις να σβήσεις;")
            remove_row(i, language)
        if list == 'Αφαίρεση 2':
            print("Πόσες στήλες θέλεις να σβήσεις;")
            remove_col(i, language)
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
            user(i, j, language)
        if list == 'Βιβλίο':
            book(i, j, language)
        if list == 'Jaccard':
            compare(list, language)
        if list == 'Κοζάνη':
            compare(list, language)
        if list == 'Dice':
            compare(list, language)
        if list == 'ΑΚοζάνη':
            compare(list, language)
        if list == 'Πρόβλεψη 1':
            print("Επιλέγεις απλή πρόβλεψη μέσου όρου σειριακή.")
            compare(list, language)
        if list == 'Πρόβλεψη 2':
            print("Επιλέγεις απλή πρόβλεψη βασισμένη σε k-κοντινότερους γείτονες.")
            compare(list, language)
        if list == 'Πρόβλεψη 3':
            print("Επιλέγεις πρόβλεψη σταθμισμένου μέσου όρου βασισμένη σε k-κοντινότερους γείτονες.")
            compare(list, language)
        if list == 'Καθαρισμός':
            print("Καθαρισμός.")
            Similarity_value = []
            QQQ = []
            Similarity_index = []
            number_grid2 = []
        if list == 'Γ':
            gamma(language, count)
            count = count + 1
        if list == 'Δ':
            delta(language)
        if list == 'Τέλος':
            print("Τέλος εργασίας.")
            break
        list = input ("Τί θέλεις να κάνεις με την εργασία;\n")
if language == '2':
    print ("shujc")
    list = input ("? αόιbgtLι JΩόuϊ djl jzujuϊ ljzLo\n")
    while True:
        if list == 'Προσθήκη 1':
            iIi = i
            if iIi == 0 and j == 0 or iIi > 0 and j == 0:
                print("jzujuϊ Shuϊtl ojzujzdtl jbuιuιιΨl jzjzc pS ? LθΩuιόg")
                row = input()
                row = int(row)
                for r in range (0, row):
                    add_row(i+r)
            else:
                print("shtl djzuojzϊuιuιιo aύgLιΌl JsiSouι Ψ pϋg .YuϊStl juιuιοuϊuι LθοLuιϋg cLuiuϊl")
                print("αd gttl aύgLιΌLu pϋg pϊ LθluιΏuιuϊιuϊ ΥόLοuιLu djzuojzdϊuιuιιotl")
        if list == 'Προσθήκη 2':
            if i > 0:
                print("jzujuϊ shuϊtl ojzujzdtl ojzocΨl jzjzc pS ? LθΩuιόg")
                col = input()
                col = int(col)
                for c in range(0, col):
                    add_col(i, j)
                    j = j
            else:
                print("pjzc αtld shύg YuϊS αύgLιΌl JsiSouι Ψ .djzιo jzdϊuιιo jzgdg")
        if list == 'Μηδέν':
            select(i, j, language)
        if list == 'Αφαίρεση 1':
            print("? Lθόjzd jzujuϊ shuϊtl jgbuιuιιtl jzjzc pS")
            remove_row(i, language)
        if list == 'Αφαίρεση 2':
            print("? Lθόjzd jzujuι shuϊtl ojzocΨl jzjzc pS")
            remove_col(i, language)
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
            user(i, j, language)
        if list == 'Βιβλίο':
            book(i, j, language)
        if list == 'Jaccard':
            compare(list, language)
        if list == 'Κοζάνη':
            compare(list, language)
        if list == 'Dice':
            compare(list, language)
        if list == 'ΑΚοζάνη':
            compare(list, language)
        if list == 'Πρόβλεψη 1':
            print("guιuiuϊtl buιuιιgϊο jLuιuϊdl JsiSouι .buιuιuιιuιtl shtuιuιιutuιuιιuϊtl")
            compare(list, language)
        if list == 'Πρόβλεψη 2':
            print("buιuιuιιuιtl guιuiuίtl jLuιuϊdl JsiSouι .djzljudtl Υjϋgl -k shlc cLuiuι")
            compare(list, language)
        if list == 'Πρόβλεψη 3':
            print("buιuιιgϊοtl Ωτθϋggϊ jLuιuϊdl JsiSouι Υjϋgl k shtl ljzLuiuϊuιuιιl τθdjotl .djzljud")
            compare(list, language)
        if list == 'Γ':
            gamma(language, count)
            count = count + 1
        if list == 'Δ':
            delta(language)
        if list == 'Καθαρισμός':
            print("YόιbuiuΪ.")
            Similarity_value = []
            QQQ = []
            Similarity_index = []
            number_grid2 = []
        if list == 'Τέλος':
            print("JoΩtl auLθui.")
            break
        list = input ("? αόιbgtLι JΩόuϊ djl jzujuϊ ljzLo\n")