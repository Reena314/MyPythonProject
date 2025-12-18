# run pip freeze for the system interpreter take the content and create a similar virtualenv

# first freeze using pip freeze > requirements.txt then create a virtualenv using python3 -m venv venv then activate using source venv/bin/activate then install requirements using pip install -r requirements.txt