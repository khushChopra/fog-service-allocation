Nodes -
    they return values given some task,
    they have a service capacity and can only run services.
    these values have execution time, upload/download time, response time, power consumption and security.

Cluster head -
    Manages which services runs where. (by keeping a map)
    (my algo) during setup, it reaches to all nodes and then returns the wos parameters from the nodes. then assignes the node with best score the service. (changes allocation if higher priority task came in)

    (random algo) picks a node at random to do the job.


Evaluation -
    We'll simulate a no. of service calls and graph the following - 
        the no. of services and the average response time per call.
        the no. of services and the average execution time per call.
        the no. of services and power consumption.

service setup call ("abc.com", "1 mb data exec", "data processing coeff", 1 mb upload/download, utility score)

service call will be of like ("abc.com", 1 mb data execution, data_processing coeff,  1 mb upload/download) 