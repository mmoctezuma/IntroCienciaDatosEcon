OK_FORMAT = True

test = {   'name': 'q5',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> assert isinstance(serie_col, pd.Series)\n'
                                               ">>> assert isinstance(serie_col.index, pd.PeriodIndex), 'El indice debe ser PeriodIndex'\n"
                                               ">>> assert str(serie_col.index.freqstr).startswith(('A', 'Y')), 'Frecuencia debe ser anual'\n"
                                               ">>> assert serie_col.name == 'inflacion_COL'\n"
                                               ">>> assert len(serie_col) == 24, 'Debe tener 24 observaciones (2000-2023)'\n"
                                               '>>> assert isinstance(n_obs_col, int) and 20 <= n_obs_col <= 24\n'
                                               '>>> assert isinstance(anio_max_inflacion_col, int)\n'
                                               '>>> assert 2000 <= anio_max_inflacion_col <= 2023\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
