from difflib import Differ, unified_diff
import pandas as pd

class Textdiff:

    def _own_method(self):
        fail_dict, pass_dict, counter = {}, {}, 0
        with open('file1.txt') as file_1, open('file2.txt') as file_2:
            data_list_1 = file_1.readlines()
            data_list_2 = file_2.readlines()

        for i in range(len(data_list_1)):
            for j in range(len(data_list_2)):
                if data_list_1[i] == data_list_2[j]:
                    counter += counter + 1
                    pass_dict[j+1] = data_list_2[j]
            if counter == 0:
                fail_dict[i+1] = data_list_1[i]
            else:
                counter = 0

        print("[Pass]The data comparison from file1 against file2[with repetitions]: ")
        for k, v in pass_dict.items():
            print(f"row : {k}, value: {v}")

        print("[Fail]The data comparison from file1 against file2[with repetitions]: ")
        for k, v in fail_dict.items():
            print(f"row : {k}, value: {v}")



obj_ref = Textdiff()
obj_ref._own_method()
