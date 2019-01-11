from email_alert import EmailAlert
from amazon_bot import AmazonBot
from oauth2client.service_account import ServiceAccountCredentials

import gspread


class PriceUpdater(object):
    def __init__(self, spreadsheet_name):
        self.item_col = 1
        self.price_col = 2
        self.frequency_col = 3
        self.url_col = 4
        self.product_name_col = 5
        
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',
                                                                 scope)
        client = gspread.authorize(creds)

        self.sheet = client.open(spreadsheet_name).sheet1

    def update_spreadsheet_price(self):
        urls = self.sheet.col_values(self.url_col)

        for i in range(1, len(urls)):
            print(f"Processing URL {i} or {len(urls)-1}")
            amazon_bot = AmazonBot(urls[i])
            product_name = amazon_bot.get_product_name()
            product_price = amazon_bot.get_product_price()

            print(f"Updating item {self.sheet.cell(i+1, self.item_col).value} from Amazon listing {product_name} with price {product_price}")
            self.sheet.update_cell(i+1, self.price_col, product_price)
            amazon_bot.close_session()

    def process_item_list(self):
        # Skip over the column heading in the spreadsheet.
        items = self.sheet.col_values(self.item_col)[1:]

        amazon_bot = AmazonBot(items)
        prices, urls, names = amazon_bot.search_items()

        print("Updating spreadsheet.")
        for i in range(len(prices)):
            self.sheet.update_cell(i+2, self.price_col, prices[i])
            self.sheet.update_cell(i+2, self.url_col, urls[i])
            self.sheet.update_cell(i+2, self.product_name_col, names[i])


price_updater = PriceUpdater("ProductPrice")
price_updater.process_item_list()

email = EmailAlert("Google Sheets Updated", "This is a message to indicate that the script has completed updating Google Sheets.")
email.send_email()
