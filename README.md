# Getting Started with EVERPRO

## Frontend

Go to frontend / everpro ,
1. **Install the dependencies:** Run command `npm install`   [ ONE TIME ]
2. **Start Development Server:** Run command `npm start`

This should automatically open in browser, if not\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

**NOTE:** 
1.To download new dependencies: `npm install --save <DEPENDENCY_NAME>`\
2.While contributing, **DO NOT PUSH YOUR BUILD OR NODE MODULES FOLDER**

## Backend

Go to backend / everpro ,
**NOTE:** First start a virtual environment
1. **Install the dependencies:** Run command `pip install -r requirements.txt`
2. **Start Development Server:** Run command `python manage.py runserver`

Open [http://localhost:8000](http://localhost:8000) to view it in the browser.

The page will reload if you make edits and **save**.\
You will also see any lint errors in the console.

### Using React UI in django

Everytime you make changes in React code, make sure you run `npm run build` to update the build folder,\
which is set as default React UI path in django settings.
**NOTE:** It correctly bundles React in production mode and optimizes the build for the best performance.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

