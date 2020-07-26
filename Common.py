import difflib


def content_comparison(filename, count, text_list1, text_list2):
    difference = difflib.HtmlDiff(wrapcolumn=80, tabsize=8).make_file(text_list1, text_list2,
                                                                      fromdesc="stage", todesc="wem")
    with open(filename + '_' + str(count) + '.html', 'w') as htmlfile:
        htmlfile.write(difference)


def main():
    pass


if __name__ == '__main__':
    main()