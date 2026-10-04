# Sample
# Arthimetic Operator ( + - * / // % **)
print (5 + 3) #8
# / always give float value
print (7/3) #2.33
print(7-3) #4
# // divides and rounds down to nearest integer
print (7//2) #3
print(7*2) #14
# % modulus returns the remainder after devision
print(7%3) #1
#exponentiation(**) raises left to the power of right
print(2**10) #1024

#comparasion(relational) operator
#basic comparisons
print(10==10) # -> True (equal to)
print(10 != 5) # -> True (not equal to)
print(10 > 20) # -> False (greater then)
print (10<12 ) # -> True ( less then)
print(5>=5) # -> True ( greater then equal to)
print(6<=6 ) #-> falsse ( less then equal to)

#Assignment operators
score = 50 #stores value in variable
score += 10 #score is now 60( add to variable and store)
score *= 2 #score is now 120(multiply and store back)
score -= 20 #score is now 100( subtract and store back)
score /= 200 #score is now 100(divide and store back )
score //= 200 #score is now 100(floor divide and store back)
score%= 1000 #score is now 10( take modulus and store back )
score **= 1 #score is now 10(raise to power and store back)

#Logical Operators
# and — both conditions must be True
age = 20
has_id = True
print(age >= 18 and has_id) # → True (both conditions satisfied)
# or — at least one condition must be True
is_student = True
is_teacher = False
print(is_student or is_teacher) # → True (one is True)
# not — inverts the boolean value
print(not True) # → False
print(not False) # → True
# Short-circuit with 'and' — right side skipped if left is False
print(False and 1/0) # → False (no ZeroDivisionError!)
# Short-circuit with 'or' — right side skipped if left is True
print(True or 1/0) # → True (no ZeroDivisionError!)
# Combining logical operators with comparison operators
marks = 72
print(marks >= 40 and marks <= 100) # → True (valid score range)
print(marks < 40 or marks > 100) # → False (not out of range)

#Bitwise operators
# bin() shows the binary representation of any number
print(bin(5)) # → 0b101
print(bin(3)) # → 0b11
# AND — 1 only where both bits are 1
print(5 & 3) # → 1 (0101 & 0011 = 0001)
# OR — 1 where either bit is 1
print(5 | 3) # → 7 (0101 | 0011 = 0111)
# XOR — 1 where bits are different
print(5 ^ 3) # → 6 (0101 ^ 0011 = 0110)
# Left shift — multiply by powers of 2
print(5 << 1) # → 10 (5 × 2)
print(5 << 2) # → 20 (5 × 4)
# Right shift — divide by powers of 2
print(20 >> 1) # → 10 (20 ÷ 2)
print(20 >> 2) # → 5 (20 ÷ 4)


#membership and identity operators
# Membership — checking if a value exists in a sequence
print("py" in "python") # → True
print("Java" in "python") # → False
print("z" not in "hello") # → True
# Identity — == checks value equality, is checks object identity
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b) # → True (same values)
print(a is b) # → False (different objects in memory)
print(a is c) # → True (same object — c points to a)
# The correct way to check for None — always use 'is'
x = None
print(x is None) # → True ✅ correct
print(x == None) # → True ⚠️ works but not recommended

#precedence in practice
# * before + (same as BODMAS)
print(2 + 3 * 4) # → 14 (* before +)
print((2 + 3) * 4) # → 20 (parentheses first)
# ** is right to left
print(2 ** 3 ** 2) # → 512 (2 ** (3 ** 2) = 2 ** 9)
print((2 ** 3) ** 2) # → 64 (different result with brackets!)
# Comparison before logical operators
print(5 > 3 and 2 < 4) # → True (comparisons first, then and)
print(not True or True) # → True (not binds tighter than or)
# When unsure — always use parentheses for clarity
result = (5 + 3) * (10 - 4)
print(result) # → 48 (clear and unambiguous)
