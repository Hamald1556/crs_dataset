import csv

# Define the header and data
header = ['first_subject', 'second_subject', 'third_subject', 'first_performance', 'second_performance', 'third_performance', 'course_names']
data = [
    # starts 01
    ['Economics', 'Business', 'Accountancy', 'S', 'F', 'F', 'No Available Courses'],
    ['Economics', 'Business', 'Accountancy', 'F', 'S', 'F', 'No Available Courses'],
    ['Economics', 'Business', 'Accountancy', 'F', 'F', 'F', 'No Available Courses'],
    # starts 02
    ['Economics', 'Geography', 'Mathematics', 'S', 'F', 'F', 'No Available Courses'],
    ['Economics', 'Geography', 'Mathematics', 'F', 'S', 'F', 'No Available Courses'],
    ['Economics', 'Geography', 'Mathematics', 'F', 'F', 'F', 'No Available Courses'],
    # starts 03
    ['Economics', 'Computer', 'Mathematics', 'S', 'F', 'F', 'No Available Courses'],
    ['Economics', 'Geography', 'Mathematics', 'F', 'S', 'F', 'No Available Courses'],
    ['Economics', 'Geography', 'Mathematics', 'F', 'F', 'F', 'No Available Courses'],
    # starts 04
    ['Business', 'Accountancy', 'Computer', 'S', 'F', 'F', 'No Available Courses'],
    ['Business', 'Accountancy', 'Computer', 'F', 'S', 'F', 'No Available Courses'],
    ['Business', 'Accountancy', 'Computer', 'F', 'F', 'F', 'No Available Courses'],
    # starts 05
    ['Business', 'Accountancy', 'Mathematics', 'S', 'F', 'F', 'No Available Courses'],
    ['Business', 'Accountancy', 'Mathematics', 'F', 'S', 'F', 'No Available Courses'],
    ['Business', 'Accountancy', 'Mathematics', 'F', 'F', 'F', 'No Available Courses'],
    # Add more rows as needed
]

# Specify the file name
csv_file_path = 'division_zero_business.csv'

# Writing to CSV file with tab delimiter
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header to the CSV file
    csv_writer.writerow(header)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print(f'CSV file "{csv_file_path}" has been created.')
