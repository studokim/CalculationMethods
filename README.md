# Calculation Methods

St. Petersburg State University, Mathematics and Mechanics.

Homework on the Calculation Methods course in the 6th semester.

## Installation guide

### Dependencies

- python
- pip

### Building the project

```bash
git clone https://github.com/studokim/CalculationMethods.git
cd CalculationMethods
python -m venv venv
source ./venv/bin/activate
pip install django numpy sympy scipy matplotlib
pip install -e .
```

### Launching the web-app

Assign any value to `SECRET_KEY` in the `webapp/settings.py`.

```bash
cd src/webapp
python manage.py runserver <ip>:<port>
```

Then navigate in browser to `http://<ip>:<port>/`.
