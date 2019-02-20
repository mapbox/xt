# xt
import re
import json


def xvert(instream, delimiter):
    for inp in instream:
        yield parsetile(inp, delimiter)


def format_hash(x, y, z, delimiter):
    return "{1}{0}{2}{0}{3}".format(delimiter, z, x, y)


def parse_xyz(input):
    z, x, y = [
        int(t)
        for t in re.findall(r"(^|[\/\s\-])(\d+)[\-\/](\d+)[\-\/](\d+)", input)[-1][1:]
    ]
    return [x, y, z]


def parsetile(inp, delimiter="/"):
    if re.match(r".*\d+[\-\/]\d+[\-\/]\d+.*", inp):
        return json.dumps(parse_xyz(inp))

    elif re.match(r"\[\d+(\,\s|\,)\d+(\,\s|\,)\d+\]", inp):
        x, y, z = json.loads(inp)

        return format_hash(x, y, z, delimiter)

    else:
        raise ValueError("Could not parse tile")
