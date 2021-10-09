import re

if __name__ == "__main__":
    str_check = "Apellido A nombre N numero T"
    valid = re.findall(r"(\w+)+ +(\b[A-Z]{1})", str_check)
    print(str_check, '==>', valid)

    str_email = "email@email.0"
    # RFC 5322
    valid_email = re.findall(
        r"^[a-z0-9!#$%&'*ç+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", str_email)
    print(str_email, '==>', valid_email)

    str_card_number = "1234-5678-9012-34567"
    str_card_number = str_card_number.replace('-', '')
    str_card_number = str_card_number.replace(' ', '')
    valid_card = re.findall(
        r"[0-9]{16}", str_card_number)
    print(str_card_number, '==>', valid_card)

    str_card_number2 = "1234 5678 9012 34567"
    str_card_number2 = str_card_number2.replace('-', '')
    str_card_number2 = str_card_number2.replace(' ', '')
    valid_card2 = re.findall(
        r"[0-9]{16}", str_card_number2)
    print(str_card_number2, '==>', valid_card2)
