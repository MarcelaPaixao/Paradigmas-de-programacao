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
    

#CONFERIR SE PODE USAR A Q6 ASSIM!!    
#Q10
def bigger_than_n_list(n, l):
    if l == []:
        return []
    elif head(l) > n:
        return concat_lists([head(l)], bigger_than_n_list(n, tail(l)))
    else:
        return bigger_than_n_list(n, tail(l))

print(bigger_than_n_list(2, [1,2,3,4]))