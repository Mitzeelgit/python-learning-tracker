def taxcalc():

    print("-----------------------------------TAX-CALCULATOR-----------------------------------")
    while True:

        try:
            cost = float(input("What if the total cost of your product in $ :   \n"))
            if cost > 0:
                break
            else:
                print("Cost cannot be negative")
        except:
            print("Enter a valid float")
            continue

    sgst = float(cost*0.18)

    gst = float(cost*0.18)

    total = gst + sgst + cost

    print("-----------------------------------TAX-CALCULATOR-----------------------------------")
    print("SGST :- {}".format(sgst))
    print("GST :- {}".format(gst))
    print("TOTAL :- {}".format(total))
taxcalc()
