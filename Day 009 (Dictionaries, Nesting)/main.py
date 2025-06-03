#BLIND AUCTION FINAL PROJECT
bid_on = True
auction_dict = {}


while bid_on:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    auction_dict[name] = bid

    keep_bidding = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if keep_bidding == "no":
        highest_bid = 0

        for key in auction_dict:
            if auction_dict[key] > highest_bid:
                highest_bid = auction_dict[key]

        bid_on = False
        result_name = [key for key, value in auction_dict.items() if value == highest_bid]
        print(f"The winner is {result_name[0]} with a bid of ${highest_bid}")


#just need to finish project by making it clear the screen when new person enters bid