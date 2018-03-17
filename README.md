# educational-tools
Educational tools which support effective educational methods

## Vyvolávač
Version: 0.1 beta 
### Short description
The script takes an input file with student names and randomly selects a student. A selected student has then lower probability of being selected again.
This script saves the state into an output file (which is read as input for the next iteration).

### Expected input/output:
File with full name (space separated), count of student being selected, and "points" from which the probability of being selected is calculated.
Less points means smaller probability of being selected.
The values should be tab-separated, thus the format should be:
`[Name space separated ]\t[selected count]\t[points]\n`

### Example input/output:
```
Arron Warde 0   27
Mattie Damsell  2   7
Rois Corkett    1   17
Ginnifer Ruvel  1   17
Jarrad Ramelet  1   17
Idaline Gipp    0   27
Samaria Trevino 0   27
Jourdan Kernar  1   17
Joete Cardinal  0   27
Danya Marusyak  1   17
```

**Note:** The initial file can contain only names and the script will add the numbers.

### Usage:
    python Vyvolavac.py input_stats.txt --save

The flag `-s` or `--save` saves the statistics to the input file.
