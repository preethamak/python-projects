from time import sleep

def timer(seconds):
    if seconds>0:
        while seconds>=0:
            print(seconds)
            sleep(1)
            seconds-=1
        
    else:
         print("seconds must be greater than 0 ")
                
seconds= int(input("enter the seconds: "))
timer(seconds)