# BU Pay

## How to Install and Run
1. first create a virtual environment (optional)
2. Run <code>pip install -r requirements.txt</code>
3. You will need to create a file called <code>.env</code>
4. Run <code>python -m app</code>


## Creating a Virtual environment
1. First download and install python
2. run <code>python -m pip install venv</code> or <code>python -m pip install virtualenv</code>
3. run <code>python -m venv env</code> or <code>python -m virtualenv env</code>
4. if you use Windows, just run the activate.bat file in env/bin
5. if you use Linux, In the terminal, run <code>source env/bin/activate</code>

## Things to be in the .env file
1. <code>PAYSTACK_SECRET</code>
2. <code>DATABASE_URI</code>
See sample_env for a better understanding of it's format

## Supported Databases
1. MySQL
2. Postgresql
3. Sqlite