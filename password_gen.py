import random
import string

print("--- मजबूत पासवर्ड जनरेटर ---")

# अक्षरे, आकडे आणि चिन्हांची यादी
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# सर्व एकत्र करणे
all_chars = letters + numbers + symbols

# ८ अंकी पासवर्ड तयार करणे
password_length = 8
password = "".join(random.sample(all_chars, password_length))

print("तुमचा नवीन पासवर्ड आहे:", password)

