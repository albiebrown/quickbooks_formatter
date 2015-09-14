# quickbooks_formatter
Generates a formatted .iif file from a csv of your expense report.

Steps:
  1. Click "Download Zip" on the right.
  2. Open the Zip.
  3. Put your expense report in the quickbooks_formatter folder that was just created (NOTE: make sure the first line of your expense report includes columns with the exact titles of DATE, ITEM, and COST).
  4. Open the formatter.py script in a text editor.
  5. Inside the quotations, fill in values for ACCOUNT_NAME (the name of your account) and TAX_REPORT (the full name of the expense report file you just placed in the folder).
  6. On a Mac, open up Terminal, on a Windows machine open up a Command Prompt.
  7. Navigate to the quickbooks_formatter directory using the "cd" command.
  8. Type the command "python formatter.py" and press enter.
  9. Enjoy your formatted file!
