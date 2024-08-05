'''
Task 3: Creating simple HTML pages [4 marks]
'''
# we have to import pandas
import os
import pandas as pd
import glob

# assign path
to_html_list = ['Tableone.html', 'Tabletwo.html', 'Tablethree.html']

# copy a new file when moved to a new system or use file_list variable
path = r"C:\Users\JOHNSON\PycharmProjects\Atuejide_Henry_Okwy"


# Change the directory
os.chdir(path)
  




# appending the datasets to the list
def make_html_file(file_path):
    with open(file_path, 'r') as f:
        # Read text File
        file_list = ['one.csv', 'two.csv', 'three.csv']
        ft = 0
        while ft <= len(file_list):
#creating an empty list
         main_dataframes = pd.DataFrame(pd.read_csv(file_list[0]))
         ft = ft + 1


        i = 0
        while i <= len(to_html_list):
            # print(to_html_list[i])            
            main_dataframes.to_html(to_html_list[i])
            i = i + 1


for file in os.listdir():
            # Check whether file is in text format or not
    if file.endswith(".csv"):
        file_path = f"{path}\{file}"

        # calling out the function 
        make_html_file(file_path)
    print("\n")



# directory =r"C:\Users\JOHNSON\PycharmProjects\Atuejide_Henry_Okwy"

# data = []

# for filename in os.listdir(directory):
#     if filename.endswith('.html'):
#         csv_filename = filename.replace('.html','.csv')
#         fname = os.path.join(directory,filename)
#         with open(fname, 'r') as f:
#             table = pd.read_html(f.read())[0]
#             table.to_csv(csv_filename, index=False)

# # print(data)
# # 
# make_html_file(directory)




# here we read from the first csv file
# make_html_file = pd.read_csv("one.csv")

# here we create the HTML for the first table
# make_html_file.to_html("one.html")

# here is for the web view display
# html_file = make_html_file.to_html()

# here we output to terminal
# print(make_html_file.to_html())

#  we use go live server extension in the browser to display in the browser


