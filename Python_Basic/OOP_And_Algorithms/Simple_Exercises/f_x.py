
def f(x):
    response = 0

    for i in range(1000):
        response += 1

    for i in range(x):
        response += 1

    for i in range(x):
        for j in range(x):
            response += 1
            response += 1
    return response

if __name__=='__main__':
    print(f(100))
            
        
        
        