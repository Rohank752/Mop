const express = require('express')
var bodyParser = require("body-parser");
const app = express()
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
var connected = false

const mqtt = require('mqtt')
// const client = mqtt.connect('mqtt://localhost:1883',{'username':'rohan','password':'root123'})

const port = 3000

app.post('/', (req, res) => {
    client = mqtt.connect('mqtt://localhost:1883',{'username':'rohan','password':'root123'})
    client.on('connect', function() { // When connected
        console.log('connected');
    
        // publish a message to a topic
        client.publish('update/test', JSON.stringify(req.body), function() {
            console.log("Message is published");
            client.end(); // Close the connection when published
        });
    });

    res.send(req.body)
})

app.listen(port, () => console.log(`app listening on port ${port}!`))
