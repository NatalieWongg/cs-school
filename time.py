import time
def typeTime():
    start = time.time()
    s = input("Type 'the lazy fox jumped over the brown dog': ")
    end = time.time()
    print(f"It took {end - start} seconds")
print(typeTime())
