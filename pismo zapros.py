import os
import time
from docxtpl import DocxTemplate
from docx2pdf import convert
from palka_kopalka import get_now_rusdate

# ---------------------------
# ВХОДНЫЕ ДАННЫЕ
# ---------------------------
num = int(input('Дай пожалуйста номерок письма\n'))
recipient = input('Кто получатель письма\n')
text_letter = input('Напиши текст письма\n')
# ---------------------------


def zapros_generator(num, date, text_letter, template, folder_template, recipient):

    # имя файла шаблона
    name_file_wd_templ = template
    doc = DocxTemplate(name_file_wd_templ)
#    print(templates)
    # соберу словарь из нужных значений
    context = {
        'num_letter': num,
        'date_letter': date,
        'text_letter': text_letter,
        'recipient': recipient,
    }

    # подставлю значения
    doc.render(context)

    # сохраню в финальный документ
    name_finale_doc = (folder_template + os.sep + "Письмо" + "_N" + str(num) + "_от_" + time.strftime('%Y%m%d') + ".docx")
    name_finale_pdf = (folder_template + os.sep + "Письмо" + "_N" + str(num) + "_от_" + time.strftime('%Y%m%d') + ".pdf")
    doc.save(name_finale_doc)

    # конвертирую в pdf
    convert(name_finale_doc, name_finale_pdf)

    # удалю ненужный doc если он не нужен
    remove_doc = input("Удалить вордовский файл (y/n) ? ")
    if remove_doc == "y":
        os.remove(name_finale_doc)


date = get_now_rusdate()

folder_template = r'Z:\04.DD\101- Закупки\Письма'
name_file_template = "шаблон"

template = folder_template + os.sep + name_file_template + ".docx"

zapros_generator(num, date, text_letter, template, folder_template, recipient)

# что бы окошко не сразу закрылось и было видно что все ок
input(r'Done. Letter is here Z:\04.DD\101- Закупки\Письма. Press Enter for close Window')