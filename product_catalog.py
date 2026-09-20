from product_data import products

response = ""
requested_tags = []
while response != "N":
    print()
    print("Input a preference:")
    preference = input()
    requested_tags.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()[0]
    #adding [0] protects against people putting "yes" or "no"

requested_tags = set(requested_tags)

def count_matches(product_tags, customer_tags):
    count = 0
    for tag in product_tags:
        if tag in customer_tags:
            count += 1
    return count

def recommend_products(products, customer_tags):
    recomend = []

    for product in products:
        for tag in customer_tags:
            if tag in product["tags"]:
                recomend.append(
                    {
                        "name": product["name"],
                        "matches": count_matches(product["tags"],customer_tags)
                    }
                )
                break
    return recomend

def sortKey(e):
    return e["matches"]

print()
print("--==RESULTS==--")
results = recommend_products(products,requested_tags)
results.sort(key=sortKey, reverse=True)
for result in results:
    print(f' - {result["name"]} ({result["matches"]} match(es))')


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
#   I used a lot of for loops to iterate through lists easily
#   I also used the key argument in the sort function to tell it to sort by the count, grouping them together
# 2. How might this code change if you had 1000+ products?
#   I would probably find a better way of iterating through the list of products to find tags