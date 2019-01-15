import PyPDF4
import re
import os
import io


def find_question(location):
    results = []
    results.append(1)
    with open(location, 'rb') as obj:
        reader = PyPDF4.PdfFileReader(obj)
        for page in range(2, reader.numPages):
            page_obj = reader.getPage(page)
            content = page_obj.extractText()
            #head = content[]
            if re.match('\d\d?\n9608/\d\d/././\d\d\n© UCLES \d\d\d\d(\n\[Turn over)?\n\d ', content, re.M) is not None:
                results.append(page)
    return results


def creat_new_folder(new, inside):
    if not os.path.exists(os.path.join(inside, new)):
        os.makedirs(os.path.join(inside, new))
    return os.path.join(inside, new)


def cutting(paper):
    starts = find_question(paper)
    source = PyPDF4.PdfFileReader(paper)
    output = []
    for index in range(len(starts)-1):
        tem = PyPDF4.PdfFileWriter()
        for page in range(starts[index], starts[index+1]):
            tem.addPage(source.getPage(page))
        output.append(tem)
    tem = PyPDF4.PdfFileWriter()
    for page in range(starts[len(starts)-1], source.numPages):
        tem.addPage(source.getPage(page))
    output.append(tem)
    return output


def parse(path='cs'):
    output_path = "C:\\Users\\asus\\Desktop\\result"
    years = os.listdir(path)
    for year in years:
        result_year = creat_new_folder(year, output_path)
        for paper in os.listdir(os.path.join(path, year)):
            questions = cutting(os.path.join(os.path.join(path, year), paper))
            path = creat_new_folder(paper, result_year)
            for index in range(len(questions)):
                name = path + "\\" + str(index + 1) + ".pdf"
                location = open(name, 'xb')
                questions[index].write(location)
                location.close()


if __name__ == '__main__':
    parse('C:\\Users\\asus\\Desktop\\cs')
