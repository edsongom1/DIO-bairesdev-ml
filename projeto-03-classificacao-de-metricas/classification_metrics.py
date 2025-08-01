class MetricasClassificacao:
    """
    Classe para calcular métricas de avaliação de modelos de classificação
    """
    
    def __init__(self, vp, vn, fp, fn):
        """
        Inicializa com os valores da matriz de confusão
        
        Args:
            vp (int): Verdadeiros Positivos
            vn (int): Verdadeiros Negativos  
            fp (int): Falsos Positivos
            fn (int): Falsos Negativos
        """
        self.vp = vp
        self.vn = vn
        self.fp = fp
        self.fn = fn
        self.n = vp + vn + fp + fn  # Total de elementos
        
    def sensibilidade(self):
        """
        Calcula a Sensibilidade (Recall)
        Fórmula: VP / (VP + FN)
        """
        if (self.vp + self.fn) == 0:
            return 0
        return self.vp / (self.vp + self.fn)
    
    def especificidade(self):
        """
        Calcula a Especificidade
        Fórmula: VN / (FP + VN)
        """
        if (self.fp + self.vn) == 0:
            return 0
        return self.vn / (self.fp + self.vn)
    
    def acuracia(self):
        """
        Calcula a Acurácia
        Fórmula: (VP + VN) / N
        """
        if self.n == 0:
            return 0
        return (self.vp + self.vn) / self.n
    
    def precisao(self):
        """
        Calcula a Precisão
        Fórmula: VP / (VP + FP)
        """
        if (self.vp + self.fp) == 0:
            return 0
        return self.vp / (self.vp + self.fp)
    
    def f_score(self):
        """
        Calcula o F-score
        Fórmula: 2 × (P × S) / (P + S)
        onde P = Precisão e S = Sensibilidade
        """
        p = self.precisao()
        s = self.sensibilidade()
        
        if (p + s) == 0:
            return 0
        return 2 * (p * s) / (p + s)
    
    def calcular_todas_metricas(self):
        """
        Calcula todas as métricas e retorna um dicionário
        """
        return {
            'Sensibilidade (Recall)': self.sensibilidade(),
            'Especificidade': self.especificidade(),
            'Acurácia': self.acuracia(),
            'Precisão': self.precisao(),
            'F-score': self.f_score()
        }
    
    def exibir_matriz_confusao(self):
        """
        Exibe a matriz de confusão em formato texto
        """
        print("\nMATRIZ DE CONFUSÃO:")
        print("                    PREDIÇÃO")
        print("                 Pos    Neg")
        print("REAL    Pos    {:4d}   {:4d}".format(self.vp, self.fn))
        print("        Neg    {:4d}   {:4d}".format(self.fp, self.vn))
        
        print(f"\nVerdadeiros Positivos (VP): {self.vp}")
        print(f"Verdadeiros Negativos (VN): {self.vn}")
        print(f"Falsos Positivos (FP): {self.fp}")
        print(f"Falsos Negativos (FN): {self.fn}")
        print(f"Total de elementos (N): {self.n}")
    
    def exibir_calculos_detalhados(self):
        """
        Exibe os cálculos passo a passo de cada métrica
        """
        print("\n" + "="*70)
        print("CÁLCULOS DETALHADOS DAS MÉTRICAS:")
        print("="*70)
        
        # Sensibilidade
        sens = self.sensibilidade()
        print(f"\n1. SENSIBILIDADE (Recall):")
        print(f"   Fórmula: VP / (VP + FN)")
        print(f"   Cálculo: {self.vp} / ({self.vp} + {self.fn}) = {self.vp} / {self.vp + self.fn}")
        print(f"   Resultado: {sens:.4f} ({sens*100:.2f}%)")
        
        # Especificidade
        esp = self.especificidade()
        print(f"\n2. ESPECIFICIDADE:")
        print(f"   Fórmula: VN / (FP + VN)")
        print(f"   Cálculo: {self.vn} / ({self.fp} + {self.vn}) = {self.vn} / {self.fp + self.vn}")
        print(f"   Resultado: {esp:.4f} ({esp*100:.2f}%)")
        
        # Acurácia
        acu = self.acuracia()
        print(f"\n3. ACURÁCIA:")
        print(f"   Fórmula: (VP + VN) / N")
        print(f"   Cálculo: ({self.vp} + {self.vn}) / {self.n} = {self.vp + self.vn} / {self.n}")
        print(f"   Resultado: {acu:.4f} ({acu*100:.2f}%)")
        
        # Precisão
        prec = self.precisao()
        print(f"\n4. PRECISÃO:")
        print(f"   Fórmula: VP / (VP + FP)")
        print(f"   Cálculo: {self.vp} / ({self.vp} + {self.fp}) = {self.vp} / {self.vp + self.fp}")
        print(f"   Resultado: {prec:.4f} ({prec*100:.2f}%)")
        
        # F-score
        f1 = self.f_score()
        print(f"\n5. F-SCORE:")
        print(f"   Fórmula: 2 × (P × S) / (P + S)")
        print(f"   Onde P = Precisão = {prec:.4f} e S = Sensibilidade = {sens:.4f}")
        print(f"   Cálculo: 2 × ({prec:.4f} × {sens:.4f}) / ({prec:.4f} + {sens:.4f})")
        print(f"   Cálculo: 2 × {prec * sens:.4f} / {prec + sens:.4f}")
        print(f"   Resultado: {f1:.4f} ({f1*100:.2f}%)")
    
    def exibir_relatorio(self):
        """
        Exibe um relatório completo com todas as métricas
        """
        print("="*70)
        print("RELATÓRIO DE MÉTRICAS DE CLASSIFICAÇÃO")
        print("="*70)
        
        self.exibir_matriz_confusao()
        self.exibir_calculos_detalhados()
        
        print("\n" + "="*70)
        print("RESUMO DAS MÉTRICAS:")
        print("="*70)
        
        metricas = self.calcular_todas_metricas()
        
        for nome, valor in metricas.items():
            print(f"{nome:25}: {valor:.4f} ({valor*100:.2f}%)")
        
        print("\n" + "="*70)
        print("INTERPRETAÇÃO DAS MÉTRICAS:")
        print("="*70)
        
        print("• Sensibilidade (Recall): Proporção de positivos reais corretamente identificados")
        print("• Especificidade: Proporção de negativos reais corretamente identificados") 
        print("• Acurácia: Proporção total de predições corretas")
        print("• Precisão: Proporção de predições positivas que estão corretas")
        print("• F-score: Média harmônica entre precisão e sensibilidade")


