
class Inventory:
    
    def __init__(self,max_capacity):
        self.max_capacity = max_capacity
        self.items = {}
        self.item_count = 0
        
    def add_item(self,name,price,quantity):
        
        if self.item_count + quantity > self.max_capacity:
            return False
        
        if name in self.items:
            return False
        
        if self.max_capacity < 0:
            return False
        
        self.items[name] = {"name" : name , "price": price, "quantity" :  quantity}
        self.item_count += quantity
        
        return True
        

    def delete_item(self,item):
        if item not in self.items:
            return False
        
        self.item_count -= self.items[item]["quantity"]        
        del self.items[item]
        
    def get_most_stocked_item(self):
        highest_quan_item = None
        largest_quantity = 0
        
        for item in self.items.values():
            name = item["name"]
            price = item["price"]
            
            if price > largest_quantity:
                largest_quantity = price
                highest_quan_item = name
                
        return highest_quan_item
        
    
    def get_items_in_price_range(self,min_price,max_price):
        new_items = []
        
        for item in self.items.values():
            price = item["price"]
            name = item["name"]
            
            if min_price <= price <= max_price:
                new_items.append(name)
                
        return new_items  
        
        
a = Inventory(4)
print(a.add_item("Chocolate",65,1))
print(a.add_item("Banana",77,2))
# print(a.delete_item("Banana"))
print(a.get_items_in_price_range(10,100))
print(a.get_most_stocked_item())
        
        
        
        


        