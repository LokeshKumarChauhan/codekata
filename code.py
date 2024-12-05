n = input()
even = []
odd = []  
for i in range(len(n)):
  a = int(n[i])
  if a%2==0:
    even.append(a)
  else:
    odd.append(a)
even.sort()
odd.sort()

print(*even)
print(*odd)