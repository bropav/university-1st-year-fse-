import string

password = input()

is_reliable = True

# 1. Проверка длины пароля
if len(password) != 8:
    print("Длина пароля не равна 8")
    is_reliable = False

# 2. Проверка на наличие заглавных букв
if not any(symbol.isupper() for symbol in password):
    print("В пароле отсутствуют заглавные буквы")
    is_reliable = False

# 3. Проверка на наличие строчных букв
if not any(symbol.islower() for symbol in password):
    print("В пароле отсутствуют строчные буквы")
    is_reliable = False

# 4. Проверка на наличие цифр
if not any(symbol.isdigit() for symbol in password):
    print("В пароле отсутствуют цифры")
    is_reliable = False

# 5. Проверка на наличие специальных символов (*, -, #)
if not any(symbol in '*-#' for symbol in password):
    print("В пароле отсутствуют специальные символы")
    is_reliable = False

# 6. Проверка на непредусмотренные символы
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
if not all(symbol in allowed for symbol in password):
    print("В пароле используются непредусмотренные символы")
    is_reliable = False

# Если ни одно из условий сшибки не сработало, пароль надежный
if is_reliable:
    print("Надежный пароль")