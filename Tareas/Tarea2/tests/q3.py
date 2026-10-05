OK_FORMAT = True

test = {   'name': 'q3',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': ">>> assert isinstance(corr_matrix, pd.DataFrame), 'corr_matrix debe ser pd.DataFrame'\n"
                                               ">>> assert corr_matrix.shape == (5, 5), 'corr_matrix debe ser 5x5'\n"
                                               '>>> _diag = np.diag(corr_matrix.to_numpy().astype(float))\n'
                                               ">>> assert np.all((_diag == 1.0) | np.isnan(_diag)), 'La diagonal debe ser 1.0 o NaN'\n"
                                               '>>> _vals = corr_matrix.to_numpy().astype(float)\n'
                                               '>>> assert np.nanmax(_vals) <= 1.0 + 1e-09\n'
                                               '>>> assert np.nanmin(_vals) >= -1.0 - 1e-09\n'
                                               ">>> _cols = {'pib_pc_ppp', 'gini', 'desempleo', 'gasto_educacion', 'participacion_fem'}\n"
                                               '>>> assert isinstance(par_mayor_corr, tuple) and len(par_mayor_corr) == 2\n'
                                               '>>> assert par_mayor_corr[0] in _cols and par_mayor_corr[1] in _cols\n'
                                               '>>> assert par_mayor_corr[0] != par_mayor_corr[1]\n'
                                               ">>> assert par_mayor_corr[0] < par_mayor_corr[1], 'Debe estar en orden alfabetico'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
