pyramid_size = 9
for i in range(0 ,pyramid_size):
    line = " " * (pyramid_size - 1 - i) + "*" + "*" * 2 * i + " " * (pyramid_size -1 - i)
    print(line)
