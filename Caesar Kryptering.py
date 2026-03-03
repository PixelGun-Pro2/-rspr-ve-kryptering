alfabet= 'abcdefghijklmnopqrstuvwxyzæøå?!,.:'

def rot(char:str,key:int):
    if not char in alfabet or len(char)!=1:
        return "#"
    rot_index=key+alfabet.find(char)
    if rot_index > len(alfabet)-1:
        rot_index=rot_index % len(alfabet)
        return alfabet[rot_index]