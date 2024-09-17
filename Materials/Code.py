#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install pandas


# In[ ]:


import pandas as pd


# In[8]:


#
dados_df = pd.read_csv("Dados.csv")
display(dados_df) # Print the first / last 5 lines


# In[9]:


#
display(dados_df.head()) # Print the first 5 lines


# In[10]:


#
print(dados_df.shape) # Returns how many rows / columns there are in the table


# In[11]:


#
display(dados_df.describe()) # Overview


# In[12]:


#
precipitation = dados_df[['Year', 'Month', 'Precipitation (mm)']] # Isolates specific columns
display(precipitation)


# In[13]:


#
display(dados_df.loc[dados_df['Month'] == 6, ['Year', 'Month', 'Precipitation (mm)']]) # Filters specific values


# In[14]:


#
max_index = dados_df['Precipitation (mm)'].idxmax()
min_index = dados_df['Precipitation (mm)'].idxmin()
# Get the index of the row with the max value in the precipitation column


# In[15]:


#
max_row = dados_df.loc[max_index]
min_row = dados_df.loc[min_index]
# Get the entire row corresponding to the max and min values
#
print(f"Year/Month with Max Precipitation:\n", max_row)
print(f"Year/Month with Min Precipitation:\n", min_row)


# In[16]:


avg_precipitation_per_month = dados_df.groupby('Month')['Precipitation (mm)'].mean()
# Group by month, then calculate the mean of precipitation
#
print(avg_precipitation_per_month)


# In[17]:


yearly_precipitation = dados_df.groupby('Year')['Precipitation (mm)'].sum() 
# Group the data by year, then calculate the total precipitation for each year
display(yearly_precipitation)


# In[18]:


import matplotlib.pyplot as plt


# In[19]:


# Create a line plot (YoY)
plt.figure(figsize=(13,5)) # Set figure size
plt.plot(yearly_precipitation.index, yearly_precipitation.values, marker='.', linestyle='-', color='m')

# Add labels and a title
plt.xlabel('Year')
plt.ylabel('Total Precipitation (mm)')
plt.title('Total Precipitation by Year')

# Rotate x-axis labels to fit better
plt.xticks(rotation=45, ha='left')

# Show every 5th year label on the x-axis
plt.xticks(ticks=yearly_precipitation.index[::5], labels=yearly_precipitation.index[::5], rotation=45)

# Show the plot
plt.tight_layout() # Adjust layout to ensure labels are not cut off
plt.show()


# In[20]:


# Create a line plot (MoM)
plt.figure(figsize=(13,8))  # Set figure size
plt.plot(dados_df['Year'] + dados_df['Month'] / 12, dados_df['Precipitation (mm)'], marker='.', linestyle='-', color='m')

# Add labels and a title
plt.xlabel('Year')
plt.ylabel('Precipitation (mm)')
plt.title('Monthly Precipitation Variation')

# Format the x-axis to show years without overcrowding
plt.xticks(rotation=45, ha='left')

# Show the plot
plt.tight_layout()
plt.show()


# In[21]:


# Create a figure for the plot
plt.figure(figsize=(13,8))

# Define month names for labeling
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

# Plot lines
for month_num in range(1, 13):
    monthly_data = dados_df[dados_df['Month'] == month_num]
    
    # Add markers on the month of June
    if month_num == 6:
        plt.plot(monthly_data['Year'], monthly_data['Precipitation (mm)'], marker='o', linestyle='-', label=month_names[month_num-1])
    else:
        plt.plot(monthly_data['Year'], monthly_data['Precipitation (mm)'], linestyle='-', label=month_names[month_num-1])

# Highlight the 3 highest precipitation values in the data
top_3 = dados_df.nlargest(3, 'Precipitation (mm)')

# Annotate the top 3 highest points
for index, row in top_3.iterrows():
    plt.annotate(f'{row["Precipitation (mm)"]} mm', 
                 (row['Year'], row['Precipitation (mm)']),
                 textcoords="offset points", xytext=(0,10), ha='center',
                 fontsize=10, color='red', fontweight='bold')

# Add labels and a title
plt.xlabel('Year')
plt.ylabel('Precipitation (mm)')
plt.title('Monthly Precipitation (1998-2024)')

# Show legend to label the months
plt.legend()

# Format the x-axis to avoid overcrowding
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()


# In[22]:


# Create a figure for the plot
plt.figure(figsize=(13,10))

# Plot the full dataset
plt.plot(dados_df['Year'] + dados_df['Month'] / 12, dados_df['Precipitation (mm)'], linestyle='-', color='grey', linewidth=0.4, label='Overall Precipitation')

# Plot the month of June
june_data = dados_df[dados_df['Month'] == 6]
plt.plot(june_data['Year'] + june_data['Month'] / 12, june_data['Precipitation (mm)'], marker='o', linestyle='-', color='black', linewidth=3, markersize=6, label='June Precipitation')

# Find the top three highest June precipitation values
top_three_junes = june_data.nlargest(3, 'Precipitation (mm)')

# Plot markers on the top three Junes
for _, row in top_three_junes.iterrows():
    plt.plot(row['Year'] + row['Month'] / 12, row['Precipitation (mm)'], marker='o', color='green', markersize=9)
    plt.annotate(f"{row['Precipitation (mm)']} mm\n({int(row['Year'])})",
                 (row['Year'] + row['Month'] / 12, row['Precipitation (mm)']),
                 textcoords="offset points", xytext=(0,10), ha='center',
                 fontsize=10, color='green', fontweight='bold')

# Find the bottom three lowest June precipitation values
lowest_three_junes = june_data.nsmallest(3, 'Precipitation (mm)')

# Plot markers on the lowest three Junes
for _, row in lowest_three_junes.iterrows():
    plt.plot(row['Year'] + row['Month'] / 12, row['Precipitation (mm)'], marker='o', color='red', markersize=9)
    plt.annotate(f"{row['Precipitation (mm)']} mm\n({int(row['Year'])})",
                 (row['Year'] + row['Month'] / 12, row['Precipitation (mm)']),
                 textcoords="offset points", xytext=(0,-15), ha='center',
                 fontsize=10, color='red', fontweight='bold')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Precipitation (mm)')
plt.title('Precipitation Over Time')

# Adjust the y-axis limit to give more space at the bottom
plt.ylim(bottom=dados_df['Precipitation (mm)'].min() - 10)

# Customize x-axis ticks to show fewer years (e.g., every 5 years)
plt.xticks(ticks=range(dados_df['Year'].min(), dados_df['Year'].max()+1, 5), rotation=45)

# Show the legend
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()


# In[23]:


# Calculate the average precipitation per month
monthly_avg_precipitation = dados_df.groupby('Month')['Precipitation (mm)'].mean()

# Merge monthly avg precipitation back to the original df
dados_df = dados_df.merge(monthly_avg_precipitation.rename('Avg_Monthly_Precipitation'), on='Month')

# Determine if each month had more or less precipitation than the avg
dados_df['Precipitation_Comparison'] = dados_df['Precipitation (mm)'] - dados_df['Avg_Monthly_Precipitation']

# Summary
result = dados_df.groupby(['Year', 'Month']).agg({
    'Precipitation (mm)': 'sum',  # Total precipitation
    'Avg_Monthly_Precipitation': 'mean',  # Avg precipitation
    'Precipitation_Comparison': 'mean'  # How much more or less it rained compared to the average
}).reset_index()

