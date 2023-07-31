db_file = "student_data.db"


def register_api():
    stu_data = {}  # ini an empty list
    print("Welcome to Gordon's college".center(50, "-"))
    print("please complete the register")
    name = input("name").strip()
    age = input("age：").strip()
    phone = input("phone number：").strip()
    id = input("ID").strip()

    course_list = ["python", "Linux", "security", "testing", "SRE"]
    for index, course in enumerate(course_list):
        print(f"{index}.{course}")

    selected_course = input("Course you pick:")
    if selected_course.isdigit():
        selected_course = int(selected_course)
        if selected_course >= 0 and selected_course < len(course_list):
            pick_course = course_list[selected_course]
        else:
            exit("no this course")
    else:
        exit("put correct code")

    stu_data["name"] = name
    stu_data["age"] = age
    stu_data["phone"] = phone
    stu_data["id"] = id
    stu_data["course"] = pick_course

    return stu_data


def commit_to_db(filename, stu_data):
    """

    :param filename: student's info.
    :param stu_data:sigle dict
    :return:
    """
    f = open(filename, "a")
    row = f"{stu_data['name']},{stu_data['age']},{stu_data['phone']},{stu_data['id']},{stu_data['course']}\n"
    f.write(row)
    f.close()


stu_data = register_api()
print(stu_data)
commit_to_db(db_file,stu_data)