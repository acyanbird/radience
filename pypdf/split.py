import PyPDF4
import re
import os
from io import StringIO


def find_question(location):
    obj = open(location, 'rb')
    reader = PyPDF4.PdfFileReader(obj)
    index = 1
    results = []
    for page in range(reader.numPages):
        page_obj = reader.getPage(page)
        pages_text = page_obj.extractText()
        lines = StringIO(pages_text).readlines()
        for line in range(len(lines)):
            for m in re.finditer(str(index)+"\t", lines[line]):
                if m.start() == 0:
                    results.append([page, index])
                    index += 1
    return results


def creat_new_folder(new, inside):
    needed = inside + "\\" + new
    if not os.path.exists(needed):
        os.makedirs(needed)


def cutting(paper):
    starts = find_question(paper)
    source = PyPDF4.PdfFileReader(paper)
    output = []
    for index in range(len(starts)-1):
        tem = PyPDF4.PdfFileWriter()
        for page in range(starts[index][0],starts[index+1][0]):
            tem.addPage(source.getPage(page))
        output.append(tem)
    tem = PyPDF4.PdfFileWriter()
    for page in range(starts[len(starts)][0], source.numPages):
        tem.addPage(source.getPage(page))
    output.append(tem)




path = "cs"
year = []
for dir_names in os.walk(path):
    year.extend(dir_names)
    break



