

JsonData
===================================

Описание
''''''''
   описание

Класс

inherits *dict*

Methods:
+++++++

**__init__**: (self)

____________

**load** (self, *str* path):
   загружает файл указанный в path; если path отсутствует то вызвывется исключение

____________

**save** (self, *dict* obj=None,  *str* path=None):

____________

**new_file** (self, *str* path):

____________

*str* **get_path** (self):

Использование
-------------

::

   path = "file.json"
   obj = JsonData()
   obj.load(path)
   obj["1"] = 10
   obj.save()
   print(obj.get_path)




