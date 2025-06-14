salir = True
ARCHIVOS = (
    './vida/calendario.txt',
    './vida/pendientes.txt',
    './vida/proyectos.txt',
    './vida/tareas_de_casa.txt',
    './vida/urgentes.txt',
)


def menu():
    while(salir):
        print("Hola :3 \nSoy tu asistente, dime, qué tienes en mente?:\n1) agregar.  2) consultar")
        num = solicitar_numero("Elije:")
        if not dentro_de_rango(num, 0,2):
            break
        if num == 1:
            archivo = seleccionar_archivo()
            definicion = definir()
            agregar(ARCHIVOS[archivo], definicion)
            tarea = f"Titulo:{definicion[0]},\n Tarea: {definicion[1]},\n urgencia: {definicion[2]}"
            print(f" se agrego al archivo: {ARCHIVOS[archivo]},\n La tarea: \n{tarea}")
        pass    
        
    

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
        while True:
            num = solicitar_numero("Que urgencia tiene? \nDel 1 al 10:")
            if dentro_de_rango(num, 0, 11):
                return titulo, tarea, num
            else:
                print("El numero debe ser entre 1 y 10")
        
    

def agregar(ruta, definicion):
    titulo = definicion[0]
    tarea = definicion[1]
    urgencia = definicion[2]
    # el modo 'a' posiciona el puntero al final del archivo.
    with open(ruta, 'a') as f:
        linea_a_escribir = f"!{titulo} \n:{tarea}\n#{urgencia}\n \n"
        f.write(linea_a_escribir)
        print(f" se agrego al archivo: {ruta}, la tarea: {tarea}")
        
if __name__ == '__main__':
    menu()
