# GraphiQL Explorer

This tool allows you to explore any GraphQL API, like it also uses Graph*i*QL. This is very useful for security testing an API from the outside.

This means you'll be able to use the code completion and documentation visualization features of Graph*i*QL.

Sometimes GraphQL APIs also don't allow introspection, but using tools like [clairvoyance](https://github.com/nikitastupin/clairvoyance) you can brute-force some of the fields. With this tool you can also import the results of these tools by simply selecting a file to take the introspection from.

This application is running on Heroku over at <https://j0r1an-graphiql-explorer.herokuapp.com/>

## Setup Browser

To setup your browser to allow requesting resources cross-origin you can look at the `/help/1` and `/help/2` pages.

## Usage

After allowing the browser to bypass CORS you can use the explorer to explore your GraphQL API. Start by inputting a URL in the field, and then execute any queries to the endpoint you want.
If you want to want to use a custom introspection file, you can select the option `Use custom introspection data from file` and then select the file you want to use.

## Example

As an example, lets try to connect to the Hackerone GraphQL API.

First open the tool with the command to bypass security features:

```cmd
"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --disable-web-security --user-data-dir="%TEMP%\Chrome" https://j0r1an-graphiql-explorer.herokuapp.com/
```

Then input the URL to the GraphQL endpoint you want to test:

![image](https://user-images.githubusercontent.com/26067369/142003992-5b4317f3-baeb-484c-b529-52aeb8effce5.png)

After clicking on the Connect button, you will be connected to the endpoint and should see code completion and an interactive schema on the right:

![image](https://user-images.githubusercontent.com/26067369/142004899-74fd5b99-2bcc-4a4f-b1a0-1ef963eca239.png)

Now you can send any query you want to the endpoint, and see the result on the right. 
