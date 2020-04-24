import math

user_input = int(input("Enter Code: "))
length = 1
threshold = 26
result = ""
while True:
    if user_input > threshold:
        length += 1
        threshold += 26 ** length
    else:
        break
letters = []
base = user_input / 26 ** (length - 1)
for i in range(length):
    letters.append(math.floor(round(base, 2)))
    base = (base - letters[i]) * 26
result = ""
for i in range(length):
    result += chr(letters[i] + 96)
print(result)
