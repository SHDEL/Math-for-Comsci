from sys import getsizeof

float_a = 0.2
float_b = 0.1

print("size_a: ",getsizeof(float_a))
print("size_b: ", getsizeof( float_b))

print("----บวก----")
float_c = float_a + float_b
print(float_c)
print("size_c: ", getsizeof( float_c))

print("----ลบ----")
float_c = float_a - float_b
print(float_c)
print("size: ", getsizeof( float_c))

print("----คูณ----")
float_c = float_a * float_b
print(float_c)
print("size: ", getsizeof( float_c))

print("----หาร----")
float_c = float_a / float_b
print(float_c)
print("size: ", getsizeof( float_c))