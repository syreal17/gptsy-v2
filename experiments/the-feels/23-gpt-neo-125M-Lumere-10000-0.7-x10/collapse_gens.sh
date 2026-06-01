#!/bin/bash

cat generation_output.1.txt >> generation_output.total.txt
cat generation_output.2.txt >> generation_output.total.txt
cat generation_output.3.txt >> generation_output.total.txt
cat generation_output.4.txt >> generation_output.total.txt
cat generation_output.5.txt >> generation_output.total.txt
cat generation_output.6.txt >> generation_output.total.txt
cat generation_output.7.txt >> generation_output.total.txt
cat generation_output.8.txt >> generation_output.total.txt
cat generation_output.9.txt >> generation_output.total.txt
cat generation_output.10.txt >> generation_output.total.txt

python3 ../../../utils/count_unique_lines.py generation_output.total.txt > output_summation.total.txt