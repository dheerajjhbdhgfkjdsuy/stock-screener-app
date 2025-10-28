from flask import Flask, render_template, request, jsonify
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)

# List of popular Indian stocks (NSE symbols)
POPULAR_STOCKS = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",
    "HINDUNUIVR.NS", "BARTINDIA.NS", "ITC.NS", "KOTAKBANK.NS", "AJANTPHARM.NS",
    "AXISBANK.NS", "BPCL.NS", "ASIANPAINT.NS", "MARUTI.NS", "TITAN.NS",
    "SUNPHARMA.NS", "ULTRACEMDO.NS", "NTPC.NS", "NESTLE.NS", "LT.NS",
    "TECHM.NS", "HCLTECH.NS", "POWERGRID.NS", "JSWSTEEL.NS", "INDALCO.NS",
    "DIVISLAB.NS", "IOC.NS", "DHIFLI.NS", "TATAMOTORS.NS", "SBIN.NS",
    "BHARTIARTL.NS", "HEROMOTOCO.NS", "WIPRO.NS", "ADANIPORTS.NS", "COALINDIA.NS",
    "GAIL.NS", "JSWENERGY.NS", "APOLLOHOSP.NS", "SIEMENS.NS", "ABB.NS",
    "TATASTEEL.NS", "BHEL.NS", "AMBUJACEM.NS", "BHIM.NS", "CIPLA.NS",
    "BINDAL.NS", "VEDDLFD.NS", "ONGC.NS", "CANRABANK.NS", "ZEE.NS"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/screen', methods=['POST'])
def screen():
    try:
        # Get user inputs
        min_volume = float(request.form.get('min_volume', 1)) * 1000000
        min_price_change = float(request.form.get('min_price_change', 0.0))
        max_price_change = float(request.form.get('max_price_change', 100.0))
        
        results = []
        
        for symbol in POPULAR_STOCKS:
            try:
                stock = yf.Ticker(symbol)
                
                # Get today's data
                today = datetime.now()
                data = stock.history(period='1d', interval='1m')
                
                if data.empty or len(data) < 2:
                    continue
                
                # Calculate metrics
                current_price = data['Close'].iloc[-1]
                open_price = data['Open'].iloc[0]
                high_price = data['High'].max()
                low_price = data['Low'].min()
                total_volume = data['Volume'].sum()
                
                # Calculate percentage change
                if open_price > 0:
                    price_change = ((current_price - open_price) / open_price) * 100
                else:
                    continue
                
                # Apply filters
                if (total_volume >= min_volume and 
                    min_price_change <= price_change <= max_price_change):
                    
                    # Get stock info
                    info = stock.info
                    company_name = info.get('shortName', symbol.replace('.NS', ''))
                    
                    results.append({
                        'symbol': symbol.replace('.NS', ''),
                        'name': company_name,
                        'current_price': round(current_price, 2),
                        'open_price': round(open_price, 2),
                        'high_price': round(high_price, 2),
                        'low_price': round(low_price, 2),
                        'price_change': round(price_change, 2),
                        'volume': int(total_volume)
                    })
                    
            except Exception as e:
                # Skip stocks with errors
                continue
        
        # Sort by price change (descending)
        results.sort(key=lambda x: x['price_change'], reverse=True)
        
        return render_template('results.html', results=results)
        
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)