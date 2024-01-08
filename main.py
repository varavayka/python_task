
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