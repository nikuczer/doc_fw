# Déploiement sur GitHub Pages

## 📦 Préparation des données

Les données de simulation sont converties en JSON statiques pour être hébergées sur GitHub Pages.

### Étape 1 : Générer les fichiers JSON

```bash
cd sim
python prepare_for_github.py
```

Cela crée :
- `doc/data/` avec 40 fichiers JSON (un par scénario)
- `doc/data/scenarios_index.json` (index des scénarios)
- Total : ~115 MB (downsampled 32Hz → 1Hz)

### Étape 2 : Structure des fichiers

```
doc/
├── index.html                    # Page d'accueil
├── golden_data_viewer.html       # Viewer interactif
├── algorithms.html
├── ble_commands.html
├── doc_plans.html
├── test_plan_boot.html
└── data/                         # Données JSON
    ├── 01_normal_rest.json
    ├── 02_elderly_rest.json
    ├── ...
    └── scenarios_index.json
```

## 🚀 Déploiement sur GitHub

### Option 1 : Dépôt existant

```bash
# Depuis la racine du projet
git add doc/
git commit -m "Add golden data viewer for GitHub Pages"
git push origin main
```

### Option 2 : Nouveau dépôt

```bash
# Créer un nouveau repo sur GitHub : cardiowatch-287-2b-docs

git init
git add doc/
git commit -m "Initial commit: Documentation and golden data viewer"
git branch -M main
git remote add origin https://github.com/[username]/cardiowatch-287-2b-docs.git
git push -u origin main
```

## ⚙️ Activer GitHub Pages

1. Aller sur le dépôt GitHub
2. **Settings** → **Pages**
3. **Source** : Deploy from a branch
4. **Branch** : `main` → `/doc` folder
5. **Save**

Attendre 1-2 minutes, puis accéder à :
```
https://[username].github.io/[repo]/
```

## 📊 Accès aux pages

- **Index** : `https://[username].github.io/[repo]/`
- **Golden Viewer** : `https://[username].github.io/[repo]/golden_data_viewer.html`
- **Algorithms** : `https://[username].github.io/[repo]/algorithms.html`
- etc.

## 🔄 Mise à jour des données

Après avoir lancé de nouvelles simulations :

```bash
cd sim

# 1. Lancer les simulations
python run_all_golden.py

# 2. Générer les JSON
python prepare_for_github.py

# 3. Commit et push
cd ..
git add doc/data/
git commit -m "Update golden data results"
git push
```

GitHub Pages se met à jour automatiquement en 1-2 minutes.

## 📝 Notes techniques

### Downsampling
- **Original** : PPG 32 Hz, ACC 32 Hz (360+ MB)
- **GitHub** : PPG 1 Hz, ACC 1 Hz (115 MB)
- **Qualité** : Suffisante pour visualisation web

### Limites GitHub Pages
- Taille max recommandée : 1 GB
- Taille actuelle : 115 MB ✅
- Bandwidth : 100 GB/mois (soft limit)

### Format JSON
```json
{
  "activity_records": [...],  // Tous les records (59 × 1h)
  "ppg_green": [...],         // Downsampled 32Hz → 1Hz
  "ppg_red": [...],           // Downsampled 32Hz → 1Hz
  "ppg_ir": [...],            // Downsampled 32Hz → 1Hz
  "acc": [...]                // Downsampled 32Hz → 1Hz
}
```

## 🐛 Troubleshooting

### Erreur 404 sur data/
- Vérifier que `doc/data/` est bien commité
- Vérifier que GitHub Pages pointe vers `/doc` folder

### Fichiers trop gros
- Augmenter le downsampling dans `prepare_for_github.py`
- Modifier `factor=32` → `factor=64` (PPG/ACC à 0.5 Hz)

### Page blanche
- Ouvrir la console du navigateur (F12)
- Vérifier les erreurs de chargement JSON
- Vérifier les chemins relatifs

## ✅ Vérification locale

Avant de push, tester localement :

```bash
cd doc
python -m http.server 8000
```

Ouvrir : `http://localhost:8000/`

Si ça marche localement, ça marchera sur GitHub Pages.

---

**Corsano Health** | CardioWatch 287-2B Documentation
