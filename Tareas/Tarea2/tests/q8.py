OK_FORMAT = True

test = {   'name': 'q8',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': ">>> assert hasattr(modelo_col, 'params')\n"
                                               ">>> assert hasattr(modelo_col, 'resid')\n"
                                               '>>> assert isinstance(pendiente_col, float)\n'
                                               ">>> assert pendiente_col < 0, 'Se espera pendiente negativa'\n"
                                               '>>> assert isinstance(dw_col, float)\n'
                                               '>>> assert 0 <= dw_col <= 4\n'
                                               '>>> assert isinstance(hay_autocorr, bool)\n'
                                               '>>> assert hay_autocorr == (dw_col < 1.5)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
