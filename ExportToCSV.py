# -*- codign: utf-8 -*-
import pandas as pd
from os import listdir
class Files():


    def readExcelFile(self, path_name):
        return pd.read_excel(path_name)

    def write_csv(self, df, path_name, separator, encoding):
        # Write the result as csv file
        df.to_csv(path_name, sep=separator, encoding=encoding, index=False)

    def convertExcelToCSV(self, path_name_excel_file, path_name_csv_file, separator, encoding):
        df = self.readExcelFile(path_name_excel_file)
        self.write_csv(df, path_name_csv_file, separator, encoding)

if __name__ == '__main__':
    _separator = '|'
    _encoding = 'UTF-8'
    # _excel_file = 'input/part1_others_publications-en-single-rows.xlsx'
    # _csv_file = 'output/part1_others_publications-en-single-rows.csv'

    _excel_file = 'input/part1_others_publications-pt-br-single-rows.xlsx'
    _csv_file = 'output/part1_others_publications-pt-br-single-rows.csv'

    # _excel_file = 'input/part2_books-en-single-rows.xlsx'
    # _csv_file = 'output/part2_books-en-single-rows.csv'

    # _excel_file = 'input/part2_books-pt-br-single-rows.xlsx'
    # _csv_file = 'output/part2_books-pt-br-single-rows.csv'

    # _excel_file = 'input/publicacoes-en-single-rows.xlsx'
    # _csv_file = 'output/publicacoes-en-single-rows.csv'

    #_excel_file = 'input/publicacoes-pt-br-single-rows.xlsx'
    #_csv_file = 'output/publicacoes-pt-br-single-rows.csv'
    f = Files()
    f.convertExcelToCSV(_excel_file, _csv_file, _separator, _encoding)
