import tkinter as tk
from tkinter import messagebox

from parser import parse_input
from minizinc_generator import generate_minizinc


def solve():

    try:
        input_text = input_area.get("1.0", tk.END)

        N, M, cities = parse_input(input_text)

        code = generate_minizinc(N, M, cities)

        output_area.delete("1.0", tk.END)
        output_area.insert(tk.END, code)

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Entrada inválida:\n{e}"
        )


root = tk.Tk()
root.title("Proyecto Optimización - Benito G")

# Entrada

tk.Label(root, text="Entrada").pack()

input_area = tk.Text(root, height=12, width=80)
input_area.pack()

input_area.insert(
    tk.END,
"""12
5
Palmira 2 3
Cali 10 2
Buga 11 0
Tulua 0 3
Rio Frio 1 2"""
)

# Botón para generar el modelo en MiniZinc

tk.Button(
    root,
    text="Generar Modelo MiniZinc",
    command=solve
).pack(pady=10)

# Salida código Minizinc

tk.Label(root, text="Código MiniZinc").pack()

output_area = tk.Text(root, height=20, width=80)
output_area.pack()

root.mainloop()