# Assignment5
Converting Ensemble gene name to a HUGO name

## Installation
1) To build your library of Ensemble and HUGO names, install Homo_sapiens.GRCh37.75.gtf using: 
```
curl http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz -o Homo_sapiens.GrCh37.75.gtf.gz
```

2) Unzip the file using: 
```
gunzip Homo_sapiens.GrCh37.75.gtf.gz
```

## Usage
In order to run program you must have both the file you want to make a dictionary with (Homo_sapiens.GRCh37.75.gtf) and the file you want to change. You can also create a symbolic link to these files using: 
```
ln -s /dirc_where_file_is_located/Homo_sapiens.GRCh37.75.gtf ~/dirc_you_are_running_your_script_in
```

To use this program assign my_file to Homo_sapiens.GRCh37.75.gtf and file_to_change to the comma seperated file that you would like to change the ensemble name to the HUGO gene name in (this script can be further modified to handle a tab seperated file).

When you run the script if you run ./ensg2hugo.py -f[1-5] it will change the corresponding column with the HUGO gene name (i.e. -f2 converts the second column in the file_to_change to the HUGO gene name from the dictionary created earlier).

To create a new file replacing the ensemble gene names in your file_to_change to the HUGO gene names, run:
```
./ensg2hugo.py -f2 > hugo_analysis.csv.
```
