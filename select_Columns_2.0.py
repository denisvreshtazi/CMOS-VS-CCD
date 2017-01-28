import pyexcel as pe

data_path = input("Directory of file data : ")
sheet = pe.get_sheet(file_name=data_path)
# Select the columns u want to keep
sheet.column.select([])
data_save = input("Directory of file data to save: ")
sheet.save_as(data_save)
