import PyPDF4
import re
import os
from io import StringIO


def find_question(location):
    obj = open(location, 'rb')
    reader = PyPDF4.PdfFileReader(obj)
    for page in range(reader.numPages):
        page_obj = reader.getPage(page)
        pages_text = page_obj.extractText()
        lines = StringIO(pages_text).readlines()
        for line in range(len(lines)):
            for m in re.finditer(r"", lines[line]):
                return [page, line, m.group(0)]


def creat_new_folder(new, inside):
    needed = inside + "\\" + new
    if not os.path.exists(needed):
        os.makedirs(needed)


path = "cs"
year = []
for dir_names in os.walk(path):
    year.extend(dir_names)
    break



