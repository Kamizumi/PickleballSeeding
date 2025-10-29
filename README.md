# Pickleball Seeding Program

This Python script is designed to automate the initial **seeding** for a pickleball tournament by calculating a weighted score for each group or player. This comprehensive score is determined by combining the **ELO rating** with a modified **win/loss ratio** to generate fair and balanced pairings for the start of the tournament.

---

## Current Version: Command-Line Interface (CLI)

This version is a **command-line interface (CLI)** tool written in Python that integrates with Google Sheets to retrieve data.

### Key Features
* **Weighted Seeding Logic:** Calculates a sophisticated seeding score using the following formula:
    $$\text{Weighted Score} = \text{ELO} + (\text{Wins} \times 0.05) + (\text{Losses} \times -0.02)$$
    *(The win and loss weights can be easily adjusted within the `calcWeight` function.)*
* **Google Sheets Integration:** Securely accesses player data (Group/Player Name, ELO, and Win/Loss Ratio) from a specified Google Sheet using the `gspread` library.
* **Automated Pairing:** Sorts the groups based on their calculated weighted scores and generates a seeded bracket or pairing for the first round.

### Prerequisites and Setup

To run the current script, you need to set up Google's **OAuth 2.0 credentials** for secure access to the Google Sheets API.

1.  **Dependencies:** Ensure you have the required Python libraries installed in your environment:
    ```bash
    pip install gspread google-auth-oauthlib requests pickle
    ```
2.  **Google Credentials Setup:**
    * Set up an OAuth 2.0 client ID through the Google Cloud Console.
    * Download the JSON file containing your client secrets.
    * **Rename** the downloaded file to `client_file.json` and place it in the **same directory** as the `PickleballSeeding.py` script.
3.  **Execution:** Run the script from your terminal:
    ```bash
    python PickleballSeeding.py
    ```
    The first time you run it, a browser window will open to authorize access to your Google account. A file named `token.pickle` will be created to securely store your login credentials for future use.
4.  **Input:** The program will prompt you to **input the exact name of your Google Sheet**. The script assumes the tournament data (Name, ELO, Ratio) starts from the second row of the first sheet.

---

## Future Development: Full-Stack Web Application 🚀

While the current script offers robust backend seeding logic, I am actively developing a **full-stack web application** to make this tool accessible to a broader audience without requiring command-line interaction or API setup.

### Planned Enhancements

* **Intuitive Graphical User Interface (GUI):** A clean web interface will replace the CLI, allowing users to upload data, input scores, and view results instantly.
* **Secure Authentication:** A full user authentication system will allow users to create and manage their own accounts.
* **Supabase Database Integration:** Player data, tournament history, and user information will be stored and managed in a persistent **Supabase** database. This will enable users to easily **add, update, and remove** their data.
* **Enhanced Reporting:** Detailed, visual reports and bracket generation based on the calculated seeds.