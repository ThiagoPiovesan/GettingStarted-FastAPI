## An introduction to FastAPI Framework

→ This repository is an compile and commented edition from the youtube [videos seris](https://youtube.com/playlist?list=PLstjCH2DwkBnKO9PdHc5NO1JOwbJdcq22).

**FastAPI Website**: https://fastapi.tiangolo.com

---

All of it was made by following the guide of the videos above, but with extra comments and explanations.

#### # Objective

Implement the FastAPI framework from beggining to the advanced, implementing database, middleware, etc.

---

#### # Creating a virtual enviroment (venv) on Windows

Run the following command at the root of the project to create the environment if you haven't created it before:
```
python -m venv fastapi-env
```
Activate the environment with the command if using cmd:
```
fastapi-env\Scripts\activate.bat
```
If you are using PowerShell, activate it with the command below:
```
fastapi-env\Scripts\Activate.ps1
```

#### # Installing the dependencies

Use pip to download project dependencies:
```
pip install -r requirements.txt
```
or 
```
pip3 install -r requirements.txt
```

#### # Execution

To run the project, use the command below in the project root:
```
uvicorn main:app --reload 
```

---

**# Tips:**
→ Don’t use global instances, that way a test can’t interfere on the other.
→ Don’t tests python standard library stuff, it is expected to work correctly.


## Thanks for the read & I hope you enjoy it!

> To get started/contribute (if you want - optional) ...

- **Option 1**
    - 🍴 Fork this repo and pull request!

- **Option 2**
    - 👯 Clone this repo: 
    ```
    $ git clone https://github.com/ThiagoPiovesan/
    ```

- **Enjoy it!**

---

Ass: Thiago Piovesan - 11/2022 -- version: 1.0.0.