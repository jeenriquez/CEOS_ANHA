#!/usr/bin/env python3
# coding: utf-8

import requests

MASK_URL = 'https://bit.ly/3TkYlGL'


def download_large_file(download_url, download_destination):
    """ Download a large file given url into destination

        Parameters
        ----------
        download_url : str
            URL location
        download_destination : str
            Path and filename where to save file.

        Return
        ----------
        Saves file in destination.

    """

    # Code from:
    # https://www.geeksforgeeks.org/how-to-download-large-file-in-python-with-requests/
    try:
        with requests.get(download_url, stream=True) as response:
            response.raise_for_status()
            with open(download_destination, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        print("File downloaded successfully!")
    except requests.exceptions.RequestException as e:
        print("Error downloading the file:", e)


def download_mask():
    """ Downloads standard mask.
    """

    # URL location for mask.
    mask_url = MASK_URL

    # Filename
    mask_destination = '../package_data/ANHA4_mask.nc'

    download_large_file(mask_url, mask_destination)


def test_download():
    """ Testing download_large_file
    """

    # TODO update to smaller file and move to tests
    # Tested with this 3Gb file, and it works well.
    url_test = 'https://releases.ubuntu.com/20.04.4/ubuntu-20.04.4-desktop-amd64.iso'

    destination_test = 'ubuntu-20.04.4-desktop-amd64.iso'

    download_large_file(url_test, destination_test)


if __name__ == '__main__':

    download_mask()