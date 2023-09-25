class Finanzas:

  def __init__(self, usuario, ingresos):
    self.usuario = usuario
    self.ingresos = ingresos
    self.conceptos = {}

  def agregar_concepto(self, concepto, valor_concepto):
    if concepto in self.conceptos.keys():
      print('Ya existe un concepto con este mismo nombre ')
    else:
      self.conceptos[concepto] = valor_concepto
