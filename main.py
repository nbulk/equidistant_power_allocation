import numpy as np

from . import distance_matrix
from . import reduction

#import distance_matrix
#import reduction

class equdistant_power():
    
    def __init__(self, modulation):
        self.modulation = modulation
        self.no_user = len(modulation)
        self.powerfactor = 0
    
        
    def __calculate_dist_matrix(self): 
        power = distance_matrix.distance_matrix_generator(self.no_user, self.modulation)
        dist_matrix = power.dist_input()
        return dist_matrix
        
    def __calculate_reduction_matrix(self):
        reduction_matrix = reduction.reduction_matrix(self.modulation)
        matrix = reduction_matrix.main()
        
        return matrix
        
    def __calculate_dist_matrix_noma(self):
        noma_user = 1
        noma_modulation = np.array([np.sum(self.modulation)])
        noma_power = distance_matrix.distance_matrix_generator(noma_user, noma_modulation)
        norm_distance_noma = noma_power.dist_input()
        
        return norm_distance_noma
    
    def main(self):
        self.dist_matrix = self.__calculate_dist_matrix()
        self.reduce_matrix = self.__calculate_reduction_matrix()
        self.reduced_dist_matrix = np.matmul(self.reduce_matrix, self.dist_matrix)
        self.inverse_dist_matrix = np.linalg.inv(self.reduced_dist_matrix)
        
        self.norm_distance_noma = self.__calculate_dist_matrix_noma()
        self.reduced_noma = np.matmul(self.reduce_matrix , self.norm_distance_noma)
        self.powerfactor = np.matmul(self.inverse_dist_matrix, self.reduced_noma)
        
        return self.powerfactor**2
    
    def get_powerfactors(self):
        return self.powerfactor**2



if __name__ == "__main__":
    modulation = np.array([2,2,6])
    allocator = equdistant_power(modulation)
    powerfactors = allocator.main()
    print(powerfactors)