# Rocket Developpement v2

**Projet Fusée Expérimentale**  
Ce dépôt contient les fichiers STEP et STL pour la modélisation ainsi que le code source pour le développement de la fusée expérimentale. Ce projet expérimente les principes de base du contrôle de roulis d'une fusée, avec des objectifs d'amélioration continue et de tests réguliers.

## Table des matières
1. [Aperçu du Projet](#1-apercu-du-projet)
2. [Caractéristiques Techniques](#2-caracteristiques-techniques)
3. [Prérequis](#3-prerequis)
4. [Installation](#4-installation)
5. [Structure du Dépôt](#5-structure-du-depot)
6. [Utilisation](#6-utilisation)
7. [Contribution](#7-contribution)
8. [Licence](#8-licence)

## 1. Aperçu du Projet

Ce projet a pour objectif la création d'une fusée expérimentale visant à tester différents aspects de l'ingénierie aérospatiale, tels que :
- La propulsion
- La stabilité et le contrôle de vol
- Les systèmes de télémétrie et de communication
- La récupération de la fusée après le lancement

## 2. Caractéristiques Techniques

- **Système de propulsion** : Utilise un moteur [Pro54-5G](http://logiqueformelle.free.fr/eti-aerospatial/doc/propulseurs_spatial_BARASINGA.pdf).
- **Structure** : Conception en aluminium pour assurer une robustesse et une légèreté optimales.
- **Système de contrôle** : Asservissement PID pour le contrôle de roulis. Voir l'[article explicatif](https://www.firediy.fr/article/asservissement-pid-drone-ch-8).
- **Système de télémétrie** : Utilise la carte [BR Mini Avionic](https://berryrocket.com/wiki/BR_Mini_Avionic) pour la collecte de données en vol.

## 3. Prérequis

- **Outils nécessaires** :
  - [Berry Rocket Mini-Avionic](https://berryrocket.com/wiki/BR_Mini_Avionic) pour la télémétrie.
  - Environnement Python (préférence pour l'[IDE Thonny](https://thonny.org/)).
  - Git (pour cloner le dépôt).
  - Logiciel de conception CAO, tel que [Autodesk Fusion 360](https://www.autodesk.com/products/fusion-360/overview?term=1-YEAR&tab=subscription&plc=FSN#top).
  
- **Dépendances** :
  - Liste des bibliothèques nécessaires (ajouter les bibliothèques spécifiques si besoin).

## 4. Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/paguielng/Rocket-developp-v2.git
