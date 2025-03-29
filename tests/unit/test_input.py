import unittest
from app.io.input import read_file, read_file_pandas


class ReadFileTests(unittest.TestCase):
    def test_read_file_reads(self):
        self.assertEqual(
            read_file('../integration/fixtures/test_read_file'),
            "I was starting to worry that my pet turtle could tell what I was thinking."
        )

    def test_read_file_not_reads(self):
        self.assertNotEqual(
            read_file('../integration/fixtures/test_read_file'),
            "blah blah blah ha ha ha ok ok ok"
        )

    def test_read_file_error(self):
        with self.assertRaises(FileNotFoundError):
            read_file('../integration/fixtures/file_not_found')


class ReadFilePandasTests(unittest.TestCase):
    def test_read_file_pandas_columns(self):
        df = read_file_pandas('../integration/fixtures/test_read_file_pandas.csv')
        self.assertEqual(list(df.columns), ["id", "first name", "last name"])

    def test_read_file_pandas_index(self):
        df = read_file_pandas('../integration/fixtures/test_read_file_pandas.csv')
        self.assertEqual(df.at[0, "last name"],"Shulepov")
        self.assertEqual(df.at[1, "first name"], "Antonina")

    def test_read_file_pandas_size(self):
        df = read_file_pandas('../integration/fixtures/test_read_file_pandas.csv')
        self.assertEqual(df.size, 9)


if __name__ == "__main__":
    unittest.main()