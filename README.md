# TYAN
TYAN is a preprocessor for JSON that improves the existing architecture for your happiness and is written in Python.

### Syntax
***TYAN code:***
	
    {
	    "name": "TYAN testing",
	    "actions":
	    {
		    ["mom", "dad"]: "sleep",
		    "son": "not born",
		    ["girlfriend", "pet"]: "not exist"
	    }
    }
    

***Generated JSON code:***

	
    {
	    "name": "TYAN testing",
	    "actions":
	    {
		    "mom": "sleep",
		    "dad": "sleep",
		    "son": "not born",
		    "girlfriend": "not exist",
		    "pet": "not exist"
	    }
    }

### Using

    import tyan

	text = "{
	    ["dogs", "cats", "people"]: "animals"
	}"
	
    dirt_object = tyan.load_file('settings.tyan')
    dirt_object = tyan.loads(text)
	string_json = tyan.convert_json_to_tyan(text)
	
	who = "people"
	print(f"{who} is {dirt_object[who]}") # result: people is animals
