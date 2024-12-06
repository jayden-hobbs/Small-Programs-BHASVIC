books = ["art", "geography", "history"]
found = False
i = 0
find = input("Enter your subject: ")
find = find.lower()

while found == False and i < len(books):
    if books[i] == find:
        found = True
    else:
        i = i+1

if found:
    print (i)
else:
    print ("-1")

