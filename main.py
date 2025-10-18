from app import LabResults, interpret_labs

if __name__ == "__main__":
    print("Enter glucose level: ")
    glucose = float(input())

    print("Enter LDL level: ")
    ldl = float(input())

    print("Enter vitamin D level: ")
    vitamin_d = float(input())

    labResults = LabResults(glucose=glucose, ldl=ldl, vitamin_d=vitamin_d)
    print("New lab results created")
    print(labResults)

    interpretation = interpret_labs(labResults)
    print(interpretation)
