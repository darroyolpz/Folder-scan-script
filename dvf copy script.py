import shutil
import pandas as pd

# Open the quotation file
excel_file = 'All files.xlsx'
df = pd.read_excel(excel_file)

for row in df['Path']:
	try:
		target_path = "Target path"
		shutil.copy(row, target_path)
	except:
		print('Error at ', row)

print('Done bro!')