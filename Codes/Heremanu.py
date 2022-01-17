def creer_nom_sauvegarde(nom:str)->str:
    """
    Fonction qui génère un nom pour la future image
    à sauvegarder, en relation avec le nom initial
    """
    assert type(nom)==str, "Il n'y a pas de nom pour le fichier" 
    lst=[]
    for i in nom:
        lst.append(i)
    for i in range(len(lst)-4, len(lst)):
        lst.pop()
    lst.append("_new.png")
    new_file="".join(lst)
    return new_file

    