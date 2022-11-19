from menu import products

def calculate_tab(account):
    total = 0
    for item in account:
        product = next((product for product in products if product['_id'] == item['_id']))
        total = total + product['price'] * item['amount']
    return {"subtotal": f'${total:,.2f}'}