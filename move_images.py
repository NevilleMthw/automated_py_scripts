import os
import shutil
import cv2

source_folder_path: str = '/media/intern/New Volume/2017/August-2017'
clean_folder_path: str = '/home/intern/Desktop/fiftyone-scripts/real_data/clean'
dirty_folder_path: str = '/home/intern/Desktop/fiftyone-scripts/real_data/dirty'
vehicle_folder_path: str = '/home/intern/Desktop/fiftyone-scripts/real_data/vehicle'
others_folder_path: str = '/home/intern/Desktop/fiftyone-scripts/others'


def move_images(source_folder: str, clean_folder: str, dirty_folder: str, vehicle_folder: str,
                others_folder: str) -> None:
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']  # Add more extensions if needed

    # Get a list of image files in the source folder
    image_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))
                   and os.path.splitext(f)[1].lower() in image_extensions]

    try:
        for image_file in image_files:
            image_path = os.path.join(source_folder, image_file)

            # Load and display the image using OpenCV
            img = cv2.imread(image_path)
            cv2.imshow('Image', img)
            key = cv2.waitKey(0) & 0xFF
            cv2.destroyAllWindows()

            # key = cv2.waitKey(0) & 0xFF
            print(key)

            if key == ord('c'):  # Move to the clean folder
                destination_folder = clean_folder
            elif key == ord('d'):  # Move to the dirty folder
                destination_folder = dirty_folder
            elif key == ord('v'):  # Move to the vehicle folder
                destination_folder = vehicle_folder
            elif key == ord('o'):  # Move to the others folder
                destination_folder = others_folder
            else:
                print("Invalid key. Skipping the image.")
                break

            destination_path = os.path.join(destination_folder, image_file)
            shutil.move(image_path, destination_path)
            print(f"Moved {image_file} to {destination_folder}")
    except Exception as e:
        print(e)


move_images(source_folder_path, clean_folder_path, dirty_folder_path, vehicle_folder_path, others_folder_path)
