import cv2
import numpy as np
import os
import time

def detect_signature(template_path, image_path):
    try:
        # Charger l'image du modèle de signature
        template = cv2.imread(template_path, 0)
        
        # Charger l'image du document
        img = cv2.imread(image_path, 0)
        
        if template is None or img is None:
            print("Impossible de charger les images.")
            return

        # Effectuer la correspondance de modèle
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

        # Définir un seuil de correspondance
        threshold = 0.8
        loc = np.where(res >= threshold)

        # Dessiner un rectangle autour des correspondances trouvées
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0, 255, 255), 2)

        # Afficher le résultat
        cv2.imshow('Signature Detection', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Vérifier si la signature a été détectée
        if loc[0].size > 0:  # Vérifie si des correspondances ont été trouvées
            print("La signature a été détectée dans", image_path)
        else:
            print("La signature n'a pas été détectée dans", image_path)
            
    except Exception as e:
        print("Une erreur est survenue lors de l'analyse de", image_path, ":", e)

# Chemin du dossier contenant les images de signature
dossier_signatures = r'C:\chemin\vers\votre\dossier\de\signatures'

# Chemin du modèle de signature
chemin_modele_signature = r'chemin_vers_votre_modele_de_signature.jpg'

# Boucle principale pour analyser en continu les signatures
while True:
    # Liste des fichiers d'images dans le dossier
    fichiers_images = [f for f in os.listdir(dossier_signatures) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # Parcourir chaque fichier d'image
    for fichier in fichiers_images:
        # Chemin complet du fichier d'image
        chemin_image = os.path.join(dossier_signatures, fichier)
        
        # Appeler la fonction detect_signature pour analyser la signature
        detect_signature(chemin_modele_signature, chemin_image)
    
    # Attendre 5 secondes avant la prochaine analyse
    time.sleep(5)

