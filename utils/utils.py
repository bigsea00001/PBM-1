class Utils:
    def __init__(self):
        pass

    def max_length_check(self, rows):
        """
        get each element's max length from rows
        """
        elements = [str(1) for i in range(len(rows[0]))]
        row_lens = [None for i in range(len(elements))]

        for rows_idx, row in enumerate(rows):
            for row_idx, row_element in enumerate(row):

                row_element_len = len(str(row_element))
                element_row_len = len(elements[row_idx])

                if row_element_len > element_row_len:
                    row_lens[row_idx] = row_element_len

        return row_lens

