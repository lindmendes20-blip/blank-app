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
