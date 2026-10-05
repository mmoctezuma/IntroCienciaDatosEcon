OK_FORMAT = True

test = {   'name': 'q1',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': ">>> assert isinstance(tabla_freq_region, pd.Series), 'tabla_freq_region debe ser pd.Series'\n"
                                               ">>> assert len(tabla_freq_region) == 2, 'Debe haber 2 categorias'\n"
                                               ">>> assert tabla_freq_region['latam'] == 19, 'latam debe tener 19 paises'\n"
                                               ">>> assert tabla_freq_region['referencia'] == 8, 'referencia debe tener 8 paises'\n"
                                               ">>> assert moda_region == 'latam', 'la moda debe ser latam'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
