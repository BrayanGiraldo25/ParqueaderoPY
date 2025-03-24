from datetime import datetime
import random


def parqueadero():
    registros = {}
    ##Espacios disponibles del parqueadero
    espacios_disponibles = [
        "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
        "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8"
    ]
    #Tarifa por hora
    Tarifa = 2000


    while True:
        #En caso de ya no haber mas espacios
        if not espacios_disponibles:
            print("⚠️ Ya no hay más espacios, no se pueden aceptar más autos. ⚠️")
            break

        #Placa del vehiculo
        Placa = input('Digite la placa: ').upper()

        if Placa in registros:
        #Placa ya registrada
            print("⚠️ Esta placa ya está registrada. Intente con otra. ⚠️")
            continue
        #Informacion general del vehiculo a registrar
        Tipo_Vehiculo = input("¿Qué tipo de vehículo maneja? (Carro/Moto): ")
        Hora_Entrada = input("Hora de entrada del vehículo (HH:MM): ")
        espacio_asignado = random.choice(espacios_disponibles)
        espacios_disponibles.remove(espacio_asignado)

        #Informacion registrada
        registros[Placa] = {
            "Tipo": Tipo_Vehiculo,
            "Hora_Entrada": Hora_Entrada,
            "Espacio": espacio_asignado
        }

        print(f"✅ Vehículo registrado en el espacio {espacio_asignado}")

        #Opcion para registrar mas vehiculos
        Confirmar = input("¿Desea registrar otro vehículo? (Si/No): ").upper()
        if Confirmar == 'NO':
            break


    while True:
        #Opcion para salida de vehiculos
        Salida = input("\n¿Desea remover algún vehículo? (Si/No): ").upper()
        if Salida == 'NO':
            break

        Remover = input("Ingrese la placa del vehículo a remover: ").upper()
        if Remover in registros:
        #Informacion de salida
            datos = registros[Remover]
            Hora_Salida = input("Ingrese la hora de salida (HH:MM): ")

        #Codigo de salida
            formato = "%H:%M"
            entrada_dt = datetime.strptime(datos["Hora_Entrada"], formato)
            salida_dt = datetime.strptime(Hora_Salida, formato)
            Tiempo_Total = salida_dt - entrada_dt
            horas = Tiempo_Total.seconds // 3600
            minutos = (Tiempo_Total.seconds % 3600) // 60

            tiempo_horas = horas + (minutos / 60)
            costo_total = tiempo_horas * Tarifa


            espacios_disponibles.append(datos["Espacio"])
            del registros[Remover]
        #Registro de salida
            print(f"✅ Vehículo con placa {Remover} removido.")
            print(f"Tiempo total estacionado: {horas} horas y {minutos} minutos.")
            print(f'La tarifa total del vehiculo seria {costo_total}')
            print(f"Espacio {datos['Espacio']} ahora está disponible.")
        else:
            print("⚠️ La placa ingresada no está registrada.")

    #Vehiculos dentro del parqueadero
    print("\n🚗🚙 Parqueadero 🚗🚙")
    for placa, datos in registros.items():
        print(f"\n🔹 Placa: {placa}")
        print(f'   🔸 Tipo de vehículo: {datos["Tipo"]}')
        print(f'   🔸 Hora de entrada: {datos["Hora_Entrada"]}')
        print(f'   🔸 Espacio asignado: {datos["Espacio"]}')


if __name__ == '__main__':
    parqueadero()
