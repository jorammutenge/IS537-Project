import pandas as pd
import os


def main():
    input_folder = 'f_scripts'
    output_file = 'f_csv/movie_2.csv'
    make_script_df(input_folder, output_file)
    print("Script dataframe successfully created.")


def make_script_df(input_folder, output_file):
    # List all files in the input folder with .md extension
    md_files = [f for f in os.listdir(input_folder) if f.endswith('.md')]

    # Read the content of each .md file and store it as a row in a list
    rows = []
    for file_name in md_files:
        with open(os.path.join(input_folder, file_name), 'r') as f:
            rows.append({'title': file_name[:-3], 'script': f.read()})

    # Create a dataframe from the list of rows
    df = pd.DataFrame(rows)

    # Write the dataframe to a CSV file
    df.to_csv(output_file, index=False)


if __name__ == '__main__':
    main()
