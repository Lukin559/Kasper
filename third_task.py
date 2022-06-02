alphabet = "qwertyuiopasdfghjklzxcvbnm_{}1234567890"
key = input()
data = input()

answer = ''
n = 0
for s in data:
    answer += alphabet[(alphabet.find(key[n % len(key)]) + alphabet.find(s)) % len(alphabet)]
    n += 1

print(answer)