print(result)


# In[24]:


# Aggregate precipitation by year to get yearly average
yearly_precipitation = dados_df.groupby('Year')['Precipitation (mm)'].mean().reset_index()
yearly_precipitation.rename(columns={'Precipitation (mm)': 'Avg_Yearly_Precipitation'}, inplace=True)
#
print(yearly_precipitation)


# In[25]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Calcular a precipitação total por ano e mês
monthly_precipitation = dados_df.groupby(['Year', 'Month'])['Precipitation (mm)'].sum().reset_index()

# Adicionar uma coluna para ordenar por ano e mês
monthly_precipitation['YearMonth'] = pd.to_datetime(monthly_precipitation[['Year', 'Month']].assign(DAY=1))

# Ordenar os dados para garantir que os meses estejam na ordem correta
monthly_precipitation = monthly_precipitation.sort_values('YearMonth')

# Carregar a paleta de cores
palette = sns.color_palette("Paired", 12)  # 12 cores para os 12 meses

# Configurar o gráfico
plt.figure(figsize=(15, 8))

# Criar o gráfico
for month in range(1, 13):  # Para cada mês de 1 a 12
    subset = monthly_precipitation[monthly_precipitation['Month'] == month]
    sns.scatterplot(data=subset, x='YearMonth', y='Precipitation (mm)', color=palette[month - 1], s=100, label=pd.to_datetime(f'2000-{month:02d}-01').strftime('%B'))

    # Adicionar as hastas em cinza escuro
    for i in range(len(subset)):
        plt.plot([subset['YearMonth'].iloc[i]] * 2,
                 [0, subset['Precipitation (mm)'].iloc[i]],
                 color='darkgray', linestyle='-', linewidth=1)

# Ajustar os labels do eixo x para mostrar apenas o ano
plt.xticks(ticks=pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                               end=monthly_precipitation['YearMonth'].max(), 
                               freq='Y'),
           labels=[dt.strftime('%Y') for dt in pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                                                             end=monthly_precipitation['YearMonth'].max(), 
                                                             freq='Y')],
           rotation=45, 
           ha='right')

plt.xlabel('Year', fontweight='bold')
plt.ylabel('Precipitation (mm)', fontweight='bold')
plt.title(f'Precipitation (mm) in São José do Rio Preto, Brazil (1998-2024)', fontweight='bold')
plt.legend(title='Month', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()

# Mostrar o gráfico
plt.show()


# In[27]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Calcular a precipitação total por ano e mês
monthly_precipitation = dados_df.groupby(['Year', 'Month'])['Precipitation (mm)'].sum().reset_index()

# Adicionar uma coluna para ordenar por ano e mês
monthly_precipitation['YearMonth'] = pd.to_datetime(monthly_precipitation[['Year', 'Month']].assign(DAY=1))

# Ordenar os dados para garantir que os meses estejam na ordem correta
monthly_precipitation = monthly_precipitation.sort_values('YearMonth')

# Calcular a média de precipitação por mês
monthly_avg_precipitation = dados_df.groupby('Month')['Precipitation (mm)'].mean()
average_precipitation = {month: monthly_avg_precipitation[month] for month in range(1, 13)}

# Criar uma figura com subplots
fig, axes = plt.subplots(4, 3, figsize=(20, 16), sharex=True, sharey=True)
axes = axes.flatten()  # Facilita a iteração sobre os subplots

# Definir o estilo de fundo
sns.set_theme(style="white")

# Definir as cores para os marcadores baseadas na comparação com a média
colors = {'below_avg': 'orange', 'above_avg': 'blue'}

# Criar um gráfico para cada mês
for month in range(1, 13):  # Para cada mês, de 1 a 12
    subset = monthly_precipitation[monthly_precipitation['Month'] == month].copy()
    ax = axes[month - 1]

    # Adicionar uma coluna 'color' com base na comparação com a média
    subset.loc[:, 'color'] = subset['Precipitation (mm)'].apply(
        lambda x: 'below_avg' if x < average_precipitation[month] else 'above_avg'
    )

    # Plotar os dados com cores individuais para os marcadores
    sns.scatterplot(data=subset, x='YearMonth', y='Precipitation (mm)', hue='color',
                    palette=colors, s=150, ax=ax, legend=False, zorder=5)

    # Adicionar as hastas pretas
    for i in range(len(subset)):
        ax.plot([subset['YearMonth'].iloc[i]] * 2,
                [0, subset['Precipitation (mm)'].iloc[i]],
                color='black', linestyle='-', linewidth=3.5, zorder=1)
    
    # Adicionar a linha vermelha para a média de precipitação
    avg_line_y = average_precipitation[month]
    ax.axhline(avg_line_y, color='red', linestyle='--', linewidth=2, zorder=3)
    
    # Adicionar o valor médio no canto superior direito
    ax.text(subset['YearMonth'].max(), avg_line_y * 1.05, f'{avg_line_y:.1f}', color='red', 
            ha='right', va='top', fontsize=12, fontweight='bold')
    
    # Ajustar o limite do eixo y para se ajustar bem aos dados
    ax.set_ylim(0, max(650, subset['Precipitation (mm)'].max() * 1.1))
    
    # Ajustar os labels do eixo x para mostrar apenas o ano
    ax.set_xticks(pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                                end=monthly_precipitation['YearMonth'].max(), 
                                freq='5Y'))
    ax.set_xticklabels([dt.strftime('%Y') for dt in pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                                                                    end=monthly_precipitation['YearMonth'].max(), 
                                                                    freq='5Y')], 
                       rotation=45, 
                       ha='right')
    
    # Adicionar linhas horizontais no eixo y para ajudar na leitura
    ax.yaxis.grid(True, linestyle='--', color='lightgray', alpha=0.6)

    # Configurar os rótulos e o título para cada gráfico
    ax.set_title(pd.to_datetime(f'2000-{month:02d}-01').strftime('%B'), fontsize=16, fontweight='bold')
    ax.set_xlabel('Year', fontsize=14, fontweight='bold')
    ax.set_ylabel('Precipitation (mm)', fontsize=14, fontweight='bold')

    # Adicionar uma borda leve em torno dos eixos
    for spine in ax.spines.values():
        spine.set_edgecolor('lightgray')
        spine.set_linewidth(1)

# Ajustar a legenda para mostrar apenas alguns anos
years = pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                      end=monthly_precipitation['YearMonth'].max(), 
                      freq='5Y').strftime('%Y').tolist()

# Adicionar uma legenda apenas uma vez, em um dos subplots
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['below_avg'], markersize=10, label='Below Avg'),
           plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['above_avg'], markersize=10, label='Above Avg')]

axes[0].legend(handles=handles, title='', fontsize='14', frameon=False)

# Ajustar o layout para reduzir o espaço em branco nas laterais
plt.tight_layout(rect=[0, 0, 0.9, 0.9])  # Ajustar o layout para remover espaço nas laterais

plt.show()


# In[28]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Calcular a precipitação total por ano e mês
monthly_precipitation = dados_df.groupby(['Year', 'Month'])['Precipitation (mm)'].sum().reset_index()

# Adicionar uma coluna para ordenar por ano e mês
monthly_precipitation['YearMonth'] = pd.to_datetime(monthly_precipitation[['Year', 'Month']].assign(DAY=1))

