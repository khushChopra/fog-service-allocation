class Node:
    def __init__(self, id, execution_coefficient, response_time, cloud_bandwidth, security_protocol, power_consumption_per_time, service_limit):
        self.id = id
        self.execution_coefficient = execution_coefficient
        self.response_time = response_time
        self.cloud_bandwidth = cloud_bandwidth
        self.security_protocol = security_protocol
        self.power_consumption_per_time = power_consumption_per_time
        self.service_limit = service_limit

    def execute(self, data_to_process, processing_effort_coefficient, cloud_upload_download):
        execution_time = self.execution_coefficient*data_to_process*processing_effort_coefficient
        network_op_time = self.cloud_bandwidth*cloud_upload_download
        response_time = self.response_time + network_op_time + execution_time
        sec_protocol = self.security_protocol
        power_consumed = self.power_consumption_per_time*(execution_time)
        return (response_time, execution_time, network_op_time, power_consumed, sec_protocol)

    def get_service_limit(self):
        return self.service_limit

    def get_node_parameters(self):
        result = "id = "+str(self.id)+ " exec_coeff = " + str(self.execution_coefficient) \
            + " response_time = " + str(self.response_time) \
            + " cloud_bandwidth = " + str(self.cloud_bandwidth) \
            + " security_protocol = " + str(self.security_protocol) \
            + " power_consumption_per_time = " + str(self.power_consumption_per_time) \
            + " service_limit = " + str(self.service_limit) 
            
        return result