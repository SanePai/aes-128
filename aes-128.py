def get_round_key(key, round):
    '''
    Function to expand key and return round keys. 
    Input: key and round number
    Output: round_key
    '''
    pass

def add_round_key(state, round_key):
    '''
    Function to add round key to current state. 
    Input: current_state
    Output: (modified) state
    '''
    pass

def mix_col (state):
    '''
    Function to mix columns in current state. 
    Input: current state
    Output: (modified) state
    '''
    pass

def shift_rows(state):
    '''
    Function to shift rows in current state. 
    Input: current state
    Output: (modified) state
    '''
    pass

def sub_bytes(state):
    '''
    Function to sub bytes from s-box. 
    Input: current state
    Output: (modified) state
    '''
    pass

def change_s_box(s_box, ab):
    '''
    Function to modify s-box from (a,b). 
    Input: s_box, ab - tuple calculated from ID numbers
    Output: modified s-box
    '''    
    pass

def aes_encrypt(pt, key):
    '''
    Function to encrypt a plaintext message using a key. 
    Input: plaintext message pt, key
    Output: ciphertext
    '''    
    pass