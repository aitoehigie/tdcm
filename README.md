# Imager

Imager is a Python script used for OCR of HDD spec-sheets and to extract MTBF and Warranty information.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements

```bash
virtualenv venv #create a virtual environment
source venv/bin/activate #activate the virtual environment 
pip install -r requirements.txt #install all requirements to run the script.

On Linux:
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
```


## Usage

```
python imager.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Support
You can reach out to the author at <aitoehigie@gmail.com> or [@pystar on twitter](https://twitter.com/pystar)


## Roadmap
Add more tests for robustness. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
