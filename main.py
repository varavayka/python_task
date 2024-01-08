
def factorial(x):
    
    if x == 1:
        return x
   
    return factorial(x - 1) * x

print('Факториал:',factorial(5))


def summation(x):
    if x == 1: return x

    return summation(x - 1) + x

print('Суммирование:',summation(8))


def sum_odd(list_nums, count=0, result=[]):
    index = len(list_nums)
    
    
    if(count == index): return sum(result)
    
    if (list_nums[count] % 2) != 0:
        result.append(list_nums[count])
        # indx = list_nums.index(list_nums[count])

       
    return sum_odd(list_nums, count + 1)
        
print('Сумма  не четных:', sum_odd([1,2,3,4]))




def sum_sub(list_nums, count=0, result=[], positive_numbers=[]):
    index = len(list_nums)
    
    
    if(count == index): 
        positive = sum(positive_numbers)
        return sum(result) - positive
    
    if (list_nums[count] % 2) != 0:
      result.append(list_nums[count])
      
    else:
        positive_numbers.append(list_nums[count])
        
    
       
    return sum_sub(list_nums, count + 1)

print('Сумма нечётных чисел и вычитание чётных чисел:', sum_sub([1,2,3,4,5]) ) 



def is_palindrome(str, count=0, result= []):
    
    if len(str) == count :
        initial_state = ''.join(result)
        result.reverse()
        reverse_state = ''.join(result)
        return initial_state == reverse_state
    
    result.append(str[count])
    return is_palindrome(str, count + 1)


print('Проверка на слово палиндром:', is_palindrome('abba'))



def is_pal(str, count=0, result= []):
    str = str.replace(' ', '')
    
    if len(str) == count :
        initial_state = ''.join(result)
        result.reverse()
        reverse_state = ''.join(result)
        return initial_state == reverse_state
    
    result.append(str[count])
    return is_pal(str, count + 1)
print('проверка на слово палиндром и игнорирование пробелов:',is_pal('                  a bb a'))




def remove_vowels(str, count=0, list_result=[]):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    
    if len(str) == count:
        return ''.join(list_result)
    if not vowels.count(str[count]):
        list_result.append(str[count])
    return remove_vowels(str, count + 1)

print('Вернутся только согласные буквы:',remove_vowels('banana'))


def double(str, count=0, result=''):
    
    if len(str) == count: return result
    return double(str, count + 1, result +str[count] * 2)

print(double('zz'))




def fib(n):
    if n == 1 or n == 0: return n
    return fib(n - 1) + fib(n - 2)
    

print(fib(9))