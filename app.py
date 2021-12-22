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

        with open('file1.txt') as file_1, open('file2.txt') as file_2:
            data_list_1 = file_1.readlines()
            data_list_2 = file_2.readlines()

        for i in range(len(data_list_1)):
            for j in range(len(data_list_2)):
                if data_list_1[i] == data_list_2[j]:
                    counter += 1
                    if len(pass_list) == 0:
                        pass_list.append(i + 1)
                        pass_list.append(data_list_2[j])
                        pass_list.append(j + 1)
                    else:
                        pass_list.append(j+1)
            if counter == 0:
                fail_dict[i+1] = data_list_1[i]
                html_txt += "<tr>"
                html_txt += "<td>File1</td>"
                html_txt += "<td>{}</td>".format(data_list_1[i])
                html_txt += "<td>{}</td>".format(i+1)
                html_txt += """<td bgcolor="red">{}</td>""".format("FAIL")
                html_txt += "</tr>"
                #print(fail_dict)

            else:
                #print(pass_list)
                #print(len(pass_list))
                file2_occ_len = len(pass_list) - 3
                #print(file2_occ_len)
                file2_pass_list = (pass_list[2:])
                #print(file2_pass_list)

                html_txt1 += "<tr>"
                html_txt1 += "<td>File1</td>"
                html_txt1 += "<td>{}</td>".format(pass_list[1])
                html_txt1 += "<td>{}</td>".format(pass_list[0])
                if len(pass_list) == 3:
                    html_txt1 += """<td rowspan="2" bgcolor="green">PASS</td>"""
                else:
                    html_txt1 += """<td rowspan="{}" bgcolor="green">PASS</td>""".format(2 + file2_occ_len)
                html_txt1 += "</tr>"

                if len(pass_list) == 3:
                    #the row number of file1 data
                    html_txt1 += "<tr>"
                    html_txt1 += "<td>File2</td>"
                    html_txt1 += "<td>{}</td>".format(pass_list[1])
                    html_txt1 += "<td>{}</td>".format(pass_list[2])
                    html_txt1 += "</tr>"
                else:
                    #the row numbers of fil2 data findings"
                    for rows in range(len(file2_pass_list)):
                        html_txt1 += "<tr>"
                        html_txt1 += "<td>File2</td>"
                        html_txt1 += "<td>{}</td>".format(pass_list[1])
                        html_txt1 += "<td>{}</td>".format(file2_pass_list[rows])
                        html_txt1 += "</tr>"

                pass_list = []
                counter = 0

        html_txt += "</table>"
        html_txt += "</body></html>"

        html_txt1 += "</table>"
        html_txt1 += "</body></html>"

        with open('fail.html', 'w') as file:
            file.writelines(html_txt)

        with open('pass.html', 'w') as file:
            file.writelines(html_txt1)


obj_ref = Textdiff()
obj_ref.own_method()
