from prettytable import PrettyTable
a=161
b=28
# a=int(input("Enter the first number : "))
# b=int((input("Enter the second Number : ")))

r1,r2,s1,s2,t1,t2=a,b,1,0,0,1
q,r,s,rem=0,0,0,0

table=PrettyTable(title="Extended Eculidean Alogrithm")
table.field_names=['Quot','Num1','Num2','REM','S1','S2','T1','T2','T']
if b > a:
    r1, r2 = r2, r1
while(r2>0):
    rem, q, s,t= r1 % r2, r1 // r2,s1-q*s2,t1-q*t2
    table.add_row([q, r1, r2,rem, s1, s2, t1, t2, t])
    r1,r2,t1,t2,s1,s2,q=r2,rem,t2,t,s2,s,rem
    if r2==0:
        table.add_row([q, r1, r2,rem, s1, s2, t1, t2, t])
        break
print(f'{table} \n g.c.d({a},{b}) = {r1}\n a:{a} , b:{b} , t:{t1} , s:{s1}')