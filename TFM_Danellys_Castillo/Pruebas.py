
import ValidacionDatosTrafico
import PruebaFlujos
import PruebaAgregarConmutador
import PruebaEliminarConmutador
import PruebaTiempoDescubrimiento

#Prueba de Flujos
def PruebaDeFlujos(QFlows, QFpr, IP_test1, ControllerType):
    #Verificación de Errores
    flows = ValidacionDatosTrafico.flowerror(QFlows)
    fpr = ValidacionDatosTrafico.fprerror(QFpr)
    IP_test=ValidacionDatosTrafico.check_iptest(IP_test1)
    #Ejecución de Prueba de Flujos
    PruebaFlujos.prueba(flows,fpr, IP_test, ControllerType)
#Prueba Agregar Conmutador
def PruebaDeAgregarConmutador(QuantityCtrl,ControllerType, IP_Address):
    PruebaAgregarConmutador.prueba(QuantityCtrl,ControllerType, IP_Address)

#Prueba Eliminar Conmutador
def PruebaDeEliminarConmutador(QuantityCtrl,ControllerType):
    PruebaEliminarConmutador.prueba(QuantityCtrl,ControllerType)

#Prueba Calcular Latencia
def CalcularLatencia(QuantityCtrl, QSwitch, ControllerType):
    PruebaTiempoDescubrimiento.CalcularLatencia(QuantityCtrl, QSwitch, ControllerType)

#Prueba Capturar Paquetes
def CapturarPaquetes(IP_Address):
    PruebaTiempoDescubrimiento.CapturarPaquetes(IP_Address)

