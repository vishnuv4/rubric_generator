class AssignmentRubricTemplate:
    _filename = ""
    _questions_dict = "questions"

    def __init__(self, filename):
        self._filename = filename

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

    def write_file(self, r=0, i=0, s=0, c=0, v=0):
        '''
        Writes code to file
        This code creates a dictionary associating questions with their points
        @param r[int] Number of R-type questions
        @param i[int] Number of S-type questions
        @param s[int] Number of R-type questions
        @param c[int] Number of S-type questions
        @param v[int] Number of S-type questions
        '''
        with open(self._filename, 'w'):
            pass

        self.append_to_file([
            "################",
            "# GENERATED CODE",
            "################",
            '',
            'from tabulate import tabulate',
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
            '    table_data = [["Questions", "Subtotal"]]',
            '    order = ["R", "I", "S", "C", "V"]',
            '    order_index = {item: index for index, item in enumerate(order)}',
            '    qtype_list = list(set([k[0] for k in data.keys()]))',
            '    qtype_list_sorted = sorted(qtype_list, key=lambda x: order_index[x])',
            '    points_set = set(data.values())',
            '    for qtype in qtype_list_sorted:',
            '        for points in points_set:',
            '            codes = [key for key in data if data[key] == points and qtype in key]',
            '            if len(codes) != 0:',
            '                ranges = ", ".join(generate_ranges(codes))',
            '                subtotal = f"{points} pt(s) x {len(codes)} = {points * len(codes)} pt(s)"',
            '                table_data.append([ranges, subtotal])',
            '    table_data.append(["Total", f"{sum(data.values())} points"])',
            '    return table_data',
            '',
            "########## RUBRIC ##########",
            '',
            f"{self._questions_dict} = {{}}",
            '',
        ])

        if r != 0:
            self.append_to_file("\n# R-type questions")
            for n in range(0, r):
                self.append_to_file(f"{self._questions_dict}['R{n+1}'] =\t1")
        if i != 0:
            self.append_to_file("\n# I-type questions")
            for n in range(0, i):
                self.append_to_file(f"{self._questions_dict}['I{n+1}'] =\t1")
        if s != 0:
            self.append_to_file("\n# S-type questions")
            for n in range(0, s):
                self.append_to_file(f"{self._questions_dict}['S{n+1}'] =\t1")
        if c != 0:
            self.append_to_file("\n# C-type questions")
            for n in range(0, c):
                self.append_to_file(f"{self._questions_dict}['C{n+1}'] =\t1")
        if v != 0:
            self.append_to_file("\n# V-type questions")
            for n in range(0, v):
                self.append_to_file(f"{self._questions_dict}['V{n+1}'] =\t1")
        
        self.append_to_file([
            "",
            'print()',
            'print(tabulate(get_points(data = questions), headers="firstrow", tablefmt="grid"))',
            'print()',
            '',
            '#######################',
            '# END OF GENERATED CODE',
            '#######################'
        ])

####################################################################

if __name__ == "__main__":
    AssignmentRubricTemplate(filename="lab1.py").write_file(r=  0,
                                                            s=  0,
                                                            i=  0
                                                            )

####################################################################
