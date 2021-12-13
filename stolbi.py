count = int(input())  # кол-во столбов
stolb = list(map(int, input().split()))  # диски

count_disk_on_stolb = []
for i in stolb:
    count_disk_on_stolb.append(1)
# на каждом столбе сейчас по 1 диску

flag_move = 0
flag = 1
while flag_move != 1:
    for i in range(len(stolb)):
        if i + 1 != count:  # если это не последний символ в списке
            # stolb[i] -> stolb[i + 1]
            if count_disk_on_stolb[i] == 1:

                if count_disk_on_stolb[i + 1] == 0 or count[i + 1] > count[i]:
                    count_disk_on_stolb[i] = 0
                    count_disk_on_stolb[i + 1] += 1
                    count[i + 1] = count[i]
                    count[i] = 0
                    break

            # stolb[i] <- stolb[i + 1]
            else:
                if count_disk_on_stolb[i + 1] == 1:

                    if count_disk_on_stolb[i] == 0 or count[i] > count[i + 1]:
                        count_disk_on_stolb[i + 1] = 0
                        count_disk_on_stolb[i] += 1
                        count[i] = count[i + 1]
                        count[i + 1] = 0
                        break
        else:
            flag_move = 1

a = 0
for i in count_disk_on_stolb:
    if i > 0:
        a += 1

if a > 1:
    print("NO")
else:
    print('YES')