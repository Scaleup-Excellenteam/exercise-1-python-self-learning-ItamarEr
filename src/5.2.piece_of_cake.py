
def piece_of_cake(prices:dict, optionals=None, **args) -> int:
    """
    :param prices: dictionary of items(str) as keys and their prices(int) as values.
    :param optionals: array of items to ignore.
    :param args: dictionary of items(str) to buy as keys and their quantities(int) in grams as values.
    :return: the total cost of the items to buy.
    """
    if optionals is None:
        optionals = []
    if not prices:
        return 0
    total_cost = 0

    for item,amount in args.items():
        if item not in optionals and item in prices:
            total_cost += prices[item] * (amount // 100)
    return total_cost


if __name__ == "__main__":
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
