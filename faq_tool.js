// FAQ Tool — REMMED Telemedicina
// Receives: tema (string)
// Returns: JSON { resposta, tema_identificado }

const faq = {
  valor: "Os valores dos nossos serviços são:\n1️⃣ Consulta médica — R$ 79,90\n2️⃣ Solicitar atestado — R$ 79,90\n3️⃣ Consulta saúde mental — R$ 249,00\n4️⃣ Renovar receita — R$ 79,90\n5️⃣ Solicitar exames — R$ 79,90\n6️⃣ Consulta hábitos/peso/saúde — R$ 249,00\n\nPagamento via Pix ou cartão de crédito.",

  pagamento: "Aceitamos Pix e cartão de crédito 💳 O pagamento é feito antes do atendimento. Não fazemos parcelamento.",

  como_funciona: "É simples 😊 Você escolhe o serviço, realiza o pagamento e recebe o link de acesso. Dentro da plataforma, você é atendido por videochamada ou chat com um médico. Após a consulta, os documentos são enviados digitalmente aqui no WhatsApp.",

  acesso: "Após o pagamento, você recebe o link de acesso direto aqui no WhatsApp 📲 Basta clicar, preencher seus dados e aguardar o médico na plataforma.",

  camera: "Para consulta por videochamada é necessário câmera e microfone funcionando 📷 Se preferir, o atendimento também pode ser feito por chat de texto dentro da plataforma.",

  atestado: "Sim, emitimos atestado médico online! 📄 O médico realiza a avaliação e, se houver indicação, emite o atestado digitalmente com assinatura e CRM. O serviço é a opção 2️⃣ — R$ 79,90.",

  atestado_validade: "Sim! O atestado emitido pela REMMED tem plena validade legal 📋 É assinado digitalmente pelo médico com nome e CRM, dentro das normas do CFM (Conselho Federal de Medicina) para telemedicina.",

  atestado_download: "O atestado é enviado aqui no WhatsApp após a consulta 📲 Você pode salvá-lo diretamente no seu celular ou fazer o download em PDF.",

  atestado_acompanhante: "O atestado de acompanhante não é emitido pela telemedicina. Esse documento precisa ser solicitado diretamente na unidade de saúde onde o acompanhamento ocorreu.",

  receita: "Sim! A receita digital tem assinatura médica certificada e é aceita em todas as farmácias do Brasil. Basta mostrar o QR Code ou informar o código na farmácia. Para renovação com receita anterior de até 6 meses, use a opção 4️⃣.",

  exame: "Sim! O pedido de exame é válido em qualquer laboratório ou posto de saúde que aceite documentos digitais 🔬 Recomendamos confirmar diretamente no posto da sua região.",

  horario: "Funcionamos de segunda a segunda 🌞 Segunda a sexta: 7h às 21h | Sábado e domingo: 9h às 18h. Atendemos também em feriados, a critério da clínica!",

  retorno: "A consulta é única e não inclui retorno automático. Se precisar de acompanhamento, podemos agendar uma nova consulta pela opção 1️⃣ 😊",

  reembolso: "Se o atendimento não acontecer por algum motivo da clínica, garantimos o reembolso. Se a consulta for realizada, não há reembolso pois é um serviço médico já prestado conforme o CFM.",

  problema_tecnico: "Sentimos muito pelo inconveniente 😔 Para problemas técnicos, nossa equipe de suporte pode te ajudar. Selecione a opção 7️⃣ ou envie um e-mail para contato@remmedtelemedicina.com.br.",

  crm: "Todos os nossos médicos possuem CRM ativo e são habilitados para atendimento em telemedicina, conforme as normas do CFM 🩺",

  lgpd: "Seus dados são tratados com total segurança e sigilo, em conformidade com a LGPD (Lei Geral de Proteção de Dados) 🔒 Não compartilhamos suas informações com terceiros sem consentimento.",

  cnpj: "A REMMED Telemedicina é regularmente registrada 😊 Nosso CNPJ é 56.069.744/0001-17 — você pode confirmar na Receita Federal ou em www.remmed.com.br",

  site_falso: "Atenção! O único site oficial da REMMED é remmedtelemedicina.com.br 🔒 Desconfie de outros domínios. Em caso de dúvida, entre em contato conosco pelo WhatsApp oficial.",

  parcelamento: "Não fazemos parcelamento, mas aceitamos Pix e cartão de crédito 💳",

  venda_atestado: "Não vendemos atestados 🚫 O atestado é um documento médico emitido apenas mediante avaliação clínica. O médico avalia sua condição e decide pela emissão ou não, seguindo a ética médica e as normas do CFM.",

  atestado_dias: "O número de dias no atestado é determinado pelo médico com base na avaliação clínica 📋 Não é possível solicitar uma quantidade específica de dias — essa decisão é exclusiva do profissional de saúde.",

  atestado_retroativo: "Não emitimos atestado retroativo 🚫 Os documentos são emitidos apenas a partir da data da consulta, conforme as normas do CFM.",

  atestado_periodo_especifico: "Não é possível solicitar atestado para um período específico no passado 🚫 O atestado é emitido a partir da data da consulta, com o número de dias determinado pelo médico.",

  documentos_nao_realizamos: "Infelizmente não realizamos esse tipo de documento 😔 Se tiver dúvidas sobre o que oferecemos, nossa equipe pode te orientar — opção 7️⃣.",

  // --- NOVAS ENTRADAS ---

  crm_estado: "O CRM é válido em todo o Brasil — nossos médicos são habilitados nacionalmente 🩺 Você pode confirmar o registro no site oficial do CFM: cfm.org.br",

  nao_recebi_documento: "O documento é enviado por aqui no WhatsApp logo após a consulta 📲 Se não chegou, pode estar em processamento — aguarde alguns instantes. Se não chegar, nossa equipe pode verificar — é só escolher a opção 7️⃣.",

  foto_exame: "Sim 😊 Durante a consulta você pode mostrar exames, fotos ou resultados diretamente pela videochamada ou pelo chat da plataforma.",

  consulta_whatsapp: "A consulta não é realizada pelo WhatsApp 😊 O WhatsApp é usado apenas para suporte e agendamento. O atendimento acontece dentro da nossa plataforma médica segura, por videochamada ou chat com o médico. Após o pagamento, você recebe o link de acesso.",

  aplicativo: "Não precisa baixar aplicativo 😊 A consulta acontece direto pelo navegador do celular ou computador. Após o pagamento, é só clicar no link.",

  computador: "Sim 😊 Você pode acessar a plataforma tanto pelo celular quanto pelo computador. Basta abrir o link enviado após o pagamento.",

  convenio: "No momento o atendimento é particular 😊 Não aceitamos convênios ou planos de saúde.",

  autenticidade: "O atestado possui QR Code de verificação e assinatura digital do médico responsável, com nome e CRM visíveis 😊 O QR Code no rodapé confirma a autenticidade. Seguimos todas as normas do CFM.",

  atestado_piscina: "Sim, realizamos atestado de piscina! 🏊 O médico avalia pele, unhas e condições gerais. Se não houver alteração, o atestado é emitido logo após. Valor: R$ 79,90 — opção 2️⃣ (Solicitar atestado).",

  atestado_retroativo_def: "Atestado retroativo é um documento que tenta justificar dias anteriores sem consulta médica nesses dias. Não emitimos atestado retroativo — os documentos são emitidos apenas a partir da data da consulta.",

  anticoncepcional: "Para renovação de anticoncepcional com receita anterior de até 6 meses, use a opção 4️⃣ Renovar receita — R$ 79,90 💊 Se não tiver receita anterior ou tiver mais de 6 meses, a opção 1️⃣ Consulta médica é o caminho certo.",

  ozempic: "Realizamos avaliação médica completa para emagrecimento, incluindo orientação sobre medicamentos quando há indicação médica 😊 O caminho é a opção 6️⃣ Consulta para hábitos/peso/saúde. Valor: R$ 249,00.",

  receita_hora: "Se houver indicação médica, a receita normalmente é emitida logo após a consulta 😊 Ela é enviada digitalmente com assinatura certificada e QR Code.",

  remarcar: "Sim 😊 Se precisar remarcar, nossa equipe pode te ajudar conforme disponibilidade da agenda e antecedência.",

  prontuario: "O prontuário é um direito seu e a REMMED disponibiliza mediante solicitação formal 😊 Entre em contato pelo e-mail contato@remmedtelemedicina.com.br informando nome completo, CPF e documentos desejados. Disponibilizamos em até 72h.",

  pediatria: "Atendemos crianças a partir de 5 anos de idade 😊 Para menores de 15 anos é obrigatória a presença de um responsável. Para bebês e crianças menores de 5 anos, recomendamos avaliação presencial pediátrica.",

  tempo_espera: "Após o pagamento, você já pode entrar na plataforma e aguardar o médico 😊 Em horários de menor movimento o atendimento começa em minutos. Em horários de pico pode haver uma pequena fila — você é atendido na ordem de chegada.",

  escolher_medico: "O sistema aloca automaticamente o médico disponível no momento 😊 Não é possível escolher um profissional específico, mas todos têm CRM ativo e experiência em telemedicina.",

  especialidades: "Atendemos com médicos clínicos gerais habilitados para telemedicina 🩺\n\nAlém da clínica geral, temos dois serviços especializados:\n🧠 Consulta de saúde mental — opção 3️⃣ — R$ 249,00\n⚖️ Consulta de emagrecimento/hábitos de saúde — opção 6️⃣ — R$ 249,00\n\nPara especialidades como cardiologia, dermatologia, ortopedia, ginecologia e outras, o médico clínico avalia, trata o que for possível por telemedicina e, quando necessário, faz o encaminhamento para o especialista presencial 😊"
};