# Ordenar os dados para garantir que os meses estejam na ordem correta
monthly_precipitation = monthly_precipitation.sort_values('YearMonth')

# Calcular a média de precipitação por mês
monthly_avg_precipitation = dados_df.groupby('Month')['Precipitation (mm)'].mean()
average_precipitation = {month: monthly_avg_precipitation[month] for month in range(1, 13)}

# Criar uma figura com subplots
fig, axes = plt.subplots(4, 3, figsize=(20, 16), sharex=True, sharey=True)
axes = axes.flatten()  # Facilita a iteração sobre os subplots

# Definir o estilo de fundo
sns.set_theme(style="white")

# Definir as cores para os marcadores baseadas na comparação com a média
colors = {'below_avg': 'orange', 'above_avg': 'blue'}

# Criar um gráfico para cada mês
for month in range(1, 13):  # Para cada mês, de 1 a 12
    subset = monthly_precipitation[monthly_precipitation['Month'] == month].copy()
    ax = axes[month - 1]

    # Adicionar uma coluna 'color' com base na comparação com a média
    subset.loc[:, 'color'] = subset['Precipitation (mm)'].apply(
        lambda x: 'below_avg' if x < average_precipitation[month] else 'above_avg'
    )

    # Plotar a linha de tendência
    sns.lineplot(data=subset, x='YearMonth', y='Precipitation (mm)', ax=ax, color='gray', linestyle='--', linewidth=1, zorder=2)

    # Plotar o gráfico de área com matplotlib
    ax.fill_between(subset['YearMonth'], subset['Precipitation (mm)'], alpha=0.1, color='gray', zorder=1)

    # Plotar os dados com cores individuais para os marcadores
    sns.scatterplot(data=subset, x='YearMonth', y='Precipitation (mm)', hue='color',
                    palette=colors, s=200, ax=ax, legend=False, marker='o', zorder=5)

    # Adicionar as hastas pretas
    for i in range(len(subset)):
        ax.plot([subset['YearMonth'].iloc[i]] * 2,
                [0, subset['Precipitation (mm)'].iloc[i]],
                color='black', linestyle='-', linewidth=3.5, zorder=1)
    
    # Adicionar a linha vermelha para a média de precipitação
    avg_line_y = average_precipitation[month]
    ax.axhline(avg_line_y, color='red', linestyle='-', linewidth=3, zorder=3)
    
    # Adicionar o valor médio no canto superior direito
    ax.text(subset['YearMonth'].max(), avg_line_y * 1.05, f'{avg_line_y:.1f}', color='red', 
            ha='right', va='top', fontsize=12, fontweight='bold')
    
    # Ajustar o limite do eixo y para se ajustar bem aos dados
    ax.set_ylim(0, max(650, subset['Precipitation (mm)'].max() * 1.1))
    
    # Ajustar os labels do eixo x para mostrar apenas o ano
    ax.set_xticks(pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                                end=monthly_precipitation['YearMonth'].max(), 
                                freq='5Y'))
    ax.set_xticklabels([dt.strftime('%Y') for dt in pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                                                                    end=monthly_precipitation['YearMonth'].max(), 
                                                                    freq='5Y')], 
                       rotation=45, 
                       ha='right')
    
    # Adicionar linhas horizontais no eixo y para ajudar na leitura
    ax.yaxis.grid(True, linestyle='--', color='lightgray', alpha=0.6)

    # Configurar os rótulos e o título para cada gráfico
    ax.set_title(pd.to_datetime(f'2000-{month:02d}-01').strftime('%B'), fontsize=16, fontweight='bold')
    ax.set_xlabel('Year', fontsize=14, fontweight='bold')
    ax.set_ylabel('Precipitation (mm)', fontsize=14, fontweight='bold')

    # Adicionar uma borda leve em torno dos eixos
    for spine in ax.spines.values():
        spine.set_edgecolor('lightgray')
        spine.set_linewidth(1)

# Adicionar uma legenda apenas uma vez, em um dos subplots
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['below_avg'], markersize=10, label='Below Avg'),
           plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['above_avg'], markersize=10, label='Above Avg')]

axes[0].legend(handles=handles, title='', fontsize='14', frameon=False)

plt.show()


# In[29]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Calcular a precipitação total por ano e mês
monthly_precipitation = dados_df.groupby(['Year', 'Month'])['Precipitation (mm)'].sum().reset_index()

# Adicionar uma coluna para ordenar por ano e mês
monthly_precipitation['YearMonth'] = pd.to_datetime(monthly_precipitation[['Year', 'Month']].assign(DAY=1))

# Ordenar os dados para garantir que os meses estejam na ordem correta
monthly_precipitation = monthly_precipitation.sort_values('YearMonth')

# Calcular a média de precipitação por mês
monthly_avg_precipitation = dados_df.groupby('Month')['Precipitation (mm)'].mean()
average_precipitation = {month: monthly_avg_precipitation[month] for month in range(1, 13)}

# Criar uma figura com subplots
fig, axes = plt.subplots(3, 4, figsize=(20, 12), sharex=True, sharey=True)
axes = axes.flatten()  # Facilita a iteração sobre os subplots

# Definir o estilo de fundo
sns.set_theme(style="whitegrid")

# Definir as cores para os marcadores baseadas na comparação com a média
colors = {'below_avg': 'lightcoral', 'above_avg': 'skyblue'}

# Criar um gráfico para cada mês
for month in range(1, 13):  # Para cada mês, de 1 a 12
    subset = monthly_precipitation[monthly_precipitation['Month'] == month].copy()
    ax = axes[month - 1]

    # Adicionar uma coluna 'color' com base na comparação com a média
    subset.loc[:, 'color'] = subset['Precipitation (mm)'].apply(
        lambda x: 'below_avg' if x < average_precipitation[month] else 'above_avg'
    )

    # Plotar a linha de tendência
    sns.lineplot(data=subset, x='YearMonth', y='Precipitation (mm)', ax=ax, color='gray', linestyle='--', linewidth=1, zorder=2)

    # Plotar o gráfico de área com matplotlib
    ax.fill_between(subset['YearMonth'], subset['Precipitation (mm)'], alpha=0.1, color='gray', zorder=1)

    # Plotar os dados com cores individuais para os marcadores
    sns.scatterplot(data=subset, x='YearMonth', y='Precipitation (mm)', hue='color',
                    palette=colors, s=100, ax=ax, legend=False, marker='o', zorder=5)

    # Adicionar as hastas mais sutis
    for i in range(len(subset)):
        ax.plot([subset['YearMonth'].iloc[i]] * 2,
                [0, subset['Precipitation (mm)'].iloc[i]],
                color='black', linestyle=' ', linewidth=2, zorder=1)
    
    # Adicionar a linha vermelha para a média de precipitação
    avg_line_y = average_precipitation[month]
    ax.axhline(avg_line_y, color='red', linestyle='-', linewidth=2, zorder=3)
    
    # Adicionar o valor médio no canto superior direito
    ax.text(subset['YearMonth'].max(), avg_line_y * 1.05, f'{avg_line_y:.1f}', color='red', 
            ha='right', va='top', fontsize=10, fontweight='bold')
    
    # Ajustar o limite do eixo y para se ajustar bem aos dados
    ax.set_ylim(0, max(650, subset['Precipitation (mm)'].max() * 1.1))
    
    # Ajustar os labels do eixo x para mostrar apenas o ano
    ax.set_xticks(pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                                end=monthly_precipitation['YearMonth'].max(), 
                                freq='5Y'))
    ax.set_xticklabels([dt.strftime('%Y') for dt in pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                                                                    end=monthly_precipitation['YearMonth'].max(), 
                                                                    freq='5Y')], 
                       rotation=45, 
                       ha='right')
    
    # Adicionar linhas horizontais no eixo y para ajudar na leitura
    ax.yaxis.grid(True, linestyle='--', color='lightgray', alpha=0.6)

    # Configurar os rótulos e o título para cada gráfico
    ax.set_title(pd.to_datetime(f'2000-{month:02d}-01').strftime('%B'), fontsize=14, fontweight='bold')
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Precipitation (mm)', fontsize=12, fontweight='bold')

    # Adicionar uma borda leve em torno dos eixos
    for spine in ax.spines.values():
        spine.set_edgecolor('lightgray')
        spine.set_linewidth(1)

