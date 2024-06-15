import csv

# Define the header and data
header = ['first_subject', 'second_subject', 'third_subject', 'first_performance', 'second_performance', 'third_performance', 'course_names']
data = [
    # starts 01
    ['Kiswahili', 'English', 'French', 'D', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'French', 'E', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'French', 'E', 'F', 'F', 'No Course Available'],
     ['Kiswahili', 'English', 'French', 'S', 'E', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'French', 'S', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'French', 'F', 'D', 'F', 'No Course Available'],
     ['Kiswahili', 'English', 'French', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 2
    ['Kiswahili', 'English', 'Arabic', 'D', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Arabic', 'E', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Arabic', 'E', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Arabic', 'S', 'E', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Arabic', 'S', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Arabic', 'F', 'D', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Arabic', 'F', 'E', 'F', 'No Course Available'],
  
    # starts 03
    ['Kiswahili', 'English', 'Chinese', 'D', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Chinese', 'E', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Chinese', 'E', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Chinese', 'S', 'E', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Chinese', 'S', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Chinese', 'F', 'D', 'F', 'No Course Available'],
    ['Kiswahili', 'English', 'Chinese', 'F', 'E', 'F', 'No Course Available'],
    
    # starts 04
    ['Kiswahili', 'Arabic', 'Chinese', 'D', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Arabic', 'Chinese', 'E', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Arabic', 'Chinese', 'E', 'F', 'F', 'No Course Available'],
     ['Kiswahili', 'Arabic', 'Chinese', 'S', 'E', 'F', 'No Course Available'],
    ['Kiswahili', 'Arabic', 'Chinese', 'S', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Arabic', 'Chinese', 'F', 'D', 'F', 'No Course Available'],
     ['Kiswahili', 'Arabic', 'Chinese', 'F', 'E', 'F', 'No Course Available'],
    
    # starts 05
    ['Kiswahili', 'Arabic', 'French', 'D', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Arabic', 'French', 'E', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Arabic', 'French', 'E', 'F', 'F', 'No Course Available'],
    ['Kiswahili', 'Arabic', 'French', 'S', 'E', 'F', 'No Course Available'],
    ['Kiswahili', 'Arabic', 'French', 'S', 'S', 'F', 'No Course Available'],
    ['Kiswahili', 'Arabic', 'French', 'F', 'D', 'F', 'No Course Available'],
    ['Kiswahili', 'Arabic', 'French', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 06
    ['English', 'French', 'Arabic', 'D', 'F', 'F', 'No Course Available'],
    ['English', 'French', 'Arabic', 'E', 'S', 'F', 'No Course Available'],
    ['English', 'French', 'Arabic', 'E', 'F', 'F', 'No Course Available'],
    ['English', 'French', 'Arabic', 'S', 'E', 'F', 'No Course Available'],
    ['English', 'French', 'Arabic', 'S', 'S', 'F', 'No Course Available'],
    ['English', 'French', 'Arabic', 'F', 'D', 'F', 'No Course Available'],
    ['English', 'French', 'Arabic', 'F', 'E', 'F', 'No Course Available'],
    
    # STARTS 07
    ['English', 'French', 'Chinese', 'D', 'F', 'F', 'No Course Available'],
    ['English', 'French', 'Chinese', 'E', 'S', 'F', 'No Course Available'],
    ['English', 'French', 'Chinese', 'E', 'F', 'F', 'No Course Available'],
      ['English', 'French', 'Chinese', 'S', 'E', 'F', 'No Course Available'],
    ['English', 'French', 'Chinese', 'S', 'S', 'F', 'No Course Available'],
    ['English', 'French', 'Chinese', 'F', 'D', 'F', 'No Course Available'],
      ['English', 'French', 'Chinese', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 08
    ['French', 'Arabic', 'Chinese', 'SD', 'F', 'F', 'No Course Available'],
    ['French', 'Arabic', 'Chinese', 'E', 'S', 'F', 'No Course Available'],
    ['French', 'Arabic', 'Chinese', 'E', 'F', 'F', 'No Course Available'],
    ['French', 'Arabic', 'Chinese', 'S', 'E', 'F', 'No Course Available'],
    ['French', 'Arabic', 'Chinese', 'S', 'S', 'F', 'No Course Available'],
    ['French', 'Arabic', 'Chinese', 'F', 'D', 'F', 'No Course Available'],
    ['French', 'Arabic', 'Chinese', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 09 
    ['History', 'English', 'French', 'D', 'F', 'F', 'No Course Available'],
    ['History', 'English', 'French', 'E', 'S', 'F', 'No Course Available'],
    ['History', 'English', 'French', 'E', 'F', 'F', 'No Course Available'],
    ['History', 'English', 'French', 'S', 'E', 'F', 'No Course Available'],
    ['History', 'English', 'French', 'S', 'S', 'F', 'No Course Available'],
    ['History', 'English', 'French', 'F', 'D', 'F', 'No Course Available'],
    ['History', 'English', 'French', 'F', 'E', 'F', 'No Course Available'],
  
    # starts 10 
    ['History', 'English', 'Arabic', 'D', 'F', 'F', 'No Course Available'],
    ['History', 'English', 'Arabic', 'E', 'S', 'F', 'No Course Available'],
    ['History', 'English', 'Arabic', 'E', 'F', 'F', 'No Course Available'],
     ['History', 'English', 'Arabic', 'S', 'E', 'F', 'No Course Available'],
    ['History', 'English', 'Arabic', 'S', 'S', 'F', 'No Course Available'],
    ['History', 'English', 'Arabic', 'F', 'D', 'F', 'No Course Available'],
     ['History', 'English', 'Arabic', 'F', 'E', 'F', 'No Course Available'],
    
    # starts 11 
    ['History', 'English', 'Chinese', 'D', 'F', 'F', 'No Course Available'],
    ['History', 'English', 'Chinese', 'E', 'S', 'F', 'No Course Available'],
    ['History', 'English', 'Chinese', 'E', 'F', 'F', 'No Course Available'],
    ['History', 'English', 'Chinese', 'S', 'E', 'F', 'No Course Available'],
    ['History', 'English', 'Chinese', 'S', 'S', 'F', 'No Course Available'],
    ['History', 'English', 'Chinese', 'F', 'D', 'F', 'No Course Available'],
    ['History', 'English', 'Chinese', 'F', 'E', 'F', 'No Course Available'],
  
    # Add more rows as needed
]

# Specify the file name
csv_file_path = 'division_four_lugha.csv'

# Writing to CSV file with tab delimiter
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header to the CSV file
    csv_writer.writerow(header)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print(f'CSV file "{csv_file_path}" has been created.')
