import csv

# Define the header and data
header = ['first_subject', 'second_subject', 'third_subject', 'first_performance', 'second_performance', 'third_performance', 'course_names']
data = [
    # starts IGH
    ['Islamic', 'History', 'Geography', 'D', 'F', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Geography', 'E', 'S', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Geography', 'E', 'F', 'F', 'No Course Available'],
     ['Islamic', 'History', 'Geography', 'S', 'E', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Geography', 'S', 'S', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Geography', 'F', 'D', 'F', 'No Course Available'],
     ['Islamic', 'History', 'Geography', 'F', 'E', 'F', 'No Course Available'],
   
    # starts DHG
    ['Divinity', 'History', 'Geography', 'D', 'F', 'F', 'No Course Available'],
    ['Divinity', 'History', 'Geography', 'E', 'S', 'F', 'No Course Available'],
    ['Divinity', 'History', 'Geography', 'E', 'F', 'F', 'No Course Available'],
      ['Divinity', 'History', 'Geography', 'S', 'E', 'F', 'No Course Available'],
    ['Divinity', 'History', 'Geography', 'S', 'S', 'F', 'No Course Available'],
    ['Divinity', 'History', 'Geography', 'F', 'D', 'F', 'No Course Available'],
      ['Divinity', 'History', 'Geography', 'F', 'E', 'F', 'No Course Available'],
   
    # starts IHAr 03
    ['Islamic', 'History', 'Arabic', 'D', 'F', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Arabic', 'E', 'S', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Arabic', 'E', 'F', 'F', 'No Course Available'],
     ['Islamic', 'History', 'Arabic', 'S', 'E', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Arabic', 'S', 'S', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Arabic', 'F', 'D', 'F', 'No Course Available'],
     ['Islamic', 'History', 'Arabic', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 04
    ['Divinity', 'Kiswahili', 'English', 'D', 'F', 'F', 'No Course Available'],
    ['Divinity', 'Kiswahili', 'English', 'E', 'S', 'F', 'No Course Available'],
    ['Divinity', 'Kiswahili', 'English', 'E', 'F', 'F', 'No Course Available'],
    ['Divinity', 'Kiswahili', 'English', 'S', 'E', 'F', 'No Course Available'],
    ['Divinity', 'Kiswahili', 'English', 'S', 'S', 'F', 'No Course Available'],
    ['Divinity', 'Kiswahili', 'English', 'F', 'D', 'F', 'No Course Available'],
    ['Divinity', 'Kiswahili', 'English', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 05
    ['Divinity', 'History', 'English', 'D', 'F', 'F', 'No Course Available'],
    ['Divinity', 'History', 'English', 'E', 'S', 'F', 'No Course Available'],
    ['Divinity', 'History', 'English', 'E', 'F', 'F', 'No Course Available'],
    ['Divinity', 'History', 'English', 'S', 'E', 'F', 'No Course Available'],
    ['Divinity', 'History', 'English', 'S', 'S', 'F', 'No Course Available'],
    ['Divinity', 'History', 'English', 'F', 'D', 'F', 'No Course Available'],
    ['Divinity', 'History', 'English', 'F', 'E', 'F', 'No Course Available'],
   
    # starts 06
    ['Islamic', 'History', 'English', 'D', 'F', 'F', 'No Course Available'],
    ['Islamic', 'History', 'English', 'E', 'S', 'F', 'No Course Available'],
    ['Islamic', 'History', 'English', 'E', 'F', 'F', 'No Course Available'],
    ['Islamic', 'History', 'English', 'S', 'E', 'F', 'No Course Available'],
    ['Islamic', 'History', 'English', 'S', 'S', 'F', 'No Course Available'],
    ['Islamic', 'History', 'English', 'F', 'D', 'F', 'No Course Available'],
    ['Islamic', 'History', 'English', 'F', 'E', 'F', 'No Course Available'],
 
    # starts 07
    ['Divinity', 'History', 'Kiswahili', 'D', 'F', 'F', 'No Course Available'],
    ['Divinity', 'History', 'Kiswahili', 'E', 'S', 'F', 'No Course Available'],
    ['Divinity', 'History', 'Kiswahili', 'E', 'F', 'F', 'No Course Available'],
     ['Divinity', 'History', 'Kiswahili', 'S', 'E', 'F', 'No Course Available'],
    ['Divinity', 'History', 'Kiswahili', 'S', 'S', 'F', 'No Course Available'],
    ['Divinity', 'History', 'Kiswahili', 'F', 'D', 'F', 'No Course Available'],
     ['Divinity', 'History', 'Kiswahili', 'F', 'E', 'F', 'No Course Available'],
    
    # starts 08
    ['Islamic', 'History', 'Kiswahili', 'D', 'F', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Kiswahili', 'E', 'S', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Kiswahili', 'E', 'F', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Kiswahili', 'S', 'E', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Kiswahili', 'S', 'S', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Kiswahili', 'F', 'D', 'F', 'No Course Available'],
    ['Islamic', 'History', 'Kiswahili', 'F', 'E', 'F', 'No Course Available'],
   
    # Add more rows as needed
]

# Specify the file name
csv_file_path = 'division_four_elimu_ya_dini.csv'

# Writing to CSV file with tab delimiter
with open(csv_file_path, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header to the CSV file
    csv_writer.writerow(header)

    # Write the data to the CSV file
    csv_writer.writerows(data)

print(f'CSV file "{csv_file_path}" has been created.')
