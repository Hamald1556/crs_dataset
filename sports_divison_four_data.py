import csv

# Define the header and data
header = ['first_subject', 'second_subject', 'third_subject', 'first_performance', 'second_performance', 'third_performance', 'course_names']
data = [
    # starts BNS
    # starts 01 

    ['Biology', 'Nutrition', 'Sports', 'D', 'F', 'F', 'No Course Available'],
    ['Biology', 'Nutrition', 'Sports', 'E', 'S', 'F', 'No Course Available'],
    ['Biology', 'Nutrition', 'Sports', 'E', 'F', 'F', 'No Course Available'],
    ['Biology', 'Nutrition', 'Sports', 'S', 'E', 'F', 'No Course Available'],
    ['Biology', 'Nutrition', 'Sports', 'S', 'S', 'F', 'No Course Available'],
    ['Biology', 'Nutrition', 'Sports', 'F', 'D', 'F', 'No Course Available'],
    ['Biology', 'Nutrition', 'Sports', 'F', 'E', 'F', 'No Course Available'],
    # starts LMS
    # STARTS 02 

    ['English', 'Music', 'Sports', 'D', 'F', 'F', 'No Course Available'],
    ['English', 'Music', 'Sports', 'E', 'S', 'F', 'No Course Available'],
    ['English', 'Music', 'Sports', 'E', 'F', 'F', 'No Course Available'],
    ['English', 'Music', 'Sports', 'S', 'E', 'F', 'No Course Available'],
    ['English', 'Music', 'Sports', 'S', 'S', 'F', 'No Course Available'],
    ['English', 'Music', 'Sports', 'F', 'D', 'F', 'No Course Available'],
    ['English', 'Music', 'Sports', 'F', 'E', 'F', 'No Course Available'],

    # starts KMS
    # starts 03 
    ['Kiswahili', 'Music', 'Sports', 'D', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Music', 'Sports', 'E', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Music', 'Sports', 'E', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Music', 'Sports', 'S', 'E', 'F', 'No Course Available'],
    ['Kiswahili', 'Music', 'Sports', 'S', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Music', 'Sports', 'F', 'D', 'F', 'No Course Available'],
    ['Kiswahili', 'Music', 'Sports', 'F', 'E', 'F', 'No Course Available'],

    # starts FaMS
    # starts 04 
    ['Fasihi', 'Music', 'Sports', 'D', 'F', 'F', 'No Course Available'],
    ['Fasihi', 'Music', 'Sports', 'E', 'S', 'F', 'No Course Available'],
    ['Fasihi', 'Music', 'Sports', 'E', 'F', 'F', 'No Course Available'],
    ['Fasihi', 'Music', 'Sports', 'S', 'E', 'F', 'No Course Available'],
    ['Fasihi', 'Music', 'Sports', 'S', 'S', 'F', 'No Course Available'],
    ['Fasihi', 'Music', 'Sports', 'F', 'D', 'F', 'No Course Available'],
    ['Fasihi', 'Music', 'Sports', 'F', 'E', 'F', 'No Course Available'],

    # starts LiMS
    # starts 05 
    ['Literature', 'Music', 'Sports', 'D', 'F', 'F', 'No Course Available'],
    ['Literature', 'Music', 'Sports', 'E', 'S', 'F', 'No Course Available'],
    ['Literature', 'Music', 'Sports', 'E', 'F', 'F', 'No Course Available'],
     ['Literature', 'Music', 'Sports', 'S', 'E', 'F', 'No Course Available'],
    ['Literature', 'Music', 'Sports', 'S', 'S', 'F', 'No Course Available'],
    ['Literature', 'Music', 'Sports', 'F', 'D', 'F', 'No Course Available'],
     ['Literature', 'Music', 'Sports', 'F', 'E', 'F', 'No Course Available'],
    
    # starts FMS
    # starts 06 
    ['French', 'Music', 'Sports', 'D', 'F', 'F', 'No Course Available'],
    ['French', 'Music', 'Sports', 'E', 'S', 'F', 'No Course Available'],
    ['French', 'Music', 'Sports', 'E', 'F', 'F', 'No Course Available'],
     ['French', 'Music', 'Sports', 'S', 'E', 'F', 'No Course Available'],
    ['French', 'Music', 'Sports', 'S', 'S', 'F', 'No Course Available'],
    ['French', 'Music', 'Sports', 'F', 'D', 'F', 'No Course Available'],
     ['French', 'Music', 'Sports', 'F', 'E', 'F', 'No Course Available'],
    
    # starts ArMS
    # starts 07 
    ['Arabic', 'Music', 'Sports', 'D', 'F', 'F', 'No Course Available'],
    ['Arabic', 'Music', 'Sports', 'E', 'S', 'F', 'No Course Available'],
    ['Arabic', 'Music', 'Sports', 'E', 'F', 'F', 'No Course Available'],
    ['Arabic', 'Music', 'Sports', 'S', 'E', 'F', 'No Course Available'],
    ['Arabic', 'Music', 'Sports', 'S', 'S', 'F', 'No Course Available'],
    ['Arabic', 'Music', 'Sports', 'F', 'D', 'F', 'No Course Available'],
    ['Arabic', 'Music', 'Sports', 'F', 'E', 'F', 'No Course Available'],
    # Add more rows as needed
]

# Specify the file name
csv_file_path = 'division_four_sports.csv'

# Writing to CSV file with tab delimiter
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header to the CSV file
    csv_writer.writerow(header)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print(f'CSV file "{csv_file_path}" has been created.')
