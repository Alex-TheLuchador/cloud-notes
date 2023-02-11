# URLs and Web Connections

## Universal Resource Locator (URL)

We will use this URL as an example: https://example.com/list/item

URLs are composed of four components:
1. Scheme
    - In our example, HTTPS is the scheme.
    - Tells the browser to connect to the server via HTTPS.
2. Domain
    - Example.com is the domain name.
3. Path
    - This is akin to a directory or folder in a file system.
    - In our example, /list is part of the path to our Resource.
4. Resource
    - This is akin to the file within a directory or folder.
    - In the example, /item is the resource, and the last part of the path.
    - The path for the resource is /list/item.

## How does the browser know which server to connect to?

The Domain Name System (DNS) is how a browser can understand that example.com is the server we expect it to be. It's like a phone book that translates domain names to IP addresses.

Typically, DNS information is cached so the lookup process is much quicker. Without caching, the browser would take extra time to load pages because it has to lookup the IP address through a lookup process:
1. Your browser would check it's own cache first.
2. If the browser can't find the IP, the OS will check its own cache.
3. If the OS can't find the IP address, the browser will look up the IP using a complex process that, in short, results in a DNS server containing the IP address that you need.
4. The correct IP address is cached for later use.

## Connecting a browser to a server

Once a server's IP address is found, the browser will establish a TCP connection with the server. This connection involves a series of "handshakes" that takes a few round trips between the browser and server to complete.

Modern browsers will usually have a "keep alive" connection, which means the browser will try to use an already established TCP connection to the server.

For connections using HTTPS, the process of establishing a connection is more involved when compared to HTTP due to the requirement of the SSL/TLS handshake, which encrypts the connection between the browser and server. To speed things up, browsers may do things like SSL/TLS Session Resumption so you aren't waiting for too long.

## Making a request and getting a response

After making a connection to the web server, the browser sends an HTTP/S request to the server

Once the request is received by the server, it is processed by the server and an HTTP/S response is sent, which contains HTML content for the browser to render. There is also usually extra content sent, like JavaScript files and other packages.