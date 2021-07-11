import sys #Modulo che fornisce l'accesso ad alcune variabili , in questo caso sys.exit
from PyQt5.QtWidgets import QApplication,QWidget

from home.views.GUI_Home import Home  #importa dalla directory home "VistaHome"

if __name__ == '__main__':

    #istanziamento per iniziare un'applicazione
    app = QApplication(sys.argv)
    #creo un oggetto della classe importata
    vista_home = Home()
    # serve a mostrare a schermo la finestra vista home
    vista_home.show()
    #esegue l'applicazione
    sys.exit(app.exec())

    #VERSIONE QT:

#import sys  # Modulo che fornisce l'accesso ad alcune variabili , in questo caso sys.exit
#from PyQt5.QtWidgets import QApplication
#from home.views.VistaHome import VistaHome  # importa dalla directory home "VistaHome"

#if __name__ == '__main__':

 #   app = QApplication(sys.argv)
  #  main = VistaHome()
   # main.show()
    #sys.exit(app.exec_())