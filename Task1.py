#Task1
#The Collatz conjecture1 is a famous unsolved problem in mathematics. The problem is to prove that if you start with any positive integer x and repeatedly apply the function f(x) below, you al ways get stuck in the repeating sequence 1, 4, 2, 1, 4, 2, . . .
#f(x) =
#x ÷ 2 if x is even
#3x + 1 otherwise
#For example, starting with the value 10, which is an even number, we divide it by 2 to get 5. Then 5 is an odd number so, we mul tiply by 3 and add 1 to get 16. Then we repeatedly divide by 2 to get 8, 4, 2, 1. Once we are at 1, we go back to 4 and get stuck in the repeating sequence 4, 2, 1 as we suspected.
#Your task is to verify, using Python, that the conjecture is true for the first 10,000 positive integers
def Collatz(n):
    out=[n]
    while n>1:
        if n%2==0:
           n = n//2
        else:
            n = (n*3)+1
        out.append(int(n))
    return out
#https://realpython.com/python-boolean/
true = []
false = []

#altering code for task
for i in range(1,10000): 
    Verif = Collatz(i) #https://www.freecodecamp.org/news/python-for-loop-for-i-in-range-example/ 
    if_true = Verif [-1] == 1
    if if_true: true.append(i)
    else: false.append(i)

print("Collatz conjecture is true:", true)
print("Collatz conjecture is false:", false)


    