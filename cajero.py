# --- CONFIGURACIÓN INICIAL ---
# El saldo inicia con un número flotante (float)
saldo = 1000.50
pin_correcto = "1234"
intentos = 0
autenticado = False

print("====================================")
print("  🤖 BIENVENIDO AL CAJERO AUTOMÁTICO  ")
print("====================================\n")

# --- PASO 1: AUTENTICACIÓN (Máximo 3 intentos) ---
while intentos < 3:
    pin_ingresado = input("Ingresa tu PIN de 4 dígitos: ")

    if pin_ingresado == pin_correcto:
        autenticado = True
        print("\n✅ ¡PIN correcto! Accediendo a tu cuenta...\n")
        break  # Rompe el bucle si el PIN es correcto
    else:
        intentos += 1  # Asignación aumentada para contar errores
        intentos_restantes = 3 - intentos
        print(f"❌ PIN incorrecto. Te quedan {intentos_restantes} intento(s).\n")

# --- PASO 2: MENÚ PRINCIPAL ---
if autenticado:
    mantenimiento = True

    while mantenimiento:
        print("------------------------------------")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        print("------------------------------------")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            # Mostrar saldo con formato de 2 decimales
            print(f"\n💰 Tu saldo actual es: ${saldo:.2f}\n")

        elif opcion == "2":
            monto_deposito = float(input("\n¿Cuánto dinero deseas depositar?: $"))

            if monto_deposito > 0:
                saldo += monto_deposito  # Asignación aumentada (Suma)
                print(f"✅ Depósito exitoso. Nuevo saldo: ${saldo:.2f}\n")
            else:
                print("⚠️ El monto a depositar debe ser mayor a 0.\n")

        elif opcion == "3":
            monto_retiro = float(input("\n¿Cuánto dinero deseas retirar?: $"))
            comision = 1.50  # 👈 Nueva variable para la comisión

            if monto_retiro > saldo:
                print("❌ Fondos insuficientes. No puedes retirar más de lo que tienes.\n")
            elif monto_retiro > 500:  # 👈 MEJORA 1: Verificamos el límite máximo
                print("⚠️ Límite excedido. No puedes retirar más de $500.00 en una sola transacción.\n")
            elif monto_retiro <= 0:
                print("⚠️ Ingresa un monto válido para retirar.\n")
            else:
                # 👈 MEJORA 2: Aplicamos asignaciones aumentadas para restar ambos cobros
                saldo -= monto_retiro
                saldo -= comision

                print(f"💵 Retiro exitoso. Retiraste: ${monto_retiro:.2f}")
                print(f"💸 Comisión bancaria aplicada: ${comision:.2f}")
                print(f"💰 Nuevo saldo disponible: ${saldo:.2f}\n")

        else:
            print("⚠️ Opción no válida. Por favor elige entre 1 y 4.\n")
else:
    print("🔒 Tarjeta bloqueada por seguridad. Contacta a tu banco.")

    