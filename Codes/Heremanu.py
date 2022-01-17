def creer_nom_sauvegarde(nom:str, caract:tuple)->str:
    """
    Fonction qui génère un nom pour la future image
    à sauvegarder, en relation avec le nom initial
    """
    assert type(nom)==str, "Il n'y a pas de nom pour le fichier"  
    new_file = nom.replace(".jpg", "_new.png")
    return new_file

    