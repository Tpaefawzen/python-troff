"""
troff: Roff language in Python implementation.

The typesetting language roff, aka troff and nroff.
"""

DEBUG = False

if __name__ == "__main__":
    DEBUG = True

class RoffLine:
    def __init__(self, line):
        self.line = line

    def __str__(self):
        return str(self.line)

    def __repr__(self):
        return f"<{type(self).__name__}: {str(self)}>"

class Request(RoffLine):
    def __init__(self, line):
        assert line[0] in ".'"
        super().__init__(line)

class Text(RoffLine):
    pass

def parse_level_0(src: str):
    # The roff source is line-oriented so splitting each by line.
    lines = src.split("\n")

    result = []
    for line in lines:
        try:
            if line[0] in ".'":
                result.append(Request(line))
                continue
        except IndexError:
            pass
        result.append(Text(line))

    return result

if DEBUG:
    from  pprint import pprint
    src = r"""This is an example source.

.\" COMMENT

\fBBOLD.\fR

.de Foo \" THIS IS COMMENT
Foo
..

. B BOLD
.B  BOLD
'   BOL D"""
    pprint(parse_level_0(src))
