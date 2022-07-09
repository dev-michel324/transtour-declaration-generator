from turtle import title
import PySimpleGUI as sg
from Exec import exec


sg.theme('DarkAmber')

layout = [
    [sg.Text("Nome do declarante"), sg.InputText(key="-NAMEOWNER-")],
    [sg.Text("Cpf do declarante"), sg.InputText(key="-CPFOWNER-")],
    [sg.Text('Importar arquivo .csv'), sg.In(size=(25, 1), enable_events=True,
                                             key='-FILECSV-'), sg.FileBrowse()],
    [sg.Text('Importar assinatura'), sg.In(size=(25, 1), enable_events=True,
                                           key='-FILEIMG-'), sg.FileBrowse()],
    [sg.Text('Escolha onde salvar'), sg.In(size=(25, 1), enable_events=True,
                                           key='-FOLDER-'), sg.FolderBrowse()],
    [sg.Button('Gerar'), sg.Button('Cancelar')]
]

window = sg.Window('Transtour - gerador de declarações', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    if event == "Gerar":

        fileCsv = str(values['-FILECSV-'])
        pathToSave = str(values['-FOLDER-'])
        ownerSignature = str(values['-FILEIMG-'])
        ownerCpf = str(values['-CPFOWNER-'])
        ownerName = str(values['-NAMEOWNER-'])

        if (fileCsv and pathToSave and ownerSignature and ownerCpf and ownerName) != "":

            sg.popup_ok('GERANDO DECLARAÇÕES!')

            exec_and_get_return = exec(
                fileCsv, pathToSave, ownerSignature, ownerCpf, ownerName)
            if exec_and_get_return:
                sg.popup_ok('Geração finalizada!', title="GERAÇÃO FINALIZADA")
            else:
                sg.popup_ok("O arquivo é inválido.",
                            title="ERRO")
        else:
            sg.popup_ok(
                "Existem dados que estão faltando.", title="ERRO")

window.close()
