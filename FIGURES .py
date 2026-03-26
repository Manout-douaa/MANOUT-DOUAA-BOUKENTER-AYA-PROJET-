"""
GÉNÉRATION DES FIGURES POUR LE PROJET
AUTEURS : MANOUT Douaa, BOUKENTER Aya
ENCG Settat - 2026

Exécution : python generate_figures.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ============================================================================
# CONFIGURATION
# ============================================================================
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["font.size"] = 12
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 12
plt.rcParams["figure.dpi"] = 150

# Couleurs
COLORS = ['#2196F3', '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#98D8C8']

# Création du dossier graphiques
if not os.path.exists('graphiques'):
    os.makedirs('graphiques')
    print("✅ Dossier 'graphiques' créé")

print("=" * 60)
print("GÉNÉRATION DES FIGURES")
print("=" * 60)

# ============================================================================
# 1. CRÉATION DU DATASET SYNTHÉTIQUE
# ============================================================================
print("\n📊 1. CRÉATION DU DATASET...")
np.random.seed(42)
n_samples = 3000

df = pd.DataFrame({
    'ID_PO': range(1000, 4000),
    'Fournisseur': np.random.choice(['V001', 'V002', 'V003', 'V004', 'V005', 'V006', 'V007', 'V008', 'V009', 'V010'], n_samples),
    'Catégorie': np.random.choice(['Électronique', 'Mécanique', 'Textile', 'Chimique', 'Alimentaire'], n_samples),
    'Poids_Livraison': np.random.exponential(100, n_samples) + 10,
    'Mode_Transport': np.random.choice(['Air', 'Road', 'Rail', 'Sea'], n_samples, p=[0.15, 0.45, 0.25, 0.15]),
    'Distance_km': np.random.exponential(500, n_samples) + 50,
    'Quantité_Cmd': np.random.poisson(50, n_samples) + 10,
    'Priorité': np.random.choice([0, 1], n_samples, p=[0.7, 0.3]),
    'Coût_Fret': np.random.exponential(300, n_samples) + 50
})

# Calcul du Lead Time
df['Lead_Time_Days'] = (
    df['Distance_km'] / 500 +
    df['Poids_Livraison'] / 500 +
    np.where(df['Mode_Transport'] == 'Air', 1, 0) * 1 +
    np.where(df['Mode_Transport'] == 'Road', 2, 0) +
    np.where(df['Mode_Transport'] == 'Rail', 4, 0) +
    np.where(df['Mode_Transport'] == 'Sea', 8, 0) +
    np.where(df['Priorité'] == 1, -1, 1) +
    np.random.normal(0, 1, n_samples)
).clip(1, 32).round().astype(int)

print(f"✅ Dataset créé : {df.shape[0]} lignes, {df.shape[1]} colonnes")

# ============================================================================
# FIGURE 1 : Distribution du Lead Time
# Emplacement : graphiques/eda_distribution_leadtime.png
# ============================================================================
print("\n📈 FIGURE 1 : Distribution du Lead Time...")
plt.figure(figsize=(12, 6))
sns.histplot(df['Lead_Time_Days'], bins=25, kde=True, color=COLORS[0], edgecolor='white')
plt.title('Distribution du Délai de Livraison (Lead Time)', fontweight='bold')
plt.xlabel('Lead Time (jours)')
plt.ylabel('Nombre de commandes')
plt.axvline(df['Lead_Time_Days'].mean(), color='red', linestyle='--', linewidth=2, 
            label=f'Moyenne: {df["Lead_Time_Days"].mean():.1f} jours')
plt.axvline(df['Lead_Time_Days'].median(), color='green', linestyle='--', linewidth=2,
            label=f'Médiane: {df["Lead_Time_Days"].median():.1f} jours')
plt.legend()
plt.tight_layout()
plt.savefig('graphiques/eda_distribution_leadtime.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("   ✅ Sauvegardé : graphiques/eda_distribution_leadtime.png")

# ============================================================================
# FIGURE 2 : Boxplot par Mode de Transport
# Emplacement : graphiques/eda_transport_leadtime.png
# ============================================================================
print("\n📊 FIGURE 2 : Boxplot par Mode de Transport...")
order = ['Air', 'Road', 'Rail', 'Sea']
plt.figure(figsize=(12, 6))
sns.boxplot(x='Mode_Transport', y='Lead_Time_Days', data=df, order=order, palette=COLORS)
plt.title('Distribution du Lead Time par Mode de Transport', fontweight='bold')
plt.xlabel('Mode de Transport')
plt.ylabel('Lead Time (jours)')
plt.tight_layout()
plt.savefig('graphiques/eda_transport_leadtime.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("   ✅ Sauvegardé : graphiques/eda_transport_leadtime.png")

# ============================================================================
# FIGURE 3 : Performance des Fournisseurs
# Emplacement : graphiques/eda_fournisseur_leadtime.png
# ============================================================================
print("\n🏭 FIGURE 3 : Performance des Fournisseurs...")
fournisseur_stats = df.groupby('Fournisseur')['Lead_Time_Days'].agg(['mean', 'std']).reset_index()
fournisseur_stats = fournisseur_stats.sort_values('mean')

plt.figure(figsize=(14, 8))
bars = plt.bar(fournisseur_stats['Fournisseur'], fournisseur_stats['mean'], 
               color=plt.cm.viridis(np.linspace(0.2, 0.9, len(fournisseur_stats))))
plt.errorbar(x=range(len(fournisseur_stats)), y=fournisseur_stats['mean'], 
             yerr=fournisseur_stats['std'], fmt='none', color='black', capsize=5, linewidth=2)
plt.title('Délai Moyen par Fournisseur (avec écart-type)', fontweight='bold')
plt.xlabel('Fournisseur')
plt.ylabel('Lead Time Moyen (jours)')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('graphiques/eda_fournisseur_leadtime.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("   ✅ Sauvegardé : graphiques/eda_fournisseur_leadtime.png")

# ============================================================================
# FIGURE 4 : Matrice de Corrélation
# Emplacement : graphiques/eda_correlation_matrix.png
# ============================================================================
print("\n🔗 FIGURE 4 : Matrice de Corrélation...")
numeric_cols = ['Poids_Livraison', 'Distance_km', 'Quantité_Cmd', 'Coût_Fret', 'Lead_Time_Days']
corr_matrix = df[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f', 
            square=True, linewidths=2, cbar_kws={"shrink": 0.8})
plt.title('Matrice des Corrélations', fontweight='bold')
plt.tight_layout()
plt.savefig('graphiques/eda_correlation_matrix.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("   ✅ Sauvegardé : graphiques/eda_correlation_matrix.png")

# ============================================================================
# MODÉLISATION POUR LES FIGURES SUIVANTES
# ============================================================================
print("\n🤖 MODÉLISATION...")
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df_encoded = pd.get_dummies(df, columns=['Mode_Transport', 'Catégorie', 'Fournisseur'], drop_first=True)
X = df_encoded.drop(['Lead_Time_Days', 'ID_PO'], axis=1)
y = df_encoded['Lead_Time_Days']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement des modèles
models = {
    'Linear Regression': LinearRegression(),
    'Random Forest': RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42),
    'XGBoost': XGBRegressor(n_estimators=200, max_depth=5, learning_rate=0.1, random_state=42)
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    results[name] = {
        'MAE': mean_absolute_error(y_test, y_pred),
        'RMSE': np.sqrt(mean_squared_error(y_test, y_pred)),
        'R2': r2_score(y_test, y_pred),
        'model': model
    }
    print(f"   {name}: MAE={results[name]['MAE']:.2f}, R²={results[name]['R2']:.2f}")

# ============================================================================
# FIGURE 5 : Comparaison des Modèles
# Emplacement : graphiques/model_performance_comparison.png
# ============================================================================
print("\n📊 FIGURE 5 : Comparaison des Modèles...")
model_names = list(results.keys())
r2_scores = [results[m]['R2'] for m in model_names]
mae_scores = [results[m]['MAE'] for m in model_names]
rmse_scores = [results[m]['RMSE'] for m in model_names]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
colors_bar = [COLORS[0], COLORS[2], COLORS[3]]

axes[0].bar(model_names, r2_scores, color=colors_bar, edgecolor='black')
axes[0].set_title('Comparaison R²', fontweight='bold')
axes[0].set_ylabel('R² Score')
axes[0].set_ylim(0, 1)
for i, v in enumerate(r2_scores):
    axes[0].text(i, v + 0.02, f'{v:.2f}', ha='center', fontweight='bold')

axes[1].bar(model_names, mae_scores, color=colors_bar, edgecolor='black')
axes[1].set_title('Comparaison MAE', fontweight='bold')
axes[1].set_ylabel('MAE (jours)')
for i, v in enumerate(mae_scores):
    axes[1].text(i, v + 0.05, f'{v:.2f}', ha='center', fontweight='bold')

axes[2].bar(model_names, rmse_scores, color=colors_bar, edgecolor='black')
axes[2].set_title('Comparaison RMSE', fontweight='bold')
axes[2].set_ylabel('RMSE (jours)')
for i, v in enumerate(rmse_scores):
    axes[2].text(i, v + 0.05, f'{v:.2f}', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('graphiques/model_performance_comparison.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("   ✅ Sauvegardé : graphiques/model_performance_comparison.png")

# ============================================================================
# FIGURE 6 : Importance des Variables
# Emplacement : graphiques/model_feature_importance.png
# ============================================================================
print("\n📈 FIGURE 6 : Importance des Variables...")
xgb_model = results['XGBoost']['model']
importance_df = pd.DataFrame({
    'Variable': X.columns,
    'Importance': xgb_model.feature_importances_
}).sort_values('Importance', ascending=False).head(12)

plt.figure(figsize=(10, 8))
sns.barplot(x='Importance', y='Variable', data=importance_df, palette='viridis', edgecolor='black')
plt.title('Importance des Variables - Modèle XGBoost', fontweight='bold')
plt.xlabel('Importance relative')
for i, v in enumerate(importance_df['Importance']):
    plt.text(v + 0.005, i, f'{v*100:.1f}%', va='center')
plt.tight_layout()
plt.savefig('graphiques/model_feature_importance.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("   ✅ Sauvegardé : graphiques/model_feature_importance.png")

# ============================================================================
# FIGURE 7 : Analyse des Résidus
# Emplacement : graphiques/model_residual_analysis.png
# ============================================================================
print("\n📉 FIGURE 7 : Analyse des Résidus...")
y_pred_xgb = xgb_model.predict(X_test)
residuals = y_test - y_pred_xgb

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].scatter(y_pred_xgb, residuals, alpha=0.5, color=COLORS[0], edgecolor='white')
axes[0].axhline(y=0, color='red', linestyle='--', linewidth=2)
axes[0].set_xlabel('Valeurs Prédites (jours)')
axes[0].set_ylabel('Résidus (jours)')
axes[0].set_title('Résidus vs Valeurs Prédites', fontweight='bold')
axes[0].grid(alpha=0.3)

sns.histplot(residuals, bins=30, kde=True, color=COLORS[0], ax=axes[1], edgecolor='white')
axes[1].axvline(x=0, color='red', linestyle='--', linewidth=2)
axes[1].set_xlabel('Résidus (jours)')
axes[1].set_title('Distribution des Résidus', fontweight='bold')

plt.tight_layout()
plt.savefig('graphiques/model_residual_analysis.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("   ✅ Sauvegardé : graphiques/model_residual_analysis.png")

# ============================================================================
# FIGURE 8 : Intégration ERP
# Emplacement : graphiques/rec_erp_integration.png
# ============================================================================
print("\n🏢 FIGURE 8 : Architecture d'intégration ERP...")
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Boîtes
boxes = [
    (5, 8, 'SAP MM\nCréation PO', COLORS[0]),
    (5, 5, 'API Python\n(FastAPI)', COLORS[1]),
    (5, 2, 'Modèle XGBoost\nPrédiction Lead Time', COLORS[2]),
    (1, 6.5, 'Fournisseur', COLORS[3]),
    (9, 6.5, 'Acheteur', COLORS[4])
]

for x, y, text, color in boxes:
    rect = plt.Rectangle((x-1.5, y-0.8), 3, 1.6, facecolor=color, edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontweight='bold', fontsize=11)

# Flèches
ax.annotate('', xy=(5, 6.3), xytext=(5, 7.2), arrowprops=dict(arrowstyle='->', lw=2, color='black'))
ax.annotate('', xy=(5, 3.8), xytext=(5, 4.7), arrowprops=dict(arrowstyle='->', lw=2, color='black'))
ax.annotate('', xy=(3.5, 6.5), xytext=(5, 7), arrowprops=dict(arrowstyle='->', lw=2, color='black'))
ax.annotate('', xy=(6.5, 6.5), xytext=(5, 7), arrowprops=dict(arrowstyle='->', lw=2, color='black'))

ax.set_title('Architecture d\'Intégration dans l\'ERP SAP MM', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig('graphiques/rec_erp_integration.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("   ✅ Sauvegardé : graphiques/rec_erp_integration.png")

# ============================================================================
# FIGURE 9 : Optimisation Stock de Sécurité
# Emplacement : graphiques/rec_safety_stock.png
# ============================================================================
print("\n📦 FIGURE 9 : Optimisation Stock de Sécurité...")
safety_data = {
    'Scénario': ['Méthode classique\n(Lead Time moyen 5j)', 'Prédiction fiable\n(Lead Time 3.5j)', 'Prédiction risquée\n(Lead Time 7.5j)'],
    'Stock': [100, 70, 150],
    'Color': [COLORS[1], COLORS[2], COLORS[0]]
}

plt.figure(figsize=(12, 6))
bars = plt.bar(safety_data['Scénario'], safety_data['Stock'], color=safety_data['Color'], edgecolor='black')
plt.title('Réduction du Stock de Sécurité grâce à la Prédiction', fontweight='bold')
plt.ylabel('Stock de Sécurité (unités)')
plt.ylim(0, 200)
for bar, val in zip(bars, safety_data['Stock']):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, f'{val}', ha='center', fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('graphiques/rec_safety_stock.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("   ✅ Sauvegardé : graphiques/rec_safety_stock.png")

# ============================================================================
# FIGURE 10 : Plan d'Action
# Emplacement : graphiques/rec_action_plan.png
# ============================================================================
print("\n🎯 FIGURE 10 : Plan d'Action...")
action_data = {
    'Action': ['Négociation\nfournisseurs', 'Optimisation\ntransport', 'Segmentation\nachats', 'Déploiement\nAPI'],
    'ROI': [12.5, 17.5, 7.5, 22.5],
    'Délai': [3, 6, 2, 4],
    'Color': [COLORS[0], COLORS[1], COLORS[2], COLORS[3]]
}

plt.figure(figsize=(12, 8))
for i, row in enumerate(action_data['Action']):
    plt.scatter(action_data['Délai'][i], action_data['ROI'][i], s=300, color=action_data['Color'][i], edgecolor='black', zorder=5)
    plt.text(action_data['Délai'][i] + 0.2, action_data['ROI'][i] + 0.8, row, fontsize=11, ha='left')

plt.title('Plan d\'Action Opérationnel et ROI Estimé', fontweight='bold', fontsize=14)
plt.xlabel('Délai de mise en œuvre (mois)')
plt.ylabel('ROI estimé (%)')
plt.xlim(1, 7)
plt.ylim(5, 25)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('graphiques/rec_action_plan.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("   ✅ Sauvegardé : graphiques/rec_action_plan.png")

# ============================================================================
# RÉCAPITULATIF FINAL
# ============================================================================
print("\n" + "=" * 60)
print("✅ GÉNÉRATION TERMINÉE AVEC SUCCÈS")
print("=" * 60)
print("\n📁 Fichiers générés dans le dossier 'graphiques/' :")
print("   1. eda_distribution_leadtime.png")
print("   2. eda_transport_leadtime.png")
print("   3. eda_fournisseur_leadtime.png")
print("   4. eda_correlation_matrix.png")
print("   5. model_performance_comparison.png")
print("   6. model_feature_importance.png")
print("   7. model_residual_analysis.png")
print("   8. rec_erp_integration.png")
print("   9. rec_safety_stock.png")
print("  10. rec_action_plan.png")
print("\n🚀 Vous pouvez maintenant uploader ces fichiers sur GitHub")