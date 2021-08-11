# GENERATE DENSE CIRCOS PLOT
This package lets you create circos plot that exceeds thousand entries. To do so, you need circos and python 3 installed on your computer. 
Python dependencies : 
* pandas

## Installation
```bash
pip install pandas
```

The input file is a two-column tab-delimited CSV file. 
The first column represents the name of the entry and the second column is the name of the group.

Python scripts generate karyotypes and links files. Two python scripts are available : 
* **generate_dense_circos_plot.py** : Generates a karyotype and a link for each entry
* **generate_circos_plot.py** : Groups entries in a karyotype and a link

## Configuration
2 configuration files can be tweaked to change the output diagram:
* **data/colors.conf**: specifiying the color of each group in RGB format
* **circos.conf**: main configuration file which specifies the karyotype and link aspects
## Usage
```bash
python generate_dense_circos_plot.py <input_file.txt>
circos -conf circos.conf
python generate_circos_plot.py <input_file.txt>
circos -conf circos.conf
```

