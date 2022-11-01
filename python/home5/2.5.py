nado_sdavit = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'


def zgimanie(a):
    arhiv = ''
    vremennaya = ''
    count = 1
    for i in a:
        if i != vremennaya:
            if vremennaya:
                arhiv += str(count) + vremennaya
            count = 1
            vremennaya = i
        else:
            count += 1
    else:
        arhiv += str(count) + vremennaya
        return arhiv


print (zgimanie (nado_sdavit))
nygnie_el = zgimanie(nado_sdavit)


def razvorachivanie(a):
    unarhiv = ''
    count = ''
    for i in a:
        if i.isdigit ():
            count += i
        else:
            unarhiv += i*int(count)
            count = ''
    return unarhiv
print (razvorachivanie(nygnie_el))