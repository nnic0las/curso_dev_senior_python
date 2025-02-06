class NuevoCanal:
    def __init__(self):
        self._suscriptor = []
        self._laters_news = None

    def suscribir(self, suscribirse):
        self._suscriptor.append(suscribirse)   

    def desuscribir(self, suscribirse):
        self._suscriptor.remove(suscribirse)

    def notificacion(Self):
        for sus in Self._suscriptor:
            sus.update(Self._laters_news)

    def publicacion(self, news):
        self._laters_news = news
        print(f"Notificacion publica: {news}")
        self.notificacion()

class Suscriptores:
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} ha recibido la notificacion: {news}")
cana1 = NuevoCanal()

sus1 = Suscriptores("juan")
sus2 = Suscriptores("eder")
sus3 = Suscriptores("carlos")

cana1.suscribir(sus1)
cana1.suscribir(sus2)

cana1.publicacion("Tenemos tutoria el dia de hoy ")




