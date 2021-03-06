# Berekent de winst of verlies van shares in te kopen en vervolgens terug te verkopen

# 2013 02 14

try:
    num_shares = int(input("# Shares: "))
    if num_shares < 0:
        raise ValueError, "Het aantal shares moet positief"
    pr_buy = float(input("Buy price: "))
    if pr_buy < 0:
        raise ValueError, "De aankoopprijs moet positief zijn"
    pr_sell = float(input("Sell price: "))
    if pr_sell < 0:
        raise ValueError, "De verkoopprijs moet positief zijn"
except ValueError as e:
    print "Slechte invoer:", e.args[0]
else:
    # Commissions
    comm_buy = pr_buy*0.02
    comm_sell = pr_sell*-0.015

    # Total prices
    tot_buy = pr_buy + comm_buy
    tot_sell = pr_sell + comm_sell

    # Profit/loss per share + percentages

    profit = tot_sell - tot_buy
    percentage = profit/tot_buy

    total_profit = num_shares * profit

    # Feedback to user
    if profit < 0:
        print "Loss is", '{:.2f}'.format(-total_profit), "(", '{:.0%}'.format(-percentage), ")"
    else:
        print "Profit is", '{:.2f}'.format(total_profit), "(", '{:.0%}'.format(percentage), ")"
