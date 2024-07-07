from datetime import datetime, timedelta

class Invoice:
    def __init__(self, seller_info, buyer_info, invoice_details, items, payment_terms, payment_methods, notes):
        self.seller_info = seller_info
        self.buyer_info = buyer_info
        self.invoice_details = invoice_details
        self.items = items
        self.payment_terms = payment_terms
        self.payment_methods = payment_methods
        self.notes = notes

    def generate_invoice(self):
        print("")
        print("=============================================================")
        print("|                        INVOICE                            |")
        print("=============================================================")
        print("")

        print("Seller's Information:")
        print(f"Name: {self.seller_info['name']}")
        print(f"Address: {self.seller_info['address']}")
        print(f"Contact Number: {self.seller_info['contact_number']}")
        print(f"Email: {self.seller_info['email']}")
        print("")

        print("Buyer's Information:")
        print(f"Name: {self.buyer_info['name']}")
        print(f"Address: {self.buyer_info['address']}")
        print(f"Contact Number: {self.buyer_info['contact_number']}")
        print(f"Email: {self.buyer_info['email']}")
        print("")

        print("Invoice Details:")
        print(f"Invoice Number: {self.invoice_details['invoice_number']}")
        print(f"Invoice Date: {self.invoice_details['invoice_date']}")
        print(f"Due Date: {self.invoice_details['due_date']}")
        print("")

        print("Itemized List of Products/Services:")
        print("=============================================================")
        print("| Description          | Quantity | Unit Price |    Total   |")
        print("=============================================================")
        subtotal = 0
        for item in self.items:
            total = item['quantity'] * item['unit_price']
            subtotal += total
            print(f"| {item['description']:20} | {item['quantity']:8} | {item['unit_price']:10} | {total:10} |")
        print("=============================================================")
        print(f"| Subtotal             |          |            | {subtotal:10} |")
        print("=============================================================")
        if 'tax' in self.invoice_details:
            tax = subtotal * (self.invoice_details['tax'] / 100)
            print(f"Tax ({self.invoice_details['tax']}%)\t\t\t\t\t      {tax:.2f}|")
            print("=============================================================")
            total_amount_due = subtotal + tax
        else:
            total_amount_due = subtotal
        print(f"| Total Amount Due     |          |            | {total_amount_due:10} |")
        print("=============================================================")
        print("")

        print("Payment Terms:")
        for term in self.payment_terms:
            print(term)
        print("")

        print("Payment Methods:")
        for method in self.payment_methods:
            print(method)
        print("")

        print("Notes:")
        print(self.notes)
        print("")


# Get user input
seller_info = {
    'name': input("Enter seller's name: "),
    'address': input("Enter seller's address: "),
    'contact_number': input("Enter seller's contact number: "),
    'email': input("Enter seller's email: ")
}

buyer_info = {
    'name': input("Enter buyer's name: "),
    'address': input("Enter buyer's address: "),
    'contact_number': input("Enter buyer's contact number: "),
    'email': input("Enter buyer's email: ")
}

invoice_number = "INV-" + str(datetime.now().strftime("%Y%m%d%H%M%S"))
invoice_date = datetime.now().strftime("%B %d, %Y")
due_date = (datetime.now() + timedelta(days=14)).strftime("%B %d, %Y")

invoice_details = {
    'invoice_number': invoice_number,
    'invoice_date': invoice_date,
    'due_date': due_date
}

tax_rate = input("Enter tax rate (optional, leave blank for no tax): ")
if tax_rate:
    invoice_details['tax'] = float(tax_rate)

num_items = int(input("Enter number of items: "))
items = []
for i in range(num_items):
    description = input(f"Enter description of item {i+1}: ")
    quantity = int(input(f"Enter quantity of item {i+1}: "))
    unit_price = float(input(f"Enter unit price of item {i+1}: "))
    items.append({'description': description, 'quantity': quantity, 'unit_price': unit_price})

payment_terms = ["100% advance"]
payment_methods = []
while True:
    print("Select payment method:")
    print("1. Cash")
    print("2. UPI")
    print("3. Credit/Debit Card")
    choice = input("Enter your choice (or 'q' to quit): ")
    if choice == 'q':
        break
    elif choice in ['1', '2', '3']:
        if choice == '1':
            payment_methods.append("Cash")
            break
        elif choice == '2':
            payment_methods.append("UPI")
            break
        elif choice == '3':
            payment_methods.append("Credit/Debit Card")
            break
    else:
        print("Invalid choice. Please try again.")


notes = input("Enter any additional notes: ")

invoice = Invoice(seller_info, buyer_info, invoice_details, items, payment_terms, payment_methods, notes)
invoice.generate_invoice()
