n_terms = int(input("ENTER NUMBER:"))

n1 = 0
n2 = 1
count = 0

print("Fibonacci sequence upto",n_terms,":")
while count < n_terms:
    print(n1, end=',')
    nth  = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

print()