# Adicionar uma legenda apenas uma vez, em um dos subplots
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['below_avg'], markersize=10, label='Below Avg'),
           plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['above_avg'], markersize=10, label='Above Avg')]

axes[0].legend(handles=handles, title='', fontsize='12', frameon=False)

plt.tight_layout(rect=[0, 0, 0.95, 0.95])  # Ajustar o layout para remover espaço nas laterais

plt.show()


# In[30]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Calcular a precipitação total por ano e mês
monthly_precipitation = dados_df.groupby(['Year', 'Month'])['Precipitation (mm)'].sum().reset_index()

# Adicionar uma coluna para ordenar por ano e mês
monthly_precipitation['YearMonth'] = pd.to_datetime(monthly_precipitation[['Year', 'Month']].assign(DAY=1))

# Ordenar os dados para garantir que os meses estejam na ordem correta
monthly_precipitation = monthly_precipitation.sort_values('YearMonth')

# Calcular a média de precipitação por mês
monthly_avg_precipitation = dados_df.groupby('Month')['Precipitation (mm)'].mean()
average_precipitation = {month: monthly_avg_precipitation[month] for month in range(1, 13)}

# Criar uma figura com subplots
fig, axes = plt.subplots(4, 3, figsize=(16, 20), sharex=True, sharey=True)
axes = axes.flatten()  # Facilita a iteração sobre os subplots

# Definir o estilo de fundo
sns.set_theme(style="whitegrid")

# Definir as cores para os marcadores baseadas na comparação com a média
colors = {'below_avg': 'wheat', 'above_avg': 'skyblue'}

# Criar um gráfico para cada mês
for month in range(1, 13):  # Para cada mês, de 1 a 12
    subset = monthly_precipitation[monthly_precipitation['Month'] == month].copy()
    ax = axes[month - 1]

    # Adicionar uma coluna com base na comparação com a média
    subset.loc[:, 'color'] = subset['Precipitation (mm)'].apply(
        lambda x: 'below_avg' if x < average_precipitation[month] else 'above_avg'
    )

    # Plotar a linha de tendência
    sns.lineplot(data=subset, x='YearMonth', y='Precipitation (mm)', ax=ax, color='gray', linestyle='--', linewidth=1, zorder=2)

    # Plotar o gráfico de área com matplotlib
    ax.fill_between(subset['YearMonth'], subset['Precipitation (mm)'], alpha=0.1, color='gray', zorder=1)

    # Plotar os dados com cores individuais para os marcadores
    sns.scatterplot(data=subset, x='YearMonth', y='Precipitation (mm)', hue='color',
                    palette=colors, s=100, ax=ax, legend=False, marker='o', zorder=5)

    # Adicionar as hastas
    for i in range(len(subset)):
        ax.plot([subset['YearMonth'].iloc[i]] * 2,
                [0, subset['Precipitation (mm)'].iloc[i]],
                color='black', linestyle=' ', linewidth=2, zorder=1)
    
    # Adicionar a linha de tendência para a média de precipitação
    avg_line_y = average_precipitation[month]
    ax.axhline(avg_line_y, color='red', linestyle='-', linewidth=2, zorder=3)
    
    # Adicionar o valor médio fora do gráfico
    ax.text(subset['YearMonth'].max() + pd.DateOffset(days=10), avg_line_y, f'{avg_line_y:.1f}', color='red', 
            ha='left', va='center', fontsize=12, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))
    
    # Ajustar o limite do eixo y para se ajustar bem aos dados
    ax.set_ylim(0, max(650, subset['Precipitation (mm)'].max() * 1.1))
    
    # Ajustar os labels do eixo x para mostrar apenas o ano
    ax.set_xticks(pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                                end=monthly_precipitation['YearMonth'].max(), 
                                freq='5Y'))
    ax.set_xticklabels([dt.strftime('%Y') for dt in pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                                                                    end=monthly_precipitation['YearMonth'].max(), 
                                                                    freq='5Y')], 
                       rotation=45, 
                       ha='right')
    
    # Adicionar linhas horizontais no eixo y para ajudar na leitura
    ax.yaxis.grid(True, linestyle='--', color='lightgray', alpha=0.6)

    # Configurar os rótulos e o título para cada gráfico
    ax.set_title(pd.to_datetime(f'2000-{month:02d}-01').strftime('%B'), fontsize=14, fontweight='bold')
    ax.set_xlabel('Year', fontsize=14, fontweight='bold')
    ax.set_ylabel('Precipitation (mm)', fontsize=14, fontweight='bold')

    # Adicionar uma borda leve em torno dos eixos
    for spine in ax.spines.values():
        spine.set_edgecolor('lightgray')
        spine.set_linewidth(1)

# Adicionar legenda
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['below_avg'], markersize=10, label='below avg'),
           plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['above_avg'], markersize=10, label='above avg')]

axes[0].legend(handles=handles, title='', fontsize='12', frameon=False)

plt.tight_layout(rect=[0, 0, 0.95, 0.95])  # Ajustar o layout para remover espaço nas laterais


# In[31]:


import numpy as np
from sklearn.linear_model import LinearRegression

# Calculate the slope of the trend
def calculate_trend(data):
    # Reshape for sklearn
    X = np.arange(len(data)).reshape(-1, 1)
    y = data.values
    model = LinearRegression().fit(X, y)
    return model.coef_[0]  # Returns the slope of the trend

# Calculate the standard deviation of the data
def calculate_variation(data):
    return np.std(data)

# Calculate trends and variations for each month
trends = {}
variations = {}

for month in range(1, 13):
    subset = monthly_precipitation[monthly_precipitation['Month'] == month]
    
    # Calculate the trend (slope)
    trend = calculate_trend(subset['Precipitation (mm)'])
    trends[month] = trend
    
    # Calculate the variation (standard deviation)
    variation = calculate_variation(subset['Precipitation (mm)'])
    variations[month] = variation

# Identify the months with the biggest descent and increase in rainfall
biggest_descent_month = min(trends, key=trends.get)
biggest_increase_month = max(trends, key=trends.get)

# Identify the month with the biggest variation
biggest_variation_month = max(variations, key=variations.get)

print(f"Month with biggest descent in rainfall: {biggest_descent_month}")
print(f"Month with biggest increase in rainfall: {biggest_increase_month}")
print(f"Month with biggest variation in rainfall: {biggest_variation_month}")


