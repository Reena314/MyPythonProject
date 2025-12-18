# create two virtual environment and install few packages in the first one. how do you create a similar environment in the secondone
      

      # ans in command  open cmd or repl using folder like chepter13

# ok now i create one virtual environment using python3 -m virtualenv env1 and for active using  source env1/bin/activate and next install package using pip install pandas and next pip install pyjokes and next pip freeze > requirements.txt
# now i deactivate the env1 using deactivate and  i want to create a similar environment in the secondone env2  and same active using source env2/bin/activate and next pip install -r requirements.txt next check  type  python3 and next type import pandas