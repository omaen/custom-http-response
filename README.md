# custom-http-response
Container image running Flask with customizable output text and background color for infrastructure testing,

## Default environment variables
```
TEXT_OUTPUT="Hello, World!"
TEXT_COLOR="black"
BACKGROUND_COLOR="white"
```

## Usage
```
docker run -p 5000:5000 -e TEXT_OUTPUT="Custom text" -e TEXT_COLOR="yellow" -e BACKGROUND_COLOR="blue" ghcr.io/omaen/custom-http-response:main
```