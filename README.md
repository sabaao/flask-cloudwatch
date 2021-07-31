# flask-cloudwatch

# Query log by cli
```
aws logs get-log-events --log-group-name watchtower --log-stream-name loggable | jq '.events[].message'
aws logs get-log-events --log-group-name watchtower --log-stream-name werkzeug | jq '.events[].message'
```

# Reference 
https://watchtower.readthedocs.io/en/latest/