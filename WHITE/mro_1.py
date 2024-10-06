#MRO Algorithm Demo Program
#Mro(x)=x+Merge(Mro(p1),Mro(p2)....,Parent List))
class A:
    pass
class B:
    pass
class C:
    pass
class D(A,B):
    pass
class E(B,C):
    pass
class F(D,E,C):
    pass
print(F.mro())

