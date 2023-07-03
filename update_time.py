from datetime import datetime

def update_time(time):
    x = datetime.now()
    month = x.strftime("%m")
    time = time.split(',')[1]
    time2 = time.split('+')[0]
    time3 = time2.split(' ')
    message = f"\nJoriy qilingan sana: 📆 {time3[1]}.{month}.{time3[3]} \n \n Joriy qilingan vaqt: 🕕 {time3[4]}\n"

    return message

