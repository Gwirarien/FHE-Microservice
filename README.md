# FHE-Microservice

## Usage 

1. Make sure you have all the libraries needed to run the app 

(Optional) Choose between the local or the already deployed server - default deployed.
If you choose the local server, open the server service
from the main folder
```bash
cd server
python run.py
```

2. Open the client service
from the main folder
```bash
cd client
python run.py
```

4. Browse to 127.0.0.1:5000 to see the app in action.
By default, the app will access the postgres database deployed on Heroku. (The default user is admin@admin.com:admin)
