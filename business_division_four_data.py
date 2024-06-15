import csv

# Define the header and data
header = ['first_subject', 'second_subject', 'third_subject', 'first_performance', 'second_performance', 'third_performance', 'course_names']
data = [
    # starts 01
    ['Economics', 'Business', 'Accountancy', 'D', 'F', 'F', 'No Available Courses'],
    ['Economics', 'Business', 'Accountancy', 'E', 'S', 'F', 'No Available Courses'],
    ['Economics', 'Business', 'Accountancy', 'E', 'F', 'F', 'No Available Courses'],
    ['Economics', 'Business', 'Accountancy', 'S', 'E', 'F', 'No Available Courses'],
    ['Economics', 'Business', 'Accountancy', 'S', 'S', 'F', 'No Available Courses'],
    ['Economics', 'Business', 'Accountancy', 'F', 'D', 'F', 'No Available Courses'],
    ['Economics', 'Business', 'Accountancy', 'F', 'E', 'F', 'No Available Courses'],
   
    # starts 02
    ['Economics', 'Geography', 'Mathematics', 'D', 'F', 'F', 'No Available Courses'],
    ['Economics', 'Geography', 'Mathematics', 'E', 'S', 'F', 'No Available Courses'],
    ['Economics', 'Geography', 'Mathematics', 'E', 'F', 'F', 'No Available Courses'],
    ['Economics', 'Geography', 'Mathematics', 'S', 'E', 'F', 'No Available Courses'],
    ['Economics', 'Geography', 'Mathematics', 'S', 'S', 'F', 'No Available Courses'],
    ['Economics', 'Geography', 'Mathematics', 'F', 'D', 'F', 'No Available Courses'],
    ['Economics', 'Geography', 'Mathematics', 'F', 'E', 'F', 'No Available Courses'],
    
    # starts 03
    ['Economics', 'Computer', 'Mathematics', 'D', 'F', 'F', 'No Available Courses'],
    ['Economics', 'Geography', 'Mathematics', 'E', 'S', 'F', 'No Available Courses'],
    ['Economics', 'Geography', 'Mathematics', 'E', 'F', 'F', 'No Available Courses'],
    ['Economics', 'Computer', 'Mathematics', 'S', 'E', 'F', 'No Available Courses'],
    ['Economics', 'Geography', 'Mathematics', 'S', 'S', 'F', 'No Available Courses'],
    ['Economics', 'Geography', 'Mathematics', 'F', 'D', 'F', 'No Available Courses'],
    ['Economics', 'Computer', 'Mathematics', 'F', 'E', 'F', 'No Available Courses'],
   
    # starts 04
    ['Business', 'Accountancy', 'Computer', 'D', 'F', 'F', 'No Available Courses'],
    ['Business', 'Accountancy', 'Computer', 'E', 'S', 'F', 'No Available Courses'],
    ['Business', 'Accountancy', 'Computer', 'E', 'F', 'F', 'No Available Courses'],
    ['Business', 'Accountancy', 'Computer', 'S', 'E', 'F', 'No Available Courses'],
    ['Business', 'Accountancy', 'Computer', 'S', 'S', 'F', 'No Available Courses'],
    ['Business', 'Accountancy', 'Computer', 'F', 'D', 'F', 'No Available Courses'],
    ['Business', 'Accountancy', 'Computer', 'F', 'E', 'F', 'No Available Courses'],
 
    # starts 05
    ['Business', 'Accountancy', 'Mathematics', 'D', 'F', 'F', 'No Available Courses'],
    ['Business', 'Accountancy', 'Mathematics', 'E', 'S', 'F', 'No Available Courses'],
    ['Business', 'Accountancy', 'Mathematics', 'E', 'F', 'F', 'No Available Courses'],
    ['Business', 'Accountancy', 'Mathematics', 'S', 'E', 'F', 'No Available Courses'],
    ['Business', 'Accountancy', 'Mathematics', 'S', 'S', 'F', 'No Available Courses'],
    ['Business', 'Accountancy', 'Mathematics', 'F', 'D', 'F', 'No Available Courses'],
    ['Business', 'Accountancy', 'Mathematics', 'F', 'E', 'F', 'No Available Courses'],
   
    # Add more rows as needed
]

# Specify the file name
csv_file_path = 'division_four_business.csv'

# Writing to CSV file with tab delimiter
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header to the CSV file
    csv_writer.writerow(header)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print(f'CSV file "{csv_file_path}" has been created.')
