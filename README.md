# Python_React_Blockchain
Python (API's Python Flask), Blockchains, Cryptocurrencies, Web Development (Backend and Frontend), JavaScript, React JS, React Hooks and more.

# Here's an overview of the overall journey:

- Python Fundamentals.
- Begin building the Blockchain Application with Python.
- Test the Application using Pytest.
- Incorporate the crucial concept of Proof of Work into the Blockchain.
- Enhance the application to prepare for networking.
- Create the Blockchain network using Flask and Pub/Sub.
- Integrate the Cryptocurrency, building Wallets, Keys, and Transactions.
- Extend the network implementation with the cryptocurrency.
- Transition from Python to JavaScript with a "From Python to JavaScript".
- Establish frontend web development skills and begin coding with React.js.
- Create the frontend portion for the blockchain portion of the system.
- Complete the frontend by building a UI for the cryptocurrency portion of the system.


# Skills gained:

- How to build a blockchain and cryptocurrency system from scratch.
- Python - data structures, object-oriented programming, modules, and more.
- The ins and outs of hashing and sha256.
- Encoding and decoding in utf-8.
- Testing Python applications with pytest.
- Python virtual environments.
- The concept of proof of work, and how it pertains to mining blocks.
- Conversion between hexadecimal to binary.
- HTTP APIs and requests.
- How to create APIs with Python Flask.
- The publish/subscribe pattern to set up networks.
- When to apply the concepts of serialization and deserialization.
- Public/private keypairs and generating data signatures.
- JavaScript.
- Frontend web development and how web applications are constructed.
- The core concepts of React and React hooks.
- How the React engine works under the hood, and how React applies hooks.
- CORS - and how to get over the CORS error properly.
- How to build a pagination system.

** Create a virtual environment **

- Execute the following command: `python -m venv blockchain-env`

** Activate the virtual environment **

- Execute the following command; `source blockchain-env/bin/activate`

# Install Requirements (install all packages)

- Check what are the requirements/packages inside the requirements.txt file
- Install them (packages) using the command: `pip install -r requirements.txt`

** Run the tests (Make sure to activate the virtual env first) **

- Execute the command: `python -m pytest backend/tests`

** Run the APP **

- Execute the command: `python -m backend.app`

** Run a PEER Instance **

- Execute command: `export PEER=True && python -m backend.app`

** To RUN the frontend pard**

- Execute command: `npm run start`
- P.D. to fetch random jokes remeber to have the server started first: `python -m backend.app`

** SEED the Backend with Data **
- Execute the command: `export SEED_DATA=True && python -m backend.app`




