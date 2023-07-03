from update_time import update_time

def order_uprinting(valyuta_n, valyuta, yangilangan_v):
    global value
    time = update_time(yangilangan_v)

    if valyuta_n == 'USD':
        value = '1$'
    if valyuta_n == 'RUB':
        value = '1₽'
    if valyuta_n == 'EUR':
        value = '1€'
    output_message = f'🔰 {value} 🔄 {valyuta} so\'m \n {time}\n' \
                    f'Bu men:👉 @Currencies_Valyutalar_Bot'
    return output_message
