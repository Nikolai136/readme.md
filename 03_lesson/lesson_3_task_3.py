from mailing import Mailing
from address import Address

def main():

    from_address = Address("123456", "Москва", "Центральная улица", "12", "34")
    to_address = Address("654321", "Санкт-Петербург", "Невский проспект", "5", "78")

    mailing = Mailing(to_address, from_address, 500, "AB123456789")

    print(mailing)

if __name__ == "__main__":
    main()