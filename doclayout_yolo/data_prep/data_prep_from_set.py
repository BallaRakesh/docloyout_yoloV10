import os
import shutil
from pathlib import Path

def find_common_files(input_folder, output_folder):
    # Create output folder and subfolders if they don't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    Path(os.path.join(output_folder, 'images')).mkdir(parents=True, exist_ok=True)
    Path(os.path.join(output_folder, 'labels')).mkdir(parents=True, exist_ok=True)
    
    # Dictionary to store files for each set
    
    # Walk through the input folder
    for set_folder in os.listdir(input_folder):
        set_files = {}
        set_path = os.path.join(input_folder, set_folder)
        print(set_path)
        if not os.path.isdir(set_path):
            continue
            
        # Store files for current set
        set_files[set_folder] = {}
        
        # Walk through subfolders in set
        for root, _, files in os.walk(set_path):
            for file in files:
                if file.endswith(('.jpg', '.jpeg', '.png', '.txt')) and file != 'classes.txt':
                    # Determine if file is in images or labels folder
                    folder_type = 'images' if file.endswith(('.jpg', '.jpeg', '.png')) else 'labels'
                    # print(f"Processing {folder_type} file: {file}")
                    # Get relative path from set folder to subfolder
                    rel_path = os.path.relpath(root, set_path)
                    # print(f"Relative path: {rel_path}")
                    # Ensure the file is in images or labels folder
                    if os.path.basename(root) not in ('images', 'labels'):
                        continue
                    # Use relative path (excluding set folder) and base filename as key
                    base_name = os.path.splitext(file)[0]
                    # print(f"Base name: {base_name}")
                    # Construct file_key as parent subfolder path + base_name
                    parent_subfolder = os.path.dirname(rel_path)  # Get parent of images/labels
                    file_key = os.path.join(parent_subfolder, base_name) if parent_subfolder else base_name
                    # print(f"File key: {file_key}")
                    if file_key not in set_files[set_folder]:
                        set_files[set_folder][file_key] = {}
                    set_files[set_folder][file_key][folder_type] = os.path.join(root, file)
 
        # Find common base filenames that have both images and labels across all sets
        common_files = None
        for set_name in set_files:
            # Get base filenames that have both images and labels in the same subfolder
            valid_keys = {
                key for key, paths in set_files[set_name].items()
                if 'images' in paths and 'labels' in paths
            }
            
            if common_files is None:
                common_files = valid_keys
            else:
                common_files = common_files.intersection(valid_keys)
        # print(f"Set: {set_name}, Common files: {valid_keys}")        
        # print(f"Common files: {common_files}")
        # Copy common files to output folder
        for file_key in common_files:
            # Get any set's file paths (they're all common)
            paths = next(iter(set_files.values()))[file_key]
            
            # Copy image file
            if 'images' in paths:
                source_path = paths['images']
                dest_path = os.path.join(output_folder, 'images', os.path.basename(source_path))
                shutil.copy2(source_path, dest_path)
                # print(f"Copied: {dest_path}")
            
            # Copy label file
            if 'labels' in paths:
                source_path = paths['labels']
                dest_path = os.path.join(output_folder, 'labels', os.path.basename(source_path))
                shutil.copy2(source_path, dest_path)
                # print(f"Copied: {dest_path}")

def main():
    input_folder = "/media/ntlpt19/5250315B5031474F/finance_data_modeling/Classification/benchmark_images/table_results/set_data/set13"
    output_folder = "/media/ntlpt19/5250315B5031474F/finance_data_modeling/Classification/benchmark_images/table_results/set_data/temp_fol"
    
    if not os.path.exists(input_folder):
        print("Input folder does not exist!")
        return
        
    find_common_files(input_folder, output_folder)
    print("Common files have been copied to the output folder.")

if __name__ == "__main__":
    main()