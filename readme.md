To test open a new terminal on your PC and type:
```
curl  http://127.0.0.1:5000/
```
sleep endpoint: This will sleep 2s and then return "Hello, World + 2s!"
```
curl  http://127.0.0.1:5000/sleep
```

fail endpoint: This will fail and return "Internal Server Error"
```
curl  http://127.0.0.1:5000/fail
```