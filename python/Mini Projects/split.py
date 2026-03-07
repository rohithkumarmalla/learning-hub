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
    items = list(bill.keys())
    # booked_by = get_name("Who booked the table? ")
    # booking_Charges = get_number("How much? ")
    # gst = get_number("How much 'gst' was charged [5%]? ")
    # tip = get_number("Enter Tip [0]: ")
    # if tip != 0:
    #     tip_by = get_name("Who paid the tip? ")
    
# Seggregation
    seg = {}
    for i in items:
        seg[i] = input(f"Enter the names (,separated) who all shared {i}: ").split(',')

# distribution
    split = {i: 0 for i in crew}
    for i in items:
        if seg[i][0] == "all":
            itr = crew
            share = bill[i]/len(crew)
        else:
            itr = seg[i]
            share = bill[i]/len(seg[i])
        for ind in itr:
            split[ind] += share
    print(split.items())

# prompts the user until he entered a number
def get_number(msg):
    while True:
        try:
            value = int(input(msg).strip().rstrip('%'))
            return value
        except ValueError:
            continue

# prompts the user until the name he entered matches in the crew
def get_name(msg):
    while True:
        name = input(msg).capitalize()
        for i in crew:
            if i.startswith(name):
                return i

def get_itemName(name):
    for i in items:
        if name in i:
            return i

if __name__ == "__main__":
    main()