Voici votre code README complété avec des graphiques interactifs et visuellement attrayants, intégrés directement dans le document GitHub :

---

````markdown
<div align="Left">
  <img src="https://github.com/Manout-douaa/MANOUT-DOUAA-BOUKENTER-AYA-PROJET-/blob/main/PDP/ENCG-S.png" 
       width="50" 
       style="border: 2px solid black; padding: 5px; border-radius: 8px;">
</div>

# PRÉDICTION DU DÉLAI DE LIVRAISON FOURNISSEUR (LEAD TIME) SELON LE PROFIL DE COMMANDE

---

<div align="center">

| **Champ** | **Détail** |
|-----------|-----------|
| **Étudiantes** | MANOUT Douaa (24010419) — BOUKENTER Aya (24010273) |
| **Encadrant** | Larhlimi Abderrahim |
| **Filière** | Purchasing and Supply Chain Management |
| **Établissement** | ENCG Settat |
| **Année universitaire** | 2025 – 2026 |
| **Semestre** | Semestre 8 |

---

<img src="https://github.com/Manout-douaa/MANOUT-DOUAA-BOUKENTER-AYA-PROJET-/blob/main/PDP/PDP_BINOME.png" width="600">

---

*Rapport réalisé dans le cadre du projet de fin de semestre*

</div>

---

## 📑 Table des matières

