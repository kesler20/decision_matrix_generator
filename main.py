import numpy as np
import pandas as pd


class DecisionMatrix(object):
    '''
    The structure of the decision matrix is one of a numpy array 
    [
        [c11 , c21 , c31],
        [c12, c22, c32],
        [c13, c23, c33]
    ]
    where c12 refers to the value of the second criterion of the first option
    '''

    def __init__(self, criteria, options, data):
        self.criteria: 'list[str]' = criteria
        self.options: 'list[str]' = options
        self.data: 'list[list[float]]' = data

    def calculate_normalized_scores(self):
        '''
        each value within the numpy array should be expressed as
        c11 = cij/sum(cij)_j
        '''
        print('this is the data passed to the score normalizer\n')
        print(np.array(self.data))
        for row_index, row in enumerate(self.data):
            total_row_value = sum(row)
            for column_index, c in enumerate(row):
                self.data[row_index][column_index] = c/total_row_value
        print('these are the normalized scores\n')
        print(np.array(self.data))

    def calculate_final_scores(self):
        '''
        Final scores will be returned as a list
        '''
        self.calculate_normalized_scores()
        return [sum(col) for col in list(zip(*self.data))]

    def create_table(self, filename: str, filetype: str):
        '''
        The table is a pandas DataFrame which can be stored as HTML or excel
        | ''          | option 1 | option2 | option3 |
        ---------------------------------------------
        | criteria 1 |     c11   |   c12   |   c13   |
        | criteria 2 |     c21   |   c22   |   c23   |
        | criteria 3 |     c31   |   c32   |   c33   |
        '''
        final_scores = self.calculate_final_scores()

        # add the total table to the data
        self.criteria.append('total score')
        self.data.append(final_scores)

        crit = {'': self.criteria}
        opt = {self.options[col_index]: c for col_index,
               c in enumerate(list(zip(*self.data)))}
        table_data = {**crit, **opt}
        table = pd.DataFrame(table_data)

        print('this is the final table\n')
        print(table)
        if filetype == 'html':
            table.to_html(filename + '.html', index=False)
        else:
            table.to_csv(filename + '.csv', index=False)


# make sure that the number of criteria is = to the number of lists in data
criteria = ['cost (£)', 'duration (hr)']
# make sure that the number of options is equal to the number of items in the list
options = ['Venn', 'Diagram', 'Bugatti']
data = [[100, 10, 3], [200, 20, 6]]
filename = 'Decision Matrix'
decision_matrix = DecisionMatrix(criteria, options, data)
filetype = 'html'
decision_matrix.create_table(filename, filetype)
