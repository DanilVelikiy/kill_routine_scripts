import time
s = 'Isaak Ivanov'
seo = 'Baranov Vladimir Raisovich'
def name_separate(s):
    i = 0
    while s[i] != ' ':
        i = i +1

    name = s[0:i]
    family = s[i+1:len(s)]
    return name, family

def full_name_to_short(seo):
    name_initial = seo[0]
    i = 0
    while seo[i] != ' ':
        index_family_name_end = i + 1
        i = i +1
    family_name = seo[0:index_family_name_end]
    name_initial = seo[index_family_name_end + 1]

    i = i+1
    while seo[i] != ' ':
        index_name_end = i + 1
        i = i +1
    father_name_initial = seo[index_name_end + 1]
    return family_name, name_initial, father_name_initial

def get_now_rusdate():
    month_list = [
        "января",
        "февраля",
        "марта",
        "апреля",
        "мая",
        "июня",
        "июля",
        "августа",
        "сентября",
        "октября",
        "ноября",
        "декабря",
    ]

    month_now = month_list[int(time.strftime('%m'))-1]
    date_now = time.strftime('%d') + " " + month_now + " " + time.strftime('%Y') + " г."
    return date_now


#s1 = full_name_to_short(seo)
#print(s1[0], s1[1] + '.', s1[2] + '.')

#date_now = get_now_rusdate()
#print(date_now)