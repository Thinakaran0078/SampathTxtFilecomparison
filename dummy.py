
html_txt = """<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
}
th, td {
  padding-top: 10px;
  padding-bottom: 10px;
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

key, value = 1, "dhina"
html_txt += "<tr>"
html_txt += "<td>File1</td>"
html_txt += "<td>{}</td>".format(value)
html_txt += "<td>{}</td>".format(key)
html_txt += """<td bgcolor="red">{}</td>""".format("FAIL")
html_txt += "</tr>"
html_txt += "</body>"
html_txt += "</table></html>"

# < tr >
# < td > File1 < / td >
# < td > dhina < / td >
# < td > 10 < / td >
# < td
# bgcolor = "red" > Fail < / td >
# < / tr >

# for fruit in d:
#     html += "<tr><td>{}</td>".format(fruit)
#     for state in "VALUES", "ROW NUMBER", "RESULT":
#         html += "<td>{}</td>".format('<br>'.join(f for f in d[fruit] if ".{}.".format(state) in f))
#     html += "</tr>"
# html += "</table></html>"

# with open('test2.html', 'w') as file:
#     file.writelines(html)




