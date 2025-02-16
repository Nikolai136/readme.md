import smartphone 

def main():
    catalog = [
    smartphone.Smartphone("Apple", "iPhone 14 Pro Max", "+79111234567"),
    smartphone.Smartphone("Samsung", "Galaxy S23 Ultra", "+79222345678"),
    smartphone.Smartphone("Google", "Pixel 7 Pro", "+79333456789"),
    smartphone.Smartphone("OnePlus", "10T", "+79444567890"),
    smartphone.Smartphone("Xiaomi", "13 Ultra", "+79555678901")
]

    for phone in catalog:
        print(f"{phone.brandPhone}, {phone.modelPhone}, {phone.numberPhone}")

main()

