# class attribute vs instance attribute

class employee:
    company = "google"              # this is a class attribute
    salary = 2000000
    language = "python"

e1 = employee()
e1.company = "microsoft"      # then result is microsoft not google  # this is an instance attribute
print(e1.company)