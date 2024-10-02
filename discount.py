price = float(input("Enter the shirt price: "))
quantity = int(input("Enter how many: "))
total = price * quantity
print("""We do discount if you have these valid ID's:
        1. PWD
        2. Senior Citizen
        3. No ID""")
valid = int(input("Enter the number of your available ID, enter '3' if none: "))

if valid == 1:
    pwd = .20 #20% discount for pwd
    pwdDis = total * pwd
    pwdTotal = total - pwdDis
    print("PWD Discount (20%), TOTAL: ", pwdTotal)
elif valid == 1:
    sr = .20 #20% discount for pwd
    srDis = total * sr
    srTotal = total - srDis
    print("PWD Discount (20%), TOTAL: ", srTotal)
elif valid == 3:
    print("TOTAL: ", total)
else:
    print("Invalid Input")