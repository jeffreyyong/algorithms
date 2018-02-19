
import re


def scrub(string):
    pattern = re.compile(r'<script[\s\S]+?/script>')
    result = re.sub(pattern, "", string)
    return result
