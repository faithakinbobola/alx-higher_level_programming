#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print (f"0{i}".format(), end=',')
    else:
        print(f"{i}".format(), end=',')