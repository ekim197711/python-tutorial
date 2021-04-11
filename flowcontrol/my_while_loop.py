
apples_left = 10
while apples_left > 0:
    apples_left -= 1
    if (apples_left % 2 == 0):
        continue
    print("Eat an apple. Apples left ", apples_left)


apples_left = 10
while apples_left > 0:
    apples_left -= 1
    if (apples_left == 5):
        break
    print("Eat an apple. Apples left ", apples_left)

print("done with loop")