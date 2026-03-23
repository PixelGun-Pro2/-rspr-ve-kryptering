alfabet= 'abcdefghijklmnopqrstuvwxyzæøå?!,.:'

# Denne funktion kan tage en karakter fra alfabetet og rotere den ud fra det angivet tal fra key
def rot(char:str,key:int):
    # Her tjekker koden om den angivet karakter er i alfabetet og om det kun er 1 bogstav
    if not char in alfabet or len(char)!=1:
        # Ellers spytter den bare et "#" ud
        return "#"
    # Her finder vi karakteren i alfabetet
    char_index=alfabet.find(char)
    # Og så rotere vi karakteren med den angivet key
    rot_index=key+char_index
    # Hvis vores roteret karakter er over alfabetet minuser vi det med 1 så det ikke går ud over
    if rot_index > len(alfabet)-1:
        #
        rot_index=rot_index % len(alfabet)
    return alfabet[rot_index]

# Her definerer vi "encrypt" til at tage en besked (msg) og et tal (key)
def encrypt(msg:str,key:int):
    out=""
# Nu tager vi hver karakter i beskeden og rotere dem med tallet angivet i key
    for char in msg:
        out += rot(char,key)
    return out

# Det vi kan gøre nu er at udskrive vores angivet besked i msg og tallet i key som rotere beskeden
print(encrypt('hello', 2))