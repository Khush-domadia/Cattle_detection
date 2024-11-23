import cv2
from ultralytics import YOLO

model = YOLO("base/service/model/yolov8n.pt")

def add_detection(source, name):
    cap = cv2.VideoCapture(source)
    frameRate = 1
    sec = round(0 + frameRate, 1)
    classes_id = [15, 16, 17, 18, 19]

    # Read the dimensions of the first frame
    hasFrames, image = cap.read()
    height, width, _ = image.shape

    # Create VideoWriter object with AVI codec
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Change codec to XVID for AVI
    output_video_filename = f'base/static/adminResourses/avi_video/output_video_{name}.avi'
    video = cv2.VideoWriter(output_video_filename, fourcc, frameRate, (width, height))

    while True:
        cap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
        hasFrames, image = cap.read()
        if hasFrames:
            results_list = model.track(image, classes=classes_id, persist=True)
            for results in results_list:
                annotated_frame = results.plot()
                video.write(annotated_frame)

                # Dictionary to store counts for each class in the current frame
                class_counts = {model.names[class_id]: 0 for class_id in classes_id}

                # Count the number of labeled data in the current frame
                for class_id, boxes in enumerate(results.boxes):
                    class_name = model.names[classes_id[class_id]]
                    # Increment count for the corresponding class name
                    class_counts[class_name] += len(boxes)

                # Print the counts for each class in the current frame
                print(f"Counts for frame {sec}:")
                for class_name, count in class_counts.items():
                    print(f"{class_name}: {count}")

        else:
            break

        sec = round(sec + frameRate, 2)

    cap.release()
    video.release()
    cv2.destroyAllWindows()






import os
import moviepy.editor as moviepy

avi_folder = "base/static/adminResourses/avi_video/"
output_folder = "base/static/adminResourses/output/"


def avi_to_mp4():
    # Iterate through all files in the AVI folder
    for filename in os.listdir(avi_folder):
        if filename.endswith(".avi"):
            # Get the full path of the input and output files
            input_path = os.path.join(avi_folder, filename)
            output_name = os.path.splitext(filename)[0] + ".mp4"
            output_path = os.path.join(output_folder, output_name)

            # Convert AVI to MP4
            clip = moviepy.VideoFileClip(input_path)
            clip.write_videofile(output_path)

            print(f"Converted {filename} to {output_name}")


