# project1-parameterized/app.py
import sys

def initialize_environment():
    # Fallback to 'dev' default input if no parameter argument is passed by Jenkins
    environment = sys.argv[1] if len(sys.argv) > 1 else 'dev'
    
    print("===============================================")
    print("      STUDENT MANAGEMENT INITIALIZATION        ")
    print("===============================================")
    print(f"Loading database configuration profiles for: [{environment.upper()}]")
    print(f"Success: Academic Portal successfully provisioned on {environment} cluster.")

if __name__ == "__main__":
    initialize_environment()
