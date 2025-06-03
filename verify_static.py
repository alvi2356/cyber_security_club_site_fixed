import os
from django.conf import settings

def verify_static_files():
    print("Verifying static files...")
    
    # Check static root
    if not os.path.exists(settings.STATIC_ROOT):
        print(f"ERROR: STATIC_ROOT directory does not exist: {settings.STATIC_ROOT}")
        return False
    
    # Check static directories
    for static_dir in settings.STATICFILES_DIRS:
        if not os.path.exists(static_dir):
            print(f"ERROR: Static directory does not exist: {static_dir}")
            return False
    
    # Check for logo file
    logo_path = os.path.join(settings.STATIC_ROOT, 'assets', 'logo1.png')
    if not os.path.exists(logo_path):
        print(f"ERROR: Logo file not found: {logo_path}")
        return False
    
    print("Static files verification completed successfully!")
    return True

if __name__ == "__main__":
    verify_static_files() 