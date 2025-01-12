import cv2

class VideoUtils:
    def __init__(self, input_video_path, output_video_path):
        self.input_video_path = input_video_path
        self.output_video_path = output_video_path
        self.cap = cv2.VideoCapture(input_video_path)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.out = cv2.VideoWriter(output_video_path, fourcc, self.fps, (self.frame_width, self.frame_height))

    def process_video(self, face_detection, zoom_manager):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break

            # Détecter les visages
            face_coords = face_detection.detect_faces(frame)

            # Appliquer le zoom si nécessaire
            zoomed_frame = zoom_manager.apply_zoom(frame, face_coords, zoom_in=True)

            # Écrire la frame modifiée dans le fichier de sortie
            self.out.write(zoomed_frame)

            # Afficher la vidéo en temps réel (optionnel)
            cv2.imshow('Video', zoomed_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()
