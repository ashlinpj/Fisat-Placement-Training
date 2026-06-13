s = "aaaabbbbcccaa"

new = ""
now = s[0]
count = 0

for i in range(len(s)):
    if s[i] == now:
        count += 1
    else:
        new += now + str(count)
        now = s[i]
        count = 1

new += now + str(count)   # Add the last group

print(new)