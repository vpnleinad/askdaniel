from flask import Flask, render_template, request
from dotenv import load_dotenv
import os, openai


load_dotenv()
openai.api_key = "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"
completion = openai.Completion()

start_chat_log = 'Meu nome é Daniel Farias. Sou formado em engenharia elétrica. Tenho um mestrado em Ciência e Tecnologia na Saúde, onde tive a oportunidade de estudar os padrões de comunicação na troca de dados entre prontuários da saúde, o HL7 e FHIR. Já o segundo mestrado em Modelagem Computacional, onde tive a oportunidade de estudar sobre séries temporais, especificamente sobre classificação do EEG e predição de sinais de radiação solar. Algumas habilidades são: curiosidade, interligar várias áreas do conhecimento, resiliência e enxergar obstáculos como desafios a serem superados, é onde mais me sinto estimulado. Atualmente trabalho na Ânima Educação na área de Realidade Virtual, Metaverso e Inteligência Artificial. Também sou avaliador da Inovativa Brasil onde promovemos aceleração de negócios inovadores, conexão com potenciais investidores e parceiros, e capacitação de empreendedores'

def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log} \n\nHuman: {question}\nDaniel:'
    print ("prompt:", prompt)
    print ("\n\n\n")
    response = completion.create(
        prompt=prompt, engine="text-davinci-001", stop=['\n'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=120)
    answer = response.choices[0].text.strip()
    return answer




def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}\n\nHuman: {question}\nDaniel: {answer}\n'    

chat_log = None


app = Flask(__name__)
app.config.from_object(config.config['development'])


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('job-description.html', **locals())


@app.route('/job-description', methods=["GET", "POST"])
def jobDescription():

    if request.method == 'POST':
        query = request.form['jobDescription']
        print("Perguntei:", query)

        prompt = 'Resposta de Daniel: '.format(query)
        answer = ask(query, chat_log)
        openAIAnswer = answer

    return render_template('job-description.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=False)