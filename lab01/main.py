import random

def Student_list(txt_file):
    
    try:
        with open(txt_file, 'r') as file:
            student_ids = [line.strip() for line in file if line.strip()]
        return student_ids
    except FileNotFoundError:
        print(f"Error: The file '{txt_file}' was not found.")
        return []

def viva_selection(student_ids):
    
    org_list = student_ids[:]
    num = 1

    while student_ids:
        selected = random.choice(student_ids)
        print(f"Student No.{num}: {selected}")
        student_ids.remove(selected)
        num += 1


    print("\nAll students have been selected for viva.\nResetting the list.")
    return org_list  

def main():
    txt_file = 'N:\CSE366\lab01\Student_info.txt'
    student_ids = Student_list(txt_file)

    if student_ids:       
        student_ids = viva_selection(student_ids)

        while True:

            print("\nStudent list has been reset. Ready for another round.")
            print("would you like to start another round ?")
            print("1.YES\n2.NO")

            ans = input("choose any:")

            if ans == '1':
                print("\nStarting another round...\n")
                student_ids = viva_selection(student_ids)

            elif ans == '2':
                 print("Exiting")
                 break

           # else :
              # print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
