## Preparation (for ML Engineer candidates)
We will be utilizing a PostgreSQL 11 server for storing and retrieving data and Docker for hosting it. To do this, first install Docker: https://docs.docker.com/. 

Once installed, run the following commands in your terminal:
1. To run the server:
`docker run -d --name ht_pg_server -v ht_dbdata:/var/lib/postgresql/data -p 54320:5432 postgres:11`
2. Check the logs to see if it is running:
`docker logs -f ht_pg_server`
3. Create the database:
`docker exec -it ht_pg_server psql -U postgres -c "create database ht_db"`

## Interacting with the DB
Throughout the home task you will be required to utilize the DB for storing and retrieving data. If you are unfamiliar with PostgreSQL, below are some examples:

```
import psycopg2
connection = psycopg2.connect(
    host='localhost',
    port=54320,
    dbname='ht_db',
    user='postgres',
)

def create_table(name: str, connection: psycopg2.extensions.connection):
	c = connection.cursor()
    schema = """ts timestamp without time zone,
    			base_ccy varchar(3),
    			ccy varchar(10),
    			rate double precision,
    			PRIMARY KEY (ts, base_ccy, ccy)"""
    ddl = f"""CREATE TABLE IF NOT EXISTS {name} ({schema})"""
	c.execute(ddl)
    connection.commit()
	c.close()

# normal
def insert_values(connection: psycopg2.extensions.connection):
	c = conn.cursor()
	c.execute(“INSERT INTO demo (id, data) VALUES (%s, %s)", (1, "hello");”)
	c.commit()
	c.close()

# bulk
def insert_values(connection: psycopg2.extensions.connection):
	c = conn.cursor()
	source = '/home/aubrey/users.csv'
	table_name = 'users'
	with open(source, 'r') as f:
		next(f) # to skip header
		cur.copy_expert(f"COPY {table_name} FROM STDIN CSV NULL AS ''", f)
	connection.commit()
	c.close()

def get_values(connection: psycopg2.extensions.connection):
	c.execute("SELECT * FROM demo;")
	result = cur.fetchone()
	print(result)
	c.close()

connection.close()
```

## Data
1. countries.csv
	- a table with all alpha-numeric representations of countries. You may need to use this to standardise country codes to one format
2. fraudsters.csv
	- this just holds a list of IDs of users who have been identified as fraudsters for this problem
	- there are others in the users table who are fraudsters, the challenge is to identify them as well
3. users.csv
	- a table of user data
	- **kyc** column indicates the status of the user's identity verification process
	- **terms_version** column indiciates the user's current version of the Revolut app
	- **state**
		LOCKED - the user's account is locked and they cannot perform any transactions. If there are transactions for this user, they occurred before the user was LOCKED.

4. transactions.csv
	- all transactions conducted by users
	- **amount** and **amount_usd** is denominated in integers at the lowest unit. e.g. 5000 USD => 50 USD (because the lowest unit in USD is a cent, w/ 100 cents = 1 dollar)
	- **entry_method** is only relevant for card transactions (CARD_PAYMENT, ATM); you may ignore it for other transactions. The values are:
		misc - unknown
		chip - chip on card
		mags - magstripe on card
		manu - manual entry of card details
		cont - contactless/tap 
		mcon - special case of magstripe & contactless
	- **source** is associated with an external party we use for handling this type of transaction. (e.g. all {CARD_PAYMENT, ATM} use GAIA)
	- **type**
		P2P - sending money internally through the Revolut platform (e.g. send money without bank account)
		BANK_TRANSFER - sending money externally to a bank account
		ATM - withdrawing money from an ATM. Revolut does not support ATM deposits at the moment

	- **state** 
		COMPLETED - the transaction was completed and the user's balance was changed
		DECLINED/FAILED - the transaction was declined for some reason, usually pertains to insufficient balance 
		REVERTED - the associated transaction was completed first but was then rolled back later in time potentially due to customer reaching out to Revolut

