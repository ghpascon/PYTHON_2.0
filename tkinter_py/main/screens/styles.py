import tkinter as tk

title_style = {
        'font': ("Arial", 30),
        'fg': "#ff0000",       # Cor do texto
        'bg': "#000000",       # Cor de fundo
        'anchor': tk.CENTER,   # Centraliza o texto
        'padx': 0,             # Espaçamento interno horizontal
        'pady': 5,             # Espaçamento interno vertical
        'borderwidth': 0,      # Largura da borda
        'relief': tk.RAISED    # Estilo da borda
    }

label_style = {
        'font': ("Arial", 20),
        'fg': "#00ff00",       # Cor do texto
        'bg': "#000000",       # Cor de fundo
        'anchor': tk.CENTER,   # Centraliza o texto
        'padx': 0,            # Espaçamento interno horizontal
        'pady': 5,            # Espaçamento interno vertical
        'borderwidth': 0,      # Largura da borda
        'relief': tk.RAISED    # Estilo da borda
    }

button_style = {
    'font': ("Arial", 20),            # Fonte e tamanho do texto
    'fg': "#ffff00",                   # Cor do texto
    'bg': "#0000ff",                   # Cor de fundo
    'anchor': tk.CENTER,               # Alinhamento do texto
    'padx': 20,                        # Espaçamento interno horizontal
    'pady': 10,                         # Espaçamento interno vertical
    'borderwidth': 3,                  # Largura da borda
    'relief': tk.RAISED,               # Estilo da borda (RAISED, SUNKEN, FLAT, GROOVE, RIDGE)
    'activebackground': "#ff0000",     # Cor de fundo quando o botão está ativo
    'activeforeground': "#ffffff",      # Cor do texto quando o botão está ativo
    'disabledforeground': "#cccccc",    # Cor do texto quando o botão está desativado
    'highlightbackground': "#00ff00",   # Cor de fundo do foco quando o botão não está ativo
    'highlightcolor': "#ff0000",        # Cor de destaque do botão
    'highlightthickness': 2,             # Espessura do destaque
    'state': tk.NORMAL,                  # Estado do botão (NORMAL, DISABLED)
    'justify': tk.CENTER,                # Justificação do texto (LEFT, CENTER, RIGHT)
    'image': None,                       # Imagem a ser exibida no botão (opcional)
    'compound': tk.TOP                   # Como a imagem deve ser posicionada em relação ao texto (TOP, BOTTOM, LEFT, RIGHT)
}
