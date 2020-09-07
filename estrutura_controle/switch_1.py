def get_tipo_dia(dia):
    dia_semana = {
        1:'Fim de Semana',
        2:'Dia de Semana',
        3:'Dia de Semana',
        4:'Dia de Semana',
        5:'Dia de Semana',
        6:'Dia de Semana',
        7:'Fim de Semana',        
    }

    return dia_semana.get(dia,'***Invalido*')


if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia}: {get_tipo_dia(dia)}')