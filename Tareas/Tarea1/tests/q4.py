test = {
    "name": "q4",
    "points": 10,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> 'df_clean' in dir()\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> id(df) != id(df_clean)\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> len(df) >= 70000\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> df_clean.duplicated(subset='folioviv').sum() == 0\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> len(df_clean) <= len(df)\nTrue",
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
