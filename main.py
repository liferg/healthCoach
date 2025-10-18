from app.labResults import LabResults

def interpret_labs(labResults: LabResults):
    results = {}

    if labResults.glucose > 100:
        results["glucose"] = "Borderline high. Consider moderating sugar intake."
    else:
        results["glucose"] = "Glucose looks good!"

    if labResults.ldl > 130:
        results["ldl"] = "High LDL cholesterol. Focus on fiber and healthy fats."
    else:
        results["ldl"] = "LDL is in a healthy range."

    if labResults.vitamin_d < 30:
        results["vitamin_d"] = "Low vitamin D. Sunlight or supplements may help."
    else:
        results["vitamin_d"] = "Vitamin D is in range."

    return results

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
