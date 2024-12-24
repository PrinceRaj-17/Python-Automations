import os
import shutil

def clear_cache():
    cache_dir = os.path.expanduser("~/Library/Caches")
    if os.path.exists(cache_dir):
        print(f"Clearing cache from {cache_dir}...")
        try:
            for item in os.listdir(cache_dir):
                item_path = os.path.join(cache_dir, item)
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            print("Cache cleared successfully.")
        except Exception as e:
            print(f"Error while clearing cache: {e}")
    else:
        print(f"Cache directory {cache_dir} does not exist.")

def clear_trash():
    trash_dir = os.path.expanduser("~/.Trash")
    if os.path.exists(trash_dir):
        print("Clearing Trash...")
        try:
            for item in os.listdir(trash_dir):
                item_path = os.path.join(trash_dir, item)
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            print("Trash cleared successfully.")
        except Exception as e:
            print(f"Error while clearing Trash: {e}")
    else:
        print("Trash directory does not exist.")

def main():
    print("This script will clear:")
    print("1. Cache files from ~/Library/Caches")
    print("2. All items in the Trash (bin)")
    confirm = input("Do you want to proceed? (yes/no): ")
    if confirm.lower() in ['yes', 'y']:
        clear_cache()
        clear_trash()
    else:
        print("Operation canceled.")

if __name__ == "__main__":
    main()