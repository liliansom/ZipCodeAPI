import pip._vendor.requests

class Request:
    def __init__(self):
        self.cep = self.inputcep()
        self.link = f'https://viacep.com.br/ws/{self.cep}/json/'
        self.response = self.request()
        self.print_result = self.print_result()
        
    def inputcep(self):
        cep = int(input('Digite seu CEP: '))
        return cep
    
    def request(self):
        response = pip._vendor.requests.get(self.link)
        dic_response = response.json()
        self.state = dic_response['uf']
        self.city = dic_response['localidade']
        self.road = dic_response['logradouro']
        self.nh = dic_response['bairro']
        self.address = (self.state, self.city, self.road, self.nh)
        return self.address
    
    def print_result(self):
        print(self.address)
        return

    
