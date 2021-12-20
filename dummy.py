d = {'kiwi': ['kiwi.good.svg'], 'apple': ['apple.good.2.svg', 'apple.good.1.svg'], 'banana': ['banana.1.ugly.svg', 'banana.bad.2.svg']}

html = """<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
}
th, td {
  padding-top: 10px;
  padding-bottom: 20px;
  padding-left: 30px;
  padding-right: 40px;
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
# for fruit in d:
#     html += "<tr><td>{}</td>".format(fruit)
#     for state in "VALUES", "ROW NUMBER", "RESULT":
#         html += "<td>{}</td>".format('<br>'.join(f for f in d[fruit] if ".{}.".format(state) in f))
#     html += "</tr>"
# html += "</table></html>"


print(html)




