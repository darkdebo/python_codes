def multiplication_table(a):
    for i in range(1,11):
        print(f"{a}x{i}={a*i}")

a=int(input("enter a number to print multiplication table\n"))
multiplication_table(a)
