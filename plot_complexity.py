import matplotlib.pyplot as plt
import numpy as np

# Dados da tabela de complexidade
n_values = [8, 16, 32, 64, 128, 256, 512]

# Funções de complexidade calculadas
o_1 = [1] * len(n_values)  # O(1) - constante
o_log_n = [3, 4, 5, 6, 7, 8, 9]  # O(log n) - logaritmo base 2
o_n = n_values  # O(n) - linear
o_n_log_n = [24, 64, 160, 384, 896, 2048, 4608]  # O(n log n)
o_n2 = [n**2 for n in n_values]  # O(n²) - quadrática
o_n3 = [n**3 for n in n_values]  # O(n³) - cúbica

# O(2^n) - exponencial (usando valores aproximados para visualização)
o_2n = [2**8, 2**16, 2**32, 2**64, 2**128, 2**256, 2**512]

# Configurar o gráfico
plt.figure(figsize=(12, 8))
plt.style.use('default')

# Plotar cada função com cores diferentes
plt.semilogy(n_values, o_1, 'o-', label='O(1) - Constante', linewidth=2, markersize=6)
plt.semilogy(n_values, o_log_n, 's-', label='O(log n) - Logarítmica', linewidth=2, markersize=6)
plt.semilogy(n_values, o_n, '^-', label='O(n) - Linear', linewidth=2, markersize=6)
plt.semilogy(n_values, o_n_log_n, 'v-', label='O(n log n) - Sublinear', linewidth=2, markersize=6)
plt.semilogy(n_values, o_n2, 'd-', label='O(n²) - Quadrática', linewidth=2, markersize=6)
plt.semilogy(n_values, o_n3, 'p-', label='O(n³) - Cúbica', linewidth=2, markersize=6)

# Para O(2^n), plotamos apenas até n=32 para não quebrar o gráfico
n_exp = n_values[:3]
o_2n_partial = o_2n[:3]
plt.semilogy(n_exp, o_2n_partial, 'h-', label='O(2^n) - Exponencial*', linewidth=2, markersize=6, color='red')

# Configurações do gráfico
plt.xlabel('Tamanho da Entrada (n)', fontsize=12, fontweight='bold')
plt.ylabel('Operações (Escala Logarítmica)', fontsize=12, fontweight='bold')
plt.title('Comparação Visual das Funções de Complexidade de Algoritmos', 
          fontsize=14, fontweight='bold', pad=20)

# Configurar grid e legenda
plt.grid(True, alpha=0.3)
plt.legend(loc='upper left', fontsize=10)

# Configurar eixos
plt.xlim(0, 550)
plt.xticks(n_values)

# Adicionar anotações explicativas
plt.annotate('Exponencial cresce muito\nrapidamente - mostrado só até n=32', 
             xy=(32, 2**32), xytext=(200, 2**25),
             arrowprops=dict(arrowstyle='->', color='red', alpha=0.7),
             fontsize=9, ha='center',
             bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7))

plt.annotate('Funções eficientes\n(O(1), O(log n), O(n))', 
             xy=(256, 256), xytext=(400, 10),
             arrowprops=dict(arrowstyle='->', color='green', alpha=0.7),
             fontsize=9, ha='center',
             bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen', alpha=0.7))

# Ajustar layout e salvar
plt.tight_layout()
plt.savefig('complexity_chart.jpg', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.show()

print("Gráfico salvo como 'complexity_chart.jpg'")
print("\nObservações:")
print("- O gráfico usa escala logarítmica para visualizar todas as funções")
print("- O(2^n) é mostrado apenas até n=32 pois cresce exponencialmente")
print("- Para n=512, O(2^n) seria aproximadamente 1.3 × 10^154 operações!")
