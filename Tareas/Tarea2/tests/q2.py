OK_FORMAT = True

test = {   'name': 'q2',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': ">>> assert isinstance(desc_pib, pd.Series), 'desc_pib debe ser pd.Series'\n"
                                               '>>> assert list(desc_pib.index) == [\'media\', \'mediana\', \'desv_std\', \'minimo\', \'maximo\'], "Las claves deben ser '
                                               '[\'media\',\'mediana\',\'desv_std\',\'minimo\',\'maximo\']"\n'
                                               ">>> assert desc_pib['media'] > desc_pib['mediana'], 'Se espera media > mediana'\n"
                                               ">>> assert isinstance(asimetria_pib, float), 'asimetria_pib debe ser float'\n"
                                               ">>> assert asimetria_pib > 0, 'Se espera asimetria positiva'\n"
                                               ">>> assert desc_pib['minimo'] < desc_pib['mediana'] < desc_pib['maximo']\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
