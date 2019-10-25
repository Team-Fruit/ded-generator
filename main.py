# -*- coding: utf-8 -*-

ded = input("ded man:")
obj = input("object:")

print("")
print("----")
print("")

print("30日夜、果実都某所で、 :{0}: に埋もれてdedしている :{1}: が発見された。".format(obj, ded))

print("")

for i in range(0, 4):
    l = ""
    for j in range(0, 7):
        if i is 3:
            if j is 3:
                l += ":{0}: ".format(ded)
                continue

        l += ":{0}: ".format(obj)
    print(l)
