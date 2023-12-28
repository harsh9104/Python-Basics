#precedence Order
"""
"OPERATORS"                                           "Meaning"
 ()                                                    Parentheses   
 **                                                    Exponent
 +x, -x, ~x                                            Unary plus, Unary minus, Bitwise NOT 
 *, /, //, %                                           Mulotiplication, Division, Floor division, Modulus
 +, -                                                  Addition, Subtraction
 <<, >>                                                Bitwise shift operator  
 &                                                     Bitwise AND
 ^                                                     Bitwise XOR
 |                                                     Bitwise OR
 ==, !=, >, >=, <, <=, is, is not, in, not in          Comparisons, Identity, Membership operators 
 not                                                   Logical NOT
 and                                                   Logical AND    
 or                                                    Logical OR
"""
result = 3 + 5 ** 2 / 5 % 2
print(result)

print(not 3 > 4)
