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
    if l == []:
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
    
print(is_prime(int(input())))
print(palindrome('abcd'))
print(list_size([1,2,3,4,5,6]))