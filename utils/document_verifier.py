# simulacao de verificacao de documentos com ia
def verify_document(document_path, cpf):
    # em uma implementação real, isso chamaria um serviço de verificação de documentos
    # como Azure Face API, AWS Rekognition, ou solução similar
    
    # sempre retorna verdadeiro para fins de demonstração
    return {
        'verified': True,
        'confidence': 0.95,
        'message': 'Documento verificado com sucesso'
    }