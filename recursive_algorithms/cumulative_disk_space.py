import os


def cumulative_size(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for file in os.listdir(path):
            childpath = os.path.join(path, file)
            total += cumulative_size(childpath)

    return total

print(cumulative_size("/home/diwas-dahal/Tm/Projects/Projects/javascript/cart/img/img"))
