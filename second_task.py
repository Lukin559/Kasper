message = input().split('|')
answer = ''.join([chr(int(i)+64) for i in message])
print(answer)
