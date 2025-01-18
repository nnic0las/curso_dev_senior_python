##patron de diseño singleton
class SingletonCreacionDeInstancia:

    _instacia = None

    def __new__(cls, *args, **kwargs):

        if not cls._instacia:
            cls._instacia = super(SingletonCreacionDeInstancia, cls)._new_(cls)
            return cls._instacia
