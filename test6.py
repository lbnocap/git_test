def find_prime_number(n,m):
    if isinstance(n,int) and isinstance(m,int):
        if m <= 1:
           return "error"
        if 1 >=n > m:
            return "error"
        numbers=list()
        num=n
        while num<=m:
           i=2
           while i<num:
            if (num%i==0) and (num!=i):
                break
            else:
               i=i+1
           if num==i:
               numbers.append(num)
           num=num+1
        return numbers
    else:
        return "error"

print(find_prime_number(1,100))