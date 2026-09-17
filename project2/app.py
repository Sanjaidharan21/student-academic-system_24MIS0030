# project2-artifact-archiver/app.py

def generate_academic_report():
    # Pre-defined default data inputs representing compiled system metrics
    total_students = 120
    active_exam_sessions = 45
    passing_rate = "88.5%"
    
    print("[SYSTEM] Compiling academic record performance figures...")
    
    # Save statistics out into a text report format
    with open("report.txt", "w") as f:
        f.write("===================================================\n")
        f.write("    STUDENT ACADEMIC PERFORMANCE PERFORMANCE REPORT \n")
        f.write("===================================================\n")
        f.write(f"Total Enrolled Records  : {total_students}\n")
        f.write(f"Active Exam Logs        : {active_exam_sessions}\n")
        f.write(f"System Average Pass Rate: {passing_rate}\n")
        f.write("Build Verification State: COMPILING SUCCESSFUL\n")
        f.write("===================================================\n")
        
    print("[SYSTEM] Data written. 'report.txt' generated locally.")

if __name__ == "__main__":
    generate_academic_report()
