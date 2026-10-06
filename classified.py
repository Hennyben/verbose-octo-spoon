x=input("Classifier: ")
target_words = ["james", "london", "mi6", "classified", "paris", "midnight", "nuclear", "asset"]
for x in x.split(" "):
    if x in target_words:
        print("[REDACTED]", end=' ')
    else:
        print(x, end=' ')

    
