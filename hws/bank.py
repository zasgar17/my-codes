def user_information(card_number,card_csv,user_list):
    for user in user_list:
        if user["card_code"]==card_number and user["card_csv"]==card_csv:
            return f"Welcome {user['name'] }!"
users=[
    {
        "name": "Zahra",
        "surname": "Asgarova",
        "card_code": 98765432,
        "card_csv": 5678,
        "balance": 124.75
    },
    {
        "name": "John",
        "surname": "Doe",
        "card_code": 55554444,
        "card_csv": 987,
        "balance": 1000.0
    },
    {
        "name": "Gunel",
        "surname": "Zeynalzade",
        "card_code": 11112222,
        "card_csv": 456,
        "balance": 789.25
    },
    {
        "name": "Arzu",
        "surname": "Mirzayeva",
        "card_code": 88887777,
        "card_csv": 321,
        "balance": 356.22
    },
    {
        "name": "Lily",
        "surname": "Chen",
        "card_code": 44443333,
        "card_csv": 789,
        "balance": 789.99
    },
    {
        "name": "Mohammed",
        "surname": "Abdullah",
        "card_code": 99998888,
        "card_csv": 234,
        "balance": 432.10
    },
    {
        "name": "Sophie",
        "surname": "Anderson",
        "card_code": 12341234,
        "card_csv": 456,
        "balance": 1023.75
    },
    {
        "name": "Daniel",
        "surname": "Nguyen",
        "card_code": 77776666,
        "card_csv": 890,
        "balance": 234.56
    }
]

bank_card_number = int(input("Enter your card number: "))
bank_card_code = int(input("Enter your card code: "))

welcome_message = user_information(bank_card_number, bank_card_code, users)
print(welcome_message)