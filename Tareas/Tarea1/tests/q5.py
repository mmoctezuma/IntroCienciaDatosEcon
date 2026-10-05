test = {
    "name": "q5",
    "points": 10,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> 'ingcor_faltante' in df_clean.columns\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> set(df_clean['ingcor_faltante'].unique()).issubset({0, 1})\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> df_clean['ingcor'].isnull().sum() == 0\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> int(df_clean['ingcor_faltante'].sum()) == int(df['ing_cor'].isnull().sum())\nTrue",
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
