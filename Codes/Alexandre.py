import sys
from PIL import Image
def creation_image(caract:tuple, coul:list, image_file)->None:
    """
    Cette procédure crée une image ayant les mêmes
    caractéristiques que l'orignal mais avec les
    nouvelles couleurs, puis la sauvegarde avec
    un nom passé en argument
    """
    assert len(caract)==3, "la liste placé en arguments n'est pas une liste sortie de \"infos_images\""
    img_modifie=Image.new(caract[1], (caract[0][0], caract[0][1]))
    a=0
    for x in range(0, caract[0][0]):
            for y in range(0, caract[0][1]):               
                img_modifie.putpixel((x, y), (coul[a], coul[a+1], coul[a+2]))
                a+=3
    img_modifie.save(image_file)
    
def recup_couleurs_image(image_file)->list:
    """
    Cette fonction prend en entrée le nom de l'image et
    renvoie une liste qui contient la valeur des composantes
    rouge, verte et bleue de chaque pixel de l'image en décimal.
    """
    try:
        nom_image= Image.open(image_file)
    except:
        print ('Erreur sur ouverture du fichier ',image_file)
        sys.exit(1)
    largeur,hauteur=nom_image.size
    # balayage de l'image colonne par colonne de gauche à droite
    liste=[]
    for i in range(0,largeur):
        for j in range(0,hauteur):
            r,g,b = nom_image.getpixel((i,j))
            liste.append(r)
            liste.append(g)
            liste.append(b)
    nom_image.close()
    return liste

if __name__=="__main__":
    print(recup_couleurs_image("minion.jpg"))