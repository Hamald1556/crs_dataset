import csv

# Define the header and data
header = ['first_subject', 'second_subject', 'third_subject', 'first_performance', 'second_performance', 'third_performance', 'course_names']
data = [
    # starts IGH
    ['Islamic', 'History', 'Geography', 'S', 'F', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Geography', 'F', 'S', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Geography', 'F', 'F', 'F', 'No Course Available'],
    # starts DHG
    ['Divinity', 'History', 'Geography', 'S', 'F', 'F', 'No Course Available'],
    ['Divinity', 'History', 'Geography', 'F', 'S', 'F', 'No Course Available'],
    ['Divinity', 'History', 'Geography', 'F', 'F', 'F', 'No Course Available'],
    # starts IHAr 03
    ['Islamic', 'History', 'Arabic', 'S', 'F', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Arabic', 'F', 'S', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Arabic', 'F', 'F', 'F', 'No Course Available'],
    # starts 04
    ['Divinity', 'Kiswahili', 'English', 'S', 'F', 'F', 'No Course Available'],
    ['Divinity', 'Kiswahili', 'English', 'F', 'S', 'F', 'No Course Available'],
    ['Divinity', 'Kiswahili', 'English', 'F', 'F', 'F', 'No Course Available'],
    # starts 05
    ['Divinity', 'History', 'English', 'S', 'F', 'F', 'No Course Available'],
    ['Divinity', 'History', 'English', 'F', 'S', 'F', 'No Course Available'],
    ['Divinity', 'History', 'English', 'F', 'F', 'F', 'No Course Available'],
    # starts 06
    ['Islamic', 'History', 'English', 'S', 'F', 'F', 'No Course Available'],
    ['Islamic', 'History', 'English', 'F', 'S', 'F', 'No Course Available'],
    ['Islamic', 'History', 'English', 'F', 'F', 'F', 'No Course Available'],
    # starts 07
    ['Divinity', 'History', 'Kiswahili', 'S', 'F', 'F', 'No Course Available'],
    ['Divinity', 'History', 'Kiswahili', 'F', 'S', 'F', 'No Course Available'],
    ['Divinity', 'History', 'Kiswahili', 'F', 'F', 'F', 'No Course Available'],
    # starts 08
    ['Islamic', 'History', 'Kiswahili', 'S', 'F', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Kiswahili', 'F', 'S', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Kiswahili', 'F', 'F', 'F', 'No Course Available'],
    # Add more rows as needed
]

# Specify the file name
csv_file_path = 'division_zero_elimu_ya_dini.csv'

# Writing to CSV file with tab delimiter
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header to the CSV file
    csv_writer.writerow(header)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print(f'CSV file "{csv_file_path}" has been created.')
