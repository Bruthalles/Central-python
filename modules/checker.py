def verify(print,function,elseprint):
    choose = input(f"\n{print}").upper()
    if(choose == "S"):
        function()
    elif(choose == "N"): return 0
    else: print(f"\n{elseprint}")