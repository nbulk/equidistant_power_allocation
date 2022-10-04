import numpy as np

class distance_matrix_generator():
    
    def __init__(self, no_user, modulation):
        self.no_user = no_user
        self.modulation = modulation
        self.number_bits = np.array(np.log2(modulation), dtype = int)

    def __calculate_rms(self,modulation):
        return (modulation**2-1)/3

    def __calculate_distance(self, user):
        distance = np.zeros((self.number_bits[user],1))
        i = 1
        for index in range(0, self.number_bits[user]):
            distance[index] = 2**(self.number_bits[user]-i)
            i += 1
        return distance

    def __norm_distance(self, distance, rms_squard):
        norm = distance/np.sqrt(rms_squard)
        return norm
    
    def __calculate_dist_matrix(self,user):
        index_1 = np.sum(self.number_bits[:user])
        index_2 = np.sum(self.number_bits[:user+1])
        self.dist_matrix[index_1:index_2,user] = self.distance_norm
        return self.dist_matrix
    
    
    def dist_input(self):
        self.dist_matrix = np.zeros((np.sum(self.number_bits), self.no_user))   
               
        for user in range(0, self.no_user):
            rms_sq = self.__calculate_rms(self.modulation[user])
            distance = self.__calculate_distance(user).flatten()
            self.distance_norm = self.__norm_distance(distance,rms_sq)
            self.__calculate_dist_matrix(user)
        
        return self.dist_matrix
    
if __name__ == "__main__":
    test = distance_matrix_generator(3,np.array([8,4,4]))
    dist_matrix = test.dist_input()
    print(dist_matrix)