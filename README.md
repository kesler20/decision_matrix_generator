# Decision Matrix Generator

tis is a simple script to generate decision matrices 
of the following format:
The table is a pandas DataFrame which can be stored as HTML or excel

|            | option 1 | option2 | option3  |
|------------|----------|---------|----------|
| criteria 1 |     c11   |   c12   |   c13   |
| criteria 2 |     c21   |   c22   |   c23   |
| criteria 3 |     c31   |   c32   |   c33   |
| total score | C1 | C2 | C3 |

where the $ c_{ij}$ values are calculated by normalising the initial input data 
with each respective total row sum:

$                                       c_{11} = \frac{c_{ij}}{\sum(c_{ij})_i} $

whereas the total socres are the sum of each normalised score of each option

$                                       C_1 = \frac{c_{ij}}{\sum(c_{ij})_j} $