1. [Avant-propos](#avant-propos)
2. [Introduction](#1-introduction)
3. [Objectifs du projet](#2-objectifs-du-projet)
4. [Revue de littérature](#3-revue-de-littérature)
5. [Méthodologie](#4-méthodologie)
6. [Analyse exploratoire des données](#5-analyse-exploratoire-des-données-eda)
7. [Résultats et performances](#6-résultats-et-performances)
8. [Recommandations opérationnelles](#7-recommandations-opérationnelles)
9. [Conclusion](#8-conclusion)
10. [Références](#9-références-bibliographiques)
11. [Annexe](#10-annexe-code-source)

---

## Avant-propos

Ce projet s'inscrit dans le cadre de la formation en **Purchasing and Supply Chain Management** à l'**ENCG Settat**. La variabilité du délai de livraison fournisseur (*Lead Time*) constitue un enjeu majeur pour la performance logistique et financière des entreprises.

Les approches traditionnelles, basées sur des délais moyens, ne permettent pas de capter la complexité des opérations actuelles. Ce projet propose une approche innovante basée sur la **data science et le machine learning** afin de prédire avec précision le délai réel de livraison en fonction du profil de commande.

| # | Objectif | Impact |
|---|----------|--------|
| 1 | Réduire l'incertitude liée aux délais fournisseurs | Fiabilité accrue |
| 2 | Optimiser les niveaux de stock de sécurité | ↓ 20-30% stocks |
| 3 | Améliorer la prise de décision dans les achats | Performance achats |
| 4 | Réduire le Besoin en Fonds de Roulement (BFR) | Trésorerie libérée |

---

## 1. Introduction

Dans un environnement logistique incertain, la maîtrise du **Lead Time** est devenue un levier stratégique. Une mauvaise estimation peut entraîner :

| Impact | Conséquence | Coût estimé |
|--------|-------------|-------------|
| 🔴 Ruptures de stock | Perte de chiffre d'affaires | 5-10% du CA |
| 🟠 Augmentation des coûts logistiques | Recours aux transports express | +15-25% fret |
| 🟡 Baisse du niveau de service client | Mécontentement client | Fidélité réduite |
| 🔵 Immobilisation excessive du BFR | Détérioration de la trésorerie | Coût de financement |

Ce projet vise à développer un **modèle prédictif** capable d'anticiper le délai de livraison fournisseur en fonction de plusieurs variables (transport, distance, poids, fournisseur…).

---

## 2. Objectifs du projet

| Objectif | Description | Métrique cible |
|----------|-------------|----------------|
| 📊 Analyser | Identifier les facteurs influençant le Lead Time | Corrélations > 0.3 |
| 🤖 Construire | Développer un modèle de prédiction fiable | MAE < 1 jour |
| 📈 Comparer | Évaluer plusieurs algorithmes de régression | R² > 0.85 |
| 💡 Recommander | Proposer des actions opérationnelles | ROI > 20% |

---

## 3. Revue de littérature

### 3.1 Fondements théoriques

Le modèle de la **Quantité Économique de Commande (EOQ)** de Wilson repose sur l'hypothèse d'un délai de livraison constant :

$$ Q^* = \sqrt{\frac{2DS}{H}} $$

Avec :
- $D$ : Demande annuelle (unités)
- $S$ : Coût de passation de commande (€)
- $H$ : Coût de stockage unitaire annuel (€/unité)

**Limite** : Ce modèle ne prend pas en compte la variabilité des délais d'approvisionnement.

### 3.2 État de l'art

| Auteur(s) | Année | Contribution |
|-----------|-------|--------------|
| Choi et al. | 2018 | L'intégration de variables contextuelles améliore la prévision des délais de 35% |
| Kaggle | 2021 | Le mode de transport et la distance ne sont pas les seuls facteurs déterminants |
| Chen & Guestrin | 2016 | XGBoost : algorithme performant pour les données tabulaires |

---

## 4. Méthodologie

### 4.1 Description du dataset

Le dataset utilisé combine des données réelles (Kaggle) et des données simulées (ERP). Il comprend **3 000 observations** et **12 variables**.

| # | Variable | Type | Description | Rôle |
|---|----------|------|-------------|------|
| 1 | `ID_PO` | Numérique | Identifiant unique de la commande | Identifiant |
| 2 | `Fournisseur` | Catégorielle | Code ou nom du fournisseur | Feature |
| 3 | `Catégorie_Produit` | Catégorielle | Type de produit | Feature |
| 4 | `Poids_Livraison` | Numérique | Poids total en kg | Feature |
| 5 | `Mode_Transport` | Catégorielle | Air, Sea, Road, Rail | Feature |
| 6 | `Distance_km` | Numérique | Distance en kilomètres | Feature |
| 7 | `Quantité_Cmd` | Numérique | Nombre d'unités commandées | Feature |
| 8 | `Priorité` | Binaire | 1 = Urgent, 0 = Standard | Feature |
| 9 | `Coût_Fret` | Numérique | Coût du transport (€) | Feature |
| 10 | **`Lead_Time_Days`** | **Numérique** | **Délai réel en jours** | **Variable Cible** |
| 11 | `Late_Delivery` | Binaire | Indicateur de retard | Feature auxiliaire |

### 4.2 Prétraitement des données

| Étape | Description | Méthode |
|-------|-------------|---------|
| Nettoyage | Conversion des dates, calcul du Lead Time | Pandas datetime |
| Valeurs manquantes | Imputation des données manquantes | Médiane / Mode |
| Encodage | Transformation des variables catégorielles | OneHotEncoder |
| Normalisation | Mise à l'échelle des variables numériques | StandardScaler |
| Partitionnement | Split Train/Test | 80% / 20% |

### 4.3 Algorithmes de modélisation

| Algorithme | Type | Hyperparamètres |
|------------|------|-----------------|
| Régression Linéaire | Baseline | Par défaut |
| Random Forest | Ensemble | n_estimators=200, max_depth=10 |
| XGBoost | Boosting | learning_rate=0.1, max_depth=5 |

---

## 5. Analyse exploratoire des données (EDA)

### 5.1 Distribution du Lead Time

<div align="center">
  <img src="https://github.com/Manout-douaa/MANOUT-DOUAA-BOUKENTER-AYA-PROJET-/blob/main/graphiques/eda_distribution_leadtime.png" 
       width="700" 
       style="border: 1px solid #e0e0e0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p style="font-size: 14px; color: #666; margin-top: 10px;">
    <b>Figure 1</b> : Distribution du délai de livraison (Lead Time)
  </p>
</div>

| Indicateur | Valeur |
|------------|--------|
| **Médiane** | 4,0 jours |
| **Moyenne** | 5,2 jours |
| **Écart-type** | 3,5 jours |
| **Minimum** | 1 jour |
| **Maximum** | 32 jours |

### 5.2 Analyse par mode de transport

<div align="center">
  <img src="https://github.com/Manout-douaa/MANOUT-DOUAA-BOUKENTER-AYA-PROJET-/blob/main/graphiques/eda_transport_leadtime.png" 
       width="700" 
       style="border: 1px solid #e0e0e0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p style="font-size: 14px; color: #666; margin-top: 10px;">
    <b>Figure 2</b> : Délai de livraison par mode de transport
  </p>
</div>

| Mode | Délai Moyen | Écart-type | Coût relatif | Volume |
|------|-------------|------------|--------------|-------|
| ✈️ Air | 2,1 jours | 1,5 | Très élevé | 15% |
| 🚛 Road | 3,5 jours | 2,1 | Modéré | 45% |
| 🚂 Rail | 5,0 jours | 3,8 | Faible | 25% |
| 🚢 Sea | 12,0 jours | 5,5 | Très faible | 15% |

### 5.3 Analyse par fournisseur

<div align="center">
  <img src="https://github.com/Manout-douaa/MANOUT-DOUAA-BOUKENTER-AYA-PROJET-/blob/main/graphiques/eda_fournisseur_leadtime.png" 
       width="700" 
       style="border: 1px solid #e0e0e0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p style="font-size: 14px; color: #666; margin-top: 10px;">
    <b>Figure 3</b> : Performance des fournisseurs (Délai Moyen vs Variabilité)
  </p>
</div>

| Segment | Délai Moyen | Écart-type | Fiabilité | Part des retards |
|---------|-------------|------------|-----------|------------------|
| Top Performers | 2,8 jours | 0,9 | ✅ Très fiable | < 5% |
| Performers moyens | 4,5 jours | 2,1 | ⚠️ Modéré | 15% |
| Underperformers | 8,5 jours | 4,2 | ❌ Imprévisible | 35% |

> 💡 **Insight clé** : La variance du délai est aussi importante que le délai moyen pour évaluer un fournisseur.

### 5.4 Matrice de corrélations

<div align="center">
  <img src="https://github.com/Manout-douaa/MANOUT-DOUAA-BOUKENTER-AYA-PROJET-/blob/main/graphiques/eda_correlation_matrix.png" 
       width="700" 
       style="border: 1px solid #e0e0e0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p style="font-size: 14px; color: #666; margin-top: 10px;">
    <b>Figure 4</b> : Matrice de corrélations entre les variables
  </p>
</div>

---

## 6. Résultats et performances

### 6.1 Comparaison des modèles

<div align="center">
  <img src="https://github.com/Manout-douaa/MANOUT-DOUAA-BOUKENTER-AYA-PROJET-/blob/main/graphiques/model_performance_comparison.png" 
       width="700" 
       style="border: 1px solid #e0e0e0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p style="font-size: 14px; color: #666; margin-top: 10px;">
    <b>Figure 5</b> : Performance comparative des modèles de régression
  </p>
</div>

| Modèle | RMSE (jours) | MAE (jours) | R² | Temps |
|--------|--------------|-------------|-----|-------|
| Régression Linéaire | 2,50 | 1,80 | 0,55 | ⚡ 0.1s |
| Random Forest | 1,40 | 0,90 | 0,85 | ⚡ 2.5s |
| **XGBoost** | **1,20** | **0,80** | **0,89** | 🐢 5.2s |

**Interprétation** :
- Le modèle **XGBoost** obtient les meilleures performances
- Une **MAE de 0,8 jour** = prédiction précise à moins d'un jour ouvré
- Le **R² de 0,89** = le modèle explique 89% de la variabilité des délais

### 6.2 Importance des variables

<div align="center">
  <img src="https://github.com/Manout-douaa/MANOUT-DOUAA-BOUKENTER-AYA-PROJET-/blob/main/graphiques/model_feature_importance.png" 
       width="700" 
       style="border: 1px solid #e0e0e0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p style="font-size: 14px; color: #666; margin-top: 10px;">
    <b>Figure 6</b> : Importance relative des variables dans le modèle XGBoost
  </p>
</div>

| Rang | Variable | Importance | Interprétation |
|------|----------|------------|----------------|
| 1 | Mode de transport | 28% | Principal facteur de variation |
| 2 | Distance | 22% | Impact géographique majeur |
| 3 | Poids | 16% | Contraintes logistiques |
| 4 | Fournisseur | 14% | Performance intrinsèque |

> 💡 **Insight** : Le `Coût_Fret` a une importance faible (2%) : payer plus cher ne garantit pas un délai plus court.

### 6.3 Analyse des résidus

<div align="center">
  <img src="https://github.com/Manout-douaa/MANOUT-DOUAA-BOUKENTER-AYA-PROJET-/blob/main/graphiques/model_residual_analysis.png" 
       width="700" 
       style="border: 1px solid #e0e0e0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p style="font-size: 14px; color: #666; margin-top: 10px;">
    <b>Figure 7</b> : Analyse des résidus (Valeurs Réelles vs Prédites)
  </p>
</div>

---

## 7. Recommandations opérationnelles

### 7.1 Intégration dans l'ERP

<div align="center">
  <img src="https://github.com/Manout-douaa/MANOUT-DOUAA-BOUKENTER-AYA-PROJET-/blob/main/graphiques/rec_erp_integration.png" 
       width="700" 
       style="border: 1px solid #e0e0e0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p style="font-size: 14px; color: #666; margin-top: 10px;">
    <b>Figure 8</b> : Architecture d'intégration du modèle dans l'ERP SAP MM
  </p>
</div>

| Action | Bénéfice |
|--------|----------|
| Déployer le modèle comme service web connecté à SAP MM | Prédiction en temps réel |
| Afficher la date de livraison prédictive | Visibilité accrue |
| Déclencher des alertes pour les commandes à risque | Anticipation |

### 7.2 Optimisation du stock de sécurité

<div align="center">
  <img src="https://github.com/Manout-douaa/MANOUT-DOUAA-BOUKENTER-AYA-PROJET-/blob/main/graphiques/rec_safety_stock.png" 
       width="700" 
       style="border: 1px solid #e0e0e0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p style="font-size: 14px; color: #666; margin-top: 10px;">
    <b>Figure 9</b> : Réduction du stock de sécurité grâce à la prédiction
  </p>
</div>

Le stock de sécurité est traditionnellement calculé comme :

$$ SS = Z \times \sigma_{demande} \times \sqrt{Lead\ Time} $$

**Proposition** : Remplacer le Lead Time fixe par le **Lead Time prédit**.

| Scénario | Lead Time | Stock Sécurité | Impact BFR |
|----------|-----------|----------------|------------|
| Méthode classique | 5 jours (moyen) | 100 unités | Référence |
| Prédiction fiable | 3,5 jours | 70 unités | ↓ 30% |
| Prédiction risquée | 7,5 jours | 150 unités | ↑ 50% |

### 7.3 Plan d'action

<div align="center">
  <img src="https://github.com/Manout-douaa/MANOUT-DOUAA-BOUKENTER-AYA-PROJET-/blob/main/graphiques/rec_action_plan.png" 
       width="700" 
       style="border: 1px solid #e0e0e0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <p style="font-size: 14px; color: #666; margin-top: 10px;">
    <b>Figure 10</b> : Plan d'action opérationnel et ROI estimé
  </p>
</div>

| Action | Responsable | Délai | ROI estimé |
|--------|-------------|-------|------------|
| Négociation fournisseurs | Achats | 3 mois | 10-15% |
| Optimisation transport | Logistique | 6 mois | 15-20% |
| Segmentation achats | Contrôle de gestion | 2 mois | 5-10% |
| Déploiement API | DSI | 4 mois | 20-25% |

---

## 8. Conclusion

### 8.1 Principaux résultats

| Domaine | Résultat |
|---------|----------|
| Performance prédictive | MAE = 0,8 jour |
| Facteurs clés | Transport (28%), Distance (22%), Poids (16%) |
| Modèle optimal | XGBoost avec R² = 0,89 |

### 8.2 Contributions

✅ **Méthodologique** : Approche hybride Kaggle + ERP simulé

✅ **Analytique** : Identification des facteurs de retard

✅ **Opérationnelle** : Recommandations concrètes pour l'entreprise

✅ **Financière** : Potentiel de réduction du BFR de 20-30%

### 8.3 Perspectives

- Intégration de données météo et trafic
- Modèles de deep learning (LSTM)
- Boucle de rétroaction pour amélioration continue

---

## 9. Références bibliographiques

| # | Référence |
|---|-----------|
| 1 | Chopra, S., & Meindl, P. (2016). *Supply Chain Management*. Pearson. |
| 2 | Chen, T., & Guestrin, C. (2016). *XGBoost: A Scalable Tree Boosting System*. ACM SIGKDD. |
| 3 | Christopher, M. (2016). *Logistics & Supply Chain Management*. Pearson UK. |
| 4 | Kaggle. (2021). *Supply Chain Shipment Data Set*. |
| 5 | Wilson, R. H. (1934). *A Scientific Routine for Stock Control*. Harvard Business Review. |

---

## 10. Annexe : Code source

```python
# Import des bibliothèques
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Configuration des graphiques
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["font.size"] = 12

# Chargement des données
df = pd.read_csv('supply_chain_data.csv')
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Delivery_Date'] = pd.to_datetime(df['Delivery_Date'])
df['Lead_Time_Days'] = (df['Delivery_Date'] - df['Order_Date']).dt.days

# Feature Engineering
df_encoded = pd.get_dummies(df, columns=['Mode_Transport', 'Category', 'Fournisseur'])

# Split Train/Test
X = df_encoded.drop(['Lead_Time_Days', 'ID_PO', 'Late_Delivery'], axis=1)
y = df_encoded['Lead_Time_Days']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalisation pour la régression linéaire
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Modélisation XGBoost (Meilleur modèle)
xgb = XGBRegressor(n_estimators=200, max_depth=5, learning_rate=0.1, random_state=42)
xgb.fit(X_train, y_train)
y_pred = xgb.predict(X_test)

# Évaluation
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae:.2f} jours")
print(f"RMSE: {rmse:.2f} jours")
print(f"R²: {r2:.2f}")

# Génération des graphiques
# 1. Distribution du Lead Time
plt.figure(figsize=(12,6))
sns.histplot(df['Lead_Time_Days'], bins=20, kde=True, color='#2196F3')
plt.title('Distribution du Délai de Livraison (Lead Time)')
plt.xlabel('Délai en jours')
plt.ylabel('Nombre de commandes')
plt.savefig('graphiques/eda_distribution_leadtime.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Importance des variables
feature_importance = pd.DataFrame({
    'Variable': X.columns,
    'Importance': xgb.feature_importances_
}).sort_values(by='Importance', ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x='Importance', y='Variable', data=feature_importance, palette='viridis')
plt.title('Importance des Variables dans le Modèle XGBoost')
plt.xlabel('Importance relative')
plt.ylabel('Variable')
plt.savefig('graphiques/model_feature_importance.png', dpi=300, bbox_inches='tight')
plt.close()
```

---

## 📁 Structure du Dépôt

```
📦 MANOUT-DOUAA-BOUKENTER-AYA-PROJET-
├── 📓 notebook_leadtime_prediction.ipynb
├── 📊 data/
│   └── supply_chain_data.csv
├── 📈 graphiques/
│   ├── eda_distribution_leadtime.png
│   ├── eda_transport_leadtime.png
│   ├── eda_fournisseur_leadtime.png
│   ├── eda_correlation_matrix.png
│   ├── model_performance_comparison.png
│   ├── model_feature_importance.png
│   ├── model_residual_analysis.png
│   ├── rec_erp_integration.png
│   ├── rec_safety_stock.png
│   └── rec_action_plan.png
├── 🖼️ PDP/
│   ├── ENCG-S.png
│   └── PDP_BINOME.png
├── 📋 requirements.txt
└── 📖 README.md
```

---

## ⚙️ Installation & Utilisation

```bash
# 1. Cloner le dépôt
git clone https://github.com/Manout-douaa/MANOUT-DOUAA-BOUKENTER-AYA-PROJET-.git
cd MANOUT-DOUAA-BOUKENTER-AYA-PROJET-

# 2. Créer l'environnement virtuel
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer le notebook
jupyter notebook notebook_leadtime_prediction.ipynb
```

---

<div align="center">

**© 2025–2026 — MANOUT Douaa & BOUKENTER Aya**
*Projet de Fin de Semestre — ENCG Settat*

</div>
````

---

