OK_FORMAT = True

test = {   'name': 'q4',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> assert isinstance(mediana_desempleo_grupo, pd.Series)\n'
                                               '>>> assert len(mediana_desempleo_grupo) == 2\n'
                                               ">>> assert set(mediana_desempleo_grupo.index) == {'latam', 'referencia'}\n"
                                               '>>> assert isinstance(region_mayor_desempleo, str)\n'
                                               '>>> _vals = list(mediana_desempleo_grupo.values)\n'
                                               ">>> assert _vals[0] >= _vals[1], 'Debe estar ordenado de mayor a menor'\n"
                                               '>>> assert isinstance(diferencia_medianas, float)\n'
                                               ">>> _exp = float(mediana_desempleo_grupo['latam'] - mediana_desempleo_grupo['referencia'])\n"
                                               '>>> assert abs(diferencia_medianas - _exp) < 0.001\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
