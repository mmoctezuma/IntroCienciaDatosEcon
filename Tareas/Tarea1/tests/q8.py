test = {
    "name": "q8",
    "points": 10,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> import os; os.path.exists('enigh2022_limpio.csv')\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> 'df_verificacion' in dir()\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> df_verificacion.shape[0] == df_clean.shape[0]\nTrue",
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
