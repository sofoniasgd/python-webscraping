### Install and activate a Python virtual environment for this project,

1. Open your terminal or command prompt.
2. From your terminal, navigate to this directory and run:  
`python -m venv myenv`
Replace `myenv` with the desired name for your virtual environment.
3. Once the virtual environment is created, activate it by running:  

    - For Windows:
`myenv\Scripts\activate`
    - For macOS and Linux:
`source myenv/bin/activate`  
4. run the `deactivate` command to deactivate enviroment.
### To install dependencies using pip:

1. Make sure your virtual environment is activated. If not, refer to the previous instructions on how to activate it.
2. Navigate to the directory where your `requirements.txt` file is located.
3. Run the following command to install the dependencies listed in the `requirements.txt` file:
    `pip install -r requirements.txt`
    This will automatically install all the required packages specified in the `requirements.txt` file.
4. Wait for the installation process to complete. Once finished, you will have all the necessary dependencies installed in your virtual environment.
