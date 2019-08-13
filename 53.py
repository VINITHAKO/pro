v = input().split()
v = list(set([*str("".join(v)).lower()]))
s = 0
a = "abcdefghijklmnopqrstuvxyz"
for i in v:
    if i in a:
        s += 1
if s == 25:
    print("yes")
else:
    print("no")
