
op = []
for x in range(100,500):
    n = x
    a = n%10
    b = int(n/10)%10
    c = int(n/100)%10
    if (a%2!=0):
        if (b%2!=0):
            if (c%2!=0):
                op.append(x)
print("List of numbers btw 100 and 500 whose digits are also odd")
print(op)

print('Part 2 - Sorting the list of numbers')
list = ["1", "4", "0", "6", "9"]
print('Input List:',list)
list.sort(key=int)
print('Output List:',list)

print('Part 3 - Counting the number of words and letters in a file')
f = open("python.txt","r")
f1 = f.readlines()
for x in f1:
    words = len(x.split())
    letters = sum(c.isalpha() for c in x)
    print(x,'Words:',words,'Letters:',letters)