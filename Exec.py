from Utils import MakeDeclarationPdf
import csv
import os
import pathlib
import PySimpleGUI as sg


def execMakeFromCsv(pathToCsv, pathToSave, signatureImg, validatorByCpf, cpfOwner, nameOwner):
    if os.path.isfile(pathToCsv) and pathlib.Path(pathToCsv).suffix == ".csv":
        reader = None
        with open(pathToCsv) as file:
            reader = csv.DictReader(file)
            for line in reader:
                studentName = line['NOME ex: Carlos Andrade']
                studentCpf = line['CPF ex: 000.000.000-00']

                with open(validatorByCpf, "r") as validator:
                    for cpf in validator:

                        if studentCpf == cpf.rstrip():
                            studentRg = line['RG ex: 000.000.000']
                            fileNameToSave = f"{studentName.replace(' ', '')}.pdf"
                            absolutePathToSave = f"{pathToSave}/{fileNameToSave}"

                            obj_make_declaration = MakeDeclarationPdf(
                                absolutePathToSave, nameOwner, signatureImg, studentName, studentRg, studentCpf, cpfOwner)

                            del obj_make_declaration
                        else:
                            with open(f"{os.path.expanduser('~/Desktop')}/logtranstour.txt", "a") as log:
                                log.write(
                                    f"NOME: {studentName} CPF: {studentCpf} STATUS: Não Aceito\n")
                                log.close()
                validator.close()
            file.close()
            return True
    return False


class WindowMakeDeclarationManually:
    def __init__(self):
        self.windowToMakeManually()

    def windowToMakeManually(self):
        sg.theme('DarkAmber')

        layout = [
            [sg.Text("Nome do declarante"), sg.InputText(key="-NAMEOWNER-")],
            [sg.Text("Cpf do declarante"), sg.InputText(key="-CPFOWNER-")],
            [sg.Text("Nome do estudante"), sg.InputText(key="-NAMESTUDENT-")],
            [sg.Text("Cpf do estudante"), sg.InputText(key="-CPFSTUDENT-")],
            [sg.Text("Rg do estudante"), sg.InputText(key="-RGSTUDENT-")],
            [sg.Text('Importar assinatura'), sg.In(size=(25, 1), enable_events=True,
                                                   key='-SIGNATUREIMG-'), sg.FileBrowse()],
            [sg.Text('Escolha onde salvar'), sg.In(size=(25, 1), enable_events=True,
                                                   key='-PATHTOSAVE-'), sg.FolderBrowse()],
            [sg.Button('Gerar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Transtour - gerador de declarações', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                break
            if event == "Gerar":

                pathToSave = str(values['-PATHTOSAVE-'])
                ownerSignatureImg = str(values['-SIGNATUREIMG-'])
                ownerCpf = str(values['-CPFOWNER-'])
                ownerName = str(values['-NAMEOWNER-'])
                studentName = str(values['-NAMESTUDENT-'])
                studentCpf = str(values['-CPFSTUDENT-'])
                studentRg = str(values['-RGSTUDENT-'])

                if (pathToSave and ownerSignatureImg and ownerCpf and ownerName and studentName and studentCpf and studentRg) != "":

                    fileNameToSave = f"{studentName.replace(' ', '')}.pdf"
                    absolutePathToSave = f"{pathToSave}/{fileNameToSave}"

                    sg.popup_ok('GERANDO DECLARAÇÕES!')

                    obj_make_declaration = MakeDeclarationPdf(
                        absolutePathToSave, ownerName, ownerSignatureImg, studentName, studentRg, studentCpf, ownerCpf)
                    if obj_make_declaration:
                        del obj_make_declaration
                        sg.popup_ok('Geração finalizada!',
                                    title="GERAÇÃO FINALIZADA")
                    else:
                        sg.popup_ok("O arquivo é inválido.",
                                    title="ERRO")
                else:
                    sg.popup_ok(
                        "Existem dados que estão faltando.", title="ERRO")
            if event == "Gerar Manualmente":
                pass
        window.close()
