import csv

# Define the header and data
header = ['first_subject', 'second_subject', 'third_subject', 'first_performance', 'second_performance', 'third_performance', 'course_names']
data = [
    # starts BNS
    ['Biology', 'Nutrition', 'Sports', 'S', 'F', 'F', 'No Course Available'],
    ['Biology', 'Nutrition', 'Sports', 'F', 'S', 'F', 'No Course Available'],
    ['Biology', 'Nutrition', 'Sports', 'F', 'F', 'F', 'No Course Available'],
    # starts LMS
    ['English', 'Music', 'Sports', 'S', 'F', 'F', 'No Course Available'],
    ['English', 'Music', 'Sports', 'F', 'S', 'F', 'No Course Available'],
    ['English', 'Music', 'Sports', 'F', 'F', 'F', 'No Course Available'],
    # starts KMS
    ['Kiswahili', 'Music', 'Sports', 'S', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Music', 'Sports', 'F', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Music', 'Sports', 'F', 'F', 'F', 'No Course Available'],
    # starts FaMS
    ['Fasihi', 'Music', 'Sports', 'S', 'F', 'F', 'No Course Available'],
    ['Fasihi', 'Music', 'Sports', 'F', 'S', 'F', 'No Course Available'],
    ['Fasihi', 'Music', 'Sports', 'F', 'F', 'F', 'No Course Available'],
    # starts LiMS
    ['Literature', 'Music', 'Sports', 'S', 'F', 'F', 'No Course Available'],
    ['Literature', 'Music', 'Sports', 'F', 'S', 'F', 'No Course Available'],
    ['Literature', 'Music', 'Sports', 'F', 'F', 'F', 'No Course Available'],
    # starts FMS
    ['French', 'Music', 'Sports', 'S', 'F', 'F', 'No Course Available'],
    ['French', 'Music', 'Sports', 'F', 'S', 'F', 'No Course Available'],
    ['French', 'Music', 'Sports', 'F', 'F', 'F', 'No Course Available'],
    # starts ArMS
    ['Arabic', 'Music', 'Sports', 'S', 'F', 'F', 'No Course Available'],
    ['Arabic', 'Music', 'Sports', 'F', 'S', 'F', 'No Course Available'],
    ['Arabic', 'Music', 'Sports', 'F', 'F', 'F', 'No Course Available'],
    # Add more rows as needed
]

# Specify the file name
csv_file_path = 'division_zero_sports.csv'

# Writing to CSV file with tab delimiter
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header to the CSV file
    csv_writer.writerow(header)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print(f'CSV file "{csv_file_path}" has been created.')
