# Distributed Web Infrastructure

<a href="https://github.com/gitloper-azara/alx-system_engineering-devops/blob/d9e16d898eabc45d8897042beedb57321d348f73/0x09-web_infrastructure_design/1-distributed_web_infrastructure.jpg" target="_blank" img src="https://github.com/gitloper-azara/alx-system_engineering-devops/blob/d9e16d898eabc45d8897042beedb57321d348f73/0x09-web_infrastructure_design/1-distributed_web_infrastructure.jpg"></a>

# Additional Elements
- __Servers__: The additional *servers* provide redundancy and scalability, ensuring that the website remains available even if one server fails.

- __Load Balancer__: The *load balancer* distributes incoming traffic across the various servers to prevent any single server from becoming overwhelmed with requests.

    - ## Setup
    HAproxy will distribute incoming traffic across multiple servers to ensure load balancing and high availability.

    HAproxy will be configured with round-robin distribution algorithm so that each new request will be routed by the algorithm to the next server in line, distributing the load evenly among all available servers.

    The HAproxy load balancer enables an *Active-Active* setup, where all servers handle incoming requests. This setup ensures better utilisation of resourses and improved performance compared to an *Active-Passive* setup.

- __Database Primary-Replica(Master-Salve) Cluster__: The primary node handles all write operations, while the Replica node replicates data from the Primary node and handles read operations. The primary node will be responsible for receiving all write requests from the application server, ensuring data consistency, whereas the Replica node assists in scaling read operations, improving performance by distributing read queries across multiple nodes.

# Issues with this Infrastructure
- Single Points of Failure (SPOF): The infastructure still has SPOFs, particulary in the load balancer and database. If either fails, it could disrupt the availability of the website.

- Security: The lack of firewall and HTTPS implementation exposes the infrastructure to risks, including unauthorised access, data breaches, and man-in-the-middle attacks.

- No Monitoring: Without monitoring tools in place, it is challenging to detect and address some performance issues, security threats, and other problems proactively.
