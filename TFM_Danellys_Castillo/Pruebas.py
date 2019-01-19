import ValidacionDatosTrafico
import PruebaFlujos
import PruebaAgregarConmutador
import PruebaEliminarConmutador
import PruebaTiempoDescubrimiento

#Prueba de Flujos
def PruebaDeFlujos(QFlows, QFpr, IP_test1, ControllerType):
    flows = ValidacionDatosTrafico.flowerror(QFlows)
    fpr = ValidacionDatosTrafico.fprerror(QFpr)
    IP_test=ValidacionDatosTrafico.check_iptest(IP_test1)
    PruebaFlujos.prueba(flows,fpr, IP_test, ControllerType)
def PruebaDeAgregarConmutador(QuantityCtrl,ControllerType, IP_Address):
    PruebaAgregarConmutador.prueba(QuantityCtrl,ControllerType, IP_Address)
def PruebaDeEliminarConmutador(QuantityCtrl,ControllerType):
    PruebaEliminarConmutador.prueba(QuantityCtrl,ControllerType)
def CalcularLatencia(QuantityCtrl, QSwitch, ControllerType):
    PruebaTiempoDescubrimiento.CalcularLatencia(QuantityCtrl, QSwitch, ControllerType)
def CapturarPaquetes(IP_Address):
    PruebaTiempoDescubrimiento.CapturarPaquetes(IP_Address)