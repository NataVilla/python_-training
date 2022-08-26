pre_hipertension_sistolica = [120,121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]
pre_hipertension_diastolica = [80, 81, 82, 83, 84, 85, 86, 87, 88, 89]

hypertensive_first_grade_sistolica = [140,141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159]
hypertensive_first_grade_diastolica = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

a = int(input("Please enter the medition sistolica: "))
b = int(input("Please enter the medition diastolica: "))

def hypertension(a, b):
    if a < 120 and b < 80:
        print("your pressure is normal, great!!")
    elif a in pre_hipertension_sistolica and b in pre_hipertension_diastolica:
        print("You are pre hypertensive")
    elif a in hypertensive_first_grade_sistolica and b in hypertensive_first_grade_diastolica:
        print("you are hypertensive first grade")
    elif a >= 160 or b >= 100:
        print("you are hypertensive second grade")
    elif a in pre_hipertension_sistolica and b in hypertensive_first_grade_diastolica or a in hypertensive_first_grade_sistolica and b in pre_hipertension_diastolica:
        print("you are hypertensive first grade")
    elif a < 120 and b in pre_hipertension_diastolica or a in pre_hipertension_sistolica and b < 80:
        print("You are pre hypertensive")
    else:
        print("HYPERTENSIVE CRISIS (consult your doctor immediately)")



hypertension(a,b)
