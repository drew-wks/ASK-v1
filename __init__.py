'''

With this init file, you can import python scripts in the directory where this init file lives directly in your scripts as long as those scripts are also within the your_project directory.
    import ask
    imprt utils
    
Examples Project
your_project/
├── __init__.py
├── app.py
├── ask.py
├── utils.py
└── other_scripts/
    └── script1.py
    
To access from app.py
    import ask
    
To access from script1.py
    from .. import ask

    
Examples Project
your_project/
├── __init__.py
├── app.py
├── ask.py
├── utils.py
└── other_scripts/
    ├── __init__.py
    └── script1.py
    
    
To access from app.py
    from .other_Scripts import script1

'''
