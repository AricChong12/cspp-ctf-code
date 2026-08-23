scrambled = "ctrs{wkcmacp_gvt_wmgwoell}"

flag = ""

for i, c in enumerate(scrambled):
    if 'a' <= c <= 'z':
        # Reverse: (index(c) - i) mod 26
        flag += chr((ord(c) - ord('a') - i) % 26 + ord('a'))
    else:
        flag += c

print(flag)