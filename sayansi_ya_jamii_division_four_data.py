import csv

# Define the header and data
header = ['first_subject', 'second_subject', 'third_subject', 'first_performance', 'second_performance', 'third_performance', 'course_names']
data = [
    # starts 01
    ['History', 'Geography', 'Kiswahili', 'D', 'F', 'F', 'No Course Available'],
    ['History', 'Geography', 'Kiswahili', 'E', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'Kiswahili', 'E', 'F', 'F', 'No Course Available'],
      ['History', 'Geography', 'Kiswahili', 'S', 'E', 'F', 'No Course Available'],
    ['History', 'Geography', 'Kiswahili', 'S', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'Kiswahili', 'F', 'D', 'F', 'No Course Available'],
      ['History', 'Geography', 'Kiswahili', 'F', 'E', 'F', 'No Course Available'],
    
    # starts 02
    ['History', 'Geography', 'English', 'D', 'F', 'F', 'No Course Available'],
    ['History', 'Geography', 'English', 'E', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'English', 'E', 'F', 'F', 'No Course Available'],
     ['History', 'Geography', 'English', 'S', 'E', 'F', 'No Course Available'],
    ['History', 'Geography', 'English', 'S', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'English', 'F', 'D', 'F', 'No Course Available'],
     ['History', 'Geography', 'English', 'F', 'E', 'F', 'No Course Available'],
    
    # starts 03
    ['History', 'Geography', 'French', 'D', 'F', 'F', 'No Course Available'],
    ['History', 'Geography', 'French', 'E', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'French', 'E', 'F', 'F', 'No Course Available'],
     ['History', 'Geography', 'French', 'S', 'E', 'F', 'No Course Available'],
    ['History', 'Geography', 'French', 'S', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'French', 'F', 'D', 'F', 'No Course Available'],
     ['History', 'Geography', 'French', 'F', 'E', 'F', 'No Course Available'],
    
    # STARTS 04
    ['History', 'Geography', 'Arabic', 'D', 'F', 'F', 'No Course Available'],
    ['History', 'Geography', 'Arabic', 'E', 'S', 'F', 'No Course Available'],
     ['History', 'Geography', 'Arabic', 'E', 'F', 'F', 'No Course Available'],
     ['History', 'Geography', 'Arabic', 'S', 'E', 'F', 'No Course Available'],
    ['History', 'Geography', 'Arabic', 'S', 'S', 'F', 'No Course Available'],
     ['History', 'Geography', 'Arabic', 'F', 'D', 'F', 'No Course Available'],
     ['History', 'Geography', 'Arabic', 'F', 'E', 'F', 'No Course Available'],
    
    #  starts 05
    ['History', 'Geography', 'Chinese', 'D', 'F', 'F', 'No Course Available'],
    ['History', 'Geography', 'Chinese', 'E', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'Chinese', 'E', 'F', 'F', 'No Course Available'],
    ['History', 'Geography', 'Chinese', 'S', 'E', 'F', 'No Course Available'],
    ['History', 'Geography', 'Chinese', 'S', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'Chinese', 'F', 'D', 'F', 'No Course Available'],
    ['History', 'Geography', 'Chinese', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 06
    ['History', 'Geography', 'Fasihi', 'D', 'F', 'F', 'No Course Available'],
    ['History', 'Geography', 'Fasihi', 'E', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'Fasihi', 'E', 'F', 'F', 'No Course Available'],
    ['History', 'Geography', 'Fasihi', 'S', 'E', 'F', 'No Course Available'],
    ['History', 'Geography', 'Fasihi', 'S', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'Fasihi', 'F', 'D', 'F', 'No Course Available'],
    ['History', 'Geography', 'Fasihi', 'F', 'E', 'F', 'No Course Available'],
    
    # starts 07
    ['History', 'Geography', 'Literature', 'D', 'F', 'F', 'No Course Available'],
    ['History', 'Geography', 'Literature', 'E', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'Literature', 'E', 'F', 'F', 'No Course Available'],
        ['History', 'Geography', 'Literature', 'S', 'E', 'F', 'No Course Available'],
    ['History', 'Geography', 'Literature', 'S', 'S', 'F', 'No Course Available'],
    ['History', 'Geography', 'Literature', 'F', 'D', 'F', 'No Course Available'],
        ['History', 'Geography', 'Literature', 'F', 'E', 'F', 'No Course Available'],
   
    # Add more rows as needed
]

# Specify the file name
csv_file_path = 'division_FOUR_sayansi_jamii.csv'

# Writing to CSV file with tab delimiter
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header to the CSV file
    csv_writer.writerow(header)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print(f'CSV file "{csv_file_path}" has been created.')
