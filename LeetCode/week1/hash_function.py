def hash_string(text: str, size: int):
    if not text:
        return 0

    h = 0
    for c in text:
        h = h * 31 + ord(c)  # *31 because its a simple way to try to avoid collision

    return h % size  # % size normalize the buckets amount


print(hash_string("hello world", 100))
