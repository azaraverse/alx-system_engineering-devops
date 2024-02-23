# Single Server Design
- The server *(Linux Server: 8.8.8.8)* is the physical or virtual machine that hosts and serves the website `www.foobar.com`. It runs the necessary software stacks, including the web server, application server and database.

- The *domain name* serves as a human-readable address for the website. It allows the user to access the site using a memorable name instead of an IP address.

- The *`www` in `www.foobar.com`* is a subdomain, and is typically associated with a CNAME (Canonical Name) DNS Record that points to the main domain (foobar.com) or directly to the server's IP address.

- The *web server (Nginx)* handles incoming HTTP(S) requests from a user's browser and serves static content.

- The *application server* executes `foobar.com`'s codebase (e.g, HTML, CSS, Python) and generates dynamic content based on a user's request. It also interacts with the database to retrieve and store data.

- The *database (MySQL)* stores and manages the website's data, including user information, content, and configurations. It allows for a data organisation and accessibilty in an efficient mannner.

- The *server* communicates with the user's computer over the internet using HTTP(S) (Hypertext Transfer Protocol (Secure)).

# Issues with this infrastructure
- Single Point of Failure (SOFP): Since all components are hosted on a single server, any failure in hardware, software, or network connectivity could lead to downtime for the entire website.

- Downtime during maintenance: Any maintenance tasks, such as deploying new code or updating software, would require taking the website offline temporarily.

- Limited scalabilty: With only one *server*, the infrastructure cannot easily handle a significant increase in traffic. Scaling require upgrading hardware or migrating to a more scalable architecture, which can be time-consuming.
