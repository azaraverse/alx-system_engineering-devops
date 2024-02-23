# Secured and Monitored Web Infrastructure

<a href="https://github.com/gitloper-azara/alx-system_engineering-devops/blob/2874d0f472f10be5c455a005490073d218d24291/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.jpg" target="_blank"><img src="https://github.com/gitloper-azara/alx-system_engineering-devops/blob/2874d0f472f10be5c455a005490073d218d24291/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.jpg"></a>

# Additional Elements
- __Three Servers__: Each additional server will host a copy of the website to distribute the load and improve redundancy.

- __Firewalls__: Each available server will have a firewall to control incoming and outgoing traffic which will enhance security by filtering potentially harmful traffic. The firewalls will block unauthorised access attempts and mitigate potential threats such as DDoS attacks or malware infections.

- __SSL Certificate__: An SSL certificate will be installed on the load balancer to encrypt traffic *(data (usernames, passwords, payment details, etc))* between the user and the server, ensuring data confidentiality.

- __Monitoring Client__: Each server will have a monitoring client installed *(Sumo Logic)* to collect data on system performance, security events, and other relevant metrics.

# Issues
- Terminating SSL at the load balancer level exposes decrypted traffic within the internal network, potentially compromising data security. It is essential that end-to-end encryption is maintained at all time.

- Single MySQL server for all writes introduces a SPOF. If the database server goes down, it could lead to data loss or service interruptions.

- Having servers with identical components (such as database, web server, applictaion server) may lead to a lack of diversity in the infrastructure. If a vulnerability or issue affects one component, it could affect all servers simultaneously, which may in turn, increase the risk of outages on a wide level.