# In[32]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Calcular a precipitação total (por ano e mês)
monthly_precipitation = dados_df.groupby(['Year', 'Month'])['Precipitation (mm)'].sum().reset_index()

# Adicionar uma coluna para ordenação
monthly_precipitation['YearMonth'] = pd.to_datetime(monthly_precipitation[['Year', 'Month']].assign(DAY=1))

# Ordenar os dados para garantir que os meses estejam na ordem correta
monthly_precipitation = monthly_precipitation.sort_values('YearMonth')

# Calcular a média de precipitação por mês
monthly_avg_precipitation = dados_df.groupby('Month')['Precipitation (mm)'].mean()
average_precipitation = {month: monthly_avg_precipitation[month] for month in range(1, 13)}

# Criar uma figura com subplots
fig, axes = plt.subplots(4, 3, figsize=(16, 20), sharex=True, sharey=True)
axes = axes.flatten()  # Facilita a iteração sobre os subplots

# Definir o estilo de fundo
sns.set_theme(style="whitegrid")

# Definir as cores para os marcadores baseadas na comparação com a média
colors = {'below_avg': 'wheat', 'above_avg': 'skyblue'} # Cores claras ajudam a manter o gráfico minimalista

# Criar os gráficos
for month in range(1, 13):  # Para cada mês, de 1 a 12
    subset = monthly_precipitation[monthly_precipitation['Month'] == month].copy()
    ax = axes[month - 1]

    # Adicionar uma coluna com base na comparação com a média
    subset.loc[:, 'color'] = subset['Precipitation (mm)'].apply(
        lambda x: 'below_avg' if x < average_precipitation[month] else 'above_avg'
    )

    # Plotar a linha de tendência
    sns.lineplot(data=subset, x='YearMonth', y='Precipitation (mm)', ax=ax, color='gray', linestyle='--', linewidth=1, zorder=2)

    # Plotar o gráfico de área
    ax.fill_between(subset['YearMonth'], subset['Precipitation (mm)'], alpha=0.1, color='gray', zorder=1)

    # Plotar os dados com cores individuais para os marcadores
    sns.scatterplot(data=subset, x='YearMonth', y='Precipitation (mm)', hue='color',
                    palette=colors, s=100, ax=ax, legend=False, marker='o', zorder=5)

    # Adicionar as hastas
    for i in range(len(subset)):
        ax.plot([subset['YearMonth'].iloc[i]] * 2,
                [0, subset['Precipitation (mm)'].iloc[i]],
                color='white', linestyle=' ', linewidth=2, zorder=1) # Deixei-as invisíveis para melhor visualização
    
    # Adicionar a linha de tendência para a média de precipitação
    avg_line_y = average_precipitation[month]
    ax.axhline(avg_line_y, color='red', linestyle='-', linewidth=2, zorder=3)
    
    # Adicionar o valor para a média de precipitação 
    ax.text(subset['YearMonth'].max() + pd.DateOffset(days=10), avg_line_y, f'{avg_line_y:.1f}', color='red', 
            ha='left', va='center', fontsize=12, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))
    
    # Ajustar o limite do eixo y para se ajustar bem aos dados
    ax.set_ylim(0, max(650, subset['Precipitation (mm)'].max() * 1.1))
    
    # Ajustar os labels do eixo x para mostrar apenas o ano
    ax.set_xticks(pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                                end=monthly_precipitation['YearMonth'].max(), 
                                freq='5Y'))
    ax.set_xticklabels([dt.strftime('%Y') for dt in pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                                                                    end=monthly_precipitation['YearMonth'].max(), 
                                                                    freq='5Y')], 
                       rotation=65, 
                       ha='right')
    
    # Adicionar linhas horizontais no eixo y para ajudar na leitura
    ax.yaxis.grid(True, linestyle='--', color='lightgray', alpha=0.6)

    # Configurar os rótulos e o título para cada gráfico
    ax.set_title(pd.to_datetime(f'2000-{month:02d}-01').strftime('%B'), fontsize=14, fontweight='bold')
    ax.set_xlabel('Year', fontsize=14, fontweight='bold')
    ax.set_ylabel('Precipitation (mm)', fontsize=14, fontweight='bold')

    # Adicionar uma borda leve em torno dos eixos
    for spine in ax.spines.values():
        spine.set_edgecolor('lightgray')
        spine.set_linewidth(1)

# Adicionar as anotações para os meses de Janeiro e Dezembro
biggest_descent_month = monthly_precipitation.loc[monthly_precipitation['YearMonth'].dt.month == 1, 'Month'].iloc[0]
biggest_variation_month = monthly_precipitation.loc[monthly_precipitation['YearMonth'].dt.month == 12, 'Month'].iloc[0]
#
axes[0].annotate(f'Biggest Rainfall\nVariation', 
                  xy=(0.05, 0.95), xycoords='axes fraction', fontsize=10, color='black',
                  bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
#
axes[-1].annotate(f'Biggest Rainfall\nIncrease', 
                  xy=(0.05, 0.95), xycoords='axes fraction', fontsize=10, color='black',
                  bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))

# Adicionar a legenda
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['below_avg'], markersize=10, label='below avg'),
           plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['above_avg'], markersize=10, label='above avg')]

axes[0].legend(handles=handles, title='', fontsize='12', frameon=False)

# Adicionar título e fonte
fig.suptitle("Precipitation variation in São José do Rio Preto, Brazil (from 1998-2024)", fontsize=16, fontweight='bold')
plt.figtext(0.5, 0.02, 'Source: Portal Agrometeorológico e Hidrológico do Estado de São Paulo', ha='center', fontsize=12, color='black')

plt.tight_layout(rect=[0, 0.05, 0.95, 0.95])  # Ajustar o layout para remover espaço nas laterais

plt.show()


# In[33]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Calcular a precipitação total (por ano e mês)
monthly_precipitation = dados_df.groupby(['Year', 'Month'])['Precipitation (mm)'].sum().reset_index()

# Adicionar uma coluna para ordenação
monthly_precipitation['YearMonth'] = pd.to_datetime(monthly_precipitation[['Year', 'Month']].assign(DAY=1))

# Ordenar os dados para garantir que os meses estejam na ordem correta
monthly_precipitation = monthly_precipitation.sort_values('YearMonth')

# Calcular a média de precipitação por mês
monthly_avg_precipitation = dados_df.groupby('Month')['Precipitation (mm)'].mean()
average_precipitation = {month: monthly_avg_precipitation[month] for month in range(1, 13)}

# Criar uma figura com subplots
fig, axes = plt.subplots(4, 3, figsize=(18, 24), sharex=True, sharey=True)
axes = axes.flatten()  # Facilita a iteração sobre os subplots

# Definir o estilo de fundo
sns.set_theme(style="whitegrid")

# Definir as cores para os marcadores baseadas na comparação com a média
colors = {'below_avg': 'wheat', 'above_avg': 'skyblue'}

