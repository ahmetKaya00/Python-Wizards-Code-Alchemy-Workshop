class Order:
    def __init__(self,customer,cart):
        self.customer = customer
        self.cart = cart
        self.total_amount = cart.get_total()
    
    def place_order(self):
        if self.total_amount > 0:
            print(f"\nSiparişiniz başarıyla oluşturuldu: ")
            print(self.customer)
            print("\nSipariş detayları:")
            self.cart.display_cart()
            print(f"Toplam Tutar: {self.total_amount} TL")
        else:
            print("\n Sepet boş, siparişiniz oluşturulamadı!")