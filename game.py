import random
secret = random.randint(1, 5)

while True:
    guess = int(input("१ ते ५ मधील एक अंक ओळखा: "))
    if guess == secret:
        print("अभिनंदन! तुम्ही जिंकलात.")
        break
    else:
        print("चुकीचे! पुन्हा प्रयत्न करा.")

