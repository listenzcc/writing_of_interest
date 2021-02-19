# Backend worker
import os
import pandas as pd

folder = os.path.dirname(os.path.abspath(__file__))


class Worker(object):
    def __init__(self):
        self.df = pd.read_json(os.path.join(os.environ.get(
            'SYNC', None), 'Statlect', 'contents.json'))

    def query(self, s, col='sentence', max_rows=100):
        '''
        Query [s] from [col] in the DataFrame
        - @s: The src of the query
        - @col: The column name (dst) of the query
        '''
        found = self.df[self.df[col].str.contains(s)]

        found['sentenceP'] = found['sentence'].map(
            lambda x: x.replace(s, f'<strong>{s}</strong>'))

        if len(found) > max_rows:
            return found.iloc[:max_rows]
        else:
            return found
