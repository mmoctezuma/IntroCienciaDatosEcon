test = {
    "name": "q6",
    "points": 10,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> str(df_clean['est_socio'].dtype) == 'category'\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> df_clean['est_socio'].cat.ordered\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> list(df_clean['est_socio'].cat.categories) == [1, 2, 3, 4]\nTrue",
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
