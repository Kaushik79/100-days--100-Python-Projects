print("Welcome to the Silent Auction.")
auction={}
condition = True
while condition:
    name = input("What is your name? :")
    bidding_price = float(input("What is your bidding price? : $"))
    auction[name] = bidding_price
    next_bidder = input("Are there any other bidders? type 'yes' or 'no'.").lower()
    if next_bidder == 'no':
        condition = False
    elif next_bidder == 'yes':
        condition = True
    else:
        print("Invalid input. Exiting the auction......\nYou were thrown away from the auction")
        break
    print("\n "*50)

highest_bid = max(auction.values())
winners = [k for k, v in auction.items() if v == highest_bid]
if len(winners) == 1:
    print(f"The winner is {winners[0]} with a bid of ${highest_bid}.")
else:
    print(f"The winners are {', '.join(winners)} with a bid of ${highest_bid}.")

