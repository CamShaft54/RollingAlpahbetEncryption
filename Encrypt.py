user_input = input("Enter text: ")
user_input = user_input.lower()
total = 0
i = len(user_input) - 1
print(i)
j = 0
while i >= 0:
    n = ord(user_input[i]) - 96
    print(user_input[i])
    total += (26 ** j) * n
    i -= 1
    j += 1
print("Encrypted text: " + str(total))
