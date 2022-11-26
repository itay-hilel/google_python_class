import sys
import re
import os
import urllib.request


# open a file with data
def open_file(filename):
    with open(filename) as f:
        content = f.read()
    return content


# getting urls to download, removing duplicates, sorting alphabetically, replacing for working link in 2020
def get_urls(text):
    urls = re.findall('GET\s(\/edu\S+)\s', text)  # searching for links in a file
    no_duplicates = []
    old_link = '/edu/languages/google-python-class/'  # worked in 2010
    new_link = 'https://developers.google.com/edu/python/'  # working in 2020
    for url in urls:
        url_upd = url.replace(old_link, new_link)  # replacing old address with a new one
        if url_upd not in no_duplicates:  # removing duplicates        
            no_duplicates.append(url_upd)
    no_duplicates.sort()  # sorting in alphabetical order
    return no_duplicates

        
# downloads all files from a urls_list to a given directory; renames files in numerical order         
def download_img(urls, folder):
    if os.path.exists(folder) == False:  # checking whether a folder exists or not
        os.mkdir(folder)  # creating a new folder if not
    to_dir = os.path.abspath(folder)
    # a loop for downloading files and renaming them
    for i in range(len(urls)):
        file_name = 'img%d' % i
        urllib.request.urlretrieve(urls[i], os.path.join(to_dir, file_name))

        
# creating an html file that will bring all the pieces of a picture together (open it in a browser)!
def html_output(urls, folder):
    to_dir = os.path.abspath(folder)
    html_file = 'index.html'
    with open(os.path.join(to_dir, html_file), 'a') as f:
        f.write('<html><body>\n')
        for i in range(len(urls)):
            file_name = 'img%d' % i
            f.write('<img src="%s">' % file_name)
        f.write(('\n</body></html>'))


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    data = open_file('animal_code.google.com')

    if todir:
        print('Script is running..')
        urls_list = get_urls(data)
        download_img(urls_list, todir)
        html_output(urls_list, todir)
        print(f'Files have been downloaded to /{todir}')

    else:
        urls_list = get_urls(data)
        for url in urls_list:
            print(url)


if __name__ == '__main__':
    main()