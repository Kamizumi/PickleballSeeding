import gspread
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os

class PickleballSeeding:
    def __init__(self):

        #What the program is allowed to access (read access to sheets)
        scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly",
                  "https://www.googleapis.com/auth/drive.readonly"
        ]


        self.creds = None

        #This is a token for when you've already logged in | If it exists, just logs you back in
        if os.path.exists("token.pickle"):
            with open("token.pickle", "rb") as token:
                self.creds = pickle.load(token)

        #If we don't have the OAUTH2.0 file downloaded, download it and rename it
        if not os.path.exists("client_file.json"):
            raise FileNotFoundError("Missing 'client_file.json', Please create OAuth credentials and place it in this directory." )

        #If credential is invalid or not available
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "client_file.json", scopes)
                self.creds = flow.run_local_server(port = 0)

            #Saves token for your login for next time
            with open("token.pickle", "wb") as token:
                pickle.dump(self.creds, token)

        self.client = gspread.authorize(self.creds)

        self.group_scores = []

        sheet_name = input("Please input the sheet's name\n")

        self.sheet = self.client.open(sheet_name).sheet1

        self.data = self.sheet.get_all_values()

        self.rows = self.data[1:]



    def main(self):

        for row in self.rows:
            weighted_values = self.calcWeight(row[1],row[2])
            group_name = row[0]
            self.group_scores.append((group_name, weighted_values))

        self.seedPlacements(self.group_scores)




    def calcWeight(self, elo, ratio, win_weight = 0.05, loss_weight = -0.02):
        wins, losses = (ratio.split(":"))
        return float(elo) + (float(wins) * win_weight) + (float(losses) * loss_weight)

    def seedPlacements(self, group_values):
        sortedGroups = sorted(self.group_scores, key = lambda x : x[1], reverse = True)

        pairs = []
        i = 0
        while i < len(sortedGroups) - 1:
            pair = (sortedGroups[i], sortedGroups[i + 1])
            pairs.append(pair)
            i += 2

        if len(sortedGroups) % 2 != 0:
            print("Last group not included", sortedGroups[-1])

        print("Seed")
        for p in pairs:
            print(f"{p[0][0]} Weighted: ({p[0][1]})  VS  {p[1][0]}  Weighted: ({p[1][1]})")




if __name__ == "__main__":
   app = PickleballSeeding()
   app.main()
