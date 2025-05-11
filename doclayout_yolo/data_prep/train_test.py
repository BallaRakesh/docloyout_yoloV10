import os
import random
from pathlib import Path

def split_dataset(images_dir, train_ratio=0.8, valid_ratio=0.10, test_ratio=0.10, seed=42):
    """
    Create text files listing train, validation, and test image paths without moving files.
    
    Args:
        images_dir (str): Path to directory containing images
        train_ratio (float): Ratio of images for training set
        valid_ratio (float): Ratio of images for validation set
        test_ratio (float): Ratio of images for test set
        seed (int): Random seed for reproducibility
    """
    # Set random seed for reproducibility
    random.seed(seed)
    
    # Get all image files
    image_files = [f for f in os.listdir(images_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
    random.shuffle(image_files)
    
    # Calculate split sizes
    total_images = len(image_files)
    train_size = int(total_images * train_ratio)
    valid_size = int(total_images * valid_ratio)
    
    # Split files
    train_files = image_files[:train_size]
    valid_files = image_files[train_size:train_size + valid_size]
    test_files = image_files[train_size + valid_size:]
    
    # Create text files listing the images
    base_dir = Path(images_dir).parent
    for split, files in [('train', train_files), ('valid', valid_files), ('test', test_files)]:
        with open(os.path.join(base_dir, f'{split}.txt'), 'w') as f:
            for file in files:
                f.write(f'./images/{file}\n')
    
    print(f"Text files created:")
    print(f"train.txt: {len(train_files)} images")
    print(f"valid.txt: {len(valid_files)} images")
    print(f"test.txt: {len(test_files)} images")

if __name__ == "__main__":
    # Example usage
    images_directory = "/media/ntlpt19/5250315B5031474F/finance_data_modeling/Classification/benchmark_images/table_results/set_data/train_master_data/images"
    split_dataset(images_directory)