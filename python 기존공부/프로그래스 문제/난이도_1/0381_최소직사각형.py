solution([[60, 50], [30, 70], [60, 30], [80, 40]])

def solution(sizes):
    temp=dict.fromkeys(["r","w"])
    temp["r"]=sizes[0][0]
    temp["w"]=sizes[0][1]
    size=lambda x:x["r"]*x["w"]
    def trans(x):