// IMPORTANT: More specific entries MUST come before generic ones.
// e.g. crm_estado before crm, atestado_retroativo_def before atestado_retroativo, etc.
const mapa = {
  // --- Mais específicos primeiro ---

  crm_estado: [
    "crm do rs", "crm do sp", "crm do rj", "crm do mg", "crm do pr", "crm do sc",
    "crm do estado", "crm ativo no", "crm válido no", "crm valido no",
    "médico registrado no", "medico registrado no",
    "médico habilitado no", "medico habilitado no",
    "crm do médico", "crm do medico", "crm é válido", "crm e valido",
    "crm vale em", "crm funciona em", "crm de outro estado"
  ],

  atestado_retroativo_def: [
    "o que é retroativo", "o que e retroativo",
    "o que significa retroativo", "retroativo significa",
    "o que quer dizer retroativo", "retroativo o que é",
    "retroativo o que e", "significado de retroativo"
  ],

  atestado_retroativo: [
    "atestado retroativo", "atestado para dias anteriores",
    "atestado de ontem", "atestado de anteontem",
    "atestado passado", "dias anteriores",
    "data passada", "retroativo"
  ],

  atestado_periodo_especifico: [
    "atestado do dia", "atestado para o dia",
    "atestado de uma data específica", "atestado de uma data especifica",
    "período específico", "periodo especifico",
    "data específica", "data especifica"
  ],

  atestado_acompanhante: [
    "atestado de acompanhante", "acompanhar familiar",
    "atestado para acompanhar", "acompanhante",
    "para ficar com", "cuidar de familiar"
  ],

  atestado_validade: [
    "atestado tem validade", "atestado é válido", "atestado e valido",
    "validade do atestado", "atestado aceito",
    "empresa aceita", "rh aceita", "atestado reconhecido",
    "atestado legal", "tem valor legal"
  ],

  atestado_download: [
    "baixar atestado", "download do atestado", "salvar atestado",
    "como pego o atestado", "onde fica o atestado", "como recebo o atestado",
    "como baixo", "pdf do atestado"
  ],

  atestado_piscina: [
    "piscina", "atestado de piscina", "natação", "natacao",
    "atestado para piscina", "academia de natação", "academia de natacao",
    "aula de natação", "aula de natacao"
  ],

  atestado_dias: [
    "quantos dias de atestado", "dias de atestado", "quantos dias",
    "mais dias de atestado", "5 dias", "3 dias", "7 dias",
    "número de dias", "numero de dias", "quantidade de dias",
    "escolher dias", "pedir dias"
  ],

  atestado: [
    "atestado", "declaração médica", "declaracao medica",
    "justificativa de falta", "justificativa médica", "justificativa medica",
    "afastamento", "folga médica", "folga medica",
    "declaração de comparecimento", "declaracao de comparecimento"
  ],

  nao_recebi_documento: [
    "não recebi", "nao recebi", "cadê", "cade",
    "onde está meu atestado", "onde esta meu atestado",
    "onde está minha receita", "onde esta minha receita",
    "onde está meu documento", "onde esta meu documento",
    "não chegou", "nao chegou", "sumiu",
    "não veio", "nao veio", "cadê o atestado", "cade o atestado",
    "cadê a receita", "cade a receita", "não recebi o documento",
    "nao recebi o documento", "documento não chegou", "documento nao chegou"
  ],

  autenticidade: [
    "autenticidade", "verificar atestado", "qr code do atestado",
    "assinatura digital do atestado", "como verificar",
    "é verdadeiro", "e verdadeiro", "atestado é verdadeiro",
    "atestado e verdadeiro", "autêntico", "autentico",
    "como confirmar", "confirmar autenticidade"
  ],

  venda_atestado: [
    "vender atestado", "comprar atestado", "atestado sem consulta",
    "atestado na hora sem", "só o atestado", "so o atestado",
    "garantia de atestado", "atestado garantido", "emite atestado direto"
  ],

  foto_exame: [
    "foto", "mandar foto", "enviar exame", "mostrar exame",
    "enviar resultado", "mostrar resultado", "tirar foto",
    "foto de exame", "foto de resultado", "mandar exame",
    "compartilhar exame", "compartilhar resultado"
  ],

  consulta_whatsapp: [
    "pelo whatsapp", "pelo zap", "por aqui mesmo",
    "aqui no whatsapp", "consulta aqui", "atendimento aqui",
    "consulta pelo zap", "atendimento pelo zap",
    "atendimento pelo whatsapp"
  ],

  aplicativo: [
    "aplicativo", "app", "baixar app", "precisa instalar", "instalar",
    "baixar aplicativo", "precisa de app", "tem app",
    "tem aplicativo", "precisa baixar", "instala algo"
  ],

  computador: [
    "computador", "notebook", "pc", "laptop", "pelo pc",
    "no computador", "no notebook", "no laptop",
    "pelo computador", "pelo notebook", "desktop"
  ],

  convenio: [
    "convênio", "convenio", "plano de saúde", "plano saude",
    "unimed", "aceita plano", "tem convênio", "tem convenio",
    "reembolso de plano", "plano médico", "plano medico",
    "sulamerica", "bradesco saude", "amil", "hapvida",
    "notredame", "são cristovão", "sao cristovao",
    "aceita convênio", "aceita convenio"
  ],

  anticoncepcional: [
    "anticoncepcional", "pílula", "pilula", "contraceptivo",
    "anticoncepcionais", "yasmin", "diane", "microvlar",
    "ciclo 21", "selene", "mercilon", "norestin",
    "método anticoncepcional", "metodo anticoncepcional",
    "pílula anticoncepcional", "pilula anticoncepcional",
    "renovar anticoncepcional", "receita anticoncepcional"
  ],

  ozempic: [
    "ozempic", "mounjaro", "wegovy", "saxenda", "semaglutida",
    "emagrecer", "emagrecimento", "perder peso", "controle de peso",
    "remédio para emagrecer", "remedio para emagrecer",
    "medicamento para emagrecer", "injeção para emagrecer",
    "injecao para emagrecer", "tirzepatida", "liraglutida",
    "consulta emagrecimento", "consulta obesidade", "obesidade"
  ],

  receita_hora: [
    "sai na hora", "receita imediata", "quando sai a receita",
    "quanto tempo receita", "receita na hora",
    "receita logo", "receita rápida", "receita rapida",
    "receita em quanto tempo", "quanto tempo para receita"
  ],

  remarcar: [
    "remarcar", "reagendar", "mudar horário", "mudar horario",
    "trocar horário", "trocar horario", "outro horário",
    "outro horario", "cancelar consulta", "cancelar agendamento",
    "remarcar consulta", "reagendar consulta", "mudança de horário",
    "mudanca de horario"
  ],

  prontuario: [
    "prontuário", "prontuario", "histórico médico", "historico medico",
    "histórico de consultas", "historico de consultas",
    "documentos antigos", "receitas antigas", "consultas anteriores",
    "meu histórico", "meu historico", "registros médicos",
    "registros medicos", "dados médicos", "dados medicos"
  ],

  pediatria: [
    "criança", "crianca", "filho", "filha", "pediatria",
    "bebê", "bebe", "menor de idade", "menor de 15",
    "meu filho", "minha filha", "meu bebe", "meu bebê",
    "criança pequena", "crianca pequena", "recém-nascido",
    "recem-nascido", "recém nascido", "recem nascido",
    "pediátrico", "pediatrico", "pediatra"
  ],

  tempo_espera: [
    "quanto tempo demora", "demora muito", "tempo de espera",
    "fila de espera", "espera muito", "quando vou ser atendido",
    "fila", "quanto demora", "demora", "aguardar",
    "tempo de atendimento", "demora para atender",
    "precisa esperar", "espera longa"
  ],

  escolher_medico: [
    "escolher médico", "escolher medico", "qual médico", "qual medico",
    "médico específico", "medico especifico",
    "quem vai me atender", "posso escolher",
    "escolher o médico", "escolher o medico",
    "médico de preferência", "medico de preferencia",
    "mesmo médico", "mesmo medico"
  ],

  especialidades: [
    "especialidade", "especialidades", "especialista", "especialistas",
    "tem especialista", "médico especialista", "medico especialista",
    "cardiologista", "dermatologista", "ortopedista", "neurologista",
    "ginecologista", "urologista", "endocrinologista", "reumatologista",
    "pneumologista", "gastroenterologista", "oftalmologista",
    "otorrinolaringologista", "otorrino", "nefrologista", "hematologista",
    "só clínico", "so clinico", "só clínico geral", "apenas clínico",
    "apenas clinico", "que tipo de médico", "que tipo de medico",
    "qual especialidade", "quais especialidades", "que especialidades",
    "atende qual especialidade", "tem psiquiatra", "tem psicólogo",
    "tem psicologo", "tem cardiologista", "tem dermatologista",
    "médico especializado", "medico especializado"
  ],

  // --- Entradas genéricas / originais ---

  valor: [
    "valor", "preço", "preco", "quanto custa", "quanto é",
    "quanto e", "custo", "tabela", "plano", "serviço",
    "servico", "opcoes", "opções", "menu", "lista",
    "quanto fica", "quanto cobram", "quanto vou pagar"
  ],

  pagamento: [
    "pagamento", "pagar", "pix", "cartão", "cartao",
    "débito", "debito", "crédito", "credito",
    "como pagar", "forma de pagamento", "formas de pagamento",
    "aceita pix", "aceita cartão", "aceita cartao",
    "boleto", "transferência", "transferencia"
  ],

  como_funciona: [
    "como funciona", "como é", "como e", "como faço",
    "como faco", "como começo", "como comeco",
    "como usar", "quero saber mais", "me explica",
    "primeira vez", "nunca usei", "como é o processo",
    "como e o processo"
  ],

  acesso: [
    "link", "acesso", "entrar", "como acesso",
    "como entro", "não recebi o link", "nao recebi o link",
    "onde acesso", "plataforma", "link de acesso",
    "como acessar", "login"
  ],

  camera: [
    "câmera", "camera", "sem câmera", "sem camera",
    "microfone", "som", "vídeo", "video",
    "videochamada", "chamada de vídeo", "chamada de video",
    "não tem câmera", "nao tem camera", "câmera não funciona",
    "camera nao funciona"
  ],

  receita: [
    "receita", "receita médica", "receita medica",
    "prescrição", "prescricao", "medicamento",
    "remédio", "remedio", "receita digital",
    "renovar receita", "renovação de receita", "renovacao de receita"
  ],

  exame: [
    "exame", "pedido de exame", "solicitação de exame",
    "solicitacao de exame", "pedir exame", "solicitar exame",
    "hemograma", "exame de sangue", "ultrassom", "ultrassonografia",
    "raio x", "raio-x", "tomografia"
  ],

  horario: [
    "horário", "horario", "hora", "horário de funcionamento",
    "horario de funcionamento", "atende quando",
    "que horas", "domingo", "sábado", "sabado",
    "feriado", "fim de semana", "final de semana",
    "abre", "fecha", "quando atende"
  ],

  retorno: [
    "retorno", "consulta de retorno", "segunda consulta",
    "revisão", "revisao", "acompanhamento", "follow up", "followup"
  ],

  reembolso: [
    "reembolso", "devolver dinheiro", "devolução", "devolucao",
    "cancelar pagamento", "estorno", "ressarcimento",
    "quero meu dinheiro de volta", "dinheiro de volta"
  ],

  problema_tecnico: [
    "problema técnico", "problema tecnico", "erro",
    "não funciona", "nao funciona", "travou", "caiu",
    "não conecta", "nao conecta", "bug", "falha",
    "plataforma caiu", "não consigo entrar", "nao consigo entrar",
    "não consigo acessar", "nao consigo acessar",
    "tela preta", "sem imagem"
  ],

  crm: [
    "crm", "médico registrado", "medico registrado",
    "médico habilitado", "medico habilitado",
    "médico qualificado", "medico qualificado",
    "médico certificado", "medico certificado",
    "médico de verdade", "medico de verdade",
    "médico licenciado", "medico licenciado"
  ],

  lgpd: [
    "lgpd", "privacidade", "dados pessoais",
    "proteção de dados", "protecao de dados",
    "meus dados", "sigilo", "confidencial",
    "compartilhar dados", "segurança dos dados",
    "seguranca dos dados"
  ],

  cnpj: [
    "cnpj", "razão social", "razao social",
    "empresa registrada", "dados da empresa",
    "nota fiscal", "registro da empresa"
  ],

  site_falso: [
    "site falso", "golpe", "fraude", "fake",
    "site oficial", "site verdadeiro", "site original",
    "domínio", "dominio", "link suspeito",
    "site diferente", "outro site"
  ],

  parcelamento: [
    "parcelamento", "parcelar", "parcelas",
    "em quantas vezes", "quantas vezes",
    "parcelar no cartão", "parcelar no cartao",
    "dividir pagamento"
  ],

  documentos_nao_realizamos: [
    "laudo", "laudo médico", "laudo medico",
    "perícia", "pericia", "habilitação", "habilitacao",
    "cnh", "carteira de motorista", "porte de arma",
    "aptidão física", "aptidao fisica", "exame admissional",
    "exame demissional", "aso", "atestado de saúde ocupacional",
    "atestado de saude ocupacional"
  ]
};

// --- Main logic ---

let tema = '';
try {
  const input = JSON.parse(query);
  tema = (input.tema || query).toLowerCase();
} catch(e) {
  tema = query.toLowerCase();
}

const norm = s => String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
const temaNorm = norm(tema);

let resposta = null;
let tema_identificado = "nao_identificado";

for (const [chave, palavras] of Object.entries(mapa)) {
  if (palavras.some(p => temaNorm.includes(norm(p)))) {
    resposta = faq[chave];
    tema_identificado = chave;
    break;
  }
}

if (!resposta) {
  resposta = "Não encontrei uma resposta específica para essa dúvida. Posso te conectar com nossa equipe para ajudar melhor!";
}

return JSON.stringify({ resposta, tema_identificado });
