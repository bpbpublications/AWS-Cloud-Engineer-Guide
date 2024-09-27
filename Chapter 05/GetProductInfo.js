const AWS = require("aws-sdk");
const dynamodb = new AWS.DynamoDB();
exports.handler = async (event) => {
  const params = {
    TableName: "ProductTable",
    Key: {
      productId: {
        S: event.pathParameters.productId,
      },
    },
  };

  const response = await dynamodb.getItem(params).promise();

  if (!response.Item) {
    throw new Error("Product not found");
  }

  const product = {
    productId: response.Item.productId.S,
    name: response.Item.name.S,
    description: response.Item.description.S,
    price: response.Item.price.N,
  };

  const responseBody = JSON.stringify(product);

  const response = {
    statusCode: 200,
    body: responseBody,
    headers: {
      "Content-Type": "application/json",
    },
  };

  return response;
};