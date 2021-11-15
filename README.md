# GraphiQL Explorer

This tool allows you to explore any GraphQL API, like it also uses Graph*i*QL. This is very useful for security testing an API from the outside.

This means you'll be able to use the code completion and documentation visualization features of GraphiQL.

Sometimes GraphQL APIs also don't allow introspection, but using tools like [clairvoyance](https://github.com/nikitastupin/clairvoyance) you can brute-force some of the fields. With this tool you can also import the results of these tools by simply selecting a file to take the introspection from.

## Setup Browser

To setup your browser to allow requesting resources cross-origin you can look at the `/help/1` and `/help/2` pages.

## Usage

After allowing the browser to bypass CORS you can use the explorer to explore your GraphQL API. Start by inputting a URL in the field, and then execute any queries to the endpoint you want.
If you want to want to use a custom introspection file, you can select the option `Use custom introspection data from file` and then select the file you want to use.
