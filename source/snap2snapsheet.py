import os
from PIL import Image
import sys
import xlsxwriter


class color():

    red = 0
    green = 1
    blue = 2


class img_to_excel():

    def int_to_hex(self, value):
        return format(value, '02X')

    def create_format(self, value, pos):
        main_value = value
        sub_value = 0
        red_val = main_value if (pos is color.red) else sub_value
        green_val = main_value if (pos is color.green) else sub_value
        blue_val = main_value if (pos is color.blue) else sub_value
        return "#" + self.int_to_hex(red_val) + self.int_to_hex(green_val) + self.int_to_hex(blue_val)

    def red_format(self, value):
        return self.create_format(value, color.red)

    def green_format(self, value):
        return self.create_format(value, color.green)

    def blue_format(self, value):
        return self.create_format(value, color.blue)

    def create_excel_from_image(self, image_name,workbook_name):
        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook(workbook_name)
        workbook_format = workbook.add_format()
        worksheet = workbook.add_worksheet()

        img = Image.open(image_name)
        pix = img.load()
        # TODO: replace all the prints with the right logging mechanism
        print img.size
        (width, length) = img.size
        excel_rows_values = []

        # TODO: Dont convert all the way to AAA, calculate it !!!
        worksheet.set_column('A:AAA', 3)
        for column in range(width):
            for row in range(length * 3):
                worksheet.set_row(row, 1)

        print "Done measuring all the pesky little pixels ."
        print "Starting to figure out where all the colors go ..."
        workbook_format = workbook.add_format()
        for column in range(width):
            for row in range(length):
                # TODO : Remove print and replace
                # with a progress bar of sorts
                print (column, row)
                red_val = pix[column, row][color.red]
                green_val = pix[column, row][color.green]
                blue_val = pix[column, row][color.blue]
                workbook_format = workbook.add_format()
                workbook_format.set_bg_color(self.red_format(red_val))
                worksheet.write(((row * 3)+color.red), column, " ", workbook_format)
                workbook_format = workbook.add_format()
                workbook_format.set_bg_color(self.green_format(green_val))
                worksheet.write(((row * 3) + color.green), column, " ", workbook_format)
                workbook_format = workbook.add_format()
                workbook_format.set_bg_color(self.blue_format(blue_val))
                worksheet.write(((row * 3) + color.blue), column, " ", workbook_format)
        print "Done collecting the pieces of the puzzle."
        print "Starting to paint your snapsheet ..."
        workbook.close()
        print "Your snapsheet is done."

def main():
    i2e_obj = img_to_excel()
    # TODO : dont hardcode values get it from the user as advertised !!!
    i2e_obj.create_excel_from_image("../images/derickmathew_dp01.thumbnail",'output.xlsx')

if __name__ == "__main__":
    main()
