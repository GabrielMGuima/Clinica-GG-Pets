1. Modelagem dos Relacionamentos

O relacionamento entre Tutor e Animal foi modelado como um para muitos (1), pois um tutor pode possuir vários animais, mas cada animal pertence a apenas um tutor.

O relacionamento entre Animal e Consulta também foi modelado como um para muitos, permitindo que um animal tenha um histórico completo de consultas ao longo do tempo.

O relacionamento entre Animal e Vacina segue a mesma lógica, permitindo registrar diversas vacinas para um único animal.

Essa modelagem facilita consultas históricas, mantém a integridade dos dados e reflete corretamente as regras de negócio de uma clínica veterinária.

2. Validações no Pydantic versus Camada de Serviço

As validações estruturais foram implementadas no Pydantic, como:

Campos obrigatórios.
Formato de e-mail.
Tipos de dados.
Restrições de tamanho e valores mínimos.

Já as regras de negócio foram implementadas na camada de serviço, como:

Verificar se o tutor existe antes de cadastrar um animal.
Impedir consultas para animais inexistentes.
Impedir alterações em consultas finalizadas ou canceladas.

Essa separação mantém o código organizado e respeita o princípio de responsabilidade única.

3. Necessidade da Migration 2

A segunda migration foi necessária após a evolução do entendimento do domínio.

Inicialmente o sistema armazenava apenas os dados básicos da consulta. Posteriormente foi identificado que seria necessário controlar o status da consulta, permitindo acompanhar seu ciclo de vida (agendada, concluída ou cancelada).

A migration permitiu adicionar novos campos sem perda dos dados já existentes.

4. Modificações Simultâneas (Race Condition)

Caso dois usuários tentem alterar simultaneamente a mesma consulta, pode ocorrer inconsistência de dados.

A abordagem recomendada é utilizar controle transacional e versionamento de registros (optimistic locking), garantindo que uma atualização não sobrescreva outra sem verificação prévia.

Como este projeto possui foco acadêmico, a situação foi documentada e considerada para futuras evoluções.

5. Estados Terminais

O sistema utiliza os seguintes estados para consultas:

agendada
concluida
cancelada

Os estados "concluida" e "cancelada" são considerados terminais.

Após atingir um estado terminal, a consulta não pode retornar para outro estado, pois isso comprometeria a consistência do histórico clínico e auditoria do sistema.

Por exemplo, uma consulta concluída representa um atendimento já realizado e não deve voltar para o estado agendada.

5.2 Consistência em Cenários de Borda
Cenário 1 - Exclusão de Tutor com Animais Vinculados

Quando um tutor é removido, todos os animais associados são removidos automaticamente através do relacionamento configurado com ON DELETE CASCADE.

Justificativa:

Evita registros órfãos no banco de dados e mantém a integridade referencial.

Cenário 2 - Exclusão de Animal com Histórico

Ao excluir um animal, todas as consultas e vacinas relacionadas também são removidas.

Justificativa:

Não faz sentido manter consultas ou registros de vacinação sem o animal correspondente.

Cenário 3 - Alteração de Consulta em Estado Terminal

Consultas com status "concluida" ou "cancelada" não podem ser modificadas.

Justificativa:

Preserva o histórico clínico e impede inconsistências operacionais.

Cenário 4 - Agendamento em Horário Já Ocupado

O sistema deve impedir o cadastro de duas consultas para o mesmo animal no mesmo horário.

Justificativa:

Evita conflitos de agenda e garante previsibilidade no atendimento.

Cenário 5 - Cadastro de Vacina com Data Inválida

O sistema não permite registrar uma vacina com data futura de aplicação.

Justificativa:

Uma vacina só pode ser registrada após sua efetiva aplicação.

5.3 Mensagens de Erro Informativas

O sistema retorna mensagens claras para facilitar a correção pelo usuário.

Tutor não encontrado
{
  "error_code": "TUTOR_NOT_FOUND",
  "message": "O tutor informado não foi encontrado."
}
Animal não encontrado
{
  "error_code": "ANIMAL_NOT_FOUND",
  "message": "O animal informado não existe."
}
Consulta em estado terminal
{
  "error_code": "CONSULTA_TERMINAL",
  "message": "Não é permitido alterar uma consulta concluída ou cancelada."
}
Conflito de horário
{
  "error_code": "CONSULTA_CONFLICT",
  "message": "Já existe uma consulta agendada para este horário."
}
E-mail duplicado
{
  "error_code": "EMAIL_ALREADY_EXISTS",
  "message": "Já existe um tutor cadastrado com este e-mail."
}