# Criar os gráficos
for month in range(1, 13):  # Para cada mês, de 1 a 12
    subset = monthly_precipitation[monthly_precipitation['Month'] == month].copy()
    ax = axes[month - 1]

    # Adicionar uma coluna com base na comparação com a média
    subset.loc[:, 'color'] = subset['Precipitation (mm)'].apply(
        lambda x: 'below_avg' if x < average_precipitation[month] else 'above_avg'
    )

    # Plotar a linha de tendência
    sns.lineplot(data=subset, x='YearMonth', y='Precipitation (mm)', ax=ax, color='gray', linestyle='--', linewidth=1, zorder=2)

    # Plotar o gráfico de área
    ax.fill_between(subset['YearMonth'], subset['Precipitation (mm)'], alpha=0.1, color='gray', zorder=1)

    # Plotar os dados com cores individuais para os marcadores
    sns.scatterplot(data=subset, x='YearMonth', y='Precipitation (mm)', hue='color',
                    palette=colors, s=100, ax=ax, legend=False, marker='o', zorder=5)

    # Adicionar as hastas
    for i in range(len(subset)):
        ax.plot([subset['YearMonth'].iloc[i]] * 2,
                [0, subset['Precipitation (mm)'].iloc[i]],
                color='white', linestyle=' ', linewidth=2, zorder=1)
    
    # Adicionar a linha de tendência para a média de precipitação
    avg_line_y = average_precipitation[month]
    ax.axhline(avg_line_y, color='red', linestyle='-', linewidth=2, zorder=3)
    
    # Adicionar o valor para a média de precipitação 
    ax.text(subset['YearMonth'].max() + pd.DateOffset(days=20), avg_line_y, f'{avg_line_y:.1f}', color='red', 
            ha='left', va='center', fontsize=14, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))
    
    # Ajustar o limite do eixo y para se ajustar bem aos dados
    ax.set_ylim(0, max(650, subset['Precipitation (mm)'].max() * 1.1))
    
    # Ajustar os labels do eixo x para mostrar apenas o ano
    ax.set_xticks(pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                                end=monthly_precipitation['YearMonth'].max(), 
                                freq='5Y'))
    ax.set_xticklabels([dt.strftime('%Y') for dt in pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                                                                    end=monthly_precipitation['YearMonth'].max(), 
                                                                    freq='5Y')], 
                       rotation=45, 
                       ha='right', fontsize=12)
    
    # Adicionar linhas horizontais no eixo y para ajudar na leitura
    ax.yaxis.grid(True, linestyle='--', color='lightgray', alpha=0.7)

    # Configurar os rótulos e o título para cada gráfico
    ax.set_title(pd.to_datetime(f'2000-{month:02d}-01').strftime('%B'), fontsize=16, fontweight='bold')
    ax.set_xlabel('Year', fontsize=14, fontweight='bold')
    ax.set_ylabel('Precipitation (mm)', fontsize=14, fontweight='bold')

    # Adicionar uma borda leve em torno dos eixos
    for spine in ax.spines.values():
        spine.set_edgecolor('lightgray')
        spine.set_linewidth(1)

# Adicionar as anotações para os meses de Janeiro e Dezembro
axes[0].annotate(f'Biggest Rainfall\nDescent', 
                  xy=(0.05, 0.95), xycoords='axes fraction', fontsize=12, color='black',
                  bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
#
axes[-1].annotate(f'Biggest Rainfall\nIncrease', 
                  xy=(0.05, 0.95), xycoords='axes fraction', fontsize=12, color='black',
                  bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))

# Adicionar a legenda
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['below_avg'], markersize=10, label='below avg'),
           plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['above_avg'], markersize=10, label='above avg')]

axes[0].legend(handles=handles, title='', fontsize='12', frameon=False)

# Adicionar título e fonte
fig.suptitle("Precipitation variation in São José do Rio Preto, Brazil (from 1998-2024)", fontsize=18, fontweight='bold')
plt.figtext(0.5, 0.02, 'Source: Portal Agrometeorológico e Hidrológico do Estado de São Paulo', ha='center', fontsize=14, color='black')

plt.tight_layout(rect=[0, 0.05, 0.95, 0.95])  # Ajustar o layout para remover espaço nas laterais

plt.show()


# In[34]:


ls /Library/Fonts /System/Library/Fonts ~/Library/Fonts


# In[62]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

# Escolher a fonte
mpl.rcParams['font.family'] = 'Avenir'

# Criar uma figura com subplots
fig, axes = plt.subplots(4, 3, figsize=(18, 24), sharex=True, sharey=True)
axes = axes.flatten()  # Facilita a iteração sobre os subplots

# Definir o estilo de fundo
sns.set_theme(style="whitegrid")

# Definir as cores para os marcadores baseadas na comparação com a média
colors = {'below_avg': 'lightsalmon', 'above_avg': 'lightskyblue'}

# Criar os gráficos
for month in range(1, 13):  # Para cada mês, de 1 a 12
    subset = monthly_precipitation[monthly_precipitation['Month'] == month].copy()
    ax = axes[month - 1]

    # Adicionar uma coluna com base na comparação com a média
    subset.loc[:, 'color'] = subset['Precipitation (mm)'].apply(
        lambda x: 'below_avg' if x < average_precipitation[month] else 'above_avg'
    )

    # Plotar as linhas
    sns.lineplot(data=subset, x='YearMonth', y='Precipitation (mm)', ax=ax, color='gray', linestyle='--', linewidth=1, zorder=2)

    # Plotar a área
    ax.fill_between(subset['YearMonth'], subset['Precipitation (mm)'], alpha=0.1, color='gray', zorder=1)

    # Plotar os dados com cores individuais para os marcadores
    sns.scatterplot(data=subset, x='YearMonth', y='Precipitation (mm)', hue='color',
                    palette=colors, s=100, ax=ax, legend=False, marker='o', zorder=5)

    # Adicionar as hastas
    for i in range(len(subset)):
        ax.plot([subset['YearMonth'].iloc[i]] * 2,
                [0, subset['Precipitation (mm)'].iloc[i]],
                color='white', linestyle=' ', linewidth=2, zorder=1)  # Deixei-as ocultas para melhor visualização
    
    # Adicionar a linha de tendência para a média de precipitação
    avg_line_y = average_precipitation[month]
    ax.axhline(avg_line_y, color='crimson', linestyle='-', linewidth=2, zorder=3)
    
    # Adicionar o valor para a média de precipitação 
    ax.text(subset['YearMonth'].max() + pd.DateOffset(days=20), avg_line_y, f'{avg_line_y:.1f}', color='crimson', 
            ha='left', va='center', fontsize=16, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8),
            fontfamily='Avenir')
    
    # Ajustar o limite do eixo y para se ajustar bem aos dados
    ax.set_ylim(0, max(650, subset['Precipitation (mm)'].max() * 1.1))
    
    # Ajustar os labels do eixo x para mostrar apenas o ano
    ax.set_xticks(pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                                end=monthly_precipitation['YearMonth'].max(), 
                                freq='5Y'))
    ax.set_xticklabels([dt.strftime('%Y').upper() for dt in pd.date_range(start=monthly_precipitation['YearMonth'].min(), 
                                                                    end=monthly_precipitation['YearMonth'].max(), 
                                                                    freq='5Y')], 
                       rotation=45, 
                       ha='right', fontsize=14, fontfamily='Avenir')
    
    # Adicionar linhas horizontais no eixo y para ajudar na leitura
    ax.yaxis.grid(True, linestyle='--', color='lightgray', alpha=0.7)

    # Configurar os rótulos e o título para cada gráfico
    ax.set_title(pd.to_datetime(f'2000-{month:02d}-01').strftime('%B').upper(), fontsize=16, fontweight='bold', fontfamily='Avenir')
    ax.set_xlabel('YEAR'.upper(), fontsize=14, fontweight='bold', fontfamily='Avenir Next')
    ax.set_ylabel('PRECIPITATION (MM)'.upper(), fontsize=14, fontweight='bold', fontfamily='Avenir Next')

    # Adicionar uma borda leve em torno dos eixos
    for spine in ax.spines.values():
        spine.set_edgecolor('lightgray')
        spine.set_linewidth(1)

# Adicionar as anotações para os meses de Janeiro e Dezembro
axes[0].annotate(f'BIGGEST RAINFALL\nVARIATION', 
                  xy=(0.05, 0.95), xycoords='axes fraction', fontsize=12, color='black',
                  bbox=dict(facecolor='white', edgecolor='none', alpha=0.7),
                  fontfamily='Avenir')
#
axes[-1].annotate(f'BIGGEST RAINFALL\nINCREASE', 
                  xy=(0.05, 0.95), xycoords='axes fraction', fontsize=12, color='black',
                  bbox=dict(facecolor='white', edgecolor='none', alpha=0.7),
                  fontfamily='Avenir')

# Adicionar a legenda
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['below_avg'], markersize=10, label='BELOW AVG'),
           plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors['above_avg'], markersize=10, label='ABOVE AVG')]

axes[0].legend(handles=handles, title='', fontsize='14', frameon=False, 
                prop={'family': 'Avenir'})

# Adicionar título e fonte em maiúsculas
fig.suptitle("PRECIPITATION VARIATION IN SÃO JOSÉ DO RIO PRETO, BRAZIL\n(1998-2024)".upper(), fontsize=24, fontweight='bold', fontfamily='Avenir Next')
plt.figtext(0.95, 0.02, 'Source: Portal Agrometeorológico e Hidrológico do Estado de São Paulo'.upper(), 
            ha='right', fontsize=14, color='black', fontfamily='Avenir', fontstyle='italic')

# Ajustar o layout para remover espaço nas laterais
plt.tight_layout(rect=[0, 0.05, 0.95, 0.95])

# Salvar o gráfico em alta qualidade
title = "PRECIPITATION_VARIATION".replace("\n", "_").replace(" ", "_")
plt.savefig(f"{title}.png", format='png', dpi=300, bbox_inches='tight')

# Exibir o gráfico
plt.show()


# In[90]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

# Definir a fonte
mpl.rcParams['font.family'] = 'Avenir'

# Criar uma figura com subplots
fig, axes = plt.subplots(4, 3, figsize=(18, 24), sharex=True, sharey=True)
axes = axes.flatten()  # Facilita a iteração sobre os subplots

# Definir o estilo de fundo
sns.set_theme(style="white")

# Calcular a média mínima e máxima para cada mês ao longo dos anos
monthly_avg_min_temp = dados_df.groupby('Month')['Min Avg Temperature (°C)'].mean()
monthly_avg_max_temp = dados_df.groupby('Month')['Max Avg Temperature (°C)'].mean()

# Criar os gráficos
for month in range(1, 13):  # Para cada mês de 1 a 12
    subset = dados_df[dados_df['Month'] == month].copy()
    ax = axes[month - 1]

    # Plotar a linha de tendência da temperatura média máxima
    ax.plot(subset['Year'], subset['Max Avg Temperature (°C)'], color='lightsalmon', linestyle='-', linewidth=2, zorder=2)
    
    # Plotar a linha de tendência da temperatura média mínima
    ax.plot(subset['Year'], subset['Min Avg Temperature (°C)'], color='lightskyblue', linestyle='-', linewidth=2, zorder=2)

    # Preencher a área entre os marcadores
    ax.fill_between(subset['Year'], subset['Min Avg Temperature (°C)'], subset['Max Avg Temperature (°C)'],
                    color='lightgray', alpha=0.3, zorder=1)
    
    # Plotar as hastes com temperatura máxima e mínima
    for i in range(len(subset)):
        ax.plot([subset['Year'].iloc[i]] * 2,
                [subset['Min Avg Temperature (°C)'].iloc[i], subset['Max Avg Temperature (°C)'].iloc[i]],
                color='whitesmoke', linestyle='-', linewidth=2.5, zorder=1)
        ax.fill_between([subset['Year'].iloc[i]] * 2,
                        subset['Min Avg Temperature (°C)'].iloc[i], subset['Max Avg Temperature (°C)'].iloc[i],
                        color='lightgray', alpha=0.5)
        
        # Marcador para temperatura mínima
        ax.scatter(subset['Year'].iloc[i], subset['Min Avg Temperature (°C)'].iloc[i], color='lightskyblue', s=100, zorder=5)
        # Marcador para temperatura máxima
        ax.scatter(subset['Year'].iloc[i], subset['Max Avg Temperature (°C)'].iloc[i], color='lightsalmon', s=100, zorder=5)

    # Adicionar linhas de tendência para a média mínima e máxima
    min_avg_line = monthly_avg_min_temp[month]
    max_avg_line = monthly_avg_max_temp[month]
    ax.axhline(min_avg_line, color='deepskyblue', linestyle='--', linewidth=2, zorder=3)
    ax.axhline(max_avg_line, color='darksalmon', linestyle='--', linewidth=2, zorder=3)

    # Adicionar o valor das médias no canto superior direito
    ax.text(subset['Year'].max() + 0.5, min_avg_line, f'{min_avg_line:.1f}°C', fontfamily='Avenir Next', color='deepskyblue', 
            ha='left', va='center', fontsize=16, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))
    ax.text(subset['Year'].max() + 0.5, max_avg_line, f'{max_avg_line:.1f}°C', fontfamily='Avenir Next', color='darksalmon', 
            ha='left', va='center', fontsize=16, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))

    # Ajustar os labels do eixo x para mostrar apenas o ano
    ax.set_xticks(subset['Year'][::5])
    ax.set_xticklabels(subset['Year'][::5], rotation=45, ha='right', fontsize=14, fontfamily='Avenir')

    # Ajustar os limites do eixo y
    ax.set_ylim(7, 50)

    # Configurar os rótulos e o título para cada gráfico
    if month in [1, 4, 7, 10]:
        ax.set_ylabel('Temperature (°C)'.upper(), fontsize=14, fontweight='bold', fontfamily='Avenir Next')
    else:
        ax.set_ylabel('')

    if month in [10, 11, 12]:
        ax.set_xlabel('Year'.upper(), fontsize=14, fontweight='bold', fontfamily='Avenir Next')
    else:
        ax.set_xlabel('')

    ax.set_title(pd.to_datetime(f'2000-{month:02d}-01').strftime('%B').upper(), fontsize=16, fontweight='bold', fontfamily='Avenir')

    # Remover o grid e adicionar bordas nos eixos X e Y
    ax.grid(False)
    for spine in ax.spines.values():
        spine.set_edgecolor('lightgray')
        spine.set_linewidth(1)

# Adicionar título e fonte
fig.suptitle("AVERAGE TEMPERATURE VARIATION IN SÃO JOSÉ DO RIO PRETO, BRAZIL\n(1998-2024)", fontsize=24, fontweight='bold', fontfamily='Avenir Next')

