from prettytable import PrettyTable
# a,b=2740,1760
# a=int(input("Enter the first number : "))
# b=int((input("Enter the second Number : ")))
a,b=23,100
r1,r2,rem,q,t1,t2,t=a,b,0,0,0,1,0
table = PrettyTable(title="Extended Euclidean Alogrithm 2 determine multplicative inverse")
table.field_names=['Quotient','Num1','Num2','REM','T1','T2','T']
if b > a:
    r1, r2 = r2,r1
while(r2>0):
    rem, q = r1 % r2, r1 // r2
    t=t1-q*t2
    table.add_row([q, r1, r2,rem,t1,t2,t])
    r1,r2,t1,t2,q,t=r2,rem,t2,t,rem,rem
    if r2==0:
        #q=r2
        table.add_row([q, r1, r2, rem, t1, t2, t])
        break
print(f'{table} \ng.c.d({max(a,b)},{min(a,b)}) = {r1}')

if r1==1:
    print(f'=> {a} and {b} have  a multplicative inverse for {min(a,b)} in set Z {max(a,b)}\n=> Multplicative inverse is : {t1}')
else:
    print(f'=> {a} and {b} have no multplicative inverse for {min(a,b)} in set Z {max(a,b)}')