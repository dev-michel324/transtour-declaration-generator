from Utils import MakeDeclarationPdf
import csv
import os
import pathlib


def exec(pathToCsv, pathToSave, signatureImg, cpfOwner, nameOwner):
    if os.path.isfile(pathToCsv) and pathlib.Path(pathToCsv).suffix == ".csv":
        reader = None
        with open(pathToCsv) as file:
            reader = csv.DictReader(file)
            for line in reader:

                studentName = line['NOME ex: Carlos Andrade']
                fileNameToSave = f"{studentName.replace(' ', '')}.pdf"
                studentRg = line['RG ex: 000.000.000']
                studentCpf = line['CPF ex: 000.000.000-00']
                absolutePathToSave = f"{pathToSave}/{fileNameToSave}"

                obj_make_declaration = MakeDeclarationPdf(
                    absolutePathToSave, nameOwner, signatureImg, studentName, studentRg, studentCpf, cpfOwner)

                del obj_make_declaration
        return True
    return False
