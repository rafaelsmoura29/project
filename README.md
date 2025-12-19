# Tutorial Cosima Docker
Primeiro é necessário clonar o repositório cosima disponivel no GitHub
'''bash
git clone https://github.com/OFFIS-DAI/cosima
'''
Para confirmar que o reposiório foi clonado, dê um
'''bash
ls
'''
e deve aparecer a pasta cosima.
Após isso é necessário criar um ambiente virtual antes de gerar a imagem docker,
'''bash
python -m venv venv
source venv/bin/activate
'''
Com isso seu ambiente virtual de nome 'venv' estará criado e ativo.
Para criar a imagem docker você deve entrar na pasta cosima e executar o comando:
'''bash
docker build -t cosima_i .
'''
Vale ressaltar caso esteja utilizando o WSL ou WSL2 para rodar o sistema Linux é necessário que abra o Docker Desktop para ele ficar rodando, caso o contrário aparecerá error.
Após finalizar o build da imagem agora é hora de entrar no container com o comando:
'''bash
docker run -it --name cosima_c cosima_i /bin/bash
'''
Com isso basta colocar o que deseja simular no centro do conteiner, o cosima possui 3 arquivos de tutorial e vamos testar o 01, para trazer o arquivo para o centro basta copiar:
'''bash
cp ~/models/cosima_core/scenarios/tutorial/01_simulators_and_connection_to_omnet.py .
'''
Por fim, basta executar o tutorial com
'''bash
python3 01_simulators_and_connection_to_omnet.py
'''
Com isso o cosima estará atuando com sucesso com mosaik e omnetpp, caso apareça um errro de NotFound no fim basta fazer o seguinte:
'''bash
mkdir -p ../results
sudo apt-get update
sudo apt-get install psmisc
'''
