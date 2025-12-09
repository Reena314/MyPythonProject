# can you change the self parameter inside a class to something else(say harry).try changeing to set self to slf or harry and see the effect

class Train:
    def __init__(slf,trainNo):
        slf.trainNo = trainNo
    def bookTicket(harry, trainNo, fro, to):
        print(f"ticket book for trainNo : {harry.trainNo} from {fro} to {to}")

t = Train(23445)
t.bookTicket(23445, "Lucknow", "Delhi")        


    # so no change with slf and harry but its not a good practice