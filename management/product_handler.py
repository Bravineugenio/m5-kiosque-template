from menu import products
from collections import Counter
def get_product_by_id(integer):
   try:
      if not isinstance (integer, int):
         raise TypeError("should be an integer")
      for product in products:
         if product["_id"] == integer:
            match = product
         print(match)
         if product["_id"] != integer:
            print("not found")
            break
   except TypeError as error:
      raise error 

def get_product_by_type(string):
   try:
      if not isinstance(string, str):
         raise TypeError("should be a string")
      for product in products:
         if product["type"] == string:
            match = product
            print(match)
   except TypeError as error:
      raise error

def menu_report():
   teste = len(products)
   result = sum(item["price"] for item in products)
   new_result = result / teste
   type_counts = Counter(d["type"] for d in products)
   test2 = type_counts.most_common(1)[0][0]
   return f"Products Count: {teste} - Average Price: ${new_result:,.2f} - Most Common Type: {test2}"
      
def add_product(products, **new_product):
   new_product['_id'] = max([product['_id']for product in products], default = 0) + 1
   products.append(new_product)
   return new_product


         


