import pandas as pd
import os

csvfile = os.path.join(os.path.dirname(__file__),
                       "../data/penguins_lter.csv")

main_db = pd.read_csv(csvfile, sep=";")
main_db.drop(columns=["Stage", "studyName", "Sample Number", "Delta 15 N (o/oo)",
             "Region", "Delta 13 C (o/oo)", "Comments"], inplace=True)

main_db.drop(main_db.columns[0], axis=1)

main_db[main_db["Sex"] == "."] = pd.NA

main_db["Date Egg"] = pd.to_datetime(main_db["Date Egg"])

main_db.dropna(inplace=True)
main_db.to_csv(os.path.join(os.path.dirname(__file__),
                            "../data/new_db.csv"))
