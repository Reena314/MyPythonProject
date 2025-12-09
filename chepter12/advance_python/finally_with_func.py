# finally block runs always but why use finally we can print without finlly block but in fuction finally must so example below
def main():
    try:
        a = int(input("enter a value :" ))
        print(a)
        return
    except Exception as e:
        print(e)
        return
                                              # so finally in function must without this finally block is not run
        print("finally block runs")

main()