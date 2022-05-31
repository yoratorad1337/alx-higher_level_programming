#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0 or number < 0:
	if number > 0:
		print(f"{number}: is Positive\n")
	else:
		print(f"{number}: is Negative\n")
else:
	print(f"{number}: is Zero\n")
