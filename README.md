# Projeto
Bem vindo ao desafio técnico de dados da FieldPRO!
O objetivo deste desafio é contruir um modelo de calibração de um sensor de chuva baseado em impactos mecânicos, além de realizar o deploy do modelo para consumo via API. 
O sistema de medição de chuva funciona por meio de um piezoelétrico e um acumulador de carga. O impacto das gotas de chuva é acumulado ao longo do tempo e gera uma queda na carga do piezoelétrico (piezo_charge).
As medidas realizadas pelo sensor estão no arquivo 'Sensor_FieldPRO.csv', para comparação, foram utilizadas medidas de uma estação metereológica próxima, que estão no arquivo 'Estacao_Convenvional.csv'.
As medidas do sensor incluem a carga medida no acumulador, a temperatura da placa, o número de resets da placa e as condições atmosféricas do ambiente.
Sugerimos o deploy do modelo na plataforma do google cloud, mas outras plataformas podem ser utilizadas também.
Quaisquer dúvidas podem ser encaminhadas para o email lucas.latyki@neofield.com.br
Boa Sorte!

# Resultado

## Modelo

Desenvolvido no Notebook presente ("desafio_tecnico_fieldpro.ipynb"), utilizando tensorflow

## API

Desenvolvida em Flask para fácil integração com o modelo também escrito em Python

### Deploy
O deploy não foi feito em nenhuma nuvem, porém o setup para deploy foi feito utilizando "gunicorn" em tools/deploy.sh