5. currency_details.csv
	- a table with iso codes and exponents for currencies
	- **exponent** column can be used to convert the integer amounts in the transactions table into cash amounts. (e.g for 5000 GBP, exponent = 2, so we apply: 5000/(10^2) = 50 GBP)


## Hints & Tips
1. Engineering practice is a strong component of ML Engineer role. Anything you include in the `code/` sub-directory should be nearly production grade.
2. Presentation, creativity and the ability to dive deep into the problem space is a strong component of the Data Scientist role. Your presentation should be one you could comfortably present to a team technical and non-technical employees.
3. Communicating your thought process is also important, we care a lot about the auditability & reproducibility of research/analysis for both Scientists and Engineers. 


## Task

Challenge - ML Engineer - FinCrime

Congratulations for making it to the Challenge stage of the application process! The goal of this task is to objectively assess your technical prowess and your ability to solve problems using machine learning. Please note that the topic, data and problem set are reflective of cases we solved in the past.

Deadline: 7 Days

Topic:	Catching Fraud

Deliverable: REQUIRED

Your submission should be in a .zip file with contents grouped into the following sub-directories (you may omit empty directories):
    • data (only include new data files, exclude raw data)
    • notebooks (include .html version of notebook)
    • artifacts
    • code
    • misc

Please label the .zip file: <your_first_name>_<your_last_name>_ht.zip. 
For example: aubrey_graham_ht.zip.

Before proceeding to the task, please go through the README.md file and complete all steps included in the preparation section, don’t worry these aren’t questions, they are just steps to set up your environment. We have also included additional information and tips to help you!


The Task:

PART I - DATABASES

Write an ETL script in Python to load the data into the PostgreSQL database. The associated DDL should be executed through Python and not directly in SQL. You can find the desired schema in schema.yaml and some sample code for the ETL (the sample code is below passing grade).






PART II - EXPLORATION, ANALYSIS, MODELLING & OPERATIONALIZATION

The fraudsters table indicates some individuals who have been marked as fraudsters. The goal is to use the data and your knowledge of Revolut to design an ML algorithm to identify fraudsters and conduct necessary actions. You should be considering the consequential impact of the model and its decisions on all domains (e.g. customers, revolut brand, internal processes, etc.).

Unless explicitly stated, you do not have the read/write the data from/to the PostgreSQL database. Instead you may just utilize read_csv() methods in Pandas/Dask/anything else.

    a) Explore the data for identified fraudsters and other users. What are your preliminary observations? 

    b) Feature Engineering
        i) Utilizing your findings from part a) and some creativity, create some features. Explain your reasoning behind the features.
        ii) Make a features.py script which when executed will create these features and store them in the DB. 

    c) Model Selection/Validation
        i) Create an ML model which identifies fraudsters. Assess the quality of your model and explain.
        ii) Make a train.py file which generates the fitted model artifact (it should be stored under the artifacts sub-directory).

    d) Operationalization
        i) How will you utilize this model to catch fraudsters? If a fraudster is identified, what should be the resulting action: LOCK_USER, ALERT_AGENT, or BOTH? Explain.
        ii) Make a patrol.py file and write a simple function which implements your logic from above. The function should accept a user_id and yield the suggested action(s) (e.g. patrol(user_id) = [‘LOCK_USER’, ‘ALERT_AGENT’])

LOCK_USER - Current transaction is blocked and user’s account is LOCKED. This prevents the user from performing any transactions with their Revolut account. Access can only be restored after contacting an agent.

ALERT_AGENT - Current transaction is not blocked. An alert is sent to a transaction monitoring agent for further review.





Guidelines:

    1. You should submit at least one Jupyter notebook to outline your exploration, analysis and logic
    2. Code should be clean, commented and production grade
    3. Assumptions can be made but should be stated and backed up with data where possible
    4. Visualizations should be insightful and relevant

 Good luck!