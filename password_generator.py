def password_generator(password_length):
    import random
    password=''
    real_password=''
    v=''
    letters=['a','A','b','B','c','C',
            'd','D','e','E','f','F',
            'g','G','h','H','i','I',
            'j','J','k','K','l','L',
            'm','M','n','N','ñ','Ñ',
            'o','O','p','P','q','Q',
            'r','R','s','S','t','T',
            'u','U','v','V','w','W',
            'x','X','y','Y','z','Z']
    
    numbers=['0','1','2','3','4',
             '5','6','7','8','9']

    symbols=['!','"','#','$','%','&','(',')',
             '*','+',',','-','.','/',':',';',
             '<','=','>','?','{','|','}','~',
             '@','^','_','[',']']
    for i in range(password_length):
        password+=random.choice(letters)+random.choice(numbers)+random.choice(symbols)

    v=password[:password_length]
    for i in range(len(v)):
        real_password+=random.choice(v)
    print(real_password)
    return real_password


password_generator(12)