# 🛡️ Framework de Auditoria de Segurança (GRC) - Baseline V1

Este documento estabelece um checklist técnico e gerencial para auditorias rápidas de conformidade, alinhado aos controles da **ISO/IEC 27001** e **NIST Cybersecurity Framework**.

## 📊 Matriz de Controle e Risco

| ID | Categoria | Controle de Segurança | Impacto (H/M/L) | Status |
| :--- | :--- | :--- | :--- | :---: |
| AC-01 | Acesso | Autenticação Multifator (MFA) ativa em sistemas críticos | High | [ ] |
| DP-01 | LGPD | Mapeamento de dados sensíveis (Data Mapping) | Critical | [ ] |
| IR-01 | Incidentes | Plano de Resposta a Incidentes testado e atualizado | High | [ ] |
| VM-01 | Vulnerabilidade | Varredura semanal de vulnerabilidades (Pentest/Scan) | Medium | [ ] |

## 🔍 Análise Técnica de Risco (Cálculo Básico)

Como profissional de GRC, utilizo a fórmula fundamental para priorização de ativos:

$$Risco = Ameaça \times Vulnerabilidade \times Valor \ do \ Ativo$$

---

## 🛠️ Automação de Compliance (Ideia de Script Python)
Futuro projeto: Script para verificar automaticamente se portas sensíveis (ex: 22, 3389) estão abertas em um servidor e gerar um relatório de não-conformidade.

---
**Status:** Em constante atualização conforme o progresso na graduação da FIAP.
