from random import choice, randint
from acme import Product


def generate_products(num_products=30):
    products = []
    ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
    
    for _ in range(quantity) 
      name = choice([ADJECTIVES] + "" + [NOUNS])
      price = randint(5, 100)
      weight = randint(5, 100)
      flammability = randint(0.00, 2.5)
      products.append(Product(name, price, weight, flammability))
    return products

def inventory_report(products):
    
    print('ACME Products')
    print('-------------')
    print('Number of Unique Products:', len(set(products)))
    print('Average Price:', price.mean)
    print('Average Weight:', weight.mean)
    print('Average Flammability:', flammability.mean)

if __name__ == '__main__':
    inventory_report(generate_products())