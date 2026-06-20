# Clinica GG Pets - API REST

## 1. Visão Geral
API REST desenvolvida para o gerenciamento de uma clínica veterinária, focada em manter a integridade dos dados e o controle do ciclo de vida clínico dos animais.

## 2. Modelagem de Entidades
* **Tutor:** Entidade raiz. Armazena dados de contato.
* **Animal:** Pertence a um tutor (FK). Possui histórico clínico.
* **Consulta:** Entidade de transação. Vincula Animal e Tutor. Possui status (Máquina de Estados).
* **Vacina:** Registro de histórico de saúde vinculado ao animal.


## 3. Regras de Negócio (RNs)

| ID | Nome | Gatilho | Ação | Erro |
| :--- | :--- | :--- | :--- | :--- |
| **RN-001** | Integridade de Tutor | Criar Animal | Verifica existência do Tutor | `TUTOR_NOT_FOUND` |
| **RN-002** | Bloqueio de Terminal | Update Consulta | Impede edição se status == concluída/cancelada | `CONSULTA_TERMINAL` |
| **RN-003** | Email Único | Criar Tutor | Verifica duplicidade de e-mail | `EMAIL_ALREADY_EXISTS` |
| **RN-004** | Agendamento Único | Criar Consulta | Valida conflito de data/animal | `CONSULTA_CONFLICT` |
| **RN-005** | Vacina Retroativa | Criar Vacina | Valida se data_aplicacao <= hoje | `INVALID_VACINA_DATE` |

## 4. Decisões de Design
* **Pydantic vs Service:** Pydantic valida a forma (tipos, formatos, campos obrigatórios). O Service valida o estado do negócio (ex: "posso mover essa consulta para finalizada?").
* **Migration 2:** Adicionada para suportar a máquina de estados (Status da Consulta), permitindo o controle de ciclo de vida.
* **Race Condition:** Implementada estratégia de verificação transacional. Em um ambiente de produção com alta concorrência, o uso de `SELECT FOR UPDATE` no PostgreSQL seria a solução definitiva para evitar sobrescrita de dados.

## 5. Máquina de Estados (Consulta)
* **Agendada** -> **Concluída** (Transição válida)
* **Agendada** -> **Cancelada** (Transição válida)
* **Estados Terminais:** Concluída e Cancelada. Não permitem reabertura para garantir a auditoria clínica.

## 6. Tratamento de Cenários de Borda
1. **Deleção em Cascata:** Configurado `ON DELETE CASCADE`. Se o tutor é removido, o sistema limpa os vínculos para evitar registros órfãos.
2. **Datas Futuras:** Bloqueio de inserções de datas inválidas (ex: vacina aplicada no futuro) através de validadores.
3. **Consistência em Cálculo:** O status terminal impede que cálculos históricos sejam corrompidos.

## 7. Padronização de Erros
Todos os erros seguem o formato JSON para integração padronizada:
```json
{
  "error": "CODIGO_DO_ERRO",
  "message": "Descrição amigável do problema",
  "details": {}
}

## 8. Como rodar localmente
 1 - Certifique-se de ter Docker e Docker Compose instalados.
 2 - Crie o arquivo .env baseado no .env.example.
 3 - Execute o comando: docker compose up --build
 4 - Para rodar os testes: docker compose exec web pytest