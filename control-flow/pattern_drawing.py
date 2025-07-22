size = int(input("Enter the size of the pattern: "))
it = 0

while it < size:
    for i in range(size):
        print('*', end='')
    print()
    it += 1