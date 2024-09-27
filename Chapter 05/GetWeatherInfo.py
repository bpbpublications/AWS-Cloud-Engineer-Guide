import json
import requests def lambda_handler(event, context):
    print("Received event:", json.dumps(event))  
    try:
        # Extract location from query parameters
        location = event['queryStringParameters'].
get('location')
                if not location:             return {
                'statusCode': 400,
                'body': json.
dumps('Missing required query parameter: location')
            }
            # Make a request to a thirdparty weather API (replace with actual API endpoint)
        api_key = 'YOUR_API_KEY'  # Replace with your actual API key
        weather_api_url = f'https://api.weatherapi.com/v1/ current.json?key={api_key}&q={location}'
                response = requests.get(weather_api_url)
        weather_data = response.json()
                # Process and return the weather information
        return {
            'statusCode': 200,
            'body': json.dumps(weather_data),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'An error occurred: {str(e)}'),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
