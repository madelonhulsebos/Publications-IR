// const data = require('')
// console.log(data)

// Load the SDK and UUID
var AWS = require('aws-sdk')

// Create credentials
AWS.config.update({
    accessKeyId: "",
    secretAccessKey: "",
    "region": "eu-west-1",
})

var dynamodb = new AWS.DynamoDB({apiVersion: '2012-08-10'})