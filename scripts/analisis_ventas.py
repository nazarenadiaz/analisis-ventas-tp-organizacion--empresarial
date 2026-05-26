import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos/ventas.csv")


ventas_totales = df["monto_total"].sum()
print(f"Ventas totales: ${ventas_totales:,.2f}")

mas_vendido = df.groupby("productos")["cantidad"].sum().idxmax()
print(f"Producto mas vendido: {mas_vendido}")

# Indicador 3: Ventas por mes
ventas_por_mes = df.groupby("mes")["monto_total"].sum().reset_index()
print(ventas_por_mes)


plt.figure(figsize=(10, 5))
plt.bar(ventas_por_mes["mes"], ventas_por_mes["monto_total"], color="steelblue")
plt.title("Evolucion de Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Monto Total ($)")
plt.tight_layout()
plt.savefig("resultados/grafico_ventas.png")
plt.show()
