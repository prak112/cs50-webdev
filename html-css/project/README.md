# Project - MyGoogle
***Front-End design as a project for learning HTML and CSS concepts***

</br>

## Background
Source : [CS50 project0 documentation](https://cs50.harvard.edu/web/2020/projects/0/search/)

 - Web applications accept user data in a form and transmit them through the web server for relevant outcome.
 - These transfer can be observed in case of a Google Search, where the url changes based on the search query, for ex. google search query for "cs50 web development" gives the following url :
    
    ```
    https://www.google.com/search?q=cs50+web+development&oq=cs50+web+development&aqs=chrome..
    ```
 - Let's start by dissecting this url
 - `?` seperates the routing url and the Query String
 - First part of the url before the `?` is  the route -
    ```
    https://www.google.com/search
    ```
 - Next part after `?` is called the Query String. It's general syntax is :
   ```
   field1=value1&field2=value2....
   ```
 - In our example, Query String consists of the query search parameter `q` and its value `cs50+web+development`

    ```
    ?q=cs50+web+development
    ```
 - Search parameters are seperated by `&` , parameter names and values are seperated by `=`
    ```
    ?q=cs50+web+development&oq=cs50+web+development&aqs=chrome..
    ```
 
## Aim
 - In this project, we will develop a basic front-end design by :
    1. Exploring Google’s interface to identify what GET parameters it expects 
    2. Adding necessary HTML and CSS to the website


## Workflow
 - Build on provided resources by CS50 - `index.html`
 - 