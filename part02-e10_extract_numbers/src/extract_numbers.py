#!/usr/bin/env python3

def extract_numbers(s):
    ss, l = s.split(), []
    for i in ss:
        try:
            l.append(int(i))
        except ValueError:
            try:
                l.append(float(i))
            except ValueError:
                pass
    return l


def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))


if __name__ == "__main__":
    main()
