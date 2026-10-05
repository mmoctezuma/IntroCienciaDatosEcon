test = {
    "name": "q1",
    "points": 10,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> 'df' in dir()\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> len(df) >= 70000\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> df.shape[1] >= 100\nTrue",
                    "hidden": False,
                    "locked": False
                },
                {
                    "code": ">>> 'folioviv' in df.columns\nTrue",
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
