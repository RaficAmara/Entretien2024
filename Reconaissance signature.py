import cv2
import numpy as np

def detect_signature(template_path, image_path):
    try:
        # Charger l'image du modèle de signature et l'image du document
        template = cv2.imread(template_path, 0)
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
            print("La signature a été détectée.")
        else:
            print("La signature n'a pas été détectée.")
            
    except Exception as e:
        print("Une erreur est survenue :", e)

# Exemple d'utilisation
if __name__ == "__main__":
    detect_signature(r'C:\Users\rafic\Desktop\tst.jpg', r'C:\Users\rafic\Desktop\tst.jpg')

