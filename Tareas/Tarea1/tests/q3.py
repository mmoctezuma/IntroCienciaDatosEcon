test = {
    "name": "q3",
    "points": 10,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> isinstance(vars_con_faltantes, list)\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> set(vars_con_faltantes) == set(c for c in df.columns if df[c].isnull().sum() > 0)\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> int(n_duplicados) == int(df.duplicated(subset='folioviv').sum())\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> col_mas_faltantes == df.isnull().mean().idxmax()\nTrue",
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
