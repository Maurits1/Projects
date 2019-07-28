import time
import numpy
import texttable

subtract_set = {1,2,3,4,5,6,7,8,9}

container = []



x = 0
while x < 9:
    container.append(list(map(int, str(input("rij " + str(x+1) + " is: ")))))
    x += 1

def check_horizontal(i,j):
    return set(container[i])

def check_vertical(i,j):
    ret_set = []
    for x in range(9):
        ret_set.append(container[x][j])
    return set(ret_set)

def check_square(i,j):
    first = [0,1,2]
    second = [3,4,5]
    third = [6,7,8]
    find_square = [first,second,third]

    for l in find_square:
        if i in l:
            row = l
        if j in l:
            col = l
    ret_set = []
    for x in row:
        for y in col:
            ret_set.append(container[x][y])
    return set(ret_set)

def zoek_mogelijkheden(h,v):
    return(subtract_set - check_square(h,v) - check_vertical(h,v) - check_horizontal(h,v))



lege_cellen = 0
for l in container:
    for v in l:
        if v == 0:
            lege_cellen += 1

print("Lege cellen: " + str(lege_cellen))

# solving = True
# while solving:
#     if lege_cellen == 0:
#         print("solved!")
#         solving = False
table = texttable.Texttable()

def tabel_tekenen(container):
    table.reset()
    table.add_rows(container)
    print(table.draw())


while lege_cellen > 0:
        for i in range(9):
            for j in range(9):
                if container[i][j] == 0:
                    megelijkheden = zoek_mogelijkheden(i,j)
                    if len(megelijkheden) == 1:
                        container[i][j] = list(megelijkheden)[0]
                        lege_cellen = lege_cellen - 1
                        print("\n\n Lege cellen: " + str(lege_cellen))
                        tabel_tekenen(container)
                        