# Exemplo de uso com matriz de confusão arbitrária
def exemplo_uso():
    """
    Exemplo prático de uso da classe
    """
    print("EXEMPLO DE USO - CLASSIFICAÇÃO DE EMAILS (SPAM vs NÃO-SPAM)")
    print("="*70)
    
    # Matriz de confusão exemplo:
    # - 85 emails não-spam classificados corretamente como não-spam (VN)
    # - 45 emails spam classificados corretamente como spam (VP)  
    # - 10 emails não-spam classificados incorretamente como spam (FP)
    # - 5 emails spam classificados incorretamente como não-spam (FN)
    
    vp = 45  # Spam detectado corretamente
    vn = 85  # Não-spam detectado corretamente  
    fp = 10  # Não-spam classificado como spam (falso alarme)
    fn = 5   # Spam não detectado (passou despercebido)
    
    # Criando o objeto e calculando as métricas
    metricas = MetricasClassificacao(vp, vn, fp, fn)
    metricas.exibir_relatorio()
    
    return metricas


def exemplo_interativo():
    """
    Permite ao usuário inserir seus próprios valores
    """
    print("\n" + "="*70)
    print("MODO INTERATIVO - INSIRA SEUS PRÓPRIOS VALORES")
    print("="*70)
    
    try:
        print("\nInsira os valores da sua matriz de confusão:")
        vp = int(input("Verdadeiros Positivos (VP): "))
        vn = int(input("Verdadeiros Negativos (VN): "))
        fp = int(input("Falsos Positivos (FP): "))
        fn = int(input("Falsos Negativos (FN): "))
        
        metricas = MetricasClassificacao(vp, vn, fp, fn)
        metricas.exibir_relatorio()
        
        return metricas
        
    except ValueError:
        print("Erro: Por favor, insira apenas números inteiros válidos.")
        return None


def exemplo_multiplos_casos():
    """
    Demonstra diferentes cenários de classificação
    """
    print("\n" + "="*70)
    print("COMPARAÇÃO DE DIFERENTES CENÁRIOS")
    print("="*70)
    
    cenarios = [
        {"nome": "Modelo Balanceado", "vp": 40, "vn": 40, "fp": 10, "fn": 10},
        {"nome": "Alta Precisão", "vp": 30, "vn": 50, "fp": 5, "fn": 15},
        {"nome": "Alta Sensibilidade", "vp": 40, "vn": 35, "fp": 15, "fn": 10},
        {"nome": "Modelo Conservador", "vp": 20, "vn": 60, "fp": 5, "fn": 15}
    ]
    
    for cenario in cenarios:
        print(f"\n{'-'*50}")
        print(f"CENÁRIO: {cenario['nome']}")
        print(f"{'-'*50}")
        
        metricas = MetricasClassificacao(
            cenario['vp'], cenario['vn'], 
            cenario['fp'], cenario['fn']
        )
        
        metricas.exibir_matriz_confusao()
        
        resultado = metricas.calcular_todas_metricas()
        print(f"\nResumo das Métricas:")
        for nome, valor in resultado.items():
            print(f"  {nome:20}: {valor:.3f} ({valor*100:.1f}%)")


if __name__ == "__main__":
    # Menu principal
    while True:
        print("\n" + "="*70)
        print("CALCULADORA DE MÉTRICAS DE CLASSIFICAÇÃO")
        print("="*70)
        print("1. Exemplo automático (Classificação de Spam)")
        print("2. Inserir valores personalizados")
        print("3. Comparar múltiplos cenários")
        print("4. Sair")
        
        try:
            opcao = input("\nEscolha uma opção (1-4): ")
            
            if opcao == "1":
                exemplo_uso()
            elif opcao == "2":
                exemplo_interativo()
            elif opcao == "3":
                exemplo_multiplos_casos()
            elif opcao == "4":
                print("Programa encerrado!")
                break
            else:
                print("Opção inválida! Escolha entre 1 e 4.")
                
        except KeyboardInterrupt:
            print("\nPrograma interrompido pelo usuário!")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
