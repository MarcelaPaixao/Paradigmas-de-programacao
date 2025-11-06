#Q1
def head(lista):
    if lista == [] or lista == '':
        return []
    else:
        return lista[0]

#Q2
def tail(lista):
    if lista == [] or lista == '':
        return []
    else:
        return lista[1:]

#Q3
def init(lista):
    if lista == [] or lista == '':
        return []
    else:
        return lista[:-1]

#Q4
def last(lista):
    if lista == [] or lista == '':
        return []
    else:
        return lista[-1]

#Q5
#def n_fibonacci(n):

#Q6
def concat_lists(l1, l2):
    if l1 == []:
        return l2
    elif l2 == []:
        return l1
    else:
        return [head(l1)] + concat_lists(tail(l1), l2)

#Q7
def is_in_list(x, l):
    if l == [] or l == '':
        return False
    elif x == head(l):
        return True
    else:
        return is_in_list(x, tail(l))

#Q8
def unite_lists(l1, l2):
    if l1 == []:
        return l2
    elif l2 == []:
        return l1    
    elif is_in_list(head(l1), l2):
        return unite_lists(tail(l1), l2)
    else:
        return [head(l1)] + unite_lists(tail(l1),l2)

#Q9
def bigger_than_n(n, l):
    if l == []:
        return 0
    elif head(l) > n:
        return 1 + bigger_than_n(n, tail(l))
    else:
        return bigger_than_n(n, tail(l))
    

#CONFERIR SE PODE USAR A Q6 ASSIM!!    
#Q10
def bigger_than_n_list(n, l):
    if l == []:
        return []
    elif head(l) > n:
        return concat_lists([head(l)], bigger_than_n_list(n, tail(l)))
    else:
        return bigger_than_n_list(n, tail(l))

<<<<<<< HEAD
#Q12
def palindrome(l):
    if l == [] or l == '':
        return []
    else:
        return concat_lists(l, list_inversion(l))
    
#Q13
def list_size(l):
    if l == [] or l == '':
        return 0
    else:
        return 1 + list_size(tail(l))

#Q14
def aux_is_prime(n, n2):
    if n == 2 or n2 == 1:
        return True
    elif n % n2 != 0:
        return aux_is_prime(n, n2-1)
    else:
        return False
def is_prime(n):
    if n <= 1:
        return False
    else:
        return aux_is_prime(n, n-1)


#Q15
#Retorna uma lista somente com os elementos de l2 que não ocorrem em l1
def strip(l1, l2):
    if l2 == [] or l2 == '':
        return []
    elif is_in_list(head(l2), l1):
        return strip(l1, tail(l2))
    else:
        return [head(l2)] + strip(l1, tail(l2))

#Q16
#FALTA FAZER


#Q17
#FALTA FAZER

#Q18
def next_prime(n):
    if is_prime(n+1) == False:
        return next_prime(n+1)
    else:
        return n+1

#Q19
def aux_primes(n, n2):
    if n2 > n or n <= 1:
        return []
    elif n%n2 == 0:
        return [n2] + aux_primes(n/n2, n2)
    else:
        return aux_primes(n, next_prime(n2))
def primes(n):
    if n <= 1:
        return []
    else:
        return aux_primes(n, 2)

#Q20
def aux_prime_factors(x, l, f):
    if l == []:
        return [(x,f)]
    elif x == head(l):
        return aux_prime_factors(x, tail(l), f+1)
    else:
        return [(x,f)] + aux_prime_factors(head(l), tail(l), 1)
    
def prime_factors(n):
    if n <= 1:
        return [()]
    else:
        return aux_prime_factors(head(primes(n)), tail(primes(n)), 1)
    
#Q21
def split_aux(x, l, b):
    if l == []:
        return [b]
    elif x != head(l):
        return split_aux(x, tail(l),  b + [head(l)])
    else:
        return [b] + split_aux(x, tail(l), [])
    
def split_token(x,l):
    if l == []:
        return []
    else:
        return split_aux(x, l, [])

#Q22
#FALTA FAZER

