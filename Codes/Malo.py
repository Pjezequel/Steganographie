from PIL import Image
def conv_message_vers_binaire(texte:str)->str:
    """
    Cette fonction prend en entrée, le texte qui doit être caché dans l'image
    et renvoie une chaine de caractère qui contient le code binaire représentant
    chaque caractère du message à cacher sur 8 bits.
    >>> conv_message_vers_binaire("coucou les nullos")
    '0110001101101111011101010110001101101111011101010010000001101100011001010111001100100000011011100111010101101100011011000110111101110011'

    
    """
    assert type(texte) == str , ' L’entrée doit être un string '
    binMsg=''
    for carac in texte:
        temp=(bin(ord(carac))[2:])
        binMsg+=temp.zfill(8)
    return binMsg

def rgb(image)->None:
    """
    Prend le nom d'une image en entrée et convertit son mode en "RGB"
    """
    
    im = Image.open(image)
    rgb_im = im.convert('RGB')
    rgb_im.save(image)

if __name__=="__main__": 

    from doctest import testmod 
    testmod() 
    print(conv_message_vers_binaire("coucou les nullos"))