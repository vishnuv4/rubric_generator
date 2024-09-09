from pathlib import Path

class AssignmentRubricTemplate:
    _filename = ""
    _folder = ""
    _excel = ""
    _questions_dict = "questions"

    def __init__(self, assignment):
        self._folder = assignment
        dir = Path(self._folder)
        dir.mkdir(parents=True, exist_ok=True)
        self._filename = Path(self._folder) / Path(assignment + ".py")
        self._excel = Path(assignment + ".xlsx")

    def append_to_file(self, text):
        '''
        Appends strings to a file
        '''
        with open(self._filename, 'a') as file:
            if isinstance(text, str):
                file.write(text + '\n')
            elif isinstance(text, list) and all(isinstance(item, str) for item in text):
                file.write("\n".join(text))
            else:
                raise ValueError("Content must be a string or list of strings")

    def write_file(self, **kwargs):
        '''
        Writes code to file
        This code creates a dictionary associating questions with their points
        @param r[int] Number of R-type questions
        @param i[int] Number of I-type questions
        @param s[int] Number of S-type questions
        @param c[int] Number of C-type questions
        @param v[int] Number of V-type questions
        '''
        with open(self._filename, 'w'):
            pass

        self.append_to_file([
            "################",
            "# GENERATED CODE",
            "################",
            '',
            'from tabulate import tabulate',
            'import pandas as pd',
            'from pathlib import Path',
            '',
            '########## HELPER FUNCTIONS ##########\n',
            'def generate_ranges(codes):',
            '    codes.sort(key=lambda x: int(x[1:]))',
            '    ranges, start = [], codes[0]',
            '    for i in range(1, len(codes)):',
            '        if int(codes[i][1:]) != int(codes[i-1][1:]) + 1:',
            '            ranges.append(start if start == codes[i-1] else f"{start}-{codes[i-1]}")',
            '            start = codes[i]',
            '    ranges.append(start if start == codes[-1] else f"{start}-{codes[-1]}")',
            '    return ranges',
            '',
            'def get_points(data):',
            '    table_data = [["Questions", "Points", "Number", "Total"]]',
            '    order = ["R", "I", "S", "C", "V"]',
            '    order_index = {item: index for index, item in enumerate(order)}',
            '    qtype_list = list(set([k[0] for k in data.keys()]))',
            '    qtype_list_sorted = sorted(qtype_list, key=lambda x: order_index[x])',
            '    points_set = set(data.values())',
            '    for qtype in qtype_list_sorted:',
            '        for points in points_set:',
            '            codes = [key for key in data if data[key] == points and qtype in key]',
            '            number = len(codes)',
            '            if number != 0:',
            '                ranges = ", ".join(generate_ranges(codes))',
            '                points_per_question = f"{points} pt(s)"',
            '                total = f"{points * number} pt(s)"',
            '                subtotal = f"{points} x {number} = {total}"',
            '                table_data.append([ranges, points_per_question, number, subtotal])',
            '    table_data.append(["Grand Total", "", "", f"{sum(data.values())} points"])',
            '    return table_data',
            '',
            "########## RUBRIC ##########",
            '',
            f"{self._questions_dict} = {{",
            '',
        ])

        for qtype, count in kwargs.items():
            if count != 0:
                self.append_to_file(f"\n# {qtype.upper()}-type questions")
                for n in range(count):
                    self.append_to_file(f"\t'{qtype.upper()}{n+1}':\t1,")

        self.append_to_file([
            "",
            "}",
            "",
            'print()',
            'table = get_points(data=questions)',
            'df = pd.DataFrame(table[1:], columns=table[0])',
            f'df.to_excel(Path(__file__).parent / "{self._excel}", index=False, engine="openpyxl")',
            'print(tabulate(table, headers="firstrow", tablefmt="simple_grid"))',
            'print()',
            '',
            '#######################',
            '# END OF GENERATED CODE',
            '#######################'
        ])

####################################################################
## Parameters to the write function must be a subset of r, i, s, c, v

if __name__ == "__main__":
    AssignmentRubricTemplate(assignment="").write_file(r= 0,
                                                       i=  0,
                                                       s=  0,
                                                       c=  0,
                                                       v=  0
                                                       )

####################################################################