#Q23
def aux_split_half(l, size):
    if l == [] or size == 0:
        return []
    else:
        return [head(l)] + aux_split_half(tail(l), size - 1)

def split_half(l):
    if (list_size(l) % 2) == 0:
        return [aux_split_half(l, list_size(l)/2), list_inversion(aux_split_half(list_inversion(l), list_size(l)/2))]
    else:
        return [aux_split_half(l, (list_size(l) - 1)/2), list_inversion(aux_split_half(list_inversion(l), (list_size(l) + 1)/2))]

#Q24
def pyths(n):
    if n == 0:
        return [()]
    else:
        return [(x,y,z) for z in range(1,n+1)
                        for y in range(1, n+1)
                        for x in range(1, n+1)
                        if x*x + y*y == z*z]

#Q25
def sum_divisors(n, d):
    if n == 0 or n == d:
        return 0
    elif n%d == 0:
        return d + sum_divisors(n, d+1)
    else:
        return sum_divisors(n, d+1)

def perfects(n):
    if n <= 0:
        return []
    else:
        return [x for x in range(1, n+1) if x == sum_divisors(x, 1)]

#Q26
def scalar_product(l1, l2):
    if l1 == [] or l2 == []:
        return 0
    else:
        return sum([x*y for x,y in zip(l1,l2)])

#Q27
#FALTA FAZER

#Q28
def is_palindrome(s):
    if s == '':
        return False
    else:
        # Aplicação de list_inversion dos dois lados porque não dá para comparar lista com string
        return list_inversion(s) == list_inversion(list_inversion(s))

#Q29
def aux_compress(x, l):
    if l == []:
        return [x]
    elif x == head(l):
        return aux_compress(x, tail(l))
    else:
        return [x] + aux_compress(head(l), tail(l))

def compress(l):
    if compress == []:
        return []
    else:
        return aux_compress(head(l), tail(l))

#Q30
def aux_pack(l, b):
    if l == [] and b == []:
        return []
    elif l == [] and b != []:
        return [b + [head(l)]]
    elif head(l) == head(tail(l)):
        return aux_pack(tail(l), b + [head(l)])
    elif b != []:
        return [b + [head(l)]] + aux_pack(tail(l), [])
    else:
        return [head(l)] + aux_pack(tail(l), [])

def pack(l):
    if l == []:
        return []
    else:
        return aux_pack(l, [])

#Q31
def aux_encode(string, f):
    if string == '':
        return []
    elif head(string) == head(tail(string)):
        return aux_encode(tail(string), f+1)
    else:
        return [(f, head(string))] + aux_encode(tail(string), 1)

def encode(string):
    if string == '':
        return []
    else:
        return aux_encode(string, 1)

#Q32
def decode(list):
    if list == []:
        return ''
    else:
        return head(list)[1] * head(list)[0] + decode(tail(list))

# print(n_fibonacci(5))
# print(is_prime(int(input())))
# print(palindrome('abcd'))
# print(strip([1,2,3,4,5], [1,2,5,7,8,1,1,1]))
# print(strip('sdd', 'saude'))

# print(consoant_list('sdd', 'saude'))
# print(consoant_list(['s','d','d'], 'saude'))
# print(consoant_list(['s','d','d'], 'saudade'))

# print(next_prime(int(input())))
# print(primes(int(input())))
# print(prime_factors(int(input())))
# print(split_half([1,2,3,4,5,6,7]))
# print(split_token(2, [1,2,3,4,2,5,67,8,9,0,3]))
# print(pyths(5))
# print(perfects(500))
# print(scalar_product([1,2,3], [4,5,6]))
# print(is_palindrome('azul'))
# print(compress([1,2,2,3,4,4,4,5]))
# print(encode('aaaabccaadeeee'))
# print(decode([(4, 'a'), (1, 'b'), (2, 'c'), (2, 'a'), (1, 'd'), (4, 'e')]))
=======
print(bigger_than_n_list(2, [1,2,3,4]))
>>>>>>> parent of cc2a5e7 (completo até q14)
