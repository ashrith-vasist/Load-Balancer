<h2>Load Balancer Prototype</h2>

<p>
  This is a basic client-server program prototype, designed to handle multiple client requests simultaneously. The server listens for incoming client connections and assigns each client its own dedicated thread for handling communication, ensuring efficient management of concurrent client requests.
</p>

<h3>Key Features:</h3>
<ul>
  <li><strong>Multi-threaded Server:</strong> The server is capable of handling multiple client connections at once, with each client being managed by a separate thread. This allows for parallel processing of client requests.</li>
  <li><strong>Client-Server Communication:</strong> Each client can send messages to the server, and the server can respond in real-time. Both the client and the server maintain a persistent connection until explicitly disconnected.</li>
  <li><strong>Scalable Design:</strong> This prototype serves as the foundation for building more complex applications such as load balancing systems, where multiple servers can handle client requests in a distributed fashion.</li>
</ul>

<p>
  This project provides a clear and simple implementation for managing concurrent client connections in a server environment, making it a solid starting point for learning about multi-threaded networking and load balancing techniques.
</p>
