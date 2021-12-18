import numpy as np

def calculate(lista):
  if len(lista) == 9:
    lista = np.array(lista, dtype='float')
    lista = lista.reshape(3, 3)
    calculation = {
      'mean':[list(np.mean(lista, axis=0)), list(np.mean(lista, axis=1)), np.mean(lista)],
      'variance': [list(np.var(lista, axis=0)), list(np.var(lista, axis=1)), np.var(lista)],
      'standard deviation': [list(np.std(lista, axis=0)), list(np.std(lista, axis=1)), np.std(lista)],
      'max': [list(np.max(lista, axis=0)), list(np.max(lista, axis=1)), np.max(lista)],
      'min': [list(np.min(lista, axis=0)), list(np.min(lista, axis=1)), np.min(lista)],
      'sum': [list(np.sum(lista, axis=0)), list(np.sum(lista, axis=1)), np.sum(lista)],
    }
    return calculation
  else:
    raise ValueError('List must contain nine numbers.')

  