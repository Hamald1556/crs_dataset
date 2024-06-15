import csv

# Define the header and data
header = ['first_subject', 'second_subject', 'third_subject', 'first_performance', 'second_performance', 'third_performance', 'course_names']
data = [
    # starts PCM
    ['Physics', 'Chemistry', 'Mathematics', 'S', 'F', 'F', 'No Course Available'],
    ['Physics', 'Chemistry', 'Mathematics', 'F', 'S', 'F', 'No Course Available'],
    ['Physics', 'Chemistry', 'Mathematics', 'F', 'F', 'F', 'No Course Available'],
    # starts PCB
    ['Physics', 'Chemistry', 'Biology', 'S', 'F', 'F', 'No Course Available'],
    ['Physics', 'Chemistry', 'Biology', 'F', 'S', 'F', 'No Course Available'],
    ['Physics', 'Chemistry', 'Biology', 'F', 'F', 'F', 'No Course Available'],
    # starts PMC
    ['Physics', 'Mathematics', 'Computer Science', 'S', 'F', 'F', 'No Course Available'],
    ['Physics', 'Mathematics', 'Computer Science', 'F', 'S', 'F', 'No Course Available'],
    ['Physics', 'Mathematics', 'Computer Science', 'F', 'F', 'F', 'No Course Available'],
    # starts CBA
    ['Chemistry', 'Biology', 'Agriculture', 'S', 'F', 'F', 'No Course Available'],
    ['Chemistry', 'Biology', 'Agriculture', 'F', 'S', 'F', 'No Course Available'],
    ['Chemistry', 'Biology', 'Agriculture', 'F', 'F', 'F', 'No Course Available'],
    #   starts CBN
    ['Chemistry', 'Biology', 'Nutrition', 'S', 'F', 'F', 'No Course Available'],
    ['Chemistry', 'Biology', 'Nutrition', 'F', 'S', 'F', 'No Course Available'],
    ['Chemistry', 'Biology', 'Nutrition', 'F', 'F', 'F', 'No Course Available'],
    # Add more rows as needed
]

# Specify the file name
csv_file_path = 'division_zero_sayansi.csv'

# Writing to CSV file with tab delimiter
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header to the CSV file
    csv_writer.writerow(header)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print(f'CSV file "{csv_file_path}" has been created.')
