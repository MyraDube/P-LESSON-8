def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    print(factorial._doc_)
    print("the factorial of 0:", factorial(0))