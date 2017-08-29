#!/usr/bin/env python

import csv

input_file1 = "old.csv"
input_file2 = "new.csv"
output_path = "diff.csv"

with open(input_file1) as fin1:
  with open(input_file2) as fin2:
    read1 = csv.reader(fin1)
    read2 = csv.reader(fin2)
    diff_rows = (row1 for row1, row2 in zip(read1, read2) if row1 != row2)
    with open(output_path, 'w') as fout:
      writer = csv.writer(fout)
      writer.writerows(diff_rows)
