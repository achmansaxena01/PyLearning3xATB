def allowed_to_attend_python_class(name):
    match name:
        case "DELL":
            print("Dell is allowed")
        case "Shubham":
            print("Shubham is allowed")
        case "Pallavi":
            print("Pallavi is allowed")
        case "Rajan":
            print("Rajan is allowed")
        case "Suresh":
            print("Suresh is allowed")
        case _:
            print("None")


print("Enter name")
name1 = input("name1")
allowed_to_attend_python_class(name1)
