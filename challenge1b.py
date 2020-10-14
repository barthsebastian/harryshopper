discounts = {1: 0, 2: 5, 3: 10, 4: 20, 5: 25}
price_per_book = 8
minimum = 0

def calc_series_price(number_of_books: int) -> float:
    return price_per_book * number_of_books * (1 - discounts[number_of_books] / 100.0)

def main():
    global minimum
    shopping_cart = [2, 2, 2, 1, 1]
    chunk_number = max(shopping_cart)
    minimum = price_per_book * sum(shopping_cart) * 2
    if chunk_number == 1:
        print(calc_series_price(sum(shopping_cart)))
    else:
        calc_recursive(shopping_cart, chunk_number)
        print(minimum)

def calc_recursive(shopping_cart: list, steps_remaining: int):
    global minimum
    if steps_remaining == 1:
        return calc_series_price(sum(shopping_cart))
    else:
        for i in list(range(1, 32)):
            subcart = [i // 16 % 2, i // 8 % 2, i // 4 % 2, i // 2 % 2, i % 2]
            valid = True
            for j in list(range(0, 5)):
                if (shopping_cart[j] == steps_remaining) and (subcart[j] == 0) and valid:
                    valid = False
            if valid:
                tmp_cart = [x - y for x, y in zip(shopping_cart, subcart)]
                if min(tmp_cart) != -1:
                    minimum = min(minimum, (calc_recursive(tmp_cart, steps_remaining - 1) + calc_series_price(sum(subcart))))

if __name__ == '__main__':
    main()
