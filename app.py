from difflib import Differ, unified_diff


class Textdiff:

    def _own_method(self):
        match_dict = {}
        with open('randomdata.txt') as file_1, open('randomdata1.txt') as file_2:
            data_list_1 = file_1.readlines()
            data_list_2 = file_2.readlines()

        for i in range(len(data_list_1)):
            for j in range(len(data_list_2)):
                if data_list_1[i] == data_list_2[j]:
                    match_dict[j+1] = data_list_2[j]

        print("The data comparison from file1 against file2[with repetitions]: ")
        for k, v in match_dict.items():
            print(f"row : {k}, value: {v}")


obj_ref = Textdiff()
obj_ref._own_method()
