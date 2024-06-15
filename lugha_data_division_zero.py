import csv

# Define the header and data
header = ['first_subject', 'second_subject', 'third_subject', 'first_performance', 'second_performance', 'third_performance', 'course_names']
data = [
    # starts 01
    ['Kiswahili', 'English', 'French', 'S', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'French', 'F', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'French', 'F', 'F', 'F', 'No Course Available'],
    # starts 2
    ['Kiswahili', 'English', 'Arabic', 'S', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Arabic', 'F', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Arabic', 'F', 'F', 'F', 'No Course Available'],
    # starts 03
    ['Kiswahili', 'English', 'Chinese', 'S', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Chinese', 'F', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Chinese', 'F', 'F', 'F', 'No Course Available'],
    # starts 04
    ['Kiswahili', 'Arabic', 'Chinese', 'S', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Arabic', 'Chinese', 'F', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Arabic', 'Chinese', 'F', 'F', 'F', 'No Course Available'],
    # starts 05
    ['Kiswahili', 'Arabic', 'French', 'S', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Arabic', 'French', 'F', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Arabic', 'French', 'F', 'F', 'F', 'No Course Available'],
    # starts 06
    ['English', 'French', 'Arabic', 'S', 'F', 'F', 'No Course Available'],
    ['English', 'French', 'Arabic', 'F', 'S', 'F', 'No Course Available'],
    ['English', 'French', 'Arabic', 'F', 'F', 'F', 'No Course Available'],
    # STARTS 07
    ['English', 'French', 'Chinese', 'S', 'F', 'F', 'No Course Available'],
    ['English', 'French', 'Chinese', 'F', 'S', 'F', 'No Course Available'],
    ['English', 'French', 'Chinese', 'F', 'F', 'F', 'No Course Available'],
    # starts 08
    ['French', 'Arabic', 'Chinese', 'S', 'F', 'F', 'No Course Available'],
    ['French', 'Arabic', 'Chinese', 'F', 'S', 'F', 'No Course Available'],
    ['French', 'Arabic', 'Chinese', 'F', 'F', 'F', 'No Course Available'],
    # starts 09 
    ['History', 'English', 'French', 'S', 'F', 'F', 'No Course Available'],
    ['History', 'English', 'French', 'F', 'S', 'F', 'No Course Available'],
    ['History', 'English', 'French', 'F', 'F', 'F', 'No Course Available'],
    # starts 10 
    ['History', 'English', 'Arabic', 'S', 'F', 'F', 'No Course Available'],
    ['History', 'English', 'Arabic', 'F', 'S', 'F', 'No Course Available'],
    ['History', 'English', 'Arabic', 'F', 'F', 'F', 'No Course Available'],
    # starts 11 
    ['History', 'English', 'Chinese', 'S', 'F', 'F', 'No Course Available'],
    ['History', 'English', 'Chinese', 'F', 'S', 'F', 'No Course Available'],
    ['History', 'English', 'Chinese', 'F', 'F', 'F', 'No Course Available'],
    # Add more rows as needed
]

# Specify the file name
csv_file_path = 'division_zero_lugha.csv'

# Writing to CSV file with tab delimiter
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header to the CSV file
    csv_writer.writerow(header)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print(f'CSV file "{csv_file_path}" has been created.')
