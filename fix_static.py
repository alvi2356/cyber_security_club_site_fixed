import os
import shutil
from pathlib import Path

def fix_static_files():
    # Get the base directory
    base_dir = Path(__file__).resolve().parent
    
    # Define paths
    static_dir = base_dir / 'static'
    staticfiles_dir = base_dir / 'staticfiles'
    
    print("Checking static files...")
    
    # Create directories if they don't exist
    static_dir.mkdir(exist_ok=True)
    staticfiles_dir.mkdir(exist_ok=True)
    
    # Check if static files exist
    if not list(static_dir.glob('**/*')):
        print("ERROR: No static files found in static directory!")
        return False
    
    # Clean staticfiles directory
    print("Cleaning staticfiles directory...")
    if staticfiles_dir.exists():
        shutil.rmtree(staticfiles_dir)
    staticfiles_dir.mkdir()
    
    # Copy static files
    print("Copying static files...")
    for item in static_dir.glob('**/*'):
        if item.is_file():
            rel_path = item.relative_to(static_dir)
            dest_path = staticfiles_dir / rel_path
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, dest_path)
            print(f"Copied: {rel_path}")
    
    print("Static files fixed successfully!")
    return True

if __name__ == "__main__":
    fix_static_files() 