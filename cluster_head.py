import random
from node import Node

class Cluster_head:
    def __init__(self):
        self.service_map = {}
        self.no_of_services_allocated = []
        self.nodes = []
        self.no_of_nodes = 0
        self.service_limit = 0

    def describe(self):
        result = {
            "service_map": self.service_map,
            "no_of_services_allocated": self.no_of_services_allocated,
            "nodes": self.nodes,
            "no_of_nodes": self.no_of_nodes,
            "service_limit": self.service_limit
        }
        return result

    def make_nodes(self):
        no_of_nodes = random.randint(4,10)
        self.no_of_nodes = no_of_nodes
        result = []
        for i in range(no_of_nodes):
            id = i
            execution_coefficient = 0.5 + 0.5*random.random()
            response_time = 2 + 10*random.random()
            cloud_bandwidth = 0.5 + 0.5*random.random()
            security_protocol = random.randint(1,3)
            power_consumption_per_time = random.randint(1,3)
            service_limit = random.randint(2,7)
            new_node = Node(id, execution_coefficient, response_time, cloud_bandwidth, security_protocol, power_consumption_per_time, service_limit)
            self.nodes.append((new_node, service_limit))
            self.service_limit += service_limit
            result.append(new_node.get_node_parameters())
        self.no_of_services_allocated = [0]*no_of_nodes
        return result
        
    def setup_service(self, services, payloads, policy="random"):
        self.service_map = {}
        self.no_of_services_allocated = [0]*self.no_of_nodes
        if policy=="random":
            for i in range(len(services)):
                service = services[i]
                if_alloted = False
                while not if_alloted:
                    candidate = random.randint(0, self.no_of_nodes-1)
                    if self.no_of_services_allocated[candidate] == self.nodes[candidate][1]:
                        continue
                    self.service_map[service] = candidate
                    self.no_of_services_allocated[candidate] += 1 
                    if_alloted = True
        else:
            # my algo
            # services come in order of preference
            for i in range(len(services)):
                service = services[i]
                payload = payloads[i]
                
                # execute with payload in the available nodes
                # calculate score and assign the node with lowest score
                candidate = -1,
                candidate_result = 999999999
                for i in range(self.no_of_nodes):
                    if self.no_of_services_allocated[i] == self.nodes[i][1]:
                        continue
                    result = self.execute_candidate(i, payload)[payload[3]]
                    if candidate_result > result:
                        candidate = i
                        candidate_result = result
                self.service_map[service] = candidate
                self.no_of_services_allocated[candidate] += 1             

    def execute(self, services, payloads):
        total_response_time = 0
        total_execution_time = 0
        total_network_op_time = 0
        total_power_consumed = 0
        for i in range(len(services)):
            service = services[i]
            payload = payloads[i]
            node = self.nodes[self.service_map[service]][0]
            result = node.execute(payload[0], payload[1], payload[2])
            total_response_time += result[0]
            total_execution_time += result[1]
            total_network_op_time += result[2]
            total_power_consumed += result[3]
        average_response_time = total_response_time/len(services)
        average_execution_time = total_execution_time/len(services)
        average_network_op_time = total_network_op_time/len(services)
        average_power_consumed = total_power_consumed/len(services)
        return(average_response_time, average_execution_time, average_network_op_time, average_power_consumed)        

    def execute_candidate(self, candidate, payload):
        node = self.nodes[candidate][0]
        result = node.execute(payload[0], payload[1], payload[2])
        return result