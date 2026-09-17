# project2-artifact-archiver/app.py
def generate_academic_report():
    # Default system metrics & mock data
    total_students = 120
    active_exam_sessions = 45
    passing_rate = "88.5%"
    
    print("Initializing Student Performance System compilation...")
    
    # Write the calculated information directly to a report text file
    with open("report.txt", "w") as f:
        f.write("===============================================\n")
        f.write("  STUDENT ACADEMIC PERFORMANCE SYSTEM REPORT   \n")
        f.write("===============================================\n")
        f.write(f"Total Registered Students : {total_students}\n")
        f.write(f"Active Exam Sessions      : {active_exam_sessions}\n")
        f.write(f"Overall Passing Rate       : {passing_rate}\n")
        f.write("System Status             : All final grades archived successfully.\n")
        f.write("===============================================\n")
        
    print("Success: 'report.txt' has been generated for archiving.")

if __name__ == "__main__":
    generate_academic_report()
