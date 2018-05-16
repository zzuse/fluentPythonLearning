q = 459
p = 0.098
print(p,q,p*q)
print(p,q,p*q,sep='--')
#%[flags][width][.precision]type
print("art = %5d, per unit=%8.2f" % (425,33.2))
print("%10.3e"% (356.08977))
print("%10.3E"% (356.08977))
print("%10o"% (25))
print("%10.3o"% (25))
print("%10.5o"% (25))
print("%5x"% (47))
print("%5.4x"% (47))
print("%5.4X"% (47))
print("Only one percentage sign: %% " % ())
print("-------------flags-----------")
print("%#5X"% (47))
print("%#5.4X"% (47))
print("%#5o"% (25))
print("%+d" % (42))
print("% d"% (42))
print("%2d"% (42))
print("%-2d"% (42))
s = "Price: $ %8.2f"% (356.08977)
print(s)
print("---------format(...)S.format(*args, **kwargs) -> str----")
print("First argument: {0}, second one: {1}".format(47,11))
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42,11))
print("First argument: {}, second one: {}".format(47,11))
print("various precisions: {0:6.2f} or {0:6.3f}".format(1.4148))
print("Art: {a:5d},  Price: {p:8.2f}".format(a=453, p=59.058))
print("{0:<20s} {1:6.2f}".format('Spam & Eggs:', 6.99))
print("{0:>20s} {1:6.2f}".format('Spam & Eggs:', 6.99))
print("The value is {:06d}".format(-368))
print("The value is {0:6,d}".format(1234567890))
print("The value is {0:12,.3f}".format(5897653423.89676))

print("-----------dictionary------------------")
print("The capital of {0:s} is {1:s}".format("Ontario","Toronto"))
print("The capital of {province} is {capital}".format(province="Ontario",capital="Toronto"))
data = dict(province="Ontario",capital="Toronto")
print("The capital of {province} is {capital}".format(**data))
capital_country = {"United States" : "Washington",
                   "US" : "Washington",
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

print("Countries and their capitals:")
for c in capital_country:
    print("{country}: {capital}".format(country=c, capital=capital_country[c]))

print("Countries and their capitals:-----")
for c in capital_country:
    format_string = c + ": {" + c + "}"
    print(format_string)
    print(format_string.format(**capital_country))

s = "Python"
print(s.center(20,"*"))
print(s.ljust(12,":"))
print(s.rjust(15, "~"))
account_number = "43447879"
print(account_number.zfill(12))
print(account_number.rjust(12,"0"))
price = 11.23
print(f"Price in Euro: {price}")
print(f"Price in Swiss Franks: {price * 1.086}")
print(f"Price in Swiss Franks: {price * 1.086:5.2f}")
for article in ["bread", "butter", "tea"]:
    print(f"{article:>10}:")