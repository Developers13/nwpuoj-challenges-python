from fractions import Fraction
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(f"({a}/{b})+({c}/{d})={Fraction(a,b)+Fraction(c,d)}")
print(f"({a}/{b})-({c}/{d})={Fraction(a,b)-Fraction(c,d)}")
print(f"({a}/{b})*({c}/{d})={Fraction(a,b)*Fraction(c,d)}")
print(f"({a}/{b})/({c}/{d})={Fraction(a,b)/Fraction(c,d)}")