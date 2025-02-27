# Detector.py
#
# Diego Iván Martínez Escobar, 2025
#
# Programa de Honores
# Universidad de las Américas Puebla

class Detector:
    def __init__(self, func_detector, param_dict):
        """
        La clase detector es la encargada de generar las detecciones usando
        alguno de los métodos disponibles.

        El diccionario de parámetros contiene los valores adicionales que las funciones detector necesitan
        para funcionar. Estos parámetros están documentados en cada una de las definiciones de las funciones
        detector.

        :param func_detector: Función detector de la forma def detector(np.ndarray, param_dic)
        :param param_dict: El diccionario de parámetros, de la forma {string: Any, ...}
        """
        self.func_detector = func_detector
        self.param_dict = param_dict

    def detectar_objetos(self, imagen):
        """
        Genera una detección basada en su función detector interna. El valor de retorno es una lista de tuplas, cada
        una con cuatro elementos de la forma (x1, y1, x2, y2).  Su interpretación se muestra a continuación:
         (x1, y1)
            #────────────────────────────┐
            │                            │
            │                            │
            │                            │
            │                            │
            │          Detección         │
            │                            │
            │                            │
            │                            │
            │                            │
            │                            │
            └────────────────────────────#
                                    (x2, y2)
        :param imagen: un np.ndarray que representa una imagen R8G8B8
        :return: Una lista de tuplas de la forma [(x1, y1, x2, y2), ...], donde (x1, y1) es la esquina superior izquierda
        de la detección, y (x2, y2) la esquina inferior derecha.
        """
        return self.func_detector(imagen, self.param_dict)