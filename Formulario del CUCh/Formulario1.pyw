import PySimpleGUI as sg 
import pandas as pd
import openpyxl
from tkinter import font


sg.theme('TanBlue')
layout = [  
            [sg.Image(r'logo2.png',pad=((220,0), (5,5)))],
            [sg.Text("Selecciona si es:", font= ("Arial Black", 8))], 
            [sg.Combo(['Administrativo','Docente','Publico en General', 'Alumno', 'Colaborador(S.S, Practicas)'], key='-Puestos-')], 
            [sg.Text("Nombre Completo:", font= ("Arial Black", 8)),sg.Text("Genero:", font= ("Arial Black", 8),  pad= ((210,0),(0,10)))],     
            [sg.InputText(key='-Nombre-'),sg.Checkbox('H', font= ("Arial Black", 8),key='-Hombre-'), sg.Checkbox('M', font= ("Arial Black", 8),key='-Mujer-')], 
            [sg.Text("Numero Telefonico:", font= ("Arial Black", 8)), sg.Text("Correo Electronico:",  font= ("Arial Black", 8), pad= ((212,0),(0,10)))],     
            [sg.InputText(key='-Tel-'), sg.InputText(key='-Correo-')],
            [sg.Text("Municipio o Alcaldia:", font= ("Arial Black", 8)), sg.Text("Colonia o Barrio:", font= ("Arial Black", 8), pad= ((200,0),(0,10)))],     
            [sg.InputText(key='-Muni-'),sg.InputText(key='-Barrio-')],
            [sg.Text("¿Has estado en contacto con personas con diagnostico confirmado de COVID-19?:               ",  font= ("Arial Black", 8)), sg.Combo(['Si', 'No','No lo se'], key='-Contacto-')],     
            [sg.Text("¿Tienes sintomas de infeccion respiratoria? (si responde un SI contestar la siguiente pregunta", font= ("Arial Black", 8)), sg.Combo(['Si ', 'No '], key='-Cuestion-')],
            [sg.Text("Selecciona los sintomas que presentas:", font= ("Arial Black", 8))],  
            [sg.Combo(['Ninguno', 'Dificultad par respirar','Dolor de cabeza','Dolor de articulaciones','Dolor muscular','Dolor de garganta al comer alimento','Escurrimiento nasal','Todas las anteriores'],key='-Sintomas-')],
            [sg.Text("¿Te has realizado la prueba de COVID-19?:         ", font= ("Arial Black", 8)), sg.Combo(['Si ', 'No ',], key='-Realizado-')],  
            [sg.Text("En caso de haber respondido SI, el resultado es:", font= ("Arial Black", 8)), sg.Combo(['Positivo ', 'Negativo '], key='-Prueba-')],  
            [sg.Button('Guardar Datos', font= ("Arial Black", 8))]]
             
window = sg.Window('Formulario CUCh', layout, icon='icono.ico', resizable='True') #margins= (100,100)


while True:
    NuevoArchivo = open ("Datos.csv", "a")
    event, values = window.read()
    
    Puesto = values['-Puestos-']
    Nombre = values['-Nombre-']
    GeneroH = values['-Hombre-']
    GeneroM = values['-Mujer-']
    Telefono = values['-Tel-']
    Correo = values['-Correo-']
    Municipio = values ['-Muni-']
    Colonia = values ['-Barrio-']
    Pregunta1 = values ['-Contacto-']
    Pregunta2 = values ['-Cuestion-']
    Sintomas = values ['-Sintomas-']
    Realizar = values ['-Realizado-']
    Resultado = values ['-Prueba-']
    
    Datos = [Puesto, Nombre, GeneroH,  GeneroM, Telefono, Correo,  Municipio,  Colonia,  Pregunta1,  Pregunta2,  Sintomas,  Realizar,  Resultado ]
    
    NuevoArchivo.write(str(Datos))
    NuevoArchivo.write("\n")
    NuevoArchivo.close()
    
    window['-Puestos-'].update('')
    window['-Nombre-'].update('')
    window['-Hombre-'].update('')
    window['-Mujer-'].update('')
    window['-Tel-'].update('')
    window['-Correo-'].update('')
    window['-Muni-'].update('')
    window['-Barrio-'].update('')
    window['-Contacto-'].update('')
    window['-Cuestion-'].update('')
    window['-Sintomas-'].update('')
    window['-Realizado-'].update('')
    window['-Prueba-'].update('')
    
   
   

    if event == sg.WINDOW_CLOSED or event == 'Salir':
        break
    
    
window.close()
