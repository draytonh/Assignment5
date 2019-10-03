#!/usr/bin/env python
import sys # Load in module that accesses the command line
import fileinput # This module gives us the ability to read files
import re # This imports the regex capability
import json

my_file= 'Homo_sapiens.GRCh37.75.gtf'
file_to_change= 'expres.anal.csv'
f1 = ("-f1")
f2 = ("-f2")
f3 = ("-f3")
f4 = ("-f4")
f5 = ("-f5")
f = ("-f")

Lookup_geneID={}

if sys.argv[1] == f2:
    for each_line_of_text in fileinput.input(my_file):
        if re.match(r'.*\t.*\tgene\t', each_line_of_text):
            gene_id_matches = re.findall('gene_id \"(.*?)\";',each_line_of_text)
            gene_name_matches = re.findall('gene_name \"(.*?)\";',each_line_of_text)
            text_in_columns = re.split('\t',each_line_of_text)
            if len(text_in_columns)>3:
                if gene_id_matches:
                    if gene_name_matches:
                        Lookup_geneID[gene_id_matches[0]] = gene_name_matches[0]

    print '"","gene_id","gene_type","logFC","AveExpr"'
    for each_line_of_text in fileinput.input(file_to_change):
        ensg_matches=re.sub('(\.\d{1,2})"','"',each_line_of_text.rstrip())
        columns = re.sub('"','',ensg_matches)
        columns_matches = re.split(",",columns)
        if columns_matches[1] in Lookup_geneID:
            print columns_matches[0] + ", " + Lookup_geneID[columns_matches[1]] + ", " + columns_matches[2] + ", " + columns_matches[3] + ", " + columns_matches[4]
elif sys.argv[1] == f1:
    for each_line_of_text in fileinput.input(my_file):
        if re.match(r'.*\t.*\tgene\t', each_line_of_text):
            gene_id_matches = re.findall('gene_id \"(.*?)\";',each_line_of_text)
            gene_name_matches = re.findall('gene_name \"(.*?)\";',each_line_of_text)
            text_in_columns = re.split('\t',each_line_of_text)
            if len(text_in_columns)>3:
                if gene_id_matches:
                    if gene_name_matches:
                        Lookup_geneID[gene_id_matches[0]] = gene_name_matches[0]

    print '"hugo_gene_name","ensemble_gene_name","gene_type","logFC","AveExpr"'
    for each_line_of_text in fileinput.input(file_to_change):
        ensg_matches=re.sub('(\.\d{1,2})"','"',each_line_of_text.rstrip())
        columns = re.sub('"','',ensg_matches)
        columns_matches = re.split(",",columns)
        if columns_matches[1] in Lookup_geneID:
            print Lookup_geneID[columns_matches[1]] + ", " + columns_matches[1] + ", " + columns_matches[2] + ", " + columns_matches[3] + ", " + columns_matches[4]
elif sys.argv[1] == f3:
    for each_line_of_text in fileinput.input(my_file):
        if re.match(r'.*\t.*\tgene\t', each_line_of_text):
            gene_id_matches = re.findall('gene_id \"(.*?)\";',each_line_of_text)
            gene_name_matches = re.findall('gene_name \"(.*?)\";',each_line_of_text)
            text_in_columns = re.split('\t',each_line_of_text)
            if len(text_in_columns)>3:
                if gene_id_matches:
                    if gene_name_matches:
                        Lookup_geneID[gene_id_matches[0]] = gene_name_matches[0]

    print '"","ensemble_gene_name","hugo_gene_name","logFC","AveExpr"'
    for each_line_of_text in fileinput.input(file_to_change):
        ensg_matches=re.sub('(\.\d{1,2})"','"',each_line_of_text.rstrip())
        columns = re.sub('"','',ensg_matches)
        columns_matches = re.split(",",columns)
        if columns_matches[1] in Lookup_geneID:
            print columns_matches[0] + ", " + columns_matches[1] + ", " + Lookup_geneID[columns_matches[1]] + ", " + columns_matches[3] + ", " + columns_matches[4]
elif sys.argv[1] == f4:
    for each_line_of_text in fileinput.input(my_file):
        if re.match(r'.*\t.*\tgene\t', each_line_of_text):
            gene_id_matches = re.findall('gene_id \"(.*?)\";',each_line_of_text)
            gene_name_matches = re.findall('gene_name \"(.*?)\";',each_line_of_text)
            text_in_columns = re.split('\t',each_line_of_text)
            if len(text_in_columns)>3:
                if gene_id_matches:
                    if gene_name_matches:
                        Lookup_geneID[gene_id_matches[0]] = gene_name_matches[0]

    print '"","ensemble_gene_name","gene_type","hugo_gene_name","AveExpr"'
    for each_line_of_text in fileinput.input(file_to_change):
        ensg_matches=re.sub('(\.\d{1,2})"','"',each_line_of_text.rstrip())
        columns = re.sub('"','',ensg_matches)
        columns_matches = re.split(",",columns)
        if columns_matches[1] in Lookup_geneID:
            print columns_matches[0] + ", " + columns_matches[1] + ", " + columns_matches[2] + ", " + Lookup_geneID[columns_matches[1]] + ", " + columns_matches[4]
elif sys.argv[1] == f5:
    for each_line_of_text in fileinput.input(my_file):
        if re.match(r'.*\t.*\tgene\t', each_line_of_text):
            gene_id_matches = re.findall('gene_id \"(.*?)\";',each_line_of_text)
            gene_name_matches = re.findall('gene_name \"(.*?)\";',each_line_of_text)
            text_in_columns = re.split('\t',each_line_of_text)
            if len(text_in_columns)>3:
                if gene_id_matches:
                    if gene_name_matches:
                        Lookup_geneID[gene_id_matches[0]] = gene_name_matches[0]

    print '"","ensemble_gene_name","gene_type","logFC","hugo_gene_name"'
    for each_line_of_text in fileinput.input(file_to_change):
        ensg_matches=re.sub('(\.\d{1,2})"','"',each_line_of_text.rstrip())
        columns = re.sub('"','',ensg_matches)
        columns_matches = re.split(",",columns)
        if columns_matches[1] in Lookup_geneID:
            print columns_matches[0] + ", " + columns_matches[1] + ", " + columns_matches[2] + ", " + columns_matches[3] + ", " + Lookup_geneID[columns_matches[1]]
elif sys.argv[1] == f:
    for each_line_of_text in fileinput.input(my_file):
        if re.match(r'.*\t.*\tgene\t', each_line_of_text):
            gene_id_matches = re.findall('gene_id \"(.*?)\";',each_line_of_text)
            gene_name_matches = re.findall('gene_name \"(.*?)\";',each_line_of_text)
            text_in_columns = re.split('\t',each_line_of_text)
            if len(text_in_columns)>3:
                if gene_id_matches:
                    if gene_name_matches:
                        Lookup_geneID[gene_id_matches[0]] = gene_name_matches[0]

    print '"hugo_gene_name","ensemble_gene_name","gene_type","logFC","AveExpr"'
    for each_line_of_text in fileinput.input(file_to_change):
        ensg_matches=re.sub('(\.\d{1,2})"','"',each_line_of_text.rstrip())
        columns = re.sub('"','',ensg_matches)
        columns_matches = re.split(",",columns)
        if columns_matches[1] in Lookup_geneID:
            print Lookup_geneID[columns_matches[1]] + ", " + columns_matches[1] + ", " + columns_matches[2] + ", " + columns_matches[4]
