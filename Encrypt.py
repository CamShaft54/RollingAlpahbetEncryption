user_input = input("Enter text: ").lower()
total = 0
i = len(user_input) - 1
for j in range(len(user_input)):
    total += (26 ** j) * (ord(user_input[i]) - 96)
    i -= 1
print("Encrypted text: " + str(total))
