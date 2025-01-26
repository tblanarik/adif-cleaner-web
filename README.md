# ADIF Cleaner Web

ADIF Cleaner Web is a web application designed to clean and filter ADIF (Amateur Data Interchange Format) files. It allows users to upload ADIF files, specify a date range, and optionally deduplicate callsigns. The filtered content can then be downloaded.

## Features

- Upload ADIF files
- Filter by start and end datetime (UTC)
- Option to deduplicate callsigns
- Download the cleaned ADIF file

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/tblanarik/adif-cleaner-web.git
    cd adif-cleaner-web
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the application:
    ```sh
    python src/app.py
    ```

4. Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Open the application in your web browser.
2. Upload an ADIF file using the file input.
3. Specify the start and end datetime (UTC) for filtering.
4. Check the "Dedup Callsigns" option if you want to remove duplicate callsigns.
5. Click the "Clean" button to process the file.
6. If the file is successfully processed, the filtered content will be displayed along with a download button to save the cleaned file.

## License

This project is licensed under the MIT License.
