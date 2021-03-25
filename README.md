# Evidencia_1_ED
s
eparador = ("*" * 40)
usuario = input("¿Cuál es tu nombre? \n")
print(f"\n             ¡Hola {usuario}!")

while True:
    print(f"""{separador}
    Bienvenido al menú principal\n
        ¿Qué desea hacer?\n
1.- Refistrar una venta.
2.- Consultar un venta.
3.- Salir.
{separador}\n""")
    op = input("Insertar opción: ")
    if op == "3":
        print(f"\n¡Gracias por haber comprado, {usuario}!")
        break
