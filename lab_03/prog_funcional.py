#Q1
def head(lista):
    return lista[0]

#Q2
def tail(lista):
    return lista[1:]

#Q3
def init(lista):
    return lista[:-1]

#Q4
def last(lista):
    return lista[-1]

#Q5
def n_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n_fibonacci(n-1) + n_fibonacci(n-2)

#Q6
def concat_lists(l1, l2):
    if l1 == [] or l1 == '':
        return l2
    elif l2 == [] or l2 == '':
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
    
#Q10
def bigger_than_n_list(n, l):
    if l == []:
        return []
    elif head(l) > n:
        return concat_lists([head(l)], bigger_than_n_list(n, tail(l)))
    else:
        return bigger_than_n_list(n, tail(l))
    
#Q11
def list_inversion(l):
    if l == [] or l == '':
        return []
    else:
        return concat_lists(list_inversion(tail(l)), [head(l)])

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
def is_consonant(x):
    if x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u':
        return True
    else:
        return False

#Retorna uma lista com somente os elementos em comum entre l1 e l2
def inverse_strip(l1, l2):
    if l2 == [] or l2 == '':
        return []
    elif is_in_list(head(l2), l1):
        return [head(l2)] + inverse_strip(l1, tail(l2))
    else:
        return inverse_strip(l1, tail(l2))

def consoant_list(l1, l2):
    if l2 == [] or l2 == '' or l1 == [] or l1 == '':
        return False
    elif l1 == inverse_strip(l1,l2):
        return True
    else:
        return False
    # elif head(l1) != head(inverse_strip(l1,l2)):
    #     return False
    # else:
    #     return consoant_list(tail(l1), tail(inverse_strip(l1,l2)))


#Q17
#def matches(l1, l2):

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

# print(is_prime(int(input())))
# print(palindrome('abcd'))
# print(list_size([1,2,3,4,5,6]))
# print(strip([1,2,3,4,5], [1,2,5,7,8,1,1,1]))
# print(strip('sdd', 'saude'))

# print(consoant_list('sdd', 'saude'))
# print(consoant_list(['s','d','d'], 'saude'))
# print(consoant_list(['s','d','d'], 'saudade'))

# print(next_prime(int(input())))
# print(primes(int(input())))
# print(prime_factors(int(input())))
print(split_half([1,2,3,4,5,6,7]))