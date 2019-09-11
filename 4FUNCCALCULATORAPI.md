## Four function calculator API

Write a Flask application that serves four api endpoints

```
http://127.0.0.1:5000/api/add/n1/n2
http://127.0.0.1:5000/api/subtract/n1/n2
http://127.0.0.1:5000/api/multiply/n1/n2
http://127.0.0.1:5000/api/divide/n1/n2
```

where in each case, n1 and n2 are two integers

that return a json response of the form

```
{
    "answer": 300
}
```

so, for instance, running this command while the Flask development server is
running:

```
curl http://127.0.0.1:5000/api/multiply/7/10
```

would give the response

```
{
    "answer": 70
}
```

