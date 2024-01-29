# This file contains all the classes for the app

# database connection is created in main app file, we just use the cursor here
# commiting the changes to the database (e.g. after add method) happens in main app file
import mysql.connector

class Prof():
    # profDetails is a dict() where keys are names of the columns in the table
    def __init__(self, profDetails):
        self.firstName = profDetails['firstName']
        self.lastName = profDetails['lastName']
        self.id = profDetails['id']
        self.nationalId = profDetails['nationalId']
        self.base = profDetails['base']
        self.grade = profDetails['grade']

    # adds the prof to the database
    def add(self, dbCursor):
        sqlStatement = (
            "INSERT INTO profs"
            "(firstName, lastName, nationalId, base, grade)"
            f"VALUES ({self.firstName}, {self.lastName}, {self.nationalId}, {self.base}, {self.grade})"
            )

        # maybe add error handling later
        dbCursor.execute(sqlStatement)

    # updates currently existing prof in the database
    def edit(self, dbCursor):
        # to be added

    # deletes prof from the database
    def delete(self, dbCursor):
        # to be added

    # calculates prof's salary
    def calculateSalary(self):
        # to be added

class Thesis():
    # thesisDetails is a dict() where keys are names of the columns in the table
    def __init__(self, thesisDetails):
        self.profId = thesisDetails['profId']
        self.studentFirstName = thesisDetails['studentFirstName']
        self.studentLastName = thesisDetails['studentLastName']
        self.studentId = thesisDetails['studentId']
        self.id = thesisDetails['id']
        self.title = thesisDetails['title']
        self.status = thesisDetails['status']
        self.grade = thesisDetails['grade']

    # addes thesis to the database
    def add(self, dbCursor):
        # to be added

    # edits currently existing thesis in the database
    def edit(self, dbCursor):
        # to be added

    # deletes thesis from the database
    def delete(self, dbCursor):
        # to be added
