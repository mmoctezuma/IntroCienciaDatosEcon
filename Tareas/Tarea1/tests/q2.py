test = {
    "name": "q2",
    "points": 10,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> 'tabla_calidad' in dir()\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> set(['variable','tipo_dato','pct_faltantes','n_unicos']).issubset(set(tabla_calidad.columns))\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> len(tabla_calidad) == len(df.columns)\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> tabla_calidad['pct_faltantes'].between(0, 100).all()\nTrue",
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
