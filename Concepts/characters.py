# chr() and ord() functions allow us to revert characters to their code point values
# as well as revert code point values to the associated characters
# Code point values being the character numbers being referenced
print(ord("A"))
print(chr(65))
# The hex() function allows us to obtain a hexadecimal representation of a decimal integer
print(hex(65))
# The chr() function can also be used here to revert the character back to its reference character
# chr() will takes the unicode code point value being referenced by the hexadecimal representation
# and give the character that unicode point value references
print(chr(0x41))
# don't use "" marks around the chr input, it needs to be an integer
# Hexadecimal numbers can be used to print special characters with chr()
print(chr(0x4EBA))
# They can also be inserted into strings with chr()
s = "Just add your character: " + chr(0x4EBA) + " ..into the string"
print(s)
# ord() can still be used on glyphs
# hex() cannot, as hex() only takes integers
print(ord('人'))
print(hex(20154))

# You can use chr() on the code point value or hexadecimal value to get the character
print(chr(20154))
print(chr(0x4eba))

# Translation tables are dictionaries
# The difference being that translation tables can be more readily used to replace characters in a string
intab = "taeo"
outtab = "7430"
trantab = str.maketrans(intab, outtab)
s = "Letters in this string will be replaced with the corresponding numbers"
s2 = s.translate(trantab)
print(s2)
