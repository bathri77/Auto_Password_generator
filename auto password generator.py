import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "[]{}():;+/-_<>,"

all = lower+upper+numbers+symbol

length = 8

password = "".join(random.sample(all, length))

print(password)
