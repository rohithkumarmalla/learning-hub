import json
def main():
# gathering information
    global crew, bill, items
    response = ["yes", "ok", "k", "kk"]
    print("Who are all sharing the bill? Eg: sachin,dhoni,virat")
    while True:
        crew = input("Enter all the names: ").replace(',', ' ').split()
        tmp = input(f'\nAre you "ok" to proceed with the names {crew}\n(yes or ok to proceed): ')
        if tmp.lower().strip() in response and len(crew) > 1:
            break

    print("\nNow enter item names and its price with comma separated\nEg: Veg Platter,120 and type 'ok' when you added all the items.")
    bill = {}
    while True:
        tmp = input(':')
        try:
            if tmp.lower().strip() in response:
                break
            key, value = tmp.split(',')
            bill[key] = float(value)
        except:
            print(f'please enter "{tmp}" in valid format: Veg Platter,799')
            pass

    print(f"\n{bill}\n")
    items = list(bill.keys())
    while True:
        tmp = input("Enter 'ok' or 'update' or 'remove' accordingly: ")
        if tmp.lower().strip() in response:
            break
        elif tmp.lower().strip() == 'update':
            name = get_itemName("Enter the item's name: ")
            amount = get_number("Enter value: ")
            bill[name] = amount
        elif tmp.lower().strip() == 'remove':
            name = get_itemName("Enter the item's name: ")
            bill.pop(name)
        else:
            continue
        print(f"\n{bill}\n")
    items = list(bill.keys())


    gst = get_number("How much 'gst' was charged [5%]? ")
    serviceCharge = get_number("Enter service charge: ")
    bookedBy = get_crewName("Who booked the table? ")
    discount = get_number("How much discount you got (in amount): ")
    coupon = get_number("Enter coupons or dine cash(in amount): ")
    cFee = get_number("Enter How much the app's convinence fee was charged: ")
    cGst = get_number("Enter the convinence fee's gst: ")
    bookingCharges = get_number("How much is booking chsrges? ")
    cashback = ("Enter cashback(in amount): ")
    tip = get_number("Enter Tip [0]: ")
    if tip != 0:
        tipBy = get_crewName("Who paid the tip? ")
    
    extras = discount + coupon - cFee - cGst

# Seggregation keeps a record of items as keys: and its consumer's list as values: 
    record = seggregation()
    # print(json.dumps(record, indent =2))

# splits the bill including restaurant's gst
    split = moneySplit(record, gst, serviceCharge)
    # print(json.dumps(split, indent =2))

# after discount, coupons, app's convinence fee + gst, bookingChanrges, tip
    split = finalDeductions(split, cashback, extras, bookingCharges, tip)
    print(json.dumps(split, indent =2))


# after discount, coupons, app's convinence fee + gst, bookingChanrges, tip
def finalDeductions(split, cashback, others, bookingCharges, tip):
    for ind in split:
        split[ind]['TotalShare'] -=  others * (split[ind]['allocation'] / 100)
        split[ind]['TotalShare'] += (bookingCharges+tip)/len(crew)
    return split

# Return a dictionary, where it Splits all the item's money to each person
# eg: 
# { Rohith : {'TotalShare': 245, 'allocation': 22}
#   Subbu : {'TotalShare': 200, 'allocation': 19}
#   ...
# }
def moneySplit(record, gst, sc):
    global totalBill
    split = {}
    for i in crew:
        split[i] = {'TotalShare': 0, 'allocation': 0}  # initialize a dictionary with all the 'crew' as keys:
    for i in items:
        if record[i][0] == "all":
            itr = crew
            share = bill[i] / len(crew)
        else:
            itr = record[i]
            share = bill[i] / len(record[i])

        for ind in itr:
            split[ind]['TotalShare'] += share
    totalBill = sum(list(bill.values()))
        
    for i in split: # Calculating individual contribution in %
        split[i]['allocation'] = round( (split[i]['TotalShare'] / totalBill) * 100 )

        # adding gst + service charge
        split[i]['TotalShare'] = split[i]['TotalShare'] * (1+ gst/100) + sc*(split[i]['allocation']/100)
    return split

# This will ask and return a record of who ate what dish
# eg: 
# { Platter: [Rohith, Subbu, Dileep]
#   Biryani: [Subbu, Rohith]
#   water: [all]
# }
def seggregation():
    seg = {}
    for i in items:
        seg[i] = input(f"Enter the names (,separated) who all shared {i}: ").split(',')
    return seg

# prompts the user until he entered a number
def get_number(msg):
    while True:
        try:
            value = float(input(msg).strip().rstrip('%'))
            return value
        except ValueError:
            continue
    msg = "Please enter a valid number: "

# prompts the user until the name he entered matches in the crew
def get_crewName(msg):
    while True:
        name = input(msg)
        for i in crew:
            if i.startswith(name):
                return i
        msg = "we don't find any match, Try Again: "

def get_itemName(msg):
    while True:
        name = input(msg)
        for i in items:
            if name in i:
                return i
        msg = "please enter a valid item name"

if __name__ == "__main__":
    main()