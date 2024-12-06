def transcription_arn(brin_codant):
    arn = ''
    for caractere in brin_codant:
        if caractere == 'T':
            arn += 'U'
        else:
            arn += caractere
    return arn
            
    
print(transcription_arn('AGTCTTACCGATCCAT'))