discounts = {1: 0, 2: 5, 3: 10, 4: 20, 5: 25}
price_per_book = 8

# I define a chunk of books as all being different so that I can calculate the price
def calc_chunk_price(number_of_books: int) -> float:
    return price_per_book * number_of_books * (1 - discounts[number_of_books] / 100.0)

def main():
    # this list represents the shopping cart
    # the first entry corrensponds to the quantity of the first book and so on
    # your example would look like this [2, 2, 2, 1, 1]
    shopping_cart = [2, 5, 3, 4, 1]

    # the algorithm needs the list sorted, in ascending order
    shopping_cart.sort()

    # the algorithm is going to take the intuitive approach and take as big a chunk as possible
    # so chunk_sizes[0] will contain info on how many chunks of size 5 I could greedily take
    # in your example the chunk_sizes would end up as [1, 0, 1, 0, 0] meaning one group of 5 and 3 books each.
    chunk_sizes = []
    removed_books = 0

    # since the shopping_cart is sorted, I can simply loop over it
    for i in list(range(0,5)):
        chunk_sizes.append(shopping_cart[i] - removed_books)
        removed_books += chunk_sizes[i]

    # now here comes the tricky part as your example kindly suggested
    # two chunks of 4 books are actually cheaper than a 3/5 split!
    # since this is the only exception I could find, I "manually" adjust the chunks
    extra_sauce = min(chunk_sizes[0], chunk_sizes[2])
    if extra_sauce:
        chunk_sizes[0] -= extra_sauce
        chunk_sizes[1] += 2 * extra_sauce
        chunk_sizes[2] -= extra_sauce

    # the rest is simple and probably needs no explanation
    price = 0
    for i, chunks in enumerate(chunk_sizes):
        price += calc_chunk_price(5 - i) * chunks;

    print(f'Die Bücher kosten {price:.2f} Euro')

if __name__ == '__main__':
    main()
