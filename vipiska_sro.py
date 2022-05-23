import os
import time
from docxtpl import DocxTemplate
from docx2pdf import convert
from palka_kopalka import get_now_rusdate

# ---------------------------
# ВХОДНЫЕ ДАННЫЕ
# ---------------------------
num = int(input('Дай пожалуйста номерок первого письма, а второй сам посчитаю'))
# ---------------------------


def zapros_generator(num, date, templates):

    # имя файла шаблона
    name_file_wd_templ = templates
    doc = DocxTemplate(name_file_wd_templ)
#    print(templates)
    # соберу словарь из нужных значений
    context = {
        'num_letter': num,
        'date_letter': date,
    }

    # подставлю значения
    doc.render(context)

    # сохраню в финальный документ
    name_finale_doc = (templates + "_" + time.strftime('%Y%m%d') + ".docx")
    name_finale_pdf = (templates + "_" + time.strftime('%Y%m%d') + ".pdf")
    doc.save(name_finale_doc)

    # конвертирую в pdf
    convert(name_finale_doc, name_finale_pdf)

    # удалю ненужный doc
    os.remove(name_finale_doc)

date = get_now_rusdate()

nums= []
nums.append(num)
nums.append(nums[0] + 1)

folder_template_1 = r'Z:\04.DD\000_HASCCA - СРО\СоветПроектировщиков\Выписки'
name_file_templates_1 = "Выписка_советпроектировщиков.docx"

folder_template_2 = r'Z:\04.DD\000_HASCCA - СРО\СоюзАтомГео\Выписки'
name_file_templates_2 = "Выписка_союзатомгео.docx"

templates = []
templates.append(folder_template_1 + os.sep + name_file_templates_1)
templates.append(folder_template_2 + os.sep + name_file_templates_2)

for i in range (0, 2):
    zapros_generator(nums[i], date, templates[i])