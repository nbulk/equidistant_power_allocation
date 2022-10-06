import numpy as np

class reduction_matrix():
    
    def __init__(self,modulation):
        M = 2** modulation
        N = np.sqrt(M)
        self.bits_layer = np.array(np.log2(N), dtype = int)
        
        self.number_layer = len(modulation)
        
    def __calculate_no_bits(self):
        self.final_bits = np.sum(self.bits_layer)
        
    def __generate_distance_vector(self):
        self.distance_vector = np.zeros(self.final_bits)
        
    def __calculate_reduction_vector(self):
        self.reduction_vector = np.zeros(self.number_layer, dtype = int)
        for k in range(0, self.number_layer):
            self.reduction_vector[k] = np.sum(self.bits_layer[:k+1])
            
    def __set_reduction_matrix(self):
        self.reduction_matrix = np.zeros((self.number_layer, self.reduction_vector[-1]))
        for i, value in enumerate(self.reduction_vector):
            self.reduction_matrix[i, value-1] = 1
            
    def main(self):
        self.__calculate_no_bits()
        self.__generate_distance_vector()
        self.__calculate_reduction_vector()
        self.__set_reduction_matrix()
        return self.reduction_matrix
            
            
            
if __name__ == "__main__":
    modulation = np.array([2,6])
    temp = reduction_matrix(modulation)
    matrix = temp.main()
    print(matrix)