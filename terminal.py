import random
if random.randint(0,1) == 1:
    phrase = "Number Required: " + str(random.randint(1,5))
else:
    phrase = "This is a garbage string"
print(phrase)


def parse(string):
    string.endswith("Number Required: ")


