import csv
import requests
import datetime
import schedule
import time
import matplotlib.pyplot as plt

CSV_FILE="crypto_price_log.csv"
API_URL="https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"


def fetch_and_log_crypto_data():
    try:
        response=requests.get(API_URL)
        print(response.status_code)
        response.raise_for_status()#if error occur then move except block.
        data=response.json()
        price=data['bitcoin']['usd'] 
        timestamp=datetime.datetime.now()
        with open(CSV_FILE, mode='a', newline='') as file:
            writer=csv.writer(file)
            writer.writerow([timestamp,price])
    except requests.RequestException as e:
        print(f"Error {e}")



def visualize_data():
    times,prices=[],[]
    try:
        with open(CSV_FILE,"r") as file:
            reader=csv.reader(file)
            next(reader)#Skip header.
            for row in reader:
                times.append(datetime.datetime.fromisoformat(row[0]))
                prices.append(float(row[1]))
       
        plt.figure(figsize=(10,5))
        plt.plot(times,prices, marker='o',color='b')
        plt.title("Bitcoin Price Over Time")
        plt.xlabel("Time")
        plt.ylabel("Price in USD")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
          
    except FileNotFoundError:
        print("File {e} can not Found")
    



def initialize_CSV():
    try:
        with open(CSV_FILE, mode="x",newline='') as file:
            writer=csv.writer(file)
            print(writer)
            writer.writerow(["Timestamp","Price (USD)"])#list represent the each row.
    except FileExistsError:
        pass
    
initialize_CSV()

schedule.every().minute.do(fetch_and_log_crypto_data)


try:
    while True:
        schedule.run_pending()
        time.sleep(30)
except KeyboardInterrupt:
    print("Data logging stop")
    
visualize_data()
        
        
            
            