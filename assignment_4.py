# Assignment:
# Create a class Bank with a class variable bank_name.
# Add a class method change_bank_name(cls, name) that allows changing the bank name.
# Show that it affects all instances.


class Bank:
    bank_name = "HABIB"


    @classmethod
    def change_bank_name(cls , name ):
        cls.bank_name = name


bank1 = Bank()

bank1.change_bank_name("BANK OF ISLAM")


print(Bank.bank_name)