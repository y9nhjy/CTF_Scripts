import base64

s = bytearray(b'GQTZlSqQXZ/ghxxwhju3hbuZ4wufWjujWrhYe7Rce7ju')
old_table = bytearray(b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
new_table = bytearray(b'+/EFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABCD')

b64_dict = {ord('='): ord('=')}
for i in range(len(old_table)):
    b64_dict[new_table[i]] = old_table[i]

for i in range(len(s)):
    s[i] = b64_dict[s[i]]
print(base64.b64decode(s.decode()).decode("utf-8", "ignore"))

# 不可见字符
# an = []
# for i in base64.b64decode(s):
#     an.append(i)
