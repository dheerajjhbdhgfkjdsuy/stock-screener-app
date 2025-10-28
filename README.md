# Stock Screener App

A Flask-based web application for screening stocks based on various financial criteria.

## Features

- Screen stocks by market cap, P/E ratio, and dividend yield
- Filter results based on custom criteria
- Clean and intuitive web interface
- Real-time stock data integration

## Requirements

- Python 3.7+
- Flask
- pandas
- yfinance (for stock data)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/dheerajjhbdhgfkjdsuy/stock-screener-app.git
cd stock-screener-app
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

3. Use the web interface to:
   - Set your screening criteria (Market Cap, P/E Ratio, Dividend Yield)
   - Click "Screen Stocks" to view results
   - Review the filtered stock list

## Project Structure

```
stock-screener-app/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
│
└── templates/
    ├── index.html        # Home page with screening form
    └── results.html      # Results display page
```

## Configuration

The app runs on `http://127.0.0.1:5000` by default. You can modify the host and port in `app.py`:

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
