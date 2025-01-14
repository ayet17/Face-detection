# Projet de Détection de Visage et Zoom Progressif

Ce projet implémente une détection de visages et de yeux avec un zoom progressif appliqué sur la vidéo, en utilisant les bibliothèques Python OpenCV et MediaPipe. Il applique un zoom sur le visage détecté, le met à jour au fur et à mesure, et effectue un dézoom lorsque le visage n'est plus détecté.

## Modules du Projet

### 1. **face_detection_zoom.py**
Ce module est le script principal qui orchestre la détection de visages, la détection des yeux et l'application du zoom progressif. Il utilise les autres modules pour effectuer les tâches suivantes :
- Détection du visage.
- Détection des yeux.
- Application du zoom centralisé sur le visage.
- Dézoom lorsque le visage n'est plus détecté.
- Sauvegarde de la vidéo traitée.

**Fonctionnalités :**
- **Détection de Visage** : Le module utilise la bibliothèque MediaPipe pour détecter les visages dans chaque image de la vidéo.
- **Détection des Yeux** : Utilisation de MediaPipe pour détecter les yeux du visage en fonction des points de repère.
- **Zoom Progressif** : Le zoom est appliqué sur la zone du visage en augmentant progressivement la taille de la région visible tout en gardant le visage centré.
- **Dézoom** : Si aucun visage n'est détecté dans une frame, un dézoom progressif est appliqué pour revenir à la vue originale.

**Dépendances** :
- `opencv-python`
- `mediapipe`
- `numpy`

### 2. **face_detection.py**
Ce module contient les fonctions liées à la détection des visages à l'aide de MediaPipe. Il est responsable de l'identification des visages dans chaque image de la vidéo. Il retourne les coordonnées des visages détectés, permettant de dessiner des cadres autour du visage.

**Fonctionnalités :**
- **Détection du visage** : Utilisation de l'API `FaceDetection` de MediaPipe pour détecter les visages dans l'image.
- **Coordonnées du visage** : Renvoie les coordonnées de chaque visage détecté dans l'image sous forme de boîtes englobantes (bounding boxes).
- **Paramètres** :
  - `min_detection_confidence` : Définie à 0.5 pour un compromis entre précision et rappel.

### 3. **zoom_manager.py**
Ce module gère l'application du zoom et du dézoom en fonction de la présence ou de l'absence d'un visage détecté. Il ajuste le niveau de zoom et de dézoom de manière fluide tout en maintenant un zoom centré sur le visage détecté.

**Fonctionnalités :**
- **Zoom Progressif** : Augmente progressivement le niveau de zoom centré sur la région du visage.
- **Dézoom Progressif** : Applique un dézoom si aucun visage n'est détecté pendant plusieurs frames.
- **Paramètres** :
  - `zoom_level` : Le niveau de zoom, qui commence à 1.0 et peut augmenter jusqu'à un maximum de 2.0.
  - `dezoom_level` : Si le visage est perdu, le zoom est progressivement réduit jusqu'à revenir à la taille initiale.

### 4. **video_utils.py**
Ce module fournit des utilitaires pour le traitement vidéo, y compris la lecture de vidéo, l'écriture de vidéo et l'affichage du flux vidéo.

**Fonctionnalités :**
- **Lecture de Vidéo** : Utilisation de `cv2.VideoCapture` pour lire les images de la vidéo à partir d'un fichier.
- **Écriture de Vidéo** : Utilisation de `cv2.VideoWriter` pour sauvegarder les frames traitées dans un nouveau fichier vidéo.
- **Affichage Vidéo** : Affiche la vidéo traitée dans une fenêtre en temps réel avec `cv2.imshow`.

## Bibliothèques utilisées

- **OpenCV** : Utilisé pour le traitement vidéo, le dessin sur l'image, la lecture et l'écriture de vidéos.
- **MediaPipe** : Utilisé pour la détection de visages et des points de repère des yeux.
- **NumPy** : Utilisé pour le traitement de matrices, notamment pour la gestion des images et des transformations géométriques.

## Étapes pour exécuter l'application

### 1. Préparer la vidéo d'entrée
Avant d'exécuter le script, assurez-vous que vous avez une vidéo prête à être traitée. Le fichier vidéo doit être placé dans le répertoire du projet, par exemple `input_video.mp4`.

### 2. Installer les dépendances
Installez les bibliothèques Python nécessaires pour le bon fonctionnement de l'application. Vous pouvez le faire en exécutant la commande suivante :

```bash
pip install opencv-python mediapipe numpy
