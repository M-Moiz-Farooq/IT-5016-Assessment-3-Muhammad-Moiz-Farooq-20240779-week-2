txt="    python    "
print(len(txt))
result=txt.strip()
print(len(result))
txt2=".....rtgf ......python..... rtgf..." 
r=txt2.strip('.rtgf')
print(r)
r2=txt2.lstrip('.rtgf')
print(r2)
r3=txt2.rstrip('.rtgf')
print(r3)
print(txt2.split())