from tkinter import *
from tkinter import ttk
from math import pi


def desabilitar_entrada_pot_tensao():
    entrada_potencia.config(state='disabled')
    entrada_tensao1.config(state='disabled')
    entrada_rpm1.config(state='disabled')


def habilitar_entrada_pot_tensao():
    entrada_potencia.config(state='normal')
    entrada_tensao1.config(state='normal')
    entrada_rpm1.config(state='normal')


def desabilitar_entrada_tensao_corrente():
    entrada_tensao2.config(state='disabled')
    entrada_corrente.config(state='disabled')
    entrada_rpm2.config(state='disabled')


def habilitar_entrada_tensao_corrente():
    entrada_tensao2.config(state='normal')
    entrada_corrente.config(state='normal')
    entrada_rpm2.config(state='normal')


def tratar_input(valor):
    return float(valor.replace(',', '.'))


def atualizar_resultados():
    if tipo_calculo.get() == 'Potência (W) e Tensão (V)':
        habilitar_entrada_pot_tensao()
        desabilitar_entrada_tensao_corrente()

        if all([var_potencia.get(), var_rpm1.get(), var_tensao1.get()]):
            potencia = tratar_input(var_potencia.get())
            rpm = tratar_input(var_rpm1.get())
            tensao = tratar_input(var_tensao1.get())

            torque = potencia / ((rpm * pi) / 60)
            corrente = potencia / tensao

            resultado_rpm.set(round(rpm, 4))
            resultado_tensao.set(round(tensao, 4))
            resultado_corrente.set(round(corrente, 4))
            resultado_potencia.set(round(potencia, 4))
            resultado_torque.set(round(torque, 4))
    else:
        desabilitar_entrada_pot_tensao()
        habilitar_entrada_tensao_corrente()
        
        if all([var_tensao2.get(), var_rpm2.get(), var_corrente.get()]):
            tensao = tratar_input(var_tensao2.get())
            rpm = tratar_input(var_rpm2.get())
            corrente = tratar_input(var_corrente.get())

            potencia = tensao * corrente
            torque = potencia / ((rpm * pi) / 60)

            resultado_rpm.set(round(rpm, 4))
            resultado_tensao.set(round(tensao, 4))
            resultado_corrente.set(round(corrente, 4))
            resultado_potencia.set(round(potencia, 4))
            resultado_torque.set(round(torque, 4))

    janela.after(100, atualizar_resultados)


# Criação da janela principal
janela = Tk()
janela.geometry('300x515+0+0')
janela.resizable(False, False)
janela.title('Parâmetros de Motores DC')

tipo_calculo = StringVar(value='Potência (W) e Tensão (V)')
Label(janela, text='Informações conhecidas:', font='Arial 10 bold').grid(row=0, column=0, padx=10, sticky='NW')

combo_tipo_calculo = ttk.Combobox(janela, values=['Potência (W) e Tensão (V)', 'Tensão (V) e Corrente (A)'], font='Arial 10', textvariable=tipo_calculo, width=37)
combo_tipo_calculo.grid(row=1, column=0, sticky='NEW', padx=10)

# Frame para Potência (W) e Tensão (V)
frame_pot_tensao = LabelFrame(janela, text='Potência (W) e Tensão (V)', font='Arial 10 bold')
frame_pot_tensao.grid(row=3, column=0, sticky='NEW', padx=10, pady=10)

var_potencia = StringVar()
Label(frame_pot_tensao, text='Potência (W):', font='Arial 10').grid(row=0, column=0, padx=10, pady=5)
entrada_potencia = Entry(frame_pot_tensao, textvariable=var_potencia, font='Arial 10', width=21)
entrada_potencia.grid(row=0, column=1, padx=10)

var_tensao1 = StringVar()
Label(frame_pot_tensao, text='Tensão (V):', font='Arial 10').grid(row=1, column=0, padx=10, pady=5)
entrada_tensao1 = Entry(frame_pot_tensao, textvariable=var_tensao1, font='Arial 10', width=21)
entrada_tensao1.grid(row=1, column=1, padx=10)

var_rpm1 = StringVar()
Label(frame_pot_tensao, text='RPM:', font='Arial 10').grid(row=2, column=0, padx=10, pady=5)
entrada_rpm1 = Entry(frame_pot_tensao, textvariable=var_rpm1, font='Arial 10', width=21)
entrada_rpm1.grid(row=2, column=1, padx=10)

# Frame para Tensão (V) e Corrente (A)
frame_tensao_corrente = LabelFrame(janela, text='Tensão (V) e Corrente (A)', font='Arial 10 bold')
frame_tensao_corrente.grid(row=4, column=0, sticky='NEW', padx=10, pady=10)

var_tensao2 = StringVar()
Label(frame_tensao_corrente, text='Tensão (V):', font='Arial 10').grid(row=0, column=0, padx=10, pady=5)
entrada_tensao2 = Entry(frame_tensao_corrente, textvariable=var_tensao2, font='Arial 10', width=21)
entrada_tensao2.grid(row=0, column=1, padx=10)

var_corrente = StringVar()
Label(frame_tensao_corrente, text='Corrente (A):', font='Arial 10').grid(row=1, column=0, padx=10, pady=5)
entrada_corrente = Entry(frame_tensao_corrente, textvariable=var_corrente, font='Arial 10', width=21)
entrada_corrente.grid(row=1, column=1, padx=10)

var_rpm2 = StringVar()
Label(frame_tensao_corrente, text='RPM:', font='Arial 10').grid(row=2, column=0, padx=10, pady=5)
entrada_rpm2 = Entry(frame_tensao_corrente, textvariable=var_rpm2, font='Arial 10', width=21)
entrada_rpm2.grid(row=2, column=1, padx=10)

# Frame para Características do Motor
frame_caracteristicas_motor = LabelFrame(janela, text='Características do Motor', font='Arial 10 bold')
frame_caracteristicas_motor.grid(row=5, column=0, sticky='NEW', padx=10, pady=10)

# Variáveis para resultados
resultado_rpm = IntVar()
resultado_tensao = StringVar()
resultado_corrente = StringVar()
resultado_potencia = StringVar()
resultado_torque = StringVar()

# Labels e Entradas para resultados
parametros = {
    "RPM:": resultado_rpm,
    'Tensão (V):': resultado_tensao,
    'Corrente Pico (A):': resultado_corrente,
    'Potência (W):': resultado_potencia,
    'Pico Torque (N·m):': resultado_torque
}

for linha, (label, var) in enumerate(parametros.items()):
    Label(frame_caracteristicas_motor, text=label, font='Arial 10').grid(row=linha, column=0, padx=10, pady=5)
    Entry(frame_caracteristicas_motor, textvariable=var, font='Arial 10', width=15, state='readonly', justify='center').grid(row=linha, column=1, padx=10)

# Inicia o processo de atualização
atualizar_resultados()

# Inicializa a interface
janela.mainloop()
