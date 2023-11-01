import pandas as pd

# Read data from the two input files
file1 = 'combined_protein1.tsv'
file2 = 'combined_protein2.tsv'

# Read the data into two separate dataframes
df1 = pd.read_csv(file1, sep='\t')
df2 = pd.read_csv(file2, sep='\t')

# Merge the dataframes on the 'Protein' column to find common entries
common_proteins = pd.merge(df1, df2, on='Protein', how='inner')

# Extract the 'Protein' and 'control_1 Intensity' columns from the common entries
common_proteins = common_proteins[['Protein', 'control_1 Intensity_x', 'control_1 Intensity_y']]

# Rename the 'control_1 Intensity' columns for clarity
common_proteins = common_proteins.rename(columns={'control_1 Intensity_x': 'control_1 Intensity_1', 'control_1 Intensity_y': 'control_1 Intensity_2'})

# Save the common proteins and their respective intensities to a new TSV file
output_file = 'common_proteins_and_intensity.tsv'
common_proteins.to_csv(output_file, sep='\t', index=False)

print(f"Common proteins and intensities saved to {output_file}")
