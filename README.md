# Face Detection and Zoom Application

## Description
Ce projet implémente une application de détection de visages et d'yeux, avec un zoom progressif centré sur le visage détecté dans une vidéo. Lorsque le visage est détecté, un cadre est tracé autour du visage et des points rouges sont affichés sur les yeux. Ensuite, un zoom progressif est appliqué de manière fluide, tout en mettant à jour la détection du visage et des yeux. Si aucun visage n'est détecté, un dézoom est appliqué pour revenir progressivement à une vue d'ensemble.

## Bibliothèques utilisées

1. **OpenCV** : Pour la gestion des vidéos, le traitement d'images et l'affichage de la vidéo avec les modifications.
   - Permet de lire et écrire des vidéos.
   - Permet de manipuler les images (zoom, recadrage, etc.).

2. **MediaPipe** : Pour la détection de visages et d'yeux.
   - Utilise un modèle pré-entrainé de détection des visages et des repères faciaux de haute qualité.

3. **NumPy** : Pour la manipulation des matrices d'images et les calculs mathématiques nécessaires pour le traitement des images.
