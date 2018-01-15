# SSN Intranet Downloader
####*Python Script to download all files for CSE/IT  given year &amp;  semester from the intranet and hence generate a local copy of the webpages.* 

###Requirements
* Python 3.6
* bs4 ([Beautiful Soup library] 
# Install bs4 using "pip install bs4" || "pip3 install bs4"

Options | Help
--------|-----------
-b | **Branch**. *CSE* . *IT*
-s | **Semester**. 1 - 8
-p | **Path** to download files to

###Example 
To run the script. (***Input using prompts)***

	python ssn.py

To download with command line arguments, use the -b to specifiy branch and -s to specify semester

eg. to download the 6th semester CSE intranet files, use

	python ssn.py -b cse -s 6

# Make sure that the python ran is python 3. If not , then use 

	python3 ssn.py -b cse -s 6 

#instead 

- Progress bar to indicate download status of each subject 
- Renames files based on headings/ link text from pages.  
- Updates downloaded files every time script is run. Does not overwrite prexisting files.

# SSN Intranet Modifier

This reformats the links and references within the htmls to make the html references work when the folder as a whole is copied from one computer to another.

If the folder "ssn_intranet_downloader_3" is copied as such from pc x to pc y, then pc y user can run ssn-modifier to reformat the already downloaded files on pc y, thereby eliminating the need to redownload the whole data again.

# Thanks to vishal gupta (py_ranoid) for making the original code for ssn.py.
# I have merely ported this to python 3 and tweaked the underlying logic while adding more robust exception handling.