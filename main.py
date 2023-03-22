import tkinter as tk
import random

def roll_dice():
    result = random.randint(1, 12)
    label_result.config(text=f"O resultado do dado é: {result}")


def open_window1():
    # anotacoes de como daria certo:
    # window1 = tk.Toplevel(root)
    # window1.title("Janela 1")
    # window1.geometry("400x300")
    # label = tk.Label(window1, text="Gere um numero de 1 a 12")
    # label.pack()

    def roll_dice():
        result = random.randint(1, 12)
        label_result.config(text=f"O resultado do dado é: {result}")

    window1 = tk.Toplevel(root)
    window1.title("Simulador de Dado")
    window1.geometry("300x200")
    button_roll = tk.Button(window1, text="Lançar o dado", command=roll_dice)
    button_roll.pack(pady=20)
    label_result = tk.Label(window1, text="")
    label_result.pack()

def open_window2():
    def nomes():
        gender = var_gender.get()  # obtém o valor selecionado no Radiobutton
        if gender == 1:  # se for masculino
            # Lista de sugestões de nomes masculinos
            names = ["Gabriel", "Lucas", "Mateus", "Pedro", "João", "Daniel", "Felipe", "André"]
        else:  # se for feminino
            # Lista de sugestões de nomes femininos
            names = ["Maria", "Ana", "Beatriz", "Clara", "Laura", "Juliana", "Isabela", "Mariana"]
        # Seleciona uma sugestão aleatoriamente
        suggestion = random.choice(names)
        # Atualiza o label com a sugestão de nome
        label_suggestion.config(text=f"Que tal o nome {suggestion}?")

    # Cria a janela principal
    window2 = tk.Toplevel(root)
    window2.title("Sugestão de Nome")
    window2.geometry("300x200")

    # Cria o label para selecionar o gênero
    label_gender = tk.Label(window2, text="Selecione o gênero:")
    label_gender.pack(pady=10)

    # Cria a variável para armazenar o valor selecionado no Radiobutton
    var_gender = tk.IntVar()

    # Cria os Radiobuttons para selecionar o gênero
    male_button = tk.Radiobutton(window2, text="Masculino", variable=var_gender, value=1)
    male_button.pack()

    female_button = tk.Radiobutton(window2, text="Feminino", variable=var_gender, value=2)
    female_button.pack()

    # Cria o botão para sugerir um nome
    button_suggest = tk.Button(window2, text="Sugerir Nome", command=nomes)
    button_suggest.pack(pady=10)

    # Cria o label para exibir a sugestão de nome
    label_suggestion = tk.Label(window2, text="")
    label_suggestion.pack(pady=20)

root = tk.Tk()
root.title("Menu")
root.geometry("400x300")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Abrir janela 1", command=open_window1)
file_menu.add_command(label="Abrir janela 2", command=open_window2)

menu_bar.add_cascade(label="Opções", menu=file_menu)

root.config(menu=menu_bar)

root.mainloop()