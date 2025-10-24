from collections import defaultdict


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, line):
        super().__init__("Bad line: " + line)


class FileEmpty(StudentsDataException):
    def __init__(self, filename):
        super().__init__("File is empty: " + filename)


class StudentsData:
    def __init__(self, name, surname, evaluations):
        self.name = name
        self.surname = surname
        self.evaluations = evaluations


# file_name = input("Enter file name: ")
file_name = "samplefile.txt"
# file_name = "samplefile1_empty.txt"
# file_name = "lab1.txt"
try:
    stream = open(file_name, "rt")
    lines = stream.readlines()
    datos = defaultdict(float)
    if not lines:
        raise FileEmpty(file_name)
    for line in lines:
        line = line.replace("\n", "").strip()
        array = [p for p in line.split() if p]
        if len(array) != 3:
            raise BadLine(line)
        try:
            datos[(array[0], array[1])] += float(array[2])
        except ValueError:
            raise BadLine(line)
    stream.close()
    if datos:
        for dato in datos:
            print(dato[0], dato[1], datos[dato])
except (BadLine, FileEmpty) as e:
    print(e)
except IOError as e:
    from os import strerror

    print("Error found :", strerror(e.errno))
