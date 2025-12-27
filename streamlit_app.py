import streamlit as st

html_code = """
<body>
    <div style="background-color:#084228;">
        <header style="display:flex;justify-content:space-between;">
            <nav style="display:flex;justify-content:space-between;color:#D9F2D0;gap:2px;">
                <ul style="display:flex;justify-content:space-between;gap:2rem;align-items:center;margin:2rem;font-size:1.5em;list-style:none;">
                    <li><a href="#" style="color:#D9F2D0;text-decoration-line:none;">Inicio </a></li>
                    <li><a href="#" style="color:#D9F2D0;text-decoration-line:none;">Sobre nós</a></li>
                </ul>
            </nav>
        </header>
    </div>
    <div style="background-color:#D9F2D0;">
        <h1 style="font-size:3rem;text-align:center;text-transform:uppercase;color:#084228;">Por que criar uma horta na Varanda?</h1>
        <p style="font-size:2rem;text-align:justify;color:#084228;margin-left:8px;margin-left: 2rem;margin-right: 2rem; margin-bottom: 0rem;">
                Criar um jardim na varanda é uma ótima maneira de trazer mais vida e frescor para o apartamento. Com um bom planejamento, 
                é possível transformar qualquer varanda em um verdadeiro oásis urbano, proporcionando conforto, beleza e conexão com a natureza. 
                Aqui estão algumas razões para considerar a criação de um jardim na varanda:
        </p>
    </div>
    <div style="background-color:#084228;">
        <h1 style="font-size:3rem;text-align:center;text-transform:uppercase;color:#D9F2D0; margin:2rem; margin-top:0rem">A Importância da Luz para as Plantas;</h1>
        <p style="font-size:1.5rem;text-align:justify;color:#D9F2D0;margin:2rem;">
                    Fotossíntese: A luz é essencial para a fotossíntese, o processo pelo qual as plantas convertem a luz solar em energia química. 
                    Durante a fotossíntese, as plantas absorvem dióxido de carbono (CO2) do ar e água do solo, 
                    utilizando a luz para transformar esses elementos em glicose (açúcar) e oxigênio (O2).
        </p>
        <p style="font-size:1.5rem;text-align:justify;color:#D9F2D0;margin:2rem;">
                    Proporciona conforto e bem-estar: Um jardim pode criar um ambiente relaxante e refrescante, 
                    ideal para momentos de descontração.
        </p>
        <p style="font-size:1.5rem;text-align:justify;color:#D9F2D0;margin:2rem">
                    Melhora a decoração: Plantas podem adicionar um toque natural à decoração do apartamento, 
                    criando um ambiente mais harmonioso.
        </p>
        <p style="font-size:1.5rem;text-align:justify;color:#D9F2D0;margin:2rem">
                    Cria um espaço funcional: Um jardim pode ser utilizado para refeições, relaxamento ou simplesmente para apreciar a natureza.
        </p>
    </div>
</body>
</html>
"""

st.markdown(html_code, unsafe_allow_html=True)


st.title("Descubra quais as melhores plantas para seu jardim!")

st.write("Para te ajudar a escolher as plantas mais adequadas para seu jardim, preciso de algumas informações sobre o local onde você planeja plantar. Por favor, responda às seguintes perguntas:")

with st.form(key='form_plantas'):
    nome = st.text_input("Qual é o seu nome?", placeholder="Digite seu nome aqui")
    telefone = st.number_input("Qual é o seu telefone?", placeholder="Digite seu telefone aqui")
    email = st.text_input("Qual é o seu email?", placeholder="Digite seu email aqui")
    horas_sol = st.number_input("Quantas horas de sol seu jardim recebe por dia?", min_value=1, max_value=24)
    tamanho_jardim = st.number_input("Qual é o tamanho de seu jardim em metros quadrados?", min_value=10, max_value=10000)
    btn_form = st.form_submit_button(label='Enviar')

    if btn_form:
        if not nome or not telefone or not email or horas_sol == 0 or tamanho_jardim == 0:
            st.error("Por favor, preencha todos os campos corretamente.")
        else:
            st.success(f"Obrigado, {nome}! Suas informações foram recebidas com sucesso. Agora, vamos descobrir quais plantas são as melhores para seu jardim!")
            if horas_sol >= 6 and tamanho_jardim >= 100:
                st.write("Para seu jardim com pelo menos 6 horas de sol por dia, algumas plantas que você pode considerar incluem: plantas frutiferas como limão, acerola, graviola, romã você pode considerar alguns vegetais como tomate, quiabo, maxixe entre outros, vale lembrar que todos esses vegetais podem ser cultivados em vasos, precisando apenas tomar cuidado com a profundidade do mesmo")
            elif horas_sol >= 4 and tamanho_jardim >= 100:
                st.write("Para seu jardim com pelo menos 4 horas de sol por dia, algumas plantas que você pode considerar incluem: plantas frutiferas como jabuticaba, acerola, você pode considerar alguns vegetais como tomate, quiabo, maxixe entre outros, vale lembrar que todos esses vegetais podem ser cultivados em vasos, precisando apenas tomar cuidado com a profundidade do mesmo")
            elif horas_sol < 4 and tamanho_jardim >= 100:
                st.write("Para seu jardim com pelo menos 4 horas de sol por dia, algumas plantas que você pode considerar incluem: plantas frutiferas como morango e amora, você pode considerar alguns vegetais como tomate, aspargos, vale lembrar que todos esses vegetais podem ser cultivados em vasos, precisando apenas tomar cuidado com a profundidade do mesmo")
            if horas_sol >= 6 and tamanho_jardim < 100:
                st.write("Para seu jardim com pelo menos 6 horas de sol por dia, algumas plantas que você pode considerar incluem: plantas como Cebolinha, coentro, acelga e agrião")
            else:
                st.write("Desculpe, mas não conseguimos encontrar plantas adequadas para seu jardim com base nas informações fornecidas. Por favor, tente novamente com outras informações.")


st.markdown(html_code, unsafe_allow_html=True)
