import time
tm = time.sleep

def up_down_timer():
    i = 10
    while i > 0:
        print("-"*i,i)
        tm(1)
        i-=1
        
    