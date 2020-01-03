
start = 2
end = int(input("Enter last number"))

for num in range(start, end):
    for pm in range(2, num):
        if num % pm == 0:
            break
        else:
            print(str(num))