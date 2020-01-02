f = open("guest_book.txt: ", "x")


i = 0
while i < len("guest_book.txt"):
    f.write(input("Enter your name: ") + "\n")
    i += 1
    if i >= 10:
        break

f.write(input("Enter your name: "))
