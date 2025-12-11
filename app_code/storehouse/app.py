from .store import InventoryService, ProductNotFound

def main():
    service = InventoryService()
    while True:
        print("\n=== Қоймадағы тауар қозғалысы ===")
        print("1. Тауар қосу")
        print("2. Қозғалысты тіркеу")
        print("3. Қойма қалдығы")
        print("4. Барлық қозғалыстар")
        print("0. Шығу")
        choice = input("Таңдаңыз: ")

        try:
            if choice == '1':
                name = input("Тауар атауы: ")
                code = input("Коды: ")
                weight = float(input("Салмағы (кг): "))
                service.add_product(name, code, weight)
                print("✅ Тауар қосылды!")

            elif choice == '2':
                code = input("Тауар коды: ")
                qty = int(input("Саны: "))
                direction = input("Бағыт (in/out): ")
                service.register_movement(code, qty, direction)
                print("✅ Қозғалыс тіркелді!")

            elif choice == '3':
                stock = service.get_stock()
                for item in stock:
                    print(f"{item['code']} - {item['name']}: {item['quantity']}")

            elif choice == '4':
                for m in service.get_movements():
                    print(m.__dict__)

            elif choice == '0':
                break

            else:
                print("❌ Қате таңдау!")

        except ProductNotFound as e:
            print(f"❌ Қате: {e}")
        except ValueError:
            print("❌ Сан енгізуде қате!")
        except Exception as e:
            print(f"❌ Белгісіз қате: {e}")

if __name__ == "__main__":
    main()
