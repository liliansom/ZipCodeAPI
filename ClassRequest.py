import pip._vendor.requests


# Class for the consume of ZipCode API
class Request:
    def __init__(self):
        self.cep = self.inputcep()
        self.link = f'https://viacep.com.br/ws/{self.cep}/json/'
        self.response = self.request()
        self.print_result = self.print_result()
     
    # Method to enter the ZipCode
    def inputcep(self):
        cep = int(input('Digite seu CEP: '))
        return cep
    
    # Method for requesting data from the API
    def request(self):
        response = pip._vendor.requests.get(self.link)
        dic_response = response.json()
        self.state = dic_response['uf']
        self.city = dic_response['localidade']
        self.road = dic_response['logradouro']
        self.nh = dic_response['bairro']
        self.address = (self.road, self.nh, self.city, self.state)
        return self.address
    
    # Method for presenting the requested data
    def print_result(self):
        print(self.address)
        return

    
