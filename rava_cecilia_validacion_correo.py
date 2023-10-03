email_addresses = ["hola@google.com", "Andresgomez.86@hotmail.com.ar", "victora_g@gmail.com", "soyjuan@gmail.com",
                   "ramiro123@gmail.com.ar", "pinocho"]
email_adress = ''
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def validationEmail(email_adress):
    #Values
    times = 4
    stop = 0
    end = 0
    username = ''
    is_not_email_adress = 0
    correct_username = 0
    correct_domain = 0
    correct_domain_extension = 0
    count = 0
    #Take an email adress of the list
    #Validation - Username
    while stop != 1:
        if email_adress[count] != "@":
            if email_adress[count] in lowercase or email_adress[count] in uppercase or email_adress[count] in numbers \
                    or email_adress[count] == "." or email_adress[count] == "_" or email_adress[count] == "%" \
                    or email_adress[count] == "-" or email_adress[count] == "+":
                username += email_adress[count]
                end += 1
                if count < len(email_adress)-1:
                    count += 1
                else:
                    stop = 1
            else:
                stop = 1
        else:
            stop = 1

    if len(username) >= 1 and len(username) <= 64:
        if email_adress[count] == "@":
            #print(f'{username} is a valid username')
            correct_username = 1


    #Validation - domain
    stop = 0
    domain = ''
    if count < len(email_adress)-1:
        count += 1

    while stop != 1:
        if email_adress[count] != ".":
            if email_adress[count] in lowercase or email_adress[count] in uppercase or email_adress[count] in numbers:
                domain += email_adress[count]
                end += 1
                if count < len(email_adress)-1:
                    count += 1
                else:
                    stop = 1
            else:
                stop = 1
        else:
            stop = 1

    if len(domain) >= 4 and len(domain) <= 255:
        if email_adress[count] == ".":
            #print(f'{domain} is a valid domain')
            correct_domain = 1

    #Validation - domain extension
    stop = 0
    domain_extension = ''
    if count < len(email_adress)-1:
        count += 1

    while stop != 1:
        if email_adress[count] in lowercase or email_adress[count] in uppercase or email_adress[count] in numbers \
            or email_adress[count] == "." or email_adress[count] == "-":
            domain_extension += email_adress[count]
            end += 1
            count += 1
            if count == len(email_adress):
                stop = 1
        else:
            stop = 1

    if len(domain_extension) >= 2 and len(domain_extension) <= 64:
        #print(f'{domain_extension} is a valid domain extension')
        correct_domain_extension = 1

    len_total = len(username) + len(domain) + len(domain_extension)

    if len_total >= 6 and len_total <= 320 and correct_username == 1 and correct_domain == 1 and correct_domain_extension == 1:
        print(f'{email_adress} is a valid email adress')
    else:
        print(f'{email_adress} is NOT a valid email adress')

#Results
for i in range (0,6):
    email_adress = email_addresses[i]
    validationEmail(email_adress)
