#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    return list(map(int,re.findall(r"\[([-+\d][\d]+)\]",re.sub(r"[\n\t\s]*", "", s))))

def main():
    print(integers_in_brackets("   afd [asd] [12 ] [a34]  [\t -43 ]tt [+12]xxx"))
    print(integers_in_brackets("  afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
