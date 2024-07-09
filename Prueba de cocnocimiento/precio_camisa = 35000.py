precio_camisa = 35.000
precio_pantalon = 75.000
precio_celular = 900.000

descuento = 0.14
subtotal_costa_azul = precio_camisa + precio_pantalon
monto_descuento = subtotal_costa_azul * descuento
total_costa_azul = subtotal_costa_azul - monto_descuento

total_compras = total_costa_azul + precio_celular

print ("subtotal en almcan costa azul:", subtotal_costa_azul)
print ("descuento en almacen costa azul: ", monto_descuento)
print ("total gastado en compras: ", total_compras)


