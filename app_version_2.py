class Textdiff:

    def file_comparison(self, file1, file2, file_no):
        html_txt = """
        <table>
          <tr>
            <th>File Name</th>
            <th>Values</th>
            <th>Row number</th>
            <th>Result</th>
          </tr>
        """
        html_txt1 = html_txt

        html_pass_txt = """
        <table>
          <tr>
            <th>File 1 Value</th>
            <th>File 1 Row</th>
            <th>File 2 Value</th>
            <th>File 2 Row(s)</th>
            <th>Rows Matched</th>
            <th>Result</th>
          </tr>
        """

        fail_dict, pass_dict, counter, fail_row_count, pass_row_count = {}, {}, 0, 0, 0
        pass_list = []

        data_list_1 = file1
        data_list_2 = file2
        if file_no == 1:
            file_comp_1 = file_no
            file_comp_2 = file_no + 1
        else:
            file_comp_1 = file_no
            file_comp_2 = file_no - 1

        for i in range(len(data_list_1)):
            print(f"file{file_comp_1} lines processed : {i+1}")
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
                fail_row_count = fail_row_count + 1
                fail_dict[i+1] = data_list_1[i]
                html_txt += "<tr>"
                html_txt += "<td>File{}</td>".format(file_comp_1)
                html_txt += "<td>{}</td>".format(data_list_1[i])
                html_txt += "<td>{}</td>".format(i+1)
                html_txt += """<td bgcolor="red">{}</td>""".format("FAIL")
                html_txt += "</tr>"

            else:
                pass_row_count = pass_row_count + 1
                file2_occ_len = len(pass_list) - 3
                file2_pass_list = (pass_list[2:])

                html_pass_txt += "<tr>"
                html_pass_txt += "<td>{}</td>".format(pass_list[1])
                html_pass_txt += "<td>{}</td>".format(pass_list[0])
                html_pass_txt += "<td>{}</td>".format(pass_list[1])

                if len(pass_list) == 3:
                    """
                    if the value has one match
                    """
                    html_pass_txt += """<td bgcolor="#6495ED">{}</td>""".format(pass_list[2])
                    html_pass_txt += "<td>{}</td>".format(1)
                    html_pass_txt += """<td bgcolor="#7FFF00">{}</td>""".format("PASS")
                    html_pass_txt += "</tr>"
                else:
                    """
                    if the value has more than one match
                    """
                    file2_rows, slice_const = str(file2_pass_list), slice(1, -1)
                    file2_rows_res = (file2_rows[slice_const])

                    html_pass_txt += """<td bgcolor="#6495ED">{}</td>""".format(file2_rows_res)
                    html_pass_txt += "<td>{}</td>".format(len(file2_pass_list))
                    html_pass_txt += """<td bgcolor="#7FFF00">{}</td>""".format("PASS")
                    html_pass_txt += "</tr>"

                pass_list = []
                counter = 0

        html_pass_txt += "</table>"
        html_pass_txt += "</body></html>"

        html_txt1 += "</table>"
        html_txt1 += "</body></html>"

        with open(f"file{file_no}fail.html", 'w') as file:
            print(f"\nWriting to file{file_no}fail.html file...")
            html_top = """<html>
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

                    <h1>File Comparison Results</h1>"""
            html_top_pass = html_top + "Rows count Processed : {}".format(fail_row_count)
            fail_final_html = html_top_pass + html_txt
            file.writelines(fail_final_html)
        print(f"file{file_no}fail.html created")

        with open(f"file{file_no}pass.html", 'w') as file:
            print(f"\nWriting to file{file_no}pass.html file...")
            html_top = """<html>
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

                    <h1>File Comparison Results</h1>"""
            html_top_pass = html_top + "Rows count Processed : {}".format(pass_row_count)
            pass_final_html = html_top_pass + html_pass_txt
            file.writelines(pass_final_html)
        print(f"file{file_no}pass.html created")


file_comp_obj = Textdiff()


def file_prep():
    print("Reading files..\n")
    with open('file1.txt') as file_1, open('file2.txt') as file_2:
        data_list_1 = file_1.readlines()
        data_list_2 = file_2.readlines()
    print("-----Reading Files Completed-----\n")
    return data_list_1, data_list_2


file_1_data, file_2_data = file_prep()

print("Comparing file1 against file2:\n")
file_comp_obj.file_comparison(file_1_data, file_2_data, 1)
print("\n-----Comparison of file1 against file2 completed-----\n")

print("Comparing file2 against file1: \n")
file_comp_obj.file_comparison(file_2_data, file_1_data, 2)
print("\n-----Comparison of file2 against file1 completed-----\n")

