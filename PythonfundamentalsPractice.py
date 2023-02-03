import math
import random 

def problem1(x, y, z):

    mean = (x + y + z)/3

    L = [x, y, z]
    L.sort()
    median = L[1]

    return mean, median

def problem2(x):

    num = x
    

    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:  
        return True

    else:
        return False


#calculate

    
def problem3(nums):

    min_value = min(nums)
    max_value = max(nums)
    range_of_values = max_value - min_value

    return min_value, max_value, range_of_values

random_numbers = [random.randint(1, 50) for i in range(10)]

min_value, max_value, range_of_values = problem3(random_numbers)


#def problem4(x, y):

    #L =[]
    #h = math.sqrt(x**2 + y**2)

def problem5(word, multiplier=1):
    score = 0
    letters = list(word.upper())
    for letter in letters:
        if letter in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']:
            score += 1
        elif letter in ['D', 'G']:
            score += 2
        elif letter in ['B', 'C', 'M', 'P']:
            score += 3
        elif letter in ['F', 'H', 'V', 'W', 'Y']:
            score += 4
        elif letter == ['K']:
            score += 5
        elif letter in ['J', 'X']:
            score += 8
        elif letter in ['Q', 'Z']:
            score += 10
    return score * multiplier




  

def main():
    print("problem 1")
    print(problem1(5, 10, 42))
    mean, median = problem1(44, 123, -5)
    print(mean)
    print(median)
    print(" ")
    
    
    print("problem 2")
    x = random.randint(1, 100)
    print(x)
    print(problem2(x))
    print(" ")

    print("problem 3")
    print("random #'s:", random_numbers)
    print("minimum", min_value)
    print("maximum", max_value)
    print("range of values", range_of_values)
    print(" ")


    




    x = 3
    y = 3


    
    h = math.sqrt(x*x + y*y)

    angle = math.asin(y/h)
    print(angle)

    

    



if __name__ == "__main__":
    main()
