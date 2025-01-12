import cv2
import numpy as np

class ZoomManager:
    def __init__(self, zoom_factor=1.2, max_zoom_level=2.0, min_zoom_level=1.0):
        self.zoom_factor = zoom_factor
        self.max_zoom_level = max_zoom_level
        self.min_zoom_level = min_zoom_level

    def apply_zoom(self, frame, face_coords, zoom_in=True):

        if not face_coords:
            return frame

        x, y, w, h = face_coords[0]
        center_x, center_y = x + w // 2, y + h // 2
        zoom_level = self.max_zoom_level if zoom_in else self.min_zoom_level

        # Calculer la nouvelle taille de la région d'intérêt (ROI)
        new_w = int(w * zoom_level)
        new_h = int(h * zoom_level)
        x1 = max(0, center_x - new_w // 2)
        y1 = max(0, center_y - new_h // 2)
        x2 = min(frame.shape[1], x1 + new_w)
        y2 = min(frame.shape[0], y1 + new_h)

        # Découper l'image autour du visage et appliquer le zoom
        zoomed_face = frame[y1:y2, x1:x2]
        return cv2.resize(zoomed_face, (w, h), interpolation=cv2.INTER_LINEAR)
