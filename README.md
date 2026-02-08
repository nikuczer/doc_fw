# Golden Data Viewer - CardioWatch 287-2B

## 🎯 Vue d'ensemble

Page HTML interactive pour visualiser et analyser les 40 scénarios cliniques de golden data du simulateur CardioWatch 287-2B.

## 📊 Fonctionnalités

### Graphes interactifs
- **PPG Signals** (Green 530nm, Red 660nm, IR 940nm)
- **Accelerometer** (X, Y, Z axes)
- **Heart Rate (BPM)** avec highlight par qualité (0-4)
- **SpO2 (%)** avec highlight par qualité (0-4)

### Interactions
- ✅ **Zoom synchronisé** : Zoomer sur un graphe ajuste tous les autres
- ✅ **Pan synchronisé** : Déplacer à droite/gauche synchronise tous les graphes
- ✅ **Hover** : Affiche les valeurs précises au survol
- ✅ **Reset** : Double-clic pour réinitialiser le zoom
- ✅ **Marqueurs d'événements** : Indique les moments critiques (arrêt cardiaque, VF, etc.)

### Descriptions cliniques
Chaque scénario inclut:
- Nom du scénario
- Description clinique détaillée
- Valeurs attendues (HR, SpO2)
- Événements importants avec timestamps

## 🚀 Utilisation

### Méthode 1 : Serveur HTTP local (Recommandé)

```bash
# Depuis le dossier doc/
cd c:\FW_287\287-2B\doc
python -m http.server 8000
```

Puis ouvrir : `http://localhost:8000/golden_data_viewer.html`

### Méthode 2 : Ouvrir directement (si CORS le permet)

Ouvrir directement `golden_data_viewer.html` dans votre navigateur.

⚠️ **Note** : Certains navigateurs bloquent les requêtes CORS pour les fichiers locaux. Si vous voyez une erreur de chargement, utilisez la Méthode 1.

## 📁 Structure des données

```
doc/
  └── golden_data_viewer.html    # Page web interactive

sim/output/golden_data/
  ├── 01_normal_rest/
  │   ├── ppg2_green_6.csv       # Signal PPG vert
  │   ├── ppg2_red_182.csv       # Signal PPG rouge
  │   ├── ppg2_infra_red_22.csv  # Signal PPG infrarouge
  │   ├── acc.csv                # Données accéléromètre
  │   └── activity_records.csv   # Enregistrements d'activité (BPM, SpO2)
  ├── 02_elderly_rest/
  │   └── ...
  └── ... (40 scénarios total)
```

## 🎨 Code couleur des qualités

### BPM et SpO2
- **Gris** (Q=0) : Aucune qualité / Non mesuré
- **Rouge** (Q=1) : Qualité faible
- **Jaune** (Q=2) : Qualité moyenne
- **Vert** (Q=3) : Bonne qualité
- **Cyan** (Q=4) : Excellente qualité

## 📋 Scénarios disponibles

### Normal/Repos (3)
- 01: Normal Rest (70 bpm, 98% SpO2)
- 02: Elderly Rest (75 bpm, 97% SpO2)
- 03: Athlete Rest (55 bpm, 99% SpO2)

### Hypoxie (3)
- 04: Mild Hypoxia (90-94% SpO2)
- 05: Moderate Hypoxia (85-89% SpO2)
- 06: Severe Hypoxia (<85% SpO2)

### Activité (3)
- 07: Walking (100-120 bpm)
- 08: Running (150-180 bpm)
- 09: Wrist Movement (artifacts)

### Arrhythmies (10)
- 10: AF Rapid (120-160 bpm irregular)
- 15: PSVT Episodes (sudden jumps)
- 16: VT Monomorphic (150-200 bpm)
- 17: Torsades de Pointes (200-250 bpm)
- ... et plus

### Situations critiques (4)
- 21: VF from Sinus ⚠️ **Arrêt cardiaque @ 30min**
- 22: VT to VF ⚠️ **VT @ 20min → VF @ 40min**
- 23: Asystole ⚠️ **Arrêt @ 20min**
- 24: PEA ⚠️ **Perte de pouls @ 25min**

### Choc/Extrême (4)
- 32: Hemorrhagic Shock
- 33: Hypothermia 32°C
- 34: Hypothermia 28°C
- 40: CO Poisoning

... et 16 autres scénarios (maladies structurelles, apnée du sommeil, etc.)

## 🔧 Mise à jour des données

Après avoir lancé de nouvelles simulations :

```bash
cd c:\FW_287\287-2B\sim

# 1. Lancer les simulations
python run_all_golden.py

# 2. Copier les CSV raw vers output
python copy_raw_data_to_output.py

# 3. Actualiser la page web (F5)
```

## 📊 Exemple d'utilisation

1. **Ouvrir** `golden_data_viewer.html`
2. **Sélectionner** un scénario (ex: "21_vf_from_sinus")
3. **Cliquer** "Load Data"
4. **Observer** :
   - Signal PPG normal au début
   - Accélération cardiaque progressive
   - Ligne rouge verticale à 1800s = Onset VF
   - Effondrement du signal PPG après l'événement
5. **Zoomer** sur la zone d'intérêt
   - Cliquer-glisser sur un graphe pour zoomer
   - Tous les autres graphes zoomment aussi
6. **Comparer** avec un autre scénario

## 🐛 Dépannage

### Problème : "Failed to load CSV"
**Solution** : Utilisez un serveur HTTP local (Méthode 1)

### Problème : Graphes vides
**Solution** : Vérifiez que `copy_raw_data_to_output.py` a été exécuté

### Problème : Scénario manquant
**Solution** : Lancez `python run_all_golden.py` pour générer les données

## 📝 Notes techniques

- **Format timestamps** : Unix epoch (secondes)
- **Fréquence PPG** : 32 Hz
- **Fréquence ACC** : 32 Hz
- **Résolution PPG** : 19-bit ADC (0-524287)
- **Résolution ACC** : 12-bit, ±2g
- **Activity records** : 1 record/minute

## 🚀 Prochaines étapes

- [ ] Ajouter export PDF des graphes
- [ ] Ajouter comparaison side-by-side de 2 scénarios
- [ ] Ajouter statistiques détaillées (HRV, etc.)
- [ ] Ajouter annotations manuelles

---

**Corsano Health** | CardioWatch 287-2B Firmware Simulator
