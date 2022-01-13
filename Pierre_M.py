from PIL import Image
def infos_image(image_file)->tuple:
    """
    Renvoie les dimensions, le format (e.g. PNG)
    et le mode (e.g. RGB) de l'image
    originale si elle est trouvée !
    >>> infos_image("image.png")
    (772, 749, 'RGBA', 'PNG')
    """
    try:
        image = Image.open(image_file)
        imageproperties=(image.width, image.height, image.mode, image.format)
        return imageproperties
    except: 
        print("Erreur dans le traitement de l'image",image_file)

if __name__=="__main__":
    from doctest import testmod
    testmod()
    nomimage=input("Donner le nom de votre fichier image avec l'extension ")
    print(infos_image(nomimage))

def lecture_fichier(nom_fichier)->str:
    """
    Fonction réalisant la lecture du fichier
    texte à écrire sur une image
    >>> lecture_fichier("texte.txt")
    'Ceci sera écrit à la fin de mon fichier !'
    """
    try:
        with open(nom_fichier, 'r', encoding="utf-8") as fichier_texte:
            lignes_texte=fichier_texte.read()
            return lignes_texte
    except: 
        print("Erreur dans le traitement du fichier", nom_fichier)
        
if __name__=="__main__":
    from doctest import testmod
    testmod()
    print(lecture_fichier(str(input("Donner le nom du fichier "))))
    