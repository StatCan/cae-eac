_[English](../../en/DeltaLake)_

# Delta Lake

Delta Lake est une couche de stockage open source qui s'exécute sur un lac de données existant, ajoutant les capacités des propriétés et des transactions ACID (atomicité, cohérence, isolation, durabilité). Delta Lake est entièrement compatible avec Apache Spark dans Azure Databricks et Synapse.

Azure Data Lake n'est _pas_ conforme à l'ACID, donc Delta Lake doit être utilisé partout où l'intégrité et la fiabilité des données sont essentielles, ou lorsqu'il existe un risque de données erronées.

### Documentation Microsoft
- [Qu'est-ce que le Delta Lake](https://docs.microsoft.com/fr-ca/azure/synapse-analytics/spark/apache-spark-what-is-delta-lake)
- [Delta Lake sur Azure](https://techcommunity.microsoft.com/t5/analytics-on-azure/delta-lake-on-azure/ba-p/1869746)

### Documents Officiels
- [Documentation Delta Lake](https://docs.delta.io/latest/index.html)

## Comment fonctionne le Delta Lake

Un lac delta est essentiellement un dossier à l'intérieur du lac de données contenant des **fichiers journaux** (dans le sous-dossier **_delta_log**) et des **fichiers de données** (stockés au format parquet dans le dossier racine) pour chaque version d'un tableau. Tant que les fichiers journaux et de données existent, vous pouvez utiliser la fonction de voyage dans le temps pour interroger les versions précédentes d'une table delta et afficher l'historique de cette table.

**Si les fichiers journaux sont supprimés**, vous ne pourrez pas du tout lire le tableau. Pour résoudre ce problème, vous devrez vider le dossier du Delta Lake (supprimer tout ce qu'il contient), puis y écrire votre fichier de données d'origine pour recommencer.

Delta Lake fonctionne au niveau de la table, les requêtes et jointures multi-tables ne sont donc pas prises en charge.

## Quand utiliser Delta Lake

Il est préférable d'utiliser le Delta Lake:

- pour toute table permanente dans Databricks;
- pour de grandes quantités de données semi-structurées (plus de 10 millions d'enregistrements pour tirer le meilleur parti des performances); ou
- lorsque vous souhaitez un contrôle de version et/ou un suivi des accès aux données (les fichiers log delta gardent une trace de chaque modification des données et par qui).

## Voyage dans le temps

Vous pouvez utiliser le voyage dans le temps pour interroger un ancien instantané d'une table, soit par numéro de version, soit par horodatage. Par défaut, les fichiers de données sont stockés pendant 30 jours.

Exemple:

**SQL**
```
SELECT * FROM example_table TIMESTAMP AS OF '2018-10-18T22:15:12.013Z'
SELECT * FROM delta.`/delta/example_table` VERSION AS OF 12
```

**Python**
```
df1 = spark.read.format("delta").option("timestampAsOf", 2020-03-13).load("/delta/example_table")
df2 = spark.read.format("delta").option("timestampAsOf", 2019-01-01T00:00:00.000Z).load("/delta/example_table")
df3 = spark.read.format("delta").option("versionAsOf", version).load("/delta/example_table")
```

### Suppression des anciens fichiers de données

Pour supprimer les anciens fichiers de données (pas les fichiers journaux) qui ne sont plus référencés par une table delta, vous pouvez exécuter la commande **vacuum**.

Exemple:

**SQL**
```
VACUUM example_table   -- fichiers vacuum non requis par les versions antérieures à la période de rétention par défaut

VACUUM '/data/example_table' -- fichiers vides dans une table basée sur les chemins

VACUUM delta.`/data/example_table/`

VACUUM delta.`/data/example_table/` RETAIN 100 HOURS  -- fichiers vides non requis par les versions de plus de 100 heures

VACUUM example_table DRY RUN    -- faire un essai à sec pour obtenir la liste des fichiers à supprimer
```

**Python**
```
from delta.tables import *

deltaTable = DeltaTable.forPath(spark, pathToTable)

deltaTable.vacuum()        # fichiers vacuum non requis par les versions antérieures à la période de rétention par défaut

deltaTable.vacuum(100)     # fichiers vides non requis par les versions de plus de 100 heures
```

**Scala**
```
import io.delta.tables._

val deltaTable = DeltaTable.forPath(spark, pathToTable)

deltaTable.vacuum()        // fichiers vacuum non requis par les versions antérieures à la période de rétention par défaut

deltaTable.vacuum(100)     // fichiers vides non requis par les versions de plus de 100 heures
```

### Revenir à une version précédente

Vous pouvez revenir à une version précédente de votre table et y travailler en utilisant la fonction de voyage dans le temps pour lire votre version cible en tant que trame de données, puis la réécrire dans le dossier delta lake.

Cela créera une nouvelle version identique à la version cible, à partir de laquelle vous pourrez ensuite travailler. Les autres versions précédentes restent intactes.

Exemple:

**Python**
```
# lire dans l'ancienne version du tableau
df = spark.read.format("delta").option("versionAsOf", 0).load(delta_table_path)

# réécrire dans la nouvelle version de la table, doit définir le mode sur "overwrite"
df.write.format("delta").mode("overwrite").save(delta_table_path)
```

### Documents officiels
- [Interroger un ancien instantané d'une table (voyage dans le temps)](https://docs.delta.io/latest/delta-batch.html#-deltatimetravel)
- [Supprimer les fichiers qui ne sont plus référencés par une table delta](https://docs.delta.io/latest/delta-utility.html#-delta-vacuum)

## Utilisation de Delta Lake dans Databricks

Databricks prend en charge en natif Delta Lake et peut exécuter des requêtes à l'aide de Python, R, Scala et SQL.

1. Vous devez d'abord créer un répertoire pour stocker les fichiers delta et noter le chemin d'accès à ce répertoire.
2. Lisez votre fichier de données, puis écrivez-le au format "delta" et enregistrez-le dans le répertoire créé ci-dessus.
```
# lire le fichier de données
testData = spark.read.format('json').options(header='true', inferSchema='true', multiline='true').load('/mnt/public-data/incoming/covid_tracking.json')

# écrire au format delta
testData.write.format("delta").mode("overwrite").save("/mnt/public-data/delta")
```
3. Facultatif (**pas une bonne pratique**) : créez une table SQL à l'aide de delta:
```
spark.sql("CREATE TABLE sample_table USING DELTA LOCATION '/mnt/public-data/delta/'")
```
4. Vous pouvez maintenant exécuter des requêtes SQL sur votre table delta, y compris des requêtes par numéro de version ou horodatage pour "voyager dans le temps" vers les versions précédentes de vos données. **Si vous avez créé une table à l'étape 3**, vous pouvez exécuter des requêtes en utilisant le nom de la table. **Sinon (meilleure pratique)**, à la place du nom de la table, vous pouvez utiliser *delta.\`{delta_table_path}\`* (remplacez {delta_table_path} par le chemin réel).
```
%sql
SELECT * FROM sample_table VERSION AS OF 0

SELECT * FROM delta.`/mnt/public-data/delta/`
```

### Documentation Microsoft
- [Démarrage rapide du Delta Lake](https://docs.microsoft.com/fr-ca/azure/databricks/delta/quick-start)

## Utilisation de Delta dans Azure Synapse

Delta Lake est compatible avec Azure Synapse. Les tables delta peuvent être créées et interrogées dans les blocs-notes Synapse de la même manière que Databricks, avec la prise en charge du langage pour PySpark, Scala et .NET (C#). Notez que SQL n'est *pas* pris en charge avec la version actuelle.

1. Lisez votre fichier de données.
```
data = spark.read.format('csv').options(header='true', inferSchema='true', multiline='true').load('abfss://public-data@statsconviddsinternal.dfs.core.windows.net/incoming/data_duplicate.csv')
```
2. Écrivez au format delta et enregistrez dans votre répertoire de table delta.
```
data.write.format("delta").save(delta_table_path)
```
3. Facultatif : créez une table SQL à l'aide de delta (requis uniquement si vous souhaitez exécuter des requêtes SQL, **pas nécessaire si vous utilisez uniquement Python, Scala ou C#**).
```
spark.sql("CREATE TABLE example USING DELTA LOCATION '{0}'".format(delta_table_path))
```
4. Vous pouvez maintenant exécuter des requêtes sur vos données.

### Documentation Microsoft
- [Travailler avec Delta Lake](https://docs.microsoft.com/fr-ca/azure/synapse-analytics/spark/apache-spark-delta-lake-overview?pivots=programming-language-python)

## Utilisation de Delta Lake dans Data Factory

Vous pouvez utiliser Azure Data Factory pour copier des données vers et depuis un Delta Lake stocké dans Azure Data Lake.

### Exemple : copier des données dans Delta Lake
1. Créez un nouveau flux de données et ajoutez une source.
2. Sous l'onglet **Paramètres source**, ajoutez l'ensemble de données à partir duquel vous souhaitez copier. Configurez tous les autres paramètres pertinents.
3. Cliquez sur le bouton plus à droite de votre source et ajoutez un récepteur.
4. Sous l'onglet **Récepteur**, choisissez **En ligne** comme type de récepteur et **Delta** comme type de jeu de données en ligne.
5. Sous l'onglet **Paramètres**, définissez le **chemin du dossier** (le chemin vers lequel vos fichiers delta seront stockés).

### Documentation Microsoft
- [Format Delta dans Azure Data Factory](https://docs.microsoft.com/fr-ca/azure/data-factory/format-delta)

## Utilisation de Delta avec Power BI

Pour lire les tables delta de manière native dans Power BI, veuillez consulter [cette documentation sur GitHub](https://github.com/gbrueckl/PowerBI/tree/main/PowerQuery/DeltaLake).

## Delta dans Azure Machine Learning

Le Delta Lake n'est actuellement pas pris en charge dans Azure ML.

# Changer la langue d'affichage
Voir la page [Langue](Langue.md) pour savoir comment changer la langue d'affichage.