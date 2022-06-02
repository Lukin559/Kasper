message = input().split('|')
answer = ''.join([chr(int(i)+1071) for i in message])
print(answer)
