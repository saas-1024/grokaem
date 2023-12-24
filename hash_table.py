book = dict()

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49
print(book)
print(book["avocado"])

print("Let's make phonebook")

phone_book = {}
phone_book["Autumn Girl"] = 88005553535
phone_book["Kurwa matka"] = 88273667221
phone_book["Black sea"] = 46228923

print(phone_book["Black sea"])
print(phone_book)

voted = {}


def check_voter(name):
    if voted.get(name):
        print("Kick them out!")
    else:
        voted[name] = True
        print("Let them vote!")


check_voter("Mike")
check_voter("Tommy")
check_voter("Obama")
check_voter("Mike")
