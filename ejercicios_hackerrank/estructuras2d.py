import numpy as np

def hourglassSum(arr):

    #sacar los relojes de arena
    for i in range(len(arr[0])):
        for j in range(len(arr[i])):
            if i <=2:
                a=(arr[i][j:j+3])
                print(a)
                print("="*100)
            
        
            
           
        
    

    

if __name__ == '__main__':
  

    arr = np.array([[1, 1, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0], 
                    [1, 1, 1, 0, 0, 0], 
                    [0, 0, 2, 4, 4, 0], 
                    [0, 0, 0, 2, 0, 0], 
                    [0, 0, 1, 2, 4, 0]])
             
    result = hourglassSum(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()