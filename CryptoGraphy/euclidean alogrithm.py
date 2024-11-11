from prettytable import PrettyTable
# a,b=2740,1760
# a=int(input("Enter the first number : "))
# b=int((input("Enter the second Number : ")))
a,b=25,60
r1,r2,rem,q=a,b,0,0

table = PrettyTable(title="Euclidean Alogrithm")
table.field_names=['Quotient','Num1','Num2','Rem']
while(r2>0):
    rem, q = r1 % r2, r1 // r2
    table.add_row([q, r1, r2, rem])
    r1,r2,q=r2,rem,rem
    if r2==0:
        #q=r2
        table.add_row([q, r1, r2, rem])
        break
print(f'{table} \ng.c.d({a},{b}) = {r1}')
