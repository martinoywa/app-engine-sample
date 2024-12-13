# app-engine-sample

### Installation Steps
Includes both Unix-based and Windows (Didn't work on my Windows thought. If it works for you please ping on Slack).

https://cloud.google.com/appengine/docs/standard/tools/local-devserver-command?tab=python

### Local Dev Server Help Menu (Ubuntu/Mac)
```
python ~/google-cloud-sdk/bin/dev_appserver.py -h
```

### Run Application (Ubuntu/Mac)
Make sure your application is a Flask App. Check `main.py` Regular prints didn't work.
```
python ~/google-cloud-sdk/bin/dev_appserver.py --python_virtualenv_path venvs app.yaml
```

### Install Additional Packages (Ubuntu/Mac)
```
. venvs/default/bin/activate
pip install -r requiremenst.txt
```

### URL
```
http://localhost:61082
``` 
Notes:
1. Update the PORT to whichever the its listening from. (This line in your terminal `Listening at:`)
2. You can change the behaviour here https://cloud.google.com/appengine/docs/standard/tools/using-local-server?tab=python#running_the_local_development_server.
