import cgi


def print_ul(list):
    output = "<ul>\n"
    for i in list:
        output += "<li>" + i + "</li>\n"
    output += "</ul>"
    print(output)
list = ["hello", "world", "!"]
print_ul(list)
