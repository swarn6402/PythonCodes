Given_items = ["swarn", "papa", "mummy", "baby", "snoopy", "swarn"]
unique_item = set()

for item in Given_items:      
    if item in unique_item:            #returns True or False and then moves next
        print("The duplicate is:", item)
        break
    unique_item.add(item)
