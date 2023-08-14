import os


def check_file_match(directory: str) -> None:
    txt_files = []
    img_files = []

    # Get all .txt and .jpg files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            txt_files.append(filename)
        elif filename.endswith(".png"):
            img_files.append(filename)

    # Check if each .txt file has a corresponding .jpg file
    for txt_file in txt_files:
        jpg_file = txt_file.replace(".txt", ".png")
        if jpg_file not in img_files:
            # Remove the unmatched .txt file
            os.remove(os.path.join(directory, txt_file))
            print(f"Removed {txt_file}")

    # Check if each img file has a corresponding .txt file
    for jpg_file in img_files:
        txt_file = jpg_file.replace(".png", ".txt")
        if txt_file not in txt_files:
            # Remove the unmatched img file
            os.remove(os.path.join(directory, jpg_file))
            print(f"Removed {jpg_file}")


# Example usage
directory_path = "/home/nevillemthw/Downloads/division2/obj_train_data"
check_file_match(directory_path)
