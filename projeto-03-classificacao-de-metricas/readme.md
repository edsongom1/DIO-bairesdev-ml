# 📊 Calculadora de Métricas de Classificação

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen.svg)
![DIO](https://img.shields.io/badge/DIO.ME-Machine%20Learning-orange.svg)

## 🎓 Sobre o Projeto

Este projeto foi desenvolvido como parte do **BairesDev Machine Learning Training** da **DIO.ME**, focando na implementação prática de métricas de avaliação para modelos de classificação em Machine Learning.

**Projeto Prático:** Calculadora de Métricas de Classificação ML

## 📋 Descrição

Este projeto implementa uma calculadora completa para métricas de avaliação de modelos de classificação em Machine Learning. O programa calcula as principais métricas utilizadas para avaliar a performance de classificadores binários.

## 🎯 Objetivo

Calcular e demonstrar as principais métricas de avaliação de modelos de classificação:

- **Sensibilidade (Recall)**: Taxa de verdadeiros positivos
- **Especificidade**: Taxa de verdadeiros negativos  
- **Acurácia**: Proporção total de acertos
- **Precisão**: Proporção de predições positivas corretas
- **F-score**: Média harmônica entre precisão e sensibilidade

## 📊 Métricas Implementadas

| Métrica | Fórmula | Descrição |
|---------|---------|-----------|
| **Sensibilidade** | `VP / (VP + FN)` | Capacidade de identificar positivos |
| **Especificidade** | `VN / (FP + VN)` | Capacidade de identificar negativos |
| **Acurácia** | `(VP + VN) / N` | Proporção total de acertos |
| **Precisão** | `VP / (VP + FP)` | Confiabilidade das predições positivas |
| **F-score** | `2 × (P × S) / (P + S)` | Equilíbrio entre precisão e sensibilidade |

**Legenda:**
- `VP`: Verdadeiros Positivos
- `VN`: Verdadeiros Negativos
- `FP`: Falsos Positivos
- `FN`: Falsos Negativos
- `N`: Total de elementos
- `P`: Precisão
- `S`: Sensibilidade

## 🚀 Funcionalidades

### ✨ Principais Recursos

- **Cálculo automático** de todas as métricas
- **Visualização da matriz de confusão** em formato texto
- **Cálculos detalhados** passo a passo com fórmulas
- **Interface interativa** com menu de opções
- **Múltiplos exemplos** para comparação
- **Interpretação didática** de cada métrica

### 🎮 Modos de Uso

1. **Exemplo Automático**: Demonstração com classificação de spam
2. **Modo Interativo**: Insira seus próprios valores
3. **Comparação de Cenários**: Veja diferentes casos de uso
4. **Menu Cíclico**: Teste múltiplas configurações

## 💻 Instalação e Execução

### Pré-requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa necessária (usa apenas Python puro)

### Como Executar

1. **Clone ou baixe o arquivo:**
```bash
# Opção 1: Clone do repositório
git clone https://github.com/edsongom1/classification-metrics.git

# Opção 2: Baixe o arquivo classification_metrics.py
```

2. **Execute o programa:**
```bash
python classification_metrics.py
```

3. **Siga o menu interativo:**
```
==========================================
CALCULADORA DE MÉTRICAS DE CLASSIFICAÇÃO
==========================================
1. Exemplo automático (Classificação de Spam)
2. Inserir valores personalizados
3. Comparar múltiplos cenários
4. Sair

Escolha uma opção (1-4):
```

## 📈 Exemplo de Uso

### Entrada (Matriz de Confusão):
```
VP = 45  # Emails spam detectados corretamente
VN = 85  # Emails normais detectados corretamente  
FP = 10  # Emails normais classificados como spam
FN = 5   # Emails spam não detectados
```

### Saída:
```
==================================================
RESUMO DAS MÉTRICAS:
==================================================
Sensibilidade (Recall)   : 0.9000 (90.00%)
Especificidade          : 0.8947 (89.47%)
Acurácia                : 0.8966 (89.66%)
Precisão                : 0.8182 (81.82%)
F-score                 : 0.8571 (85.71%)
```

## 🔧 Estrutura do Código

### Classe Principal
```python
class MetricasClassificacao:
    def __init__(self, vp, vn, fp, fn)
    def sensibilidade()
    def especificidade() 
    def acuracia()
    def precisao()
    def f_score()
    def calcular_todas_metricas()
    def exibir_relatorio()
```

### Funções Auxiliares
- `exemplo_uso()`: Demonstração automática
- `exemplo_interativo()`: Input do usuário
- `exemplo_multiplos_casos()`: Comparação de cenários

## 📚 Interpretação das Métricas

| Métrica | Quando usar | Valores ideais |
|---------|-------------|----------------|
| **Sensibilidade** | Quando é crítico não perder positivos (ex: diagnósticos médicos) | Alto (>90%) |
| **Especificidade** | Quando falsos positivos são custosos (ex: filtros de spam) | Alto (>90%) |
| **Acurácia** | Quando as classes são balanceadas | Alto (>85%) |
| **Precisão** | Quando falsos positivos são problemáticos | Alto (>80%) |
| **F-score** | Para equilibrar precisão e sensibilidade | Alto (>80%) |

## 🎯 Casos de Uso

### 1. **Classificação Médica**
- Alta sensibilidade para não perder doenças
- Aceita alguns falsos positivos

### 2. **Detecção de Spam**
- Alta especificidade para não bloquear emails legítimos
- Alguma tolerância a spam não detectado

### 3. **Detecção de Fraude**
- Equilibrio entre precisão e sensibilidade
- F-score como métrica principal

## 🔍 Exemplos de Cenários

O programa inclui 4 cenários pré-configurados:

1. **Modelo Balanceado**: Métricas equilibradas
2. **Alta Precisão**: Poucos falsos positivos
3. **Alta Sensibilidade**: Poucos falsos negativos  
4. **Modelo Conservador**: Muito cauteloso com positivos

## 📝 Notas Técnicas

- **Tratamento de divisão por zero**: Retorna 0 quando denominador é 0
- **Validação de entrada**: Verifica se os valores são inteiros válidos
- **Interface robusta**: Tratamento de erros e interrupções
- **Código limpo**: Documentação completa e estrutura clara

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Edson Gomes**
- GitHub: [@edsongom1](https://github.com/edsongom1)
- Email: [edsgom@gmail.com](mailto:edsgom@gmail.com)
- LinkedIn: [Conecte-se comigo](https://linkedin.com/in/edsongom1)

### 🎯 Contexto Acadêmico
- **Bootcamp:** BairesDev Machine Learning Training
- **Plataforma:** DIO.ME (Digital Innovation One)
- **Projeto:** Calculadora de Métricas de Classificação ML
- **Objetivo:** Aplicação prática dos conceitos de avaliação de modelos de ML

Desenvolvido como projeto educacional para demonstrar o cálculo de métricas de classificação em Machine Learning.

## 📞 Suporte

Se encontrar algum problema ou tiver sugestões:

- Abra uma [Issue](https://github.com/edsongom1/classification-metrics/issues)
- Envie um Pull Request
- Entre em contato: [edsgom@gmail.com](mailto:edsgom@gmail.com)

---

## 🏆 Status do Projeto

✅ **Concluído** - Projeto do Bootcamp BairesDev Machine Learning Training (DIO.ME)

### Funcionalidades Implementadas:
- [x] Cálculo de todas as métricas
- [x] Interface interativa
- [x] Exemplos práticos
- [x] Documentação completa
- [x] Tratamento de erros
- [x] Menu de opções
- [x] Múltiplos cenários

### 📚 Conceitos de ML Aplicados:
- [x] Matriz de Confusão
- [x] Métricas de Classificação Binária
- [x] Análise de Performance de Modelos
- [x] Interpretação de Resultados
- [x] Casos de Uso Práticos

### Possíveis Melhorias Futuras:
- [ ] Suporte para classificação multiclasse
- [ ] Exportação de relatórios em PDF
- [ ] Interface gráfica (GUI)
- [ ] Visualizações com matplotlib
- [ ] Comparação de múltiplos modelos

---

**⭐ Se este projeto foi útil, considere dar uma estrela!**

**🎓 Desenvolvido durante o Bootcamp BairesDev Machine Learning Training - DIO.ME**