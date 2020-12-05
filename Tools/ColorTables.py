def BuildsFormatTables():
    """
    Builds tables with all the possibles styles
    """
    for style in range(8):
        for textColor in range(30, 38):
            cad_cod = ''
            for backgroundColor in range(40, 48):
                fmto = ';'.join([str(style),
                                 str(textColor),
                                 str(backgroundColor)])
                cad_cod += "\033["+fmto+"m "+fmto+" \033[0m"
            print(cad_cod)
        print('\n')

# Test
BuildsFormatTables()