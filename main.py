import os
from datetime import *
from time import sleep
from docxtpl import DocxTemplate


def week_test()-> bool:
    if datetime.today().weekday() >= 5:
        return False
    else:
        return True




doc = DocxTemplate("Увал Шаблон.docx")
go_out = datetime.strftime(datetime.now(), "%d.%m.%Y")
next_day = timedelta(days=1)
arrive = datetime.strftime(datetime.now()+next_day, "%d.%m.%Y")
date_ = datetime.strftime(datetime.now(), "%d")
month_number = datetime.strftime(datetime.now(), "%m")
month_dict={
    "01": 'января',
    '02': "февраля",
    "03": "марта",
    '04': "апреля",
    '05': "мая",
    '06': "июня",
    '07': "июля",
    '08': "августа",
    '09': "сентября",
    '10': "октября",
    '11': "ноября",
    '12': "декабря"
}
month = month_dict[month_number]
context = {
    'go_out': go_out,
    'arrive': arrive,
    'date': date_,
    'month': month,
    }
doc.render(context)
dir_path = os.getcwd()
doc.save(f'{dir_path}/Увал.docx')
sleep(5)
weekend = week_test()
if weekend == True:
    os.startfile(f'{dir_path}/Увал.docx', 'print')
    print("Идет печать")
    sleep(10)
    os.startfile(f'{dir_path}/Увал.docx', 'print')
else:
    pass