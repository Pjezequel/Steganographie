def encode_message(msg:str, coul:list)->list:
    """
    Cette fonction modifie les valeurs (couleurs) de
    la liste passée en paramètre selon le procédé suivant :
    si le nombre représentant la couleur est pair et le code binaire
    à écrire est 1, on doit rendre le nombre représentant la couleur impair.
    De même si le code binaire à écrire est 0 et que le nombre représentant
    la couleur est impair, on doit rendre le nombre représentant la couleur pair.
    >>> print(encode_message("0100",[1,254,122,123]))
    [0, 255, 122, 122]
    """
    assert len(msg)<=len(coul), "Le binaire du message doit être plus court que le nombre de couleurs."
    for bn in msg:
        assert bn=="0"or bn=="1", "Le message doit être en binaire"
    lst=[]
    
    for i in range(len(msg)):
        if msg[i]=="0" and coul[i]%2==1:
            lst.append(coul[i]-1)
        elif msg[i]=="1" and coul[i]%2==0:
            lst.append(coul[i]+1)
        else:
            lst.append(coul[i])
    return lst

if __name__=="__main__":
    from doctest import testmod
    testmod()
    #assert(encode_message("0100",[1,254,122,123]))==[0, 255, 122, 122]
    print(encode_message("0100",[1,254,122,123]))


