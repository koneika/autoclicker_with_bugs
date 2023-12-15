import mouse
import time

counter = 0
j = 1

input()
for i in range(99999999999999999999):
    time.sleep(0.05)
    if(counter == 50*j):
        j += 1
        print(counter)
    counter += 1
    mouse.click()
    
	
        
        
    
