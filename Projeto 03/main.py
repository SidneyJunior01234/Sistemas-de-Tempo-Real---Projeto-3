import threading
from train import *
from dinamic_viewer import *
from control_view import *
from settings import *

event = threading.Event()

# Criação dos trens
train_1 = Train("T1", YELLOW, 40, 20, 360, 170, event)
train_2 = Train("T2", BLUE, 40, 210, 170, 170, event)
train_3 = Train("T3", RED, 230, 210, 170, 170, event)
train_4 = Train("T4", GREEN, 40, 400, 360, 170, event)

# Criação da Thread de visualização
viewer = threading.Thread(target=dinamic_viewer, args=(train_1, train_2, train_3, train_4))

# Criação da Thread de controle
#control = threading.Thread(target=control_view, args=(train_1, train_2, train_3, train_4))

# Início da thread gráfica
viewer.start()

# Início da thread de controle
#control.start()

# Início das threads dos trens
train_1.start()
train_2.start()
train_3.start()
train_4.start()

# Finalização das threads
while True:
    if not viewer.is_alive():
        event.set()
        train_1.join()
        train_2.join()
        train_3.join()
        train_4.join()
        break