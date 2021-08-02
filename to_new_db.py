from typing import NewType

csvfile = './penguins_lter.csv'

main_db = pd.read_csv(csvfile, sep=";")
main_db.drop(columns=["Stage", "studyName", "Sample Number", "Delta 15 N (o/oo)",
             "Region", "Delta 13 C (o/oo)", "Comments"], inplace=True)
main_db.drop(main_db.columns[0], axis=1)
main_db.to_csv('./new_db.csv')
