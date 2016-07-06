from models import CategoryResult, Violation
import csv
import xlrd
import datetime

CATEGORY_NAMES = [u'Garbage and Refuse',
 u'Unsanitary Conditions',
 u'Animals and Pests',
 u'Building Conditions',
 u'Vegetation',
 u'Chemical Hazards',
 u'Biohazards',
 u'Air Pollutants and Odors',
 u'Retail Food']

def convert_excel_float_to_python_date(sheet, row, col, wb):
    date = sheet.cell_value(rowx=row, colx=col)
    try:
        dt_tuple = xlrd.xldate_as_tuple(date, wb.datemode)
    except:
        final_date = 'Date Unavailable'
        return final_date

    final_date = datetime.datetime(*dt_tuple)
    return final_date

def retrieve_violation_data(f):
    categories = [CategoryResult(name=n) for n in CATEGORY_NAMES]
    book = xlrd.open_workbook(f)
    first_sheet = book.sheet_by_index(0)
    total_violations = first_sheet.nrows
    for row_num in range(0, total_violations):
        if row_num is not 0:
            try:
                row = first_sheet.row_values(row_num)
            except (IOError, csv.Error):
                print "Couldn't read row %s from violations file. Exiting." % (row_num)
                raise
            category = row[2]
            violation_date = convert_excel_float_to_python_date(wb=book,sheet=first_sheet,
                                                                                       col=3,
                                                                                       row=row_num)
            violation_date_closed = convert_excel_float_to_python_date(wb=book,sheet=first_sheet,
                                                                                       col=4,
                                                                                       row=row_num)
            v = Violation(v_id=row[0],
                      inspection_id=row[1],
                      category=category,
                      violation_date=violation_date,
                      violation_date_closed=violation_date_closed,
                      violation_type=row[5])

            c = [c for c in categories if c.name == category]
            relevant_category = c[0]
            relevant_category.violations.append(v)

    return categories, total_violations -1
