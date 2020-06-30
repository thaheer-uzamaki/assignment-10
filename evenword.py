def printWords(s): 
      
      
    s = s.split(' ')  
      
      
    for word in s:  
          
        
        if len(word)%2==0: 
            print(word)  
  
  
st = 'Print every word in this sentence that has an even number of letters' 
printWords(st)  