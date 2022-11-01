import random
import string


def get_random_word(num=random.randint(0, 100)):

    return ''.join(random.choice(string.ascii_letters) for i in range(num))


def get_random_password_and_email():
    lower_alphabet = list(string.ascii_lowercase)
    upper_alphabet = list(string.ascii_uppercase)
    cyrillic_alphabet = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
    password = ''
    password += upper_alphabet[random.randint(0, len(upper_alphabet) - 1)]

    for i in range(5):
        password += lower_alphabet[random.randint(0, len(lower_alphabet) - 1)]
        password += str(random.randint(0, 9))
    password += cyrillic_alphabet[random.randint(0, len(cyrillic_alphabet) - 1)]

    email = '' + password[1]
    domain = ''
    for i in range(5):
        email += lower_alphabet[random.randint(0, len(lower_alphabet) - 1)]
        domain += lower_alphabet[random.randint(0, len(lower_alphabet) - 1)]

    return password, email, domain
