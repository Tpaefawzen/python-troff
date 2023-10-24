"""
troff: Roff language in Python implementation.

The typesetting language roff, aka troff and nroff.
"""

DEBUG = False

if __name__ == "__main__":
    DEBUG = True

def parse_level_0(src: str):
    # The roff source is line-oriented so splitting each by line.
    lines = src.split("\n")

    result = []
    for line in lines:
        try:
            if line[0] in ".'":
                result.append(["request", line])
                continue
        except IndexError:
            pass
        result.append(["text", line])

    return result

if DEBUG:
    from  pprint import pprint
    src = r"""\
This is an example source.

.\" COMMENT

\fBBOLD.\fR

.de Foo \" THIS IS COMMENT
Foo
..

. B BOLD
.B  BOLD
'   BOL D"""
    pprint(parse_level_0(src))
