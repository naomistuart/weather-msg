# :sunny: weather-msg
The goal of this project is to build an [AWS Lambda function](https://aws.amazon.com/lambda/) which sends a SMS message every morning to a user's phone, summarising today's weather forecast.


## Features
- AWS Lambda function automatically triggered every morning at 7:30 am to send a short SMS message
- SMS message summarises the latest weather forecast for Sydney, including maximum temperature, chance of rain, and time period when sun protection is recommended.


## Built with
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Python library used to scrap the Bureau of Meteorology's web page for Sydney weather
- [Twilio](https://www.twilio.com/) - API used to send SMS messages
- [AWS Lambda](https://aws.amazon.com/lambda/) - Used to automatically execute Python code every morning.


## Method
A brief description of the steps in this project:

### 1. Web scraping
- Use Python's [Requests](https://pypi.org/project/requests/) library to grab HTML content from the [Sydney Forecast webpage](http://www.bom.gov.au/nsw/forecasts/sydney.shtml)
- Use [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse the HTML content and pull out relevant information, including today's weather description, maximum temperature, chance of rain, and sun protection recommendations.

### 2. Use Twilio to send SMS
- Format the scraped data into a tidy text string, to be used in the body of the SMS message
- Send the SMS message using [Twilio's Python helper library](https://www.twilio.com/docs/sms/quickstart/python).

### 3. Build AWS Lambda function
- Combine the code from steps 1-2 into a function
- Create a zip archive of library dependencies, together with the function code
- [Upload the deployment package](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html) to AWS Lambda
- Schedule the AWS Lambda function to run every morning, by using a [cron expression](https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html) in a [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html) trigger.


## References
- https://towardsdatascience.com/make-data-acquisition-easy-with-aws-lambda-python-in-12-steps-33fe201d1bb4 
- https://docs.aws.amazon.com/en_pv/lambda/latest/dg/python-programming-model.html