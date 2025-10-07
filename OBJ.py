def Change_bank():
    print("1. Barclays")
    print("2. Santander")
    print("3. Starling")
    print("4. Metro")
    print("5. Monzo")
    print("6. HSBC")
    numb = input("What should it be changed to: ")
    return numb


class AyoBetiku:
    def __init__(self, first, last, grade, bank, money):
        self.first = first
        self.last = last
        self.grade = grade
        self.bank = bank
        self.money = money

    def Target_met(self):
        self.grade = self.grade + 1

    def Target_lower(self):
        self.grade = self.grade - 1

    def bank_dsadd(self, new_bank):
        self.bank = new_bank
        print("Bank successfully changed to:", self.bank)


# Create instances
Dante123 = AyoBetiku("Dante", "Atta-Mensah", 6, "Santander", 29.70)
LittleNawur = AyoBetiku("Nawur", "Dos-Santos", 6, "Metro", 2.00)
Osi = AyoBetiku("Osi", "Chijioke", 6, "Metro", 5.20)
Neil = AyoBetiku("Neil", "Patel", 6, "Santander", 1000000000)
Joshwa = AyoBetiku("Joshwa", "John", 7, "Starling", 1)

# Select person
person = input("Whose file do you want to open? 1. Neil  2. Dante  3. Nawur  4. Osi  5. Joshwa: ")

# Validate input
while not person.isdigit() or int(person) < 1 or int(person) > 5:
    person = input("Invalid choice. Please enter a number between 1 and 5: ")

person = int(person)

# Select correct person object
if person == 1:
    selected = Neil
elif person == 2:
    selected = Dante123
elif person == 3:
    selected = LittleNawur
elif person == 4:
    selected = Osi
elif person == 5:
    selected = Joshwa

# Show class file
def ClassFile(obj):
    print("Name =", obj.first)
    print("Surname =", obj.last)
    print("Bank =", obj.bank)
    print("Money =", obj.money)
    print("Grade =", obj.grade)


# Show details
ClassFile(selected)

# Ask if want to change
ans = input("Do you want to change anything in the record? (yes/no): ").lower()
if ans == "yes":
    change = input("What do you want to change? (Bank/Grade): ").capitalize()
    if change == "Bank":
        new_bank = Change_bank()
        selected.bank_dsadd(new_bank)
    elif change == "Grade":
        action = input("Do you want to increase or decrease the grade? (+/-): ")
        if action == "+":
            selected.Target_met()
        elif action == "-":
            selected.Target_lower()
        print("Updated grade:", selected.grade)



     















