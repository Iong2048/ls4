n = int(input())

if n % 3 == 0 and n % 5 == 0:
    print(f"{n} chia hết cho cả 3 và 5.")
elif n % 3 == 0 and n % 5 != 0:
    print(f"{n} chia hết cho 3 nhg ko chia hết cho 5.")
elif n % 5 == 0 and n % 3 != 0:
    print(f"{n} chia hết cho 5 nhg ko chia hết cho 3.")
else:
    print(f"{n} không chia hết cho cả 3 và 5.")