import CSVTable
import CSVCatalog
import json
import csv
import time

#Must clear out all tables in CSV Catalog schema before using if there are any present
#Please change the path name to be whatever the path to the CSV files are
#First methods set up metadata!! Very important that all of these be run properly

# Only need to run these if you made the tables already in your CSV Catalog tests
# You will not need to include the output in your submission as executing this is not required
# Implementation is provided
def drop_tables_for_prep():
    cat = CSVCatalog.CSVCatalog()
    cat.drop_table("people")
    cat.drop_table("batting")
    cat.drop_table("appearances")

#drop_tables_for_prep()

# Implementation is provided
# You will need to update these with the correct path
def create_lahman_tables():
    people_columns = ["playerID", "birthYear", "birthMonth", "birthDay", "birthCountry", "birthState", "birthCity",
                	"deathYear", "deathMonth", "deathDay", "deathCountry", "deathState", "deathCity", "nameFirst",
                    "nameLast", "nameGiven", "weight", "height", "bats", "throws", "debut", "finalGame", "retroID", "bbrefID"]
    batting_columns = ["playerID", "yearID", "stint", "teamID", "lgID", "G", "AB", "R", "H", "2B", "3B", "HR", "RBI",
                        "SB", "CS", "BB", "SO", "IBB", "HBP", "SH", "SF", "GIDP"]
    appearances_columns = ["yearID", "teamID", "lgID", "playerID", "G_all", "GS", "G_batting", "G_defense", "G_p", "G_c", 
                        "G_1b", "G_2b", "G_3b", "G_ss", "G_lf", "G_cf", "G_rf", "G_of", "G_dh", "G_ph", "G_pr"]
    cat = CSVCatalog.CSVCatalog()
    cat.create_table("people", "NewPeople.csv", people_columns)
    cat.create_table("batting","NewBatting.csv", batting_columns)
    cat.create_table("appearances", "NewAppearances.csv", appearances_columns)

#create_lahman_tables()

# Note: You can default all column types to text
def update_people_columns():
    # ************************ TO DO ***************************
    table = CSVTable.CSVTable("people")
    print('All columns loaded into table')

#update_people_columns()

def update_appearances_columns():
    # ************************ TO DO ***************************
    table = CSVTable.CSVTable("appearances")
    print('All columns loaded into table')

#update_appearances_columns()

def update_batting_columns():
    # ************************ TO DO ***************************
    table = CSVTable.CSVTable("batting")
    print('All columns loaded into table')

#update_batting_columns()

#Add primary key indexes for people, batting, and appearances in this test
def add_index_definitions():
    # ************************ TO DO ***************************
    table1 = CSVTable.CSVTable("people")
    table1.__description__.define_index("playerID", ["playerID"], "PRIMARY")
    table1.__load__()
    print()

    table2 = CSVTable.CSVTable("batting")
    table2.__description__.define_index("playerID_yearID_teamID", ["playerID", "yearID", "teamID"], "PRIMARY")
    table2.__load__()
    print()

    table3 = CSVTable.CSVTable("appearances")
    table3.__description__.define_index("yearID_teamID_playerID", ["yearID", "teamID", "playerID"], "PRIMARY")
    table3.__load__()

#add_index_definitions()


def test_load_info():
    table = CSVTable.CSVTable("people")
    print(table.__description__.file_name)

#test_load_info()

def test_get_col_names():
    table = CSVTable.CSVTable("people")
    names = table.__get_column_names__()
    print(names)

#test_get_col_names()

def add_other_indexes():
    """
    We want to add indexes for common user stories
    People: nameLast, nameFirst
    Batting: teamID
    Appearances: None that are too important right now
    :return:
    """
    # ************************ TO DO ***************************
    table1 = CSVTable.CSVTable("people")
    table1.__description__.define_index("nameLast_nameFirst", ["nameLast", "nameFirst"], "INDEX")
    table1.__load__()
    print()

    # Ed #570 Use another column
    table2 = CSVTable.CSVTable("batting")
    table2.__description__.define_index("G", ["G"], "INDEX")
    table2.__load__()

#add_other_indexes()

def load_test():
    batting_table = CSVTable.CSVTable("batting")
    print(batting_table)

#load_test()


def dumb_join_test():
    batting_table = CSVTable.CSVTable("batting")
    appearances_table = CSVTable.CSVTable("appearances")
    t1 = time.time()
    result = batting_table.dumb_join(appearances_table, ["playerID", "yearID"], {"playerID": "baxtemi01"},
                                     ["playerID", "yearID", "teamID", "AB", "H", "G_all", "G_batting"])
    t2 = time.time()
    print(result)
    print('Time spent for dumb_join: %fs.'%(t2 - t1))


#dumb_join_test()


def get_access_path_test():
    people_table = CSVTable.CSVTable("people")
    template = ["teamID", "playerID", "yearID"]
    index_result, count = people_table.__get_access_path__(template)
    print(index_result)
    print(count)

#get_access_path_test()

def sub_where_template_test():
    # ************************ TO DO ***************************
    batting_table = CSVTable.CSVTable("batting")
    where_template = {"teamID":"CHN", "playerID":"aardsda01", "food":"chips"}
    sub_template = batting_table.__get_sub_where_template__(where_template)
    print("sub_template is", sub_template)
    print()

    people_table = CSVTable.CSVTable("people")
    where_template = {"birthCity":"Denver", "food":"chips"}
    sub_template = people_table.__get_sub_where_template__(where_template)
    print("sub_template is", sub_template)

#sub_where_template_test()


def test_find_by_template_index():
    # ************************ TO DO ***************************
    batting_table = CSVTable.CSVTable("batting")
    template = {"teamID":"CHN", "playerID":"aardsda01"}
    result_rows = batting_table.__find_by_template__(template, fields=["playerID", "teamID", "lgID"])
    print("result rows are", result_rows)
    print()

    appearances_table = CSVTable.CSVTable("appearances")
    template = {"teamID":"CHN", "G_all":"45"}
    result_rows = appearances_table.__find_by_template__(template, fields=["teamID", "playerID", "G_all"])
    print("result rows are", result_rows)


#test_find_by_template_index()

def smart_join_test():
    # ************************ TO DO ***************************
    batting_table = CSVTable.CSVTable("batting")
    appearances_table = CSVTable.CSVTable("appearances")
    t1 = time.time()
    result = batting_table.__smart_join__(appearances_table, ["playerID", "yearID"], {"playerID": "baxtemi01"},
                                     ["playerID", "yearID", "teamID", "AB", "H", "G_all", "G_batting"])
    t2 = time.time()
    print(result)
    print('Time spent for smart_join: %fs.'%(t2 - t1))

#smart_join_test()
