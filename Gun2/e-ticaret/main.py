import sys
from product import Product
from customer import Customer
from cart import Cart
from order import Order

def main():
    products = [
        Product("Laptop",15000,10),
        Product("Telefon",10000,10),
        Product("Kulaklık",1500,10),
    ]

    name = input("Adınızı girin: ")
    email = input("E-postanızı girin: ")
    customer = Customer(name,email)

    cart = Cart()

    while True:
        print("\nÜrünler")
        for i, product in enumerate(products):
            print(f"{i+1}. {product}")
        
        print("\nYapmak İstediğiniz İşlemi Seçiniz:")
        print("1. Ürün Ekle")
        print("2. Ürün Çıkar")
        print("3. Sepeti Görüntüle")
        print("4. Siparişi Tamamla")
        print("5. Çıkış")

        choice = input("Seçimizi yapın: ")

        if choice == "1":
            try:
                product_index = int(input("Hangi ürünü eklemek istiyorsun (Numara):")) - 1
                if 0<=product_index < len(products):
                    quantity = int(input("Kaç adet eklemek istiyorsunuz ?: "))
                    cart.add_product(products[product_index],quantity)
                else:
                    print("Geçersiz ürün numarası!")
            except ValueError:
                print("Geçersiz giriş, tekrar deneyin.")
        
        elif choice == "2":
            product_name = input("Çıkarmak istediğiniz ürünün adını yazın:")
            cart.remove_product(product_name)
            print(f"{product_name} sepetten çıkarıldı.")
        
        elif choice == "3":
            print("\nSepetiniz")
            cart.display_cart()
            print(f"Toplam Tutar: {cart.get_total()} TL")

        elif choice == "4":
            order = Order(customer,cart)
            order.place_order()
        
        elif choice == "5":
            print("Uygulama kapanıyor...")
            sys.exit()
        
        else:
            print("Geçersiz seçim, tekrar deneyin!")

if __name__ == "__main__":
    main()
