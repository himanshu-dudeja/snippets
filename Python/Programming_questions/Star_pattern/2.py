# Pattern

#    *
#   **
#  ***
# ****

for i in range(1, 5):
    for j in range(1, 5):
        if j >= (4 - i) + 1:
            print("*", end='')
        else:
            print(" ", end='')
    print()
