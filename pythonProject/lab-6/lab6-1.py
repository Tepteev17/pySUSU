a = bool(int(input('a: ')))
b = bool(int(input('b: ')))
c = bool(int(input('c: ')))

# x1 = a or b and c
# x2 = False
#
# if b:
#     if c:
#         x2 = True
#     else:
#         if a:
#             x2 = True
#         else:
#             x2 = False
# else:
#     if a:
#         x2 = True
#     else:
#         x2 = False
# print(x1)
# print(x2)
x1 = a and b or not a and c
if a:
   x2 = b
else:
   x2 = c

print(x1)
print(x2)

