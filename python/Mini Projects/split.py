import json
def main():
# gathering information
    global crew, bill, items
    crew = ['ro','ha', 'su', 'na', 'ad']
    bill = {'veg Platter': 739,
             'Chicken Tikka': 399,
             'Water': 18,
             'Missi Roti': 70,
             'Garlic Naan': 90,
             'Chilli Naan': 90,
             'Paneer Tikka Lababdar': 399,
             'Prawns Biryani': 479,
             'Thumbs Up': 178,
             'Jalebi With Rabdi': 199}
    gst = get_number("How much 'gst' was charged [5%]? ")
    serviceCharge = get_number("Enter service charge: ")
    bookedBy = get_name("Who booked the table? ")
    discount = get_number("How much discount you got (in amount): ")
    coupon = get_number("Enter coupons or dine cash(in amount): ")
    cFee = get_number("Enter How much the app's convinence fee was charged: ")
    cGst = get_number("Enter the convinence fee's gst: ")
    bookingCharges = get_number("How much is booking chsrges? ")
    cashback = ("Enter cashback(in amount): ")
    tip = get_number("Enter Tip [0]: ")
    if tip != 0:
        tipBy = get_name("Who paid the tip? ")
    
    items = list(bill.keys())
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

# prompts the user until the name he entered matches in the crew
def get_name(msg):
    while True:
        name = input(msg)
        for i in crew:
            if i.startswith(name):
                return i

def get_itemName(name):
    for i in items:
        if name in i:
            return i

if __name__ == "__main__":
    main()