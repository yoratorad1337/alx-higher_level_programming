#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):  # ord('a') == 97 and ord('z') == 123
    if chr(i) != 'q' and chr(i) != 'e':
        print('{}'.format(chr(i)), end='')
