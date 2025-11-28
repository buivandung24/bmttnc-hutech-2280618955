class RailFenceCipher:
    def _init__(self):
        pass
    
    def rail_fence_encrypt(self, plain_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1 #1: down, -1: up
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        cipler_text = ''.join([''.join(rail) for rail in rails])
        return cipher_text
    
    def rail_fence_decrypt(self, cipher_text, num_rails):
        rail_lengths = [0] * num_rails
        rail_index=0
        direction = 1
        for _ in range(len(cipher_text)):
            rail_lengths [rail_index] += 1
            if rail_index== 0:
                direction=1
            elif rail_index == num_rails - 1:
                direction=-1
            rail_index += direction
            
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(cipher_text[start:start + length])
            start += length
        plain_text = ""
        rail_index=0
        direction =1
        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index] [0]
            rails[rail_index] = rails[rail_index] [1:]
            if rail_index == 0:
                direction=1
            elif rail_index == num_rails - 1:
                direction=1
            rail_index += direction
        return plain_text
    
    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        decrypted_text1 =""
        for i in range(0, len (cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords (matrix, pair[0])
            row2, col2 = self.find_letter_coords (matrix, pair[1])
            if row1 == row2:
                decrypted_text += matrix [row1] [(col1 - 1) % 5] + matrix[row2] [(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix [(row1 - 1) % 5][col1] + matrix [(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix [row1] [col2] + matrix [row2] [col1]
            
        banro = ""
        
        for i in range(0, len (decrypted_text)-2, 2):
            if decrypted_text[i] == decrypted_text[i+2]:
                banro += decrypted_text[i]
            else:
                banro + decrypted_text[i] + "" + decrypted_text[i+1]
        if decrypted_text[-1] == "X":
            banro += decrypted_text[-2]
        else:
            banro += decrypted_text[-2]
            banro += decrypted_text[-1]
            return banro