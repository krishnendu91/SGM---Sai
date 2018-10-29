def poweroutage(v1,v2,v3):
  if (v1&v2&v3==0):
    print("no input voltage supply")
    #return 
  if (v1|v2|v3==0):
    print("Line fault")

def frequency(f1,f2,f3):
  if(f1|f2|f3 <49.5):
    print("Low Frequency")
  
  if(f1|f2|f3 >50.5):
    print("High Frequency")
    
