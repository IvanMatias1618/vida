from datetime import datetime
from datetime import date

salir = True
ARCHIVOS = (
    './vida/calendario.txt',
    './vida/pendientes.txt',
    './vida/proyectos.txt',
    './vida/tareas_de_casa.txt',
    './vida/urgentes.txt',
)

def verificar_fecha(fecha):
    try:
        datetime.strptime(fecha,"%y-%m-%d")
        return True
    except ValueError:
        return False

def menu():
    while(salir):
        print("Hola :3 \nSoy tu asistente, dime, qué tienes en mente?:\n1) agregar.  2) consultar")
        num = solicitar_numero("Elije:")
        if not dentro_de_rango(num, 0,5):
            break
        if num == 1:
            archivo = seleccionar_archivo()
            definicion = definir()
            agregar(ARCHIVOS[archivo], definicion)
            tarea = f"Titulo:{definicion[0]},\n Tarea: {definicion[1]},\n urgencia: {definicion[2]}"
            print(f" se agrego al archivo: {ARCHIVOS[archivo]},\n La tarea: \n{tarea}")
        if num == 2:
            archivo = seleccionar_archivo()
            consultor(ARCHIVOS[archivo])
            
            
def consultor(ruta):
    with open(ruta, "r",) as f:
        for linea in f:
            if linea.startswith('!'):
                print("El titulo de la tarea es:")
            if linea.startswith(':'):
                print("Tarea: ")
            if linea.startswith('#'):
                print("Prioridad: ")
            if linea.startswith('$'):
                print("Fecha de vencimiento:")
                if linea[1:] == str(datetime.today()):
                    print("La fecha vence hoy")
            print(linea[1:]) #imprime la cadena despues del primer caracter    

def solicitar_numero(mensaje):
    while True:
        try:
            res = input(mensaje).strip()
            num= int(res)
            return num
        except:
            ValueError: print("Por favor escribe un numero.")
            
def dentro_de_rango(num, inf,super):
    if inf < num < super:
        return True
    else: return False

def seleccionar_archivo():
    while True:
        print("Que archivo quieres editar:\n1) Calendario.     2) Pendientes    3) Proyectos\n4) Tareas del hogar.  5) Urgentes")
        while True:
            res = solicitar_numero("Elije:")
            res -= 1
            if dentro_de_rango(res, -1, 5):
                return res
            else:
                continue
             

def definir():
    while True:
        titulo = input("Cual sera el titulo de la tarea?").strip()
        if not titulo:
            print("La tarea esta vacia")
            continue
        tarea = input("Que tarea gustas agregar?")
        if not tarea:
            print("La tarea no puede estar vacia")
            continue
        print("Cual es la fecha de vencimiento:")
        fecha_formato: str
        while True:
            dia = solicitar_numero("Día:")
            if not dentro_de_rango(dia, 0, 32):
                print("El valor deberia de estar dentro de los esperados para un dia. (1-31)")
                continue
            mes = solicitar_numero("Mes:")
            if not dentro_de_rango(mes, 0, 13):
                print("Solo hay 12 meses")
            año = datetime.date.today().year
            fecha_formato = f"{año}-{mes}-{dia}"
            break
            
        while True:
            num = solicitar_numero("Que urgencia tiene? \nDel 1 al 10:")
            if dentro_de_rango(num, 0, 11):
                return titulo, tarea, num, fecha
            else:
                print("El numero debe ser entre 1 y 10")
        
    

def agregar(ruta, definicion):
    titulo = definicion[0]
    tarea = definicion[1]
    urgencia = definicion[2]
    fecha = definicion[3]
    # el modo 'a' posiciona el puntero al final del archivo.
    with open(ruta, 'a') as f:
        linea_a_escribir = f"!{titulo} \n:{tarea}\n#{urgencia}\n ${fecha}\n \n"
        f.write(linea_a_escribir)
        print(f" se agrego al archivo: {ruta}, la tarea: {tarea}")
        
if __name__ == '__main__':
    menu()
