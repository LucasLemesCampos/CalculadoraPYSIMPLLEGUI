# OBEJETIVO: CRIAR UM INTERFACE GRAFICA CAPAZ DE EXECUTAR FUNÇOES
import pandas as pd
import PySimpleGUI as sg

sg.theme('DarkBlack')   
fonteTitulo = ('Lucida',30)
fonteSubtitulo = ('lucida',20)
fonteicone = ('Lucida',30)
layout = [  [sg.Text('MATH-CALC',justification='center',size=(30,3),font=fonteTitulo)],
            [sg.Text('DIGITE NUMERO 1',justification='center',size=(20,2),font=fonteSubtitulo),sg.Text('DIGITE NUMERO 2',justification='center',size=(20,2),font=fonteSubtitulo) ],
            [sg.InputText(key='numero1',justification='left',size=(45,5)),sg.InputText(key='numero2',justification='right',size=(45,5))],
            [sg.Button('+',size=(4,1),font=fonteicone),sg.Button('C',size=(4,1),font=fonteicone), sg.Button('-',size=(4,1),font=fonteicone), sg.Button('x',size=(4,1),font=fonteicone),sg.Text('',size=(4,1),font=fonteicone), sg.Button('÷',size=(4,1),font=fonteicone)],
            [sg.Text(' ',key='resultado',justification='center',size=(20,3),font=fonteTitulo)]
]

# Create interface
janela = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED: 
        break
    #BOTAO SOMA
    if evento == '+':
        numero1 = float(valores['numero1'])
        numero2 = float(valores['numero2'])
        janela['resultado'].update(f'Seu Resultado é: {numero1+numero2} ')
    #BOTAO Subtração
    if evento == '-':
        numero1 = float(valores['numero1'])
        numero2 = float(valores['numero2'])
        janela['resultado'].update(f'Seu Resultado é: {numero1-numero2}')
    #BOTAO MULTIPLICAÇÂO
    if evento == 'x':
        numero1 = float(valores['numero1'])
        numero2 = float(valores['numero2'])
        janela['resultado'].update(f'Seu Resultado é: {numero1*numero2} ')
    #BOTAO DIVISAO
    if evento == '÷':
        numero1 = float(valores['numero1'])
        numero2 = float(valores['numero2'])
        janela['resultado'].update(f'Seu Resultado é: {numero1/numero2}')
    #BOTAO C RESET
    if evento == 'C':
         janela['resultado'].update(' ')
         janela['numero1'].update(' ')
         janela['numero2'].update(' ')

janela.close() 