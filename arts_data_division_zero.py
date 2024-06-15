import csv

# Define the header and data
header = ['first_subject', 'second_subject', 'third_subject', 'first_performance', 'second_performance', 'third_performance', 'course_names']
data = [
    # starts 1
    ['Kiswahili', 'English', 'Arts', 'S', 'F', 'F','No Course Available'],
    ['Kiswahili', 'English', 'Arts', 'F', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Arts', 'F', 'F', 'F', 'No Course Available'],
    # starts 2
    ['Kiswahili', 'French', 'Arts', 'S', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Arts', 'F', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Arts', 'F', 'F', 'F', 'No Course Available'],
    # starts 3
    ['Fasihi', 'English', 'Arts', 'S', 'F', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Arts', 'F', 'S', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Arts', 'F', 'F', 'F', 'No Course Available'],
    # starts 4
    ['Kiswahili', 'Literature', 'Arts', 'S', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Arts', 'F', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Arts', 'F', 'F', 'F', 'No Course Available'],
    # starts 5
    ['Kiswahili', 'English', 'Music', 'S', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Music', 'F', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Music', 'F', 'F', 'F', 'No Course Available'],
    # starts 6
    ['Kiswahili', 'French', 'Music', 'S', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Music', 'F', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Music', 'F', 'F', 'F', 'No Course Available'],
    # starts 7
    ['Fasihi', 'English', 'Music', 'S', 'F', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Music', 'F', 'S', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Music', 'F', 'F', 'F', 'No Course Available'],
    # starts 8
    ['Kiswahili', 'Literature', 'Music', 'S', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Music', 'F', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Music', 'F', 'F', 'F', 'No Course Available'],
    # starts 9
    ['Kiswahili', 'English', 'Fine Arts', 'S', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Fine Arts', 'F', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Fine Arts', 'F', 'F', 'F', 'No Course Available'],
    # starts 10
    ['Kiswahili', 'French', 'Fine Arts', 'S', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Fine Arts', 'F', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Fine Arts', 'F', 'F', 'F', 'No Course Available'],
    # starts 11
    ['Fasihi', 'English', 'Fine Arts', 'S', 'F', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Fine Arts', 'F', 'S', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Fine Arts', 'F', 'F', 'F', 'No Course Available'],
    # starts 12
    ['Kiswahili', 'Literature', 'Fine Arts', 'S', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Fine Arts', 'F', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Fine Arts', 'F', 'F', 'F', 'No Course Available'],
    # starts 13
    ['Kiswahili', 'Textile', 'Fine Arts', 'S', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Textile', 'Fine Arts', 'F', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Textile', 'Fine Arts', 'F', 'F', 'F', 'No Course Available'],
    # starts 14
    ['English', 'Textile', 'Fine Arts', 'S', 'F', 'F', 'No Course Available'],
    ['English', 'Textile', 'Fine Arts', 'F', 'S', 'F', 'No Course Available'],
    ['English', 'Textile', 'Fine Arts', 'F', 'F', 'F', 'No Course Available'],
    # starts 15
    ['Arabic', 'Textile', 'Fine Arts', 'S', 'F', 'F', 'No Course Available'],
    ['Arabic', 'Textile', 'Fine Arts', 'F', 'S', 'F', 'No Course Available'],
    ['Arabic', 'Textile', 'Fine Arts', 'F', 'F', 'F', 'No Course Available'],
    # starts 16
    ['Chinese', 'Textile', 'Fine Arts', 'S', 'F', 'F', 'No Course Available'],
    ['Chinese', 'Textile', 'Fine Arts', 'F', 'S', 'F', 'No Course Available'],
    ['Chinese', 'Textile', 'Fine Arts', 'F', 'F', 'F', 'No Course Available'],
    # Add more rows as needed
]

# Specify the file name
csv_file_path = 'division_zero_arts.csv'

# Writing to CSV file with tab delimiter
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header to the CSV file
    csv_writer.writerow(header)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print(f'CSV file "{csv_file_path}" has been created.')
