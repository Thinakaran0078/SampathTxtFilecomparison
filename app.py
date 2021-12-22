
class Textdiff:

    def own_method(self):
        html_txt = """<html>
        <head>
        <style>
        table, th, td {
          border: 1px solid black;
        }
        th, td {
          padding-top: 5px;
          padding-bottom: 5px;
        }   
        </style>
        </head>
        <body>

        <h1>The table element</h1>

        <table>
          <tr>
            <th>Filename</th>
            <th>Values</th>
            <th>Rownumber</th>
            <th>Result</th>
          </tr>"""
        html_txt1 = html_txt

        fail_dict, pass_dict, counter = {}, {}, 0
        pass_list = []
        pass_set = {}
        j_count = 0

        with open('file1.txt') as file_1, open('file2.txt') as file_2:
            data_list_1 = file_1.readlines()
            data_list_2 = file_2.readlines()

        for i in range(len(data_list_1)):
            for j in range(len(data_list_2)):
                if data_list_1[i] == data_list_2[j]:
                    counter += counter + 1
                    pass_set = {data_list_2[j]}
                    pass_set.add(j+1)
                    #pass_dict[j+1] = data_list_2[j]

                    # TODO : pass html file need to be created here
            if counter == 0:
                fail_dict[i+1] = data_list_1[i]
                html_txt += "<tr>"
                html_txt += "<td>File1</td>"
                html_txt += "<td>{}</td>".format(data_list_1[i])
                html_txt += "<td>{}</td>".format(i+1)
                html_txt += """<td bgcolor="red">{}</td>""".format("FAIL")
                html_txt += "</tr>"

            else:
                print(pass_set)
                pass_set.clear()
                counter = 0

        html_txt += "</table>"
        html_txt += "</body></html>"

        with open('fail.html', 'w') as file:
            file.writelines(html_txt)

        print("[Pass]The data comparison from file1 against file2[with repetitions]: ")
        for k, v in pass_dict.items():
            print(f"row : {k}, value: {v}")
        print(pass_dict)

        print("[Fail]The data comparison from file1 against file2[with repetitions]: ")
        for k, v in fail_dict.items():
            print(f"row : {k}, value: {v}")


obj_ref = Textdiff()
obj_ref.own_method()
