import random
from datetime import datetime, timedelta

def generate_random_visa_data():
    # Visa card numbers start with '4'
    visa_prefix = '4'

    # Generate the rest of the digits (excluding the last one)
    remaining_digits = [random.randint(0, 9) for _ in range(14)]

    # Calculate the Luhn check digit
    check_digit = calculate_luhn_check_digit(visa_prefix + ''.join(map(str, remaining_digits)))

    # Concatenate the digits with the check digit
    visa_number = visa_prefix + ''.join(map(str, remaining_digits)) + str(check_digit)

    # Generate random expiry date (valid for the next 10 years)
    current_date = datetime.now()
    expiry_date = current_date + timedelta(days=random.randint(365, 365 * 10))
    expiry_date_str = expiry_date.strftime('%m/%y')

    # Generate random CVV (3 digits)
    cvv = str(random.randint(100, 999))

    # Generate random postal code (5 digits)
    postal_code = ''.join(str(random.randint(0, 9)) for _ in range(5))

    return visa_number, expiry_date_str, cvv, postal_code

def calculate_luhn_check_digit(card_number):
    card_digits = list(map(int, card_number))
    for i in range(len(card_digits) - 2, -1, -2):
        card_digits[i] *= 2
        if card_digits[i] > 9:
            card_digits[i] -= 9
    total = sum(card_digits)
    return (total * 9) % 10

if __name__ == "__main__":
    # Example: Generate and print random Visa card data
    visa_number, expiry_date, cvv, postal_code = generate_random_visa_data()
    
    print("Generated Visa Card Data:")
    print("Card Number:", visa_number)
    print("Expiry Date:", expiry_date)
    print("CVV:", cvv)
    print("Postal Code:", postal_code)
