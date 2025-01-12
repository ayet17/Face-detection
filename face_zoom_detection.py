import cv2
from src.face_detection import FaceDetection
from src.zoom_manager import ZoomManager
from src.video_utils import VideoUtils

def main():
    input_video_path = 'example_video.mp4'
    output_video_path = 'output_video.mp4'

    # Initialisation des modules
    face_detection = FaceDetection()
    zoom_manager = ZoomManager()
    video_utils = VideoUtils(input_video_path, output_video_path)

    # Processus vidéo
    video_utils.process_video(face_detection, zoom_manager)

if __name__ == "__main__":
    main()
