"""*** BEGIN PROVIDED CODE ***"""
def check_row_types(row):
    """
    Checks to ensure that a list is of length 8 and that each element is type float

    :param row: a list to check
    :return: True if the length of row is 8 and all elements are floats
    """
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True
"""*** END PROVIDED CODE ***"""



"""*** WRITE YOUR CODE BELOW THIS LINE ***"""
def convert_row_type(row):
    converted_row = []
    for value in row:
        converted_row.append(float(value))

    return converted_row


def calculate_score(admission_info):
    sat,gpa,interest,hs_quality = admission_info
    normalized_sat = sat / 160
    normalized_gpa = gpa * 2
    score = (normalized_sat * 0.3) + (normalized_gpa * 0.4) + (interest * 0.1) + (hs_quality * 0.2)

    return score


def is_outlier(admission_info):
    sat,gpa,interest,hs_quality = admission_info
    normalized_sat = sat / 160
    normalized_gpa = gpa * 2

    if interest == 0 or normalized_gpa > normalized_sat + 2:
        return True
    return False


def calculate_score_improved(admission_info):
    score = calculate_score(admission_info)
    outlier = is_outlier(admission_info)

    if score >= 6 or outlier:
        return True
    return False


def grade_outlier(semester_grades):
    sorted_grades = sorted(semester_grades)
    lowest = sorted_grades[0]
    second_lowest = sorted_grades[1]

    if second_lowest - lowest >= 20:
        return True
    return False


def grade_improvement(semester_grades):
    return semester_grades == sorted(semester_grades)





def main():
    filename = "admission_algorithms_dataset.csv"
    with open(filename, "r") as input_file:
        print("Processing " + filename + "...")
        headers = input_file.readline() # grab the line with the headers

        lines = input_file.readlines()

        scores_file = open("student_scores.csv", "w")
        chosen_file = open("chosen_students.csv", "w")
        outliers_file = open("outliers.csv", "w")
        chosen_improved_file = open("chosen_improved.csv", "w")
        better_improved_file = open("better_improved.csv", "w")
        composite_chosen_file = open("composite_chosen.csv", "w")

        for line in lines:
            line = line.strip("\n")
            fields = line.split(",")
            name = fields[0]
            del fields[0]
            # print(fields) # only displays student information

            converted_row = convert_row_type(fields)
            if not check_row_types(converted_row):
                print(f"Error converting row for {name}")

            admission_info = converted_row[:4]
            semester_grades = converted_row[4:]

            score = calculate_score(admission_info)
            scores_file.write(f"{name},{score:.2f}\n")

            if score >= 6:
                chosen_file.write(f"{name}\n")

            outlier = is_outlier(admission_info)
            if outlier:
                outliers_file.write(f"{name}\n")

            if score >= 6 or (outlier and score >= 5):
                chosen_improved_file.write(f"{name}\n")

            if calculate_score_improved(admission_info):
                sat,gpa,interest,hs_quality = admission_info
                better_improved_file.write(f"{name},{sat},{gpa},{interest},{hs_quality}\n")

            has_grade_outlier = grade_outlier(semester_grades)
            # if has_grade_outlier:
            #     print(f"{name} has a grade outlier: {semester_grades}")
            has_improvement = grade_improvement(semester_grades)
            if score >= 6 or (score >= 5 and (outlier or has_grade_outlier or has_improvement)):
                composite_chosen_file.write(f"{name}\n")

        scores_file.close()
        chosen_file.close()
        outliers_file.close()
        chosen_improved_file.close()
        better_improved_file.close()

    print("done!")





# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()