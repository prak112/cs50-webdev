# Background
 - Web applications accept user data in a form and transmit them through the web server for relevant outcome.
 - These transfer can be observed in case of a Google Search, where the url changes based on the search query, for ex. google search query for "cs50 web development" gives the following url :
    
    ```
    https://www.google.com/search?q=cs50+web+development&oq=cs50+web+development&aqs=chrome..
    ```
 - Let's check what we know by dissecting this url
 - `?` seperates the routing url and the query
 - First part of the url before the `?` is  the route -
    ```
    https://www.google.com/search
    ```
 - Next part after `?` consists of the query search parameter `q` and its value `cs50+web+development`

    ```
    ?q=cs50+web+development
    ```
 - Search parameters are seperated by `&` , parameter names and values are seperated by `=`
    ```
    ?q=cs50+web+development&oq=cs50+web+development&aqs=chrome..
    ```
 
 # Aim
 - In this project, we will develop a basic front-end design by :
    1. Exploring Google’s interface to identify what GET parameters it expects 
    2. Adding necessary HTML and CSS to the website


 # Workflow
 - Build on provided resources by CS50 - `index.html`
 - 