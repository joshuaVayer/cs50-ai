# Degrees

Les spécifications de l'exercice sont disponibles [ici](https://cs50.harvard.edu/ai/2020/projects/0/degrees/).

## Utilisation

Il y a de bases de données disponibles dans le dossier `large` et `small`. `small`est utilisé pour le développement et le débogage, tandis que `large` est utilisé pour les tests de performance.

Pour exécuter le programme, il faut exécuter la commande suivante :

```bash
python degrees.py small

# ou

python degrees.py large
```

Le programme va demander de saisir le nom de deux acteurs. Il est possible de saisir le nom complet ou une partie du nom. Par exemple, si on veut trouver le chemin entre `Kevin Bacon` et `Tom Hanks`, il est possible de saisir `Kevin` ou `Tom` ou `Hanks` ou `Bacon` ou `Tom Hanks` ou `Kevin Bacon`.

## Fonctionnement

Le programme utilise la stratégie `Breadth-First Search` pour trouver le chemin le plus court entre deux acteurs. Pour ce faire, il utilise une file FIFO (First In First Out) pour stocker les acteurs à explorer. Pour chaque acteur, il stocke le nom de l'acteur et le chemin qui a été utilisé pour l'atteindre. Ainsi, pour chaque acteur, il est possible de retrouver le chemin qui a été utilisé pour l'atteindre.