# Adicionar a legenda
handles = [
    plt.Line2D([0], [0], color='lightsalmon', linewidth=2, linestyle='-', label='Mean Max Temp'),
    plt.Line2D([0], [0], color='lightskyblue', linewidth=2, linestyle='-', label='Mean Min Temp'),
    plt.Line2D([0], [0], color='deepskyblue', linewidth=2, linestyle='--', label='Avg Min Temp'),
    plt.Line2D([0], [0], color='darksalmon', linewidth=2, linestyle='--', label='Avg Max Temp')
]

fig.legend(handles=handles, loc='lower left', bbox_to_anchor=(0.01, 0.01), fontsize=12, title='Legend', title_fontsize='12', frameon=False, ncol=2)

plt.figtext(0.95, 0.02, 'Source: Portal Agrometeorológico e Hidrológico do Estado de São Paulo'.upper(), 
            ha='right', fontsize=14, color='black', fontstyle='italic', fontfamily='Avenir')

# Ajustar o layout para remover espaços
plt.tight_layout(rect=[0, 0.05, 0.93, 0.95])

# Salvar o gráfico em alta qualidade
plt.savefig("TEMPERATURE_VARIATION.png", format='png', dpi=300, bbox_inches='tight')

# Exibir o gráfico
plt.show()


# In[96]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

# Definir a fonte
mpl.rcParams['font.family'] = 'Avenir'

# Criar uma figura com subplots
fig, axes = plt.subplots(4, 3, figsize=(18, 24), sharex=True, sharey=True)
axes = axes.flatten()  # Facilita a iteração sobre os subplots

# Definir o estilo de fundo
sns.set_theme(style="white")

# Calcular a média mínima e máxima para cada mês ao longo dos anos
monthly_avg_min_humidity = dados_df.groupby('Month')['Min Avg Air Humidity (%)'].mean()
monthly_avg_max_humidity = dados_df.groupby('Month')['Max Avg Air Humidity (%)'].mean()

# Criar os gráficos
for month in range(1, 13):  # Para cada mês de 1 a 12
    subset = dados_df[dados_df['Month'] == month].copy()
    ax = axes[month - 1]

    # Plotar a linha de tendência da umidade média máxima
    ax.plot(subset['Year'], subset['Max Avg Air Humidity (%)'], color='lightskyblue', linestyle='-', linewidth=2, zorder=2)
    
    # Plotar a linha de tendência da umidade média mínima
    ax.plot(subset['Year'], subset['Min Avg Air Humidity (%)'], color='lightsalmon', linestyle='-', linewidth=2, zorder=2)

    # Preencher a área entre os marcadores
    ax.fill_between(subset['Year'], subset['Min Avg Air Humidity (%)'], subset['Max Avg Air Humidity (%)'],
                    color='lightgray', alpha=0.3, zorder=1)
    
    # Plotar as hastes com umidade máxima e mínima
    for i in range(len(subset)):
        ax.plot([subset['Year'].iloc[i]] * 2,
                [subset['Min Avg Air Humidity (%)'].iloc[i], subset['Max Avg Air Humidity (%)'].iloc[i]],
                color='whitesmoke', linestyle='-', linewidth=2.5, zorder=1)
        ax.fill_between([subset['Year'].iloc[i]] * 2,
                        subset['Min Avg Air Humidity (%)'].iloc[i], subset['Max Avg Air Humidity (%)'].iloc[i],
                        color='lightgray', alpha=0.5)
        
        # Marcador para umidade mínima
        ax.scatter(subset['Year'].iloc[i], subset['Min Avg Air Humidity (%)'].iloc[i], color='lightsalmon', s=100, zorder=5)
        # Marcador para umidade máxima
        ax.scatter(subset['Year'].iloc[i], subset['Max Avg Air Humidity (%)'].iloc[i], color='lightskyblue', s=100, zorder=5)

    # Adicionar linhas de tendência para a média mínima e máxima
    min_avg_line = monthly_avg_min_humidity[month]
    max_avg_line = monthly_avg_max_humidity[month]
    ax.axhline(min_avg_line, color='darksalmon', linestyle='--', linewidth=2, zorder=3)
    ax.axhline(max_avg_line, color='deepskyblue', linestyle='--', linewidth=2, zorder=3)

    # Adicionar o valor das médias no canto superior direito
    ax.text(subset['Year'].max() + 0.5, min_avg_line, f'{min_avg_line:.1f}%', fontfamily='Avenir Next', color='darksalmon', 
            ha='left', va='center', fontsize=16, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))
    ax.text(subset['Year'].max() + 0.5, max_avg_line, f'{max_avg_line:.1f}%', fontfamily='Avenir Next', color='deepskyblue', 
            ha='left', va='center', fontsize=16, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))

    # Ajustar os labels do eixo x para mostrar apenas o ano
    ax.set_xticks(subset['Year'][::5])
    ax.set_xticklabels(subset['Year'][::5], rotation=45, ha='right', fontsize=14, fontfamily='Avenir')

    # Ajustar os limites do eixo y
    ax.set_ylim(0, 100)

    # Configurar os rótulos e o título para cada gráfico
    if month in [1, 4, 7, 10]:
        ax.set_ylabel('Humidity (%)'.upper(), fontsize=14, fontweight='bold', fontfamily='Avenir Next')
    else:
        ax.set_ylabel('')

    if month in [10, 11, 12]:
        ax.set_xlabel('Year'.upper(), fontsize=14, fontweight='bold', fontfamily='Avenir Next')
    else:
        ax.set_xlabel('')

    ax.set_title(pd.to_datetime(f'2000-{month:02d}-01').strftime('%B').upper(), fontsize=16, fontweight='bold', fontfamily='Avenir')

    # Remover o grid e adicionar bordas nos eixos X e Y
    ax.grid(False)
    for spine in ax.spines.values():
        spine.set_edgecolor('lightgray')
        spine.set_linewidth(1)

# Adicionar título e fonte
fig.suptitle("AVERAGE AIR HUMIDITY VARIATION IN SÃO JOSÉ DO RIO PRETO, BRAZIL\n(1998-2024)", fontsize=24, fontweight='bold', fontfamily='Avenir Next')

# Adicionar a legenda
handles = [
    plt.Line2D([0], [0], color='lightskyblue', linewidth=2, linestyle='-', label='Max Avg Humidity'),
    plt.Line2D([0], [0], color='lightsalmon', linewidth=2, linestyle='-', label='Min Avg Humidity'),
    plt.Line2D([0], [0], color='darksalmon', linewidth=2, linestyle='--', label='Avg Min Humidity'),
    plt.Line2D([0], [0], color='deepskyblue', linewidth=2, linestyle='--', label='Avg Max Humidity')
]

fig.legend(handles=handles, loc='lower left', bbox_to_anchor=(0.01, 0.01), fontsize=12, title='Legend', title_fontsize='12', frameon=False, ncol=2)

plt.figtext(0.95, 0.02, 'Source: Portal Agrometeorológico e Hidrológico do Estado de São Paulo'.upper(), 
            ha='right', fontsize=14, color='black', fontstyle='italic', fontfamily='Avenir')

# Ajustar o layout para remover espaços
plt.tight_layout(rect=[0, 0.05, 0.93, 0.95])

# Salvar o gráfico em alta qualidade
plt.savefig("HUMIDITY_VARIATION.png", format='png', dpi=300, bbox_inches='tight')

# Exibir o gráfico
plt.show()


# In[ ]:




