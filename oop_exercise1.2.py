def get_max_value():
    return int(input("Enter the maximum value for the AP: "))

def generate_ap(max_value):
    ap = []
    term = 3
    while term <= max_value:
        ap.append(term)
        term += 3
    return ap

def length_of_ap(ap):
    return len(ap)

def get_ap_sum(ap):
    return sum(ap)

def get_ap_square_sum(ap):
    return sum([i**2 for i in ap])

def main():
    max_value = get_max_value()
    ap = generate_ap(max_value)
    
    print("AP: ", ap)
    print("Number of terms in AP: ", length_of_ap(ap))
    print("Sum of AP: ", get_ap_sum(ap))
    print("Sum of squares of AP: ", get_ap_square_sum(ap))

main()