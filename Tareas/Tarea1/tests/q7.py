test = {
    "name": "q7",
    "points": 10,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> 'reporte' in dir()\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> set(reporte.columns) == {'dataset', 'n_filas', 'total_nan'}\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> len(reporte) == 2\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> int(reporte.set_index('dataset').loc['original', 'n_filas']) == len(df)\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> int(reporte.set_index('dataset').loc['limpio', 'n_filas']) == len(df_clean)\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> reporte.set_index('dataset').loc['limpio', 'total_nan'] <= reporte.set_index('dataset').loc['original', 'total_nan']\nTrue",
                    "hidden": False,
                    "locked": False
                }
            ],
            "scored": True,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}
