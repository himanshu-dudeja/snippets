# Pattern

# 1
# 12
# 123
# 1234

for i in range(1, 5):
    for j in range(1, 5):
        if j <= i:
            print(j, end='')
    print()
