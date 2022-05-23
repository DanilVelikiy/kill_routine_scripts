import os
import shutil
import time
# _________________________________________
# бэкап файла сравнения подрядчиков в архив
# -----------------------------------------
# объявление переменных
sourceFileName = "Таблица_подрядчиков.xlsx"
sourseFileCompareContarctorLapino3 = r'Z:\04.DD\01_Лапино 3\08_Адм_работа\06_Подрядчики\00-Сравнение'
archiveFileCompareContarctorLapino3 = r'Z:\04.DD\01_Лапино 3\08_Адм_работа\06_Подрядчики\00-Сравнение\Archive'
nameArchiveFileCompareContarctorLapino3 = ("Таблица_подрядчиков_ред." + time.strftime('%Y%m%d') + "_" +
                                          time.strftime('%H%M') + ".xlsx")
#sourseFileTheMacros = "D:\Macros\FilesMacros"
#nameSourseFileTheMacros = "backup.py"
#print("nameArchiveFileCompareContarctorLapino3", nameArchiveFileCompareContarctorLapino3)
#print("Name of sourseFileCompareContarctorLapino3", sourseFileCompareContarctorLapino3+os.sep+sourceFileName)
# проверка сущестсвования исходного файла
# print("проверка исходного файла - ", os.path.exists(sourseFileCompareContarctorLapino3+os.sep+sourceFileName))
#print("проверка файла макроса - ", os.path.exists(sourseFileTheMacros + os.sep + nameSourseFileTheMacros))

#для ориентации во времени
print("Now is ", time.strftime('%Y%m%d') + "_" + time.strftime('%H%M'))


# создание резвервной копии в архиве и проверка что создан
shutil.copy2(sourseFileCompareContarctorLapino3+os.sep+sourceFileName,
             archiveFileCompareContarctorLapino3 + os.sep + nameArchiveFileCompareContarctorLapino3)
print("резервная копия файла сравнения подрядчиков по Лапино3 создана - ",
      os.path.exists(archiveFileCompareContarctorLapino3 + os.sep + nameArchiveFileCompareContarctorLapino3))
# _________________________________________
# бэкап файла бюджета Лапино3 в архив
# -----------------------------------------
# объявление переменных
Src_File_Money_Nm = "Бюджет_МиД_Разбивка оплат по месяцам.xlsx"
Src_Folder_File_Money = r'Z:\03.FIN\01.DD\П_админ\01_МиД_Лапино3\02_Бюджет'
Arch_Folder_File_Money = r'Z:\03.FIN\01.DD\П_админ\01_МиД_Лапино3\02_Бюджет\Архив'
Arch_File_Money_Nm = ("Бюджет_МиД_Разбивка оплат по месяцам_ред." + time.strftime('%Y%m%d') + "_" +
                                          time.strftime('%H%M') + ".xlsx")
# создание резвервной копии в архиве и проверка что создан
shutil.copy2(Src_Folder_File_Money + os.sep + Src_File_Money_Nm,
             Arch_Folder_File_Money + os.sep + Arch_File_Money_Nm)
print("резервная копия файла бюджета по Лапино3 создана - ",
      os.path.exists(Arch_Folder_File_Money + os.sep + Arch_File_Money_Nm))
# _________________________________________
# бэкап файла анализа конкурсов в архив
# -----------------------------------------
# объявление переменных
Src_File_Analis_Tender_Nm = "Список аукционов ПСД.xlsx"
Src_Folder_Analis_Tender = r'Z:\04.DD\100_Расчет ресурсов\01_Администрирование'
Arch_Folder_Analis_Tender = r'Z:\04.DD\100_Расчет ресурсов\01_Администрирование\Архив'
Arch_File_Analis_Tender_Nm = ("Список аукционов ПСД_ред." + time.strftime('%Y%m%d') + "_" +
                                          time.strftime('%H%M') + ".xlsx")
# создание резвервной копии в архиве и проверка что создан
shutil.copy2(Src_Folder_Analis_Tender + os.sep + Src_File_Analis_Tender_Nm,
             Arch_Folder_Analis_Tender + os.sep + Arch_File_Analis_Tender_Nm)
print("резервная копия файла анализа конкурсов создана - ",
      os.path.exists(Arch_Folder_Analis_Tender + os.sep + Arch_File_Analis_Tender_Nm))

input('Press Enter for Qiut')