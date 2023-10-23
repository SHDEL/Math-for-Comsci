from sys import getsizeof
from decimal import Decimal

dec_a = Decimal('0.2')
dec_b = Decimal('0.1')
print("size a :", getsizeof(dec_a))
print("size b :", getsizeof(dec_b))

print("----บวก----")
dec_c = dec_a + dec_b
print(dec_c)
print("size c :", getsizeof(dec_c))

print("----ลบ----")
dec_c = dec_a - dec_b
print(dec_c)
print("size c :", getsizeof(dec_c))

print("----คูณ----")
dec_c = dec_a * dec_b
print(dec_c)
print("size c :", getsizeof(dec_c))

print("----หาร----")
dec_c = dec_a / dec_b
print(dec_c)
print("size c :", getsizeof(dec_c))