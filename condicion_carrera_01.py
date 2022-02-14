import threading
import time

class Recepcion():
    def __init__(self, conta = 0):
        self.locket = threading.Lock()
        self.conta_send = conta
        

    def paso_pacientes(self):
        lista_pacientes=["juan","pedro","susanna","liz"]
        self.locket.acquire()
        try:
            paciente = lista_pacientes[self.conta_send]
            print("Paciente esperando ",paciente )
            paciente_ingreso = lista_pacientes[self.conta_send]
            print("Acaba de pasar ", paciente_ingreso)
            self.conta_send += 1
           
        finally:
            self.locket.release()
    
def func_conta(x):
    for y in range(2):
        time.sleep(2)
        x.paso_pacientes()
        

if __name__ == "__main__":
    paso = Recepcion()
    for y in range(2):
        consult = threading.Thread(target=func_conta, args=(paso,))
        consult.start()

    