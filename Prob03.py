x = int(input())
factorial = []
twonums=[9999,9999]
for i in range(1, x + 1):
  if x % i == 0:
    factorial.append(i)
for i in factorial:
  idx = (factorial.index(i))+1
  num2 = factorial[-idx]

  if twonums[0]+twonums[1] > i+num2:
    twonums[0] = i
    twonums[1] = num2
print(twonums[0]+twonums[1])