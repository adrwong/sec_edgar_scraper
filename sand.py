string1 = 'Hello'
string2 = 'hello'

if string1.casefold() == string2.casefold():
    print("The strings are the same (case insensitive)")
    print(string1.casefold())
    print(string2.casefold())
else:
    print("The strings are NOT the same (case insensitive)")