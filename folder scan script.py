import os
import pandas as pd

all_files, clean_files = [], []

for dirpath, dirnames, filenames in os.walk('.'):
	if 'DVF' in dirpath:
		for filename in [f for f in filenames if f.endswith('.pdf')]:
			if '(CD)' not in filename:
				dvf_file = os.path.join(dirpath, filename)
				all_files.append(dvf_file)


bad_words = ['obsoleto', 'rev 0', 'rev0', 'r0', '(ed)', '(ed)',
			'dx coil', 'bateria', 'v0', 'anulado', 'dx', 'eliminado',
			'batería', 'coil', 'datacenters', 'avl', 'ifc', 'dcc',
			'atex', 'fanwall', 'wiring diagram', 'curvas', 'etix',
			'advania']

for file in all_files:
	counter = 0
	for word in bad_words:
		if word not in file.lower():
			counter += 1

	if counter == len(bad_words):
		clean_files.append(file)
	else:
		# Show the files you're throwing away
		print(file)

# Create dataframe
col = ['Path']
df = pd.DataFrame(clean_files, columns=col)

# Export to Excel
name = 'All files.xlsx'
writer = pd.ExcelWriter(name)
df.to_excel(writer, index = False)
writer.save()