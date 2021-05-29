# flask-server-profiler
This sample code helps to profile python flask server activities

## Sample Flask App
app.py is a sample flask app that will be used to demonstrate the profiling task. 

## Dependencies
You need to install Flask(https://pypi.org/project/Flask/)

To profile a request you need to add these two lines prior to app.run
```
  app.config['PROFILE'] = True
  app.config["DEBUG"] = True
  app.wsgi_app = ProfilerMiddleware(app.wsgi_app, profile_dir=".")
```
You can see the configurations here: https://werkzeug.palletsprojects.com/en/1.0.x/middleware/profiler/

profile_dir="." saves the \*.prof files to the same location as the directory you are running the code from. 

-Run the Flask app.
-Send a request from the browser or Postman. 
  http://127.0.0.1:5000/test
- Now you should be able to see the .prof file created 

The console will show an output like below with time.
  ```
  PATH: '/test'
           645 function calls (635 primitive calls) in 0.001 seconds

     Ordered by: internal time, call count

     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
         24    0.000    0.000    0.000    0.000 /home/user/.local/lib/python3.7/site-packages/werkzeug/local.py:162(top)
```
You can see the time spent on all the functions calls here. You can also change the order of the results by changing the configuration.
Also each request will be saved to a .prof file in the same directory.

## Visualize the profiling
You can use snakeviz for this.
- Install snakeviz with
  ```
  pip install snakeviz
```
- Run snakeviz in the directory same as the .prof files
  ```
  snakeviz .
```
- Click the link on the console and open it in a browser. 
- You can click on a file and see the profiling details for that. 
