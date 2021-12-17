d = {'kiwi': ['kiwi.good.svg'], 'apple': ['apple.good.2.svg', 'apple.good.1.svg'], 'banana': ['banana.1.ugly.svg', 'banana.bad.2.svg']}

html = """<html><table border="1">
<tr><th>Object</th><th>VALUES</th><th>ROW NUMBER</th><th>RESULT</th></tr>"""
for fruit in d:
    html += "<tr><td>{}</td>".format(fruit)
    for state in "VALUES", "ROW NUMBER", "RESULT":
        html += "<td>{}</td>".format('<br>'.join(f for f in d[fruit] if ".{}.".format(state) in f))
    html += "</tr>"
html += "</table></html>"


print(html)

# with open('test2.html', 'w') as file:
#     file.write(html)


