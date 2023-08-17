[
    {
        '$lookup': {
            'from': 'Montadoras', 
            'localField': 'Montadora', 
            'foreignField': 'Montadora', 
            'as': 'Montadora_info'
        }
    }, {
        '$unwind': {
            'path': '$Montadora_info', 
            'preserveNullAndEmptyArrays': True
        }
    }, {
        '$project': {
            '_id': 1, 
            'Carro': 1, 
            'Cor': 1, 
            'Montadora': 1, 
            'Pais': '$Montadora_info.Pais'
        }
    }, {
        '$group': {
            '_id': '$Pais', 
            'Carros': {
                '$push': {
                    'Carro': '$Carro', 
                    'Cor': '$Cor', 
                    'Montadora': '$Montadora'
                }
            }
        }
    }
]