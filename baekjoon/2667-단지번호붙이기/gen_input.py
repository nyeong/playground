#!/usr/bin/env python
from random import choice

n = 25
print(n)
for _ in range(n):
	str = ''
	for _ in range(n):
		str += f'{choice([0, 1])}'
	print(str)
