from stack import ArrayStack


def is_valid(raw_html):
    temp_stack = ArrayStack()
    opening_tag = raw_html.find("<")
    while opening_tag != -1:
        closing_tag = raw_html.find(">", opening_tag + 1)
        if closing_tag == -1:
            return False
        tag = raw_html[opening_tag+1:closing_tag]
        if not tag.startswith("/"):
            temp_stack.push(tag)
        else:
            if temp_stack.is_empty():
                return False
            if tag[1:] != temp_stack.pop():
                return False
        opening_tag = raw_html.find("<", closing_tag + 1)
    return temp_stack.is_empty()

decoy_html = "<html><head><title>hello</title></head><body><p>p tag</p></body></html>"
print(is_valid(decoy_html))