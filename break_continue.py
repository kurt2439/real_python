while True:
    user = input("Enter some text, q/Q to quit: ")
    if user == "q" or user == "Q":
        break
print("Exiting...")

for i in range(1,51):
    if i % 3 == 0:
        continue
    else:
        print(i)
