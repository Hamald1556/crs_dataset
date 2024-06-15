import csv

# Define the header and data
header = ['first_subject', 'second_subject', 'third_subject', 'first_performance', 'second_performance', 'third_performance', 'course_names']
data = [
    # starts 1
    ['Kiswahili', 'English', 'Arts', 'D', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Arts', 'E', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Arts', 'E', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Arts', 'S', 'E', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Arts', 'S', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Arts', 'F', 'D', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Arts', 'F', 'E', 'F', 'No Course Available'],
    
    # starts 2
    ['Kiswahili', 'French', 'Arts', 'D', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Arts', 'E', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Arts', 'E', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Arts', 'S', 'E', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Arts', 'S', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Arts', 'F', 'D', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Arts', 'F', 'E', 'F', 'No Course Available'],
 
    # starts 3
    ['Fasihi', 'English', 'Arts', 'D', 'F', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Arts', 'E', 'S', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Arts', 'E', 'F', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Arts', 'S', 'E', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Arts', 'S', 'S', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Arts', 'F', 'D', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Arts', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 4
    ['Kiswahili', 'Literature', 'Arts', 'D', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Arts', 'E', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Arts', 'E', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Arts', 'S', 'E', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Arts', 'S', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Arts', 'F', 'D', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Arts', 'F', 'E', 'F', 'No Course Available'],
 
    # starts 5
    ['Kiswahili', 'English', 'Music', 'D', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Music', 'E', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Music', 'E', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Music', 'S', 'E', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Music', 'S', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Music', 'F', 'D', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Music', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 6
    ['Kiswahili', 'French', 'Music', 'D', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Music', 'E', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Music', 'E', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Music', 'S', 'E', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Music', 'S', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Music', 'F', 'D', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Music', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 7
    ['Fasihi', 'English', 'Music', 'D', 'F', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Music', 'E', 'S', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Music', 'E', 'F', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Music', 'S', 'E', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Music', 'S', 'S', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Music', 'F', 'D', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Music', 'F', 'E', 'F', 'No Course Available'],

    # starts 8
    ['Kiswahili', 'Literature', 'Music', 'D', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Music', 'E', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Music', 'E', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Music', 'S', 'E', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Music', 'S', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Music', 'F', 'D', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Music', 'F', 'E', 'F', 'No Course Available'],
    
    # starts 9
    ['Kiswahili', 'English', 'Fine Arts', 'D', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Fine Arts', 'E', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Fine Arts', 'E', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Fine Arts', 'S', 'E', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Fine Arts', 'S', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Fine Arts', 'F', 'D', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Fine Arts', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 10
    ['Kiswahili', 'French', 'Fine Arts', 'D', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Fine Arts', 'E', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Fine Arts', 'E', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Fine Arts', 'S', 'E', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Fine Arts', 'S', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Fine Arts', 'F', 'D', 'F', 'No Course Available'],
    ['Kiswahili', 'French', 'Fine Arts', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 11
    ['Fasihi', 'English', 'Fine Arts', 'D', 'F', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Fine Arts', 'E', 'S', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Fine Arts', 'E', 'F', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Fine Arts', 'S', 'E', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Fine Arts', 'S', 'S', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Fine Arts', 'F', 'D', 'F', 'No Course Available'],
    ['Fasihi', 'English', 'Fine Arts', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 12
    ['Kiswahili', 'Literature', 'Fine Arts', 'D', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Fine Arts', 'E', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Fine Arts', 'E', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Fine Arts', 'S', 'E', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Fine Arts', 'S', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Fine Arts', 'F', 'D', 'F', 'No Course Available'],
    ['Kiswahili', 'Literature', 'Fine Arts', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 13
    ['Kiswahili', 'Textile', 'Fine Arts', 'D', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Textile', 'Fine Arts', 'E', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Textile', 'Fine Arts', 'E', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Textile', 'Fine Arts', 'S', 'E', 'F', 'No Course Available'],
    ['Kiswahili', 'Textile', 'Fine Arts', 'S', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Textile', 'Fine Arts', 'F', 'D', 'F', 'No Course Available'],
    ['Kiswahili', 'Textile', 'Fine Arts', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 14
    ['English', 'Textile', 'Fine Arts', 'D', 'F', 'F', 'No Course Available'],
    ['English', 'Textile', 'Fine Arts', 'E', 'S', 'F', 'No Course Available'],
    ['English', 'Textile', 'Fine Arts', 'E', 'F', 'F', 'No Course Available'],
    ['English', 'Textile', 'Fine Arts', 'S', 'E', 'F', 'No Course Available'],
    ['English', 'Textile', 'Fine Arts', 'S', 'S', 'F', 'No Course Available'],
    ['English', 'Textile', 'Fine Arts', 'F', 'D', 'F', 'No Course Available'],
    ['English', 'Textile', 'Fine Arts', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 15
    ['Arabic', 'Textile', 'Fine Arts', 'D', 'F', 'F', 'No Course Available'],
    ['Arabic', 'Textile', 'Fine Arts', 'E', 'S', 'F', 'No Course Available'],
    ['Arabic', 'Textile', 'Fine Arts', 'E', 'F', 'F', 'No Course Available'],
    ['Arabic', 'Textile', 'Fine Arts', 'S', 'E', 'F', 'No Course Available'],
    ['Arabic', 'Textile', 'Fine Arts', 'S', 'S', 'F', 'No Course Available'],
    ['Arabic', 'Textile', 'Fine Arts', 'F', 'D', 'F', 'No Course Available'],
    ['Arabic', 'Textile', 'Fine Arts', 'F', 'E', 'F', 'No Course Available'],
    
    # starts 16
    ['Chinese', 'Textile', 'Fine Arts', 'D', 'F', 'F', 'No Course Available'],
    ['Chinese', 'Textile', 'Fine Arts', 'E', 'S', 'F', 'No Course Available'],
    ['Chinese', 'Textile', 'Fine Arts', 'E', 'F', 'F', 'No Course Available'],
    ['Chinese', 'Textile', 'Fine Arts', 'S', 'E', 'F', 'No Course Available'],
    ['Chinese', 'Textile', 'Fine Arts', 'S', 'S', 'F', 'No Course Available'],
    ['Chinese', 'Textile', 'Fine Arts', 'F', 'D', 'F', 'No Course Available'],
    ['Chinese', 'Textile', 'Fine Arts', 'F', 'E', 'F', 'No Course Available'],
   
    # Add more rows as needed
]

# Specify the file name
csv_file_path = 'sanaa_divison_four.csv'

# Writing to CSV file with tab delimiter
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header to the CSV file
    csv_writer.writerow(header)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print(f'CSV file "{csv_file_path}" has been created.')
