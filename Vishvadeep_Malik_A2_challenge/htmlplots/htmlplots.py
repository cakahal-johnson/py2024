import pandas as pd
import matplotlib.pyplot as plt
import os

def make_html_files():
  # Read the index.txt file and get the list of CSV files
  with open("htmlplots/index.txt") as f:
    csv_files = f.read().splitlines()
  # Loop through each CSV file
  for i, csv_file in enumerate(csv_files):
    # Read the CSV file as a DataFrame
    df = pd.read_csv(f"htmlplots/{csv_file}")
    # Get the name of the dataset by removing the .csv extension
    name = csv_file[:-4]
    # Create a PNG image of a line plot of the data and save it in the htmlplots folder
    df.plot()
    plt.savefig(f"htmlplots/{name}.png")
    # Create an HTML file with the same name and save it in the htmlplots folder
    with open(f"htmlplots/{name}.html", "w") as f:
      # Write the header with the name of the dataset
      f.write(f"<html><body>\n<h1>{name}</h1>\n<p>\n")
      # Write the link to the previous HTML file, unless this is the first
      if i > 0:
        prev_name = csv_files[i-1][:-4]
        f.write(f"<a href='{prev_name}.html'>Previous</a>\n")
      # Write the link to the next HTML file, unless this is the last
      if i < len(csv_files) - 1:
        next_name = csv_files[i+1][:-4]
        f.write(f"<a href='{next_name}.html'>Next</a>\n")
      # Write the closing tag for the paragraph
      f.write("</p>\n")
      # Write the HTML code for the table of data using pandas
      f.write(df.to_html())
      # Write the image tag for the PNG image of the plot
      f.write(f"<img src='{name}.png'>\n")
      # Write the closing tags for the body and html
      f.write("</body></html>\n")