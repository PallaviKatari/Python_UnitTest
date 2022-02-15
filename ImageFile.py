import pandas as pd
from pandas.testing import assert_frame_equal
import unittest


class UnitTestDF(unittest.TestCase):
    def __init__(self, df, expected):
        self.df = pd.read_csv(df)
        self.expected = pd.read_csv(expected)


class Identify_Less_Than_1Mb(UnitTestDF):
    def image_less_then_1Mb(self):
        # act
        actual = self.df[self.df['File Size(in Mb)'].apply(lambda x: x < 1)].reset_index(drop=True)

        actual = actual.loc[:, ~actual.columns.str.match("Unnamed")]
        self.expected = self.expected.loc[:, ~self.expected.columns.str.match("Unnamed")]

        # assert
        assert_frame_equal(actual, self.expected, check_dtype=False)
        print(self.expected)
        return "Test Successfully Completed"


print(Identify_Less_Than_1Mb('Test1.csv', 'Test2.csv').image_less_then_1Mb())


#
# # DataFrame Creation
# class UnitTestDF(unittest.TestCase):
#     def __init__(self):
#         self.df = pd.DataFrame({
#                     "File Name":['D:\\Home\\Course\\Python1','D:\\Home\\Course\\Python2','D:\\Home\\Course\\Python3','D:\\Home\\Course\\Python4','D:\\Home\\Course\\Python5','D:\\Home\\Course\\Python6','D:\\Home\\Course\\Python7','D:\\Home\\Course\\Python8','D:\\Home\\Course\\Python9','D:\\Home\\Course\\Python10'],
#                     "File Size(in Mb)":[1.0, 0.3, 3.1, 2.1, 0.4, 0.25, 1.9, 0.5, 0.2, 0.7],
#                     'File Resolution':['1000x800','800x700','500x600', '700x600', '900x500', '555x400', '300x800', '700x800', '400x500', '700x600'],
#                     'Image Name':['Python1','Python2','Python3','Python4','Python5','Python6','Python7','Python8','Python9','Python10'],
#                     'No of Objects in the Image':[2,3,1,4,5,6,2,5,3,1],
#                     'Object Resolution': ['Context1','Context2','Context3','Context4','Context5','Context6','Context7','Context8','Context9','Context10']
#                 })
#         self.expected = pd.DataFrame({'File Name': ['D:\\Home\\Course\\Python2', 'D:\\Home\\Course\\Python5','D:\\Home\\Course\\Python6', 'D:\\Home\\Course\\Python8', 'D:\\Home\\Course\\Python9', 'D:\\Home\\Course\\Python10'],
#             'File Size(in Mb)': [0.3, 0.4, 0.25, 0.5, 0.2, 0.7],
#             'File Resolution': ['800x700','900x500','555x400','700x800','400x500','700x600'],
#             'Image Name': ['Python2','Python5','Python6','Python8','Python9','Python10'],
#             'No of Objects in the Image': [3, 5, 6, 5, 3, 1],
#             'Object Resolution': ['Context2','Context5','Context6','Context8','Context9','Context10']})
#
#     def create_csv(self):
#         self.df.to_csv('Test1.csv')
#         self.expected.to_csv('Test2.csv')
#
# obj = UnitTestDF()
# obj.create_csv()
