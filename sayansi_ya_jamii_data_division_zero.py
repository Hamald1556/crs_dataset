import csv

# Define the header and data
header = ['first_subject', 'second_subject', 'third_subject', 'first_performance', 'second_performance', 'third_performance', 'course_names']
data = [
    # starts 01
    ['History', 'Geography', 'Kiswahili', 'S', 'F', 'F', 'No Course Available'],
    ['History', 'Geography', 'Kiswahili', 'F', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'Kiswahili', 'F', 'F', 'F', 'No Course Available'],
    # starts 02
    ['History', 'Geography', 'English', 'S', 'F', 'F', 'No Course Available'],
    ['History', 'Geography', 'English', 'F', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'English', 'F', 'F', 'F', 'No Course Available'],
    # starts 03
    ['History', 'Geography', 'French', 'S', 'F', 'F', 'No Course Available'],
    ['History', 'Geography', 'French', 'F', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'French', 'F', 'F', 'F', 'No Course Available'],
    # STARTS 04
    ['History', 'Geography', 'Arabic', 'S', 'F', 'F', 'No Course Available'],
    ['History', 'Geography', 'Arabic', 'F', 'S', 'F', 'No Course Available'],
     ['History', 'Geography', 'Arabic', 'F', 'F', 'F', 'No Course Available'],
    #  starts 05
    ['History', 'Geography', 'Chinese', 'S', 'F', 'F', 'No Course Available'],
    ['History', 'Geography', 'Chinese', 'F', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'Chinese', 'F', 'F', 'F', 'No Course Available'],
    # starts 06
    ['History', 'Geography', 'Fasihi', 'S', 'F', 'F', 'No Course Available'],
    ['History', 'Geography', 'Fasihi', 'F', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'Fasihi', 'F', 'F', 'F', 'No Course Available'],
    # starts 07
    ['History', 'Geography', 'Literature', 'S', 'F', 'F', 'No Course Available'],
    ['History', 'Geography', 'Literature', 'F', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'Literature', 'F', 'F', 'F', 'No Course Available'],
    # Add more rows as needed
]

# Specify the file name
csv_file_path = 'division_zero_sayansi_jamii.csv'

# Writing to CSV file with tab delimiter
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header to the CSV file
    csv_writer.writerow(header)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print(f'CSV file "{csv_file_path}" has been created.')
