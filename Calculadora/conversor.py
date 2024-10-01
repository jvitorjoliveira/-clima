import tkinter as tk
from tkinter import messagebox

# Dados históricos de temperatura
historical_min_avg_temp = {1: 21, 2: 21, 3: 20, 4: 18, 5: 15, 6: 14, 7: 14, 8: 15, 9: 18, 10: 19, 11: 20, 12: 21}
historical_max_avg_temp = {1: 31, 2: 32, 3: 32, 4: 31, 5: 29, 6: 29, 7: 29, 8: 31, 9: 33, 10: 33, 11: 32, 12: 32}

# Função para calcular a diferença de temperatura
def temp_dif():
    try:
        day = int(day_var.get())
        month = int(month_var.get())
        max_temp = int(max_temp_var.get())
        min_temp = int(min_temp_var.get())

        # Comparação com a média histórica
        avg_max_temp = historical_max_avg_temp[month]
        avg_min_temp = historical_min_avg_temp[month]
        max_diff = max_temp - avg_max_temp
        min_diff = min_temp - avg_min_temp

        # Resultados
        if max_diff > 0:
            result_max.config(fg="orange2", text=f"Acima da média máxima em +{max_diff}°C")
        else:
            result_max.config(fg="DodgerBlue2", text=f"Abaixo da média máxima em {max_diff}°C")

#

        if min_diff > 0:
            result_min.config(fg="orange2", text=f"Acima da média mínima em +{min_diff}°C")
        else:
            result_min.config(fg="DodgerBlue2", text=f"Abaixo da média mínima em {min_diff}°C")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Função para limpar campos e resultados
def clear():
    for var in [day_var, month_var, max_temp_var, min_temp_var]:
        var.set("")
    result_max.config(text="")
    result_min.config(text="")

# Interface
root = tk.Tk()
root.title("Comparador de Temperatura")
root.geometry("420x700")
root.resizable(False, False)
root.config(bg="#f0f0f0")

# Descrição
description = tk.Label(root,
                       text="Como a temperatura atual se compara com as médias históricas em São José do Rio Preto (SP)? "
                            "Insira os dados abaixo e descubra você mesmo:",
                       font=("Franklin Gothic", 13), wraplength=380, bg="#f0f0f0", justify="center")
description.pack(pady=10)

# Variáveis
day_var = tk.StringVar()
month_var = tk.StringVar()
max_temp_var = tk.StringVar()
min_temp_var = tk.StringVar()

# Widgets
tk.Label(root, text="Que dia é hoje?", font=("Franklin Gothic Book", 12), bg="#f0f0f0").pack(pady=5)
day_menu = tk.OptionMenu(root, day_var, *range(1, 32))
day_menu.config(font=("Franklin Gothic Book", 10), bg="white")
day_menu.pack()

tk.Label(root, text="De qual mês?", font=("Franklin Gothic", 12), bg="#f0f0f0").pack(pady=5)
month_menu = tk.OptionMenu(root, month_var, *range(1, 13))
month_menu.config(font=("Franklin Gothic", 10), bg="white")
month_menu.pack()

tk.Label(root, text="Temperatura máxima (°C)", font=("Franklin Gothic Book", 12), bg="#f0f0f0").pack(pady=5)
tk.Entry(root, textvariable=max_temp_var, width=10, font=("Franklin Gothic Book", 12)).pack()

tk.Label(root, text="Temperatura mínima (°C)", font=("Franklin Gothic Book", 12), bg="#f0f0f0").pack(pady=5)
tk.Entry(root, textvariable=min_temp_var, width=10, font=("Franklin Gothic Book", 12)).pack()

# Botões de ação
tk.Button(root, text="Verificar", command=temp_dif, font=("Franklin Gothic", 12), bg="forestgreen", fg="white").pack(
    pady=10)
tk.Button(root, text="Limpar", command=clear, font=("Franklin Gothic", 12), bg="brown3", fg="white").pack(pady=5)

# Resultados
result_max = tk.Label(root, text="", font=("Franklin Gothic", 13, "bold"), bg="#f0f0f0")
result_max.pack(pady=5)
result_min = tk.Label(root, text="", font=("Franklin Gothic", 13, "bold"), bg="#f0f0f0")
result_min.pack(pady=5)

# Rodapé
footer = tk.Label(root, text="*Base de dados: Portal Agrometeorológico e Hidrológico do Estado de São Paulo.",
                  font=("Franklin Gothic Book", 9), bg="#f0f0f0", anchor="w")
footer.pack(side="bottom", fill="x")

# Executar o programa
root.mainloop()