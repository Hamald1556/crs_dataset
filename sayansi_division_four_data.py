import csv

# Define the header and data
header = ['first_subject', 'second_subject', 'third_subject', 'first_performance', 'second_performance', 'third_performance', 'course_names']
data = [
    # starts 01  
    ['Physics', 'Chemistry', 'Mathematics', 'D', 'F', 'F', 'No Course Available'],
    ['Physics', 'Chemistry', 'Mathematics', 'E', 'S', 'F', 'No Course Available'],
    ['Physics', 'Chemistry', 'Mathematics', 'E', 'F', 'F', 'No Course Available'],
    ['Physics', 'Chemistry', 'Mathematics', 'S', 'E', 'F', 'No Course Available'],
    ['Physics', 'Chemistry', 'Mathematics', 'S', 'F', 'F', 'No Course Available'],
    ['Physics', 'Chemistry', 'Mathematics', 'F', 'D', 'F', 'No Course Available'],
    ['Physics', 'Chemistry', 'Mathematics', 'F', 'E', 'F', 'No Course Available'],

    # starts 02 
    ['Physics', 'Chemistry', 'Biology', 'D', 'F', 'F', 'No Course Available'],
    ['Physics', 'Chemistry', 'Biology', 'E', 'S', 'F', 'No Course Available'],
    ['Physics', 'Chemistry', 'Biology', 'E', 'F', 'F', 'No Course Available'],
    ['Physics', 'Chemistry', 'Biology', 'S', 'E', 'F', 'No Course Available'],
    ['Physics', 'Chemistry', 'Biology', 'S', 'F', 'F', 'No Course Available'],
    ['Physics', 'Chemistry', 'Biology', 'F', 'D', 'F', 'No Course Available'],
    ['Physics', 'Chemistry', 'Biology', 'F', 'E', 'F', 'No Course Available'],

    # starts 03 
    ['Physics', 'Mathematics', 'Computer', 'D', 'F', 'F', 'No Course Available'],
    ['Physics', 'Mathematics', 'Computer', 'E', 'S', 'F', 'No Course Available'],
    ['Physics', 'Mathematics', 'Computer', 'E', 'F', 'F', 'No Course Available'],
    ['Physics', 'Mathematics', 'Computer', 'S', 'E', 'F', 'No Course Available'],
    ['Physics', 'Mathematics', 'Computer', 'S', 'F', 'F', 'No Course Available'],
    ['Physics', 'Mathematics', 'Computer', 'F', 'D', 'F', 'No Course Available'],
    ['Physics', 'Mathematics', 'Computer', 'F', 'E', 'F', 'No Course Available'],

    # STARTS 04 
    ['Chemistry', 'Biology', 'Agriculture', 'D', 'F', 'F', 'No Course Available'],
    ['Chemistry', 'Biology', 'Agriculture', 'E', 'S', 'F', 'No Course Available'],
    ['Chemistry', 'Biology', 'Agriculture', 'E', 'F', 'F', 'No Course Available'],
    ['Chemistry', 'Biology', 'Agriculture', 'S', 'E', 'F', 'No Course Available'],
    ['Chemistry', 'Biology', 'Agriculture', 'S', 'F', 'F', 'No Course Available'],
    ['Chemistry', 'Biology', 'Agriculture', 'F', 'D', 'F', 'No Course Available'],
    ['Chemistry', 'Biology', 'Agriculture', 'F', 'E', 'F', 'No Course Available'],

    # starts 05 
    ['Chemistry', 'Biology', 'Nutrition', 'D', 'F', 'F', 'No Course Available'],
    ['Chemistry', 'Biology', 'Nutrition', 'E', 'S', 'F', 'No Course Available'],
    ['Chemistry', 'Biology', 'Nutrition', 'E', 'F', 'F', 'No Course Available'],
    ['Chemistry', 'Biology', 'Nutrition', 'S', 'E', 'F', 'No Course Available'],
    ['Chemistry', 'Biology', 'Nutrition', 'S', 'F', 'F', 'No Course Available'],
    ['Chemistry', 'Biology', 'Nutrition', 'F', 'D', 'F', 'No Course Available'],
    ['Chemistry', 'Biology', 'Nutrition', 'F', 'E', 'F', 'No Course Available'],


    # Add more rows as needed
]

# Specify the file name
csv_file_path = 'division_four_sayansi.csv'

# Writing to CSV file with tab delimiter
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header to the CSV file
    csv_writer.writerow(header)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print(f'CSV file "{csv_file_path}" has been created.')
