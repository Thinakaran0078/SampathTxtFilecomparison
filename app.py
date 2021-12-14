from difflib import Differ, unified_diff


class Textdiff:

    def _unified_method(self):
        with open('randomdata.txt') as file_1:
            file_1_txt = file_1.readlines()

        with open('randomdata1.txt') as file_2:
            file_2_txt = file_2.readlines()

        for line in unified_diff(
            file_1_txt, file_2_txt, fromfile='randomdata.txt', tofile='randomdata1.txt', lineterm=''
        ):
            print(line)

    def _differ_method(self):
            with open('randomdata.txt') as file_1, open('randomdata1.txt') as file_2:
                differ = Differ()
                for line in differ.compare(file_1.readlines(), file_2.readlines()):
                    print(line)

    def _loop_method(self):
        file_1, file_2 = open('randomdata.txt', 'r'), open('randomdata1.txt', 'r')

        print("Comparing files ", " @ " + 'randomdata.txt', " # " + 'randomdata1.txt', sep='\n')

        file_1_line = file_1.readline()
        file_2_line = file_2.readline()

        # Use as a Counter
        line_no = 1

        with open('file1.txt') as file1:
            with open('file2.txt') as file2:
                same = set(file1).intersection(file2)

        print("Common Lines in Both Files")

    def _own_method(self):
        #matches = []
        match_dict = {}
        differences = []
        with open('randomdata.txt') as file_1, open('randomdata1.txt') as file_2:
            data_list_1 = file_1.readlines()
            data_list_2 = file_2.readlines()

        for i in range(len(data_list_1)):
            #print(data_list_1[i])
            for j in range(len(data_list_2)):
                if data_list_1[i] == data_list_2[j]:
                    #matches.append(data_list_2[j])
                    match_dict[j+1] = data_list_2[j]
        #print(match_dict)
        print("The data comparison from file1 against file2[with repetitions]: ")
        for k, v in match_dict.items():
            print(f"row : {k}, value: {v}")


obj_ref = Textdiff()
obj_ref._own_method()

# with open('randomdata.txt') as file_1, open('randomdata1.txt') as file_2:
#     file1_cont = file_1.readlines()
#     file2_cont = file_2.readlines()
#
#     file1_list = []
#     for i in file1_cont:
#         file1_list.append(i)
#     print(file1_list)