#hashtable and hashmaping using python

def get_hash(key):
    h = 0

    for char in key:
        h += ord(char)

    return h % 100

index_value = get_hash('march 28')
print(f"Index value is {index_value}")