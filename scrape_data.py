import requests
from bs4 import BeautifulSoup
import pandas as pd


def main():
    output_file = 'f_csv'
    get_movie_list(output_file)
    print("Movie list successfully scraped.")


def get_movie_list(output_file):
    url = "https://ofdollarsanddata.com/wall-street-movies/"

    # sending get request to the URL and storing the response
    response = requests.get(url)

    # parsing the content of the HTML page
    soup = BeautifulSoup(response.content, "html.parser")

    # extracting the h2 and p tags
    h2_tags = [h2.text for h2 in soup.find_all("h2")[:-3]]
    p_tags = [p.text for i, p in enumerate(soup.find_all("p")[3:-9]) if i != 5]

    # creating a dataframe from the extracted data
    data = {"title": h2_tags, "description": p_tags}
    df = pd.DataFrame(data)

    # write data to csv
    df.to_csv(f'{output_file}/movie_1.csv', index=False)


if __name__ == '__main__':
    main()
