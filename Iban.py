import random

def generate_iban():
    country_code = "NL"
    bank_codes = ["ABNA", "INGB", "RABO", "SNSB", "TRIO", "KNAB", "BUNQ", "ASNB", "RBRB"]

    while True:
        bank_code = random.choice(bank_codes)
        account_number = str(random.randint(1000000000, 9999999999)).zfill(9)

        # Calculate 11-check
        total = sum(int(digit) * (9 - idx) for idx, digit in enumerate(account_number))
        if total % 11 == 0:
            break

    # Generate check digits (using a simple placeholder)
    bban = f"{bank_code}{account_number}"
    numeric_bban = "".join(str(int(c, 36)) for c in bban)
    check_digits = 98 - (int(numeric_bban + "232100") % 97)

    iban = f"{country_code}{check_digits:02d}{bban}"
    return iban

# Generate 5 valid Dutch IBAN numbers
for _ in range(5):
    print(generate_iban())