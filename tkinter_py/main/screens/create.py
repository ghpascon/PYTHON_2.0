# create.py
import tkinter as tk

def create_label(frame, txt, style):
    """
    Cria um label dentro do frame dado e retorna a instância do label.
    """
    label = tk.Label(frame, text=txt, **style)
    label.pack(side=tk.TOP, pady=10)
    return label  # Retorna a instância do label criado

def create_button(frame, txt, style, command=None):
    """
    Cria um botão dentro do frame dado e retorna a instância do botão.
    :param frame: O frame onde o botão será adicionado
    :param txt: O texto que será exibido no botão
    :param style: O dicionário de estilo para o botão
    :param command: A função que será chamada quando o botão for clicado (opcional)
    """
    button = tk.Button(frame, text=txt, command=command, **style)
    button.pack(side=tk.TOP, pady=10)
    return button  # Retorna a instância do botão criado