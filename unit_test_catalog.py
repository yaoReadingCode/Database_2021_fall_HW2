import CSVCatalog
import json
import pymysql

def reset_db():
    conn = pymysql.connect(host="tutorialdb.cbezzskgwcl3.us-east-2.rds.amazonaws.com",
            port=3306,
            user="admin",
            password="7Senses_kiki",
            db="CSVCatalog",
            cursorclass=pymysql.cursors.DictCursor)
    
    q = "delete from csvindexes"
    res = CSVCatalog.run_q(conn, q, args=None)
    q = "delete from csvcolumns"
    res = CSVCatalog.run_q(conn, q, args=None)
    q = "delete from csvtables"
    res = CSVCatalog.run_q(conn, q, args=None)

# Example test, you will have to update the connection info
# Implementation Provided
def create_table_test():
    cat = CSVCatalog.CSVCatalog()
    cat.create_table("test_table", "file_path_test.woo")
    t = cat.get_table("test_table")
    print("Table = ", t)

#create_table_test()

def drop_table_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog(
        dbhost="tutorialdb.cbezzskgwcl3.us-east-2.rds.amazonaws.com",
        dbport=3306,
        dbuser="admin",
        dbpw="7Senses_kiki",
        db="CSVCatalog")
    cat.drop_table("test_table")


#drop_table_test()

def add_column_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    t = cat.get_table("test_table")
    col1 = CSVCatalog.ColumnDefinition("test_col1", "text", False)
    col2 = CSVCatalog.ColumnDefinition("test_col2", "text", True)
    col3 = CSVCatalog.ColumnDefinition("test_col3", "number", False)
    t.add_column_definition(col1)
    t.add_column_definition(col2)
    t.add_column_definition(col3)


#add_column_test()

# Implementation Provided
# Fails because no name is given
def column_name_failure_test():
    cat = CSVCatalog.CSVCatalog()
    col = CSVCatalog.ColumnDefinition(None, "text", False)
    t = cat.get_table("test_table")
    t.add_column_definition(col)

#column_name_failure_test()

# Implementation Provided
# Fails because "canary" is not a permitted type
def column_type_failure_test():
    cat = CSVCatalog.CSVCatalog()
    col = CSVCatalog.ColumnDefinition("bird", "canary", False)
    t = cat.get_table("test_table")
    t.add_column_definition(col)

#column_type_failure_test()

# Implementation Provided
# Will fail because "happy" is not a boolean
def column_not_null_failure_test():
    cat = CSVCatalog.CSVCatalog()
    col = CSVCatalog.ColumnDefinition("name", "text", "happy")
    t = cat.get_table("test_table")
    t.add_column_definition(col)

#column_not_null_failure_test()


def add_index_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    t = cat.get_table("test_table")
    t.define_index("test_ind1", ["test_col1"], "INDEX")
    t.define_index("test_ind2", ["test_col2", "test_col3"], "UNIQUE")

#add_index_test()


def col_drop_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    t = cat.get_table("test_table")
    t.drop_column_definition("test_col1")
    t.drop_column_definition("test_col2")
    t.drop_column_definition("test_col3")

#col_drop_test()

def index_drop_test():
    # ************************ TO DO ***************************
    cat = CSVCatalog.CSVCatalog()
    t = cat.get_table("test_table")
    t.drop_index("test_ind1")
    t.drop_index("test_ind2")

#index_drop_test()

# Implementation provided
def describe_table_test():
    cat = CSVCatalog.CSVCatalog()
    t = cat.get_table("test_table")
    desc = t.describe_table()
    print("DESCRIBE People = \n", json.dumps(desc, indent = 2))

#describe_table_test()

