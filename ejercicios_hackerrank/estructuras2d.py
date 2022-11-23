import numpy as np

def hourglassSum(arr):

    #sacar los relojes de arena
    list_muestra = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ## fila superior
            muestra = arr[i:(i+3),j:(j+3)]
            if muestra.shape == (3,3):
                list_muestra.append(muestra)


    for element in list_muestra:
        # e = element
        # e[1][0]= 0
        # e[1][-1] = 0
        
        print (element)
        print ("="*64)
                
        
            
           
        
    

    

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