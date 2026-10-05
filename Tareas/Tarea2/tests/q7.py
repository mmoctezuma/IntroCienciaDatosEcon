OK_FORMAT = True

test = {   'name': 'q7',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': ">>> assert isinstance(acf_col, np.ndarray), 'acf_col debe ser np.ndarray'\n"
                                               ">>> assert len(acf_col) == 6, 'Debe tener 6 elementos (lags 0-5)'\n"
                                               ">>> assert abs(acf_col[0] - 1.0) < 1e-06, 'Lag 0 debe ser 1.0'\n"
                                               '>>> assert np.all(acf_col >= -1.0 - 1e-09)\n'
                                               '>>> assert np.all(acf_col <= 1.0 + 1e-09)\n'
                                               '>>> assert isinstance(lag_mayor_acf, int)\n'
                                               '>>> assert 1 <= lag_mayor_acf <= 5\n'
                                               '>>> assert acf_col[lag_mayor_acf] == max(acf_col[1:])\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
