num = 0
gum = 0

i = range(1,100)
for n in i:
    for k in i:
        if (n < (4*k*k)):
            sum = (4*k*k - n)**0.5
            if( ( sum%1 == 0)): # and (k>sum)):
                x1 = k + sum
                x2 = k - sum
                eq1 = (x1+2*k)**2 - (x1+k)**2 - x1**2
                eq2 = (x2+2*k)**2 - (x2+k)**2 - x2**2
             '''   if( ( (eq1 == n) | (eq2 == n) ) ): # & ( ( x1 > 0) & (x2 >0 ) ) ):
                    print("eq1 sequence :")
                    print(x1+2*k,x1+k,x1,n,"increment:",k, "valid:",(eq1 ==n))
                    print("eq2 sequence :")
                    print(x2+2*k,x2+k,x2,n,"increment:",k , "valid:",(eq1 ==n))
                    num = num+1
                    print("num:",num) '''
                if( ( (eq1 == n) | (eq2 == n) )  & ( ( x1 < 0) | (x2  <0 ) ) ):
                    print("eq1 sequence :")
                    print(x1+2*k,x1+k,x1,n,"increment:",k, "valid:",(eq1 ==n))
                    print("eq2 sequence :")
                    print(x2+2*k,x2+k,x2,n,"increment:",k , "valid:",(eq1 ==n))
                    gum = gum+1
                    print("gum:",gum)

                    

