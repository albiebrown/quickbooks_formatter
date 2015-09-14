import csv

ACCOUNT_NAME = ""
#i.e. Chase, Bank of America, etc.

TAX_REPORT = ""
#i.e. taxes.csv (make sure this is in the same directory as the python script)

fileToRead = open(TAX_REPORT, 'rU')
reader = csv.reader(fileToRead)

header = next(reader)

DATE_IDX = header.index('DATE')
ITEM_IDX = header.index('ITEM')
COST_IDX = header.index('COST')

with open('Formatted_Tax_Report.iif', 'wb') as fileToWrite:
	writer = csv.writer(fileToWrite)

	row1 = ['!ACCNT', 'NAME', 'ACCNTTYPE', 'DESC', 'ACCNUM', 'EXTRA']
	row2 = ['ACCNT', 'Accounts Payable', 'AP']
	row3 = ['ACCNT', 'ACCOUNT_NAME', 'CCARD']

	rows = [row1, row2, row3]

	writer.writerows(rows)

	for row in reader:		
		row1 = ['!VEND', 'NAME', 'REFNUM', 'PRINTAS', 'ADDR1', 'ADDR2', 'ADDR3', 'ADDR4', 'ADDR5', 'VTYPE', 'CONT1', 'CONT2', 'PHONE1', 'PHONE2', 'FAXNUM', 'EMAIL', 'NOTE', 'TAXID', 'LIMIT', 'TERMS', 'NOTEPAD', 'SALUTATION', 'COMPANYNAME', 'FIRSTNAME', 'MIDINIT', 'LASTNAME']
		row2 = ['VEND', row[ITEM_IDX], '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Jon', '', 'Vendor']
		row3 = ['!TRNS', 'TRNSID', 'TRNSTYPE', 'DATE', 'ACCNT', 'NAME', 'AMOUNT', 'DOCNUM', 'MEMO', 'CLEAR', 'TOPRINT', 'NAMEISTAXABLE', 'ADDR1', 'ADDR2', 'ADDR3', 'ADDR4', 'ADDR5', 'DUEDATE', 'TERMS', 'PAID', 'SHIPVIA', 'SHIPDATE', 'YEARTODATE', 'WAGEBASE']
		row4 = ['!SPL', 'SPLID', 'TRNSTYPE', 'DATE', 'ACCNT', 'NAME', 'AMOUNT', 'DOCNUM', 'MEMO', 'CLEAR', 'QNTY', 'PRICE', 'INVITEM', 'PAYMETH', 'TAXABLE', 'VALADJ', 'REIMBEXP', 'SERVICEDATE', 'OTHER2', 'OTHER3', 'YEARTODATE', 'WAGEBASE']
		row5 = ['!ENDTRNS']
		row6 = ['TRNS', '', 'CCARD', row[DATE_IDX], ACCOUNT_NAME, row[ITEM_IDX], '-' + row[COST_IDX], '', '', 'N', 'N', 'N', '', '', '', '', '', '0/0/0', '', 'Y', '', '0/0/0', '0', '0']
		row7 = ['SPL', '', 'CCARD', row[DATE_IDX], 'Accounts Payable', row[ITEM_IDX], row[COST_IDX], '', '', 'N', '', '', '', '', 'N', 'N', 'NOTHING', '0/0/0', '', '', '0', '0']
		row8 = ['ENDTRNS']

		rows = [row1, row2, row3, row4, row5, row6, row7, row8]

		writer.writerows(rows)
