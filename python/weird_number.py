


def weird_number(n):

    c = 0

    while(n!=1 or c==0):

        print (int(n), end = " ")

        if n % 2 == 0: 
            n = n /2 
        elif n%2 !=0 : 
            n = 3*n + 1
        
        if n == 1 and c!=0:
            print(int(n), end = " ")
            return
        
        c+=1
        
        

if __name__ == '__main__':
    
    weird_number(n)
