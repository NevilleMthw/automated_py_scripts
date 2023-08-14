import os
import filecmp


def compare_and_remove(source_folder: str, target_folder: str) -> None:
    common_files = filecmp.dircmp(source_folder, target_folder).common_files

    for common_file in common_files:
        source_path = os.path.join(source_folder, common_file)
        target_path = os.path.join(target_folder, common_file)

        if os.path.isfile(source_path) and os.path.isfile(target_path):
            os.remove(target_path)
            print(f"Removed: {target_path}")


if __name__ == "__main__":
    source_folder_path = "/home/nevillemthw/Downloads/obj_train_data"
    target_folder_path = "/home/nevillemthw/Downloads/png-img"

    compare_and_remove(source_folder_path, target_folder_path)
