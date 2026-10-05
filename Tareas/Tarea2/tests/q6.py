OK_FORMAT = True

test = {   'name': 'q6',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': ">>> assert hasattr(descomp_col, 'trend')\n"
                                               ">>> assert hasattr(descomp_col, 'seasonal')\n"
                                               ">>> assert hasattr(descomp_col, 'resid')\n"
                                               '>>> assert isinstance(tendencia_col, pd.Series)\n'
                                               ">>> assert tendencia_col.isna().sum() == 0, 'tendencia_col no debe tener NaN'\n"
                                               '>>> assert isinstance(residuos_col, pd.Series)\n'
                                               ">>> assert residuos_col.isna().sum() == 0, 'residuos_col no debe tener NaN'\n"
                                               '>>> assert len(tendencia_col) > 0\n'
                                               '>>> assert np.isfinite(tendencia_col.values).all()\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
