'''
Write a module that enables the robots to easily recall their passwords through codes when they return home.
The cipher grille and the ciphered password are represented as an array (tuple) of strings.
Input: A cipher grille and a ciphered password as a tuples of strings.
Output: The password as a string.
'''

def recall_password(cipher_grille, ciphered_password):
    
    decoded = ''
    def decipher(cipher_grille):
        text = ''
        for x in range(4):
            for y in range(4):
                if cipher_grille[x][y] == 'X':
                    text += ciphered_password[x][y]
        return text
​
    def rotate(cipher_grille):
        rotated_grille = [[] for i in range(4)]
        for x in range(4):
            for y in range(3,-1,-1):
                rotated_grille[x].append(cipher_grille[y][x])
        return rotated_grille
        
    decoded += (decipher(cipher_grille))
    decoded += (decipher(rotate(cipher_grille)))
    decoded += (decipher(rotate(rotate(cipher_grille))))
    decoded += (decipher(rotate(rotate(rotate(cipher_grille)))))
            
    return decoded
    
print(recall_password( 
        ('X...', 
         '..X.', 
         'X..X', 
         '....'), 
        ('itdf', 
         'gdce', 
         'aton', 
         'qrdi')) 
    ) 
print(recall_password( 
        ('....', 
         'X..X', 
         '.X..', 
         '...X'), 
        ('xhwc', 
         'rsqx', 
         'xqzz', 
         'fyzr')) 
    ) 