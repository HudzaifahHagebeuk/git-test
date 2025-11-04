a = 17
b = 23
print ( "a =", a, "en b =", b )
a += b #hier staat a = a + b, dus a = 40
#b moet 17 worden, dus de nieuwe b = a - b
b = a - b
#nu moet a 23 worden, dus a - b, a -= b is hetzelfde als a = a - b
a -= b 

print ( "a =", a, "en b =", b ) #dit is hetzelfde als..

print ( "a =", a,
        "en b =", b ) #en dit is ook hetzelfde als..

print(
    "a ="
    , a,
    "en b ="
    , b
)