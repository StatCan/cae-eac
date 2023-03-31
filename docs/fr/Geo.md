# Environnement dâ€™analyse gÃ©ospatial (EGA) - AccÃ¨s multiplateforme

??? danger Â«Â DonnÃ©es non protÃ©gÃ©es uniquement; SSI Ã  venir bientÃ´t:Â Â»
	Ã€ lâ€™heure actuelle, notre serveur gÃ©ospatial ne peut hÃ©berger et fournir un accÃ¨s quâ€™Ã  des informations statistiques non sensibles. 
	
## Mise en route

??? succÃ¨s Â« PrÃ©requis Â»
	1. Un projet intÃ©grÃ© avec accÃ¨s Ã  DAS GAE ArcGIS Portal 	
	2. Un id client ArcGIS Portal (clÃ© API)

ArcGIS Enterprise Portal est accessible dans AAW ou CAE Ã  lâ€™aide de lâ€™API, Ã  partir de nâ€™importe quel service qui exploite le langage de programmation Python. 

Par exemple, dans AAW et lâ€™utilisation de [Jupyter Notebooks](https://statcan.github.io/daaas/en/1-Experiments/Jupyter/) dans lâ€™espace, ou dans CAE lâ€™utilisation de [Databricks](https://statcan.github.io/cae-eac/en/DataBricks/), DataFactory, etc.

[Le portail Das GAE ArcGIS Enterprise est accessible directement ici] (https://geoanalytics.cloud.statcan.ca/portal)

[Pour obtenir de lâ€™aide sur lâ€™auto-inscription en tant quâ€™utilisateur du portail gÃ©ospatial DAS] (https://statcan.github.io/daaas-dads-geo/english/portal/)

<hr>

## Utilisation dâ€™ArcGIS API for Python

### Connexion Ã  ArcGIS Enterprise Portal Ã  lâ€™aide de lâ€™API ArcGIS

1. Installer les packages :

	```python
	conda install -c esri arcgis
	```

	ou en utilisant Artifactory

	```python3333
	conda install -c https://jfrog.aaw.cloud.statcan.ca/artifactory/api/conda/esri-remote arcgis
	```

2. Importez les bibliothÃ¨ques nÃ©cessaires dont vous aurez besoin dans le Bloc-notes.
	```python
	from arcgis.gis import GIS
	from arcgis.gis import Item
	```
	
3. AccÃ©der au portail
	Votre groupe de projet recevra un ID client lors de lâ€™intÃ©gration. Collez lâ€™ID client entre les guillemets ```client_id='######'```. 
	
	```python
	gis = GIS("https://geoanalytics.cloud.statcan.ca/portal", client_id=' ')
	print("Successfully logged in as: " + gis.properties.user.username)
	```

4. - Le rÃ©sultats vous redirigera vers un portail de connexion.
	- Utilisez lâ€™option connexion Azure de StatCan et votre ID cloud 
	- AprÃ¨s une connexion rÃ©ussie, vous recevrez un code pour vous connecter Ã  lâ€™aide de SAML. 
	- Collez ce code dans le rÃ©sultat. 

	![OAuth2 Approval](images/OAuth2Key.png)

<hr>

### Afficher les informations de lâ€™utilisateur
En utilisant la fonction Â«Â me Â», nous pouvons afficher diverses informations sur lâ€™utilisateur connectÃ©.
```python
me = gis.users.me
username = me.username
description = me.description
display(me)
```

<hr>

### Recherche de contenu
Recherchez le contenu que vous avez hÃ©bergÃ© sur le portail gÃ©ographique DAaaS. En utilisant la fonction Â«Â meÂ Â», nous pouvons rechercher tout le contenu hÃ©bergÃ© sur le compte. Il existe plusieurs faÃ§ons de rechercher du contenu. Deux mÃ©thodes diffÃ©rentes sont dÃ©crites ci-dessous.

**Rechercher tous vos itmes hÃ©bergÃ©s dans le portail gÃ©ographique DAaaS.**
```python
my_content = me.items()
my_content
```
**Recherchez le contenu spÃ©cifique que vous possÃ©dez dans le portail gÃ©ographique DAaaS.**

Ceci est similaire Ã  lâ€™exemple ci-dessus, mais si vous connaissez le titre de la couche quâ€™ils souhaitez utiliser, vous pouvez lâ€™enregistrer en tant que fonction.
```python
my_items = me.items()
for items in my_items:
    print(items.title, " | ", items.type)
    if items.title == "Flood in Sorel-Tracy":
        flood_item = items
        
    else:
        continue
print(flood_item)
```

**Recherchez tout le contenu auquel vous avez accÃ¨s, pas seulement le vÃ´tre.**

```python
flood_item = gis.content.search("tags: flood", item_type ="Feature Service")
flood_item
```

<hr>

### Obtenir du contenu
Nous devons obtenir lâ€™Ã©lÃ©ment du portail gÃ©ographique DAaaS afin de lâ€™utiliser dans le bloc-notes Jupyter. Pour ce faire, vous fournissez le numÃ©ro dâ€™identification unique de lâ€™Ã©lÃ©ment que vous souhaitez utiliser. Trois exemples sont dÃ©crits ci-dessous, tous accÃ©dant Ã  la couche identique.
```python
item1 = gis.content.get(my_content[5].id) #from searching your content above
display(item1)

item2 = gis.content.get(flood_item.id) #from example above -searching for specific content
display(item2)

item3 = gis.content.get('edebfe03764b497f90cda5f0bfe727e2') #the actual content id number
display(item3)
```

<hr>

### Effectuer une analyse
Une fois les couches introduites dans le bloc-notes Jupyter, nous sommes en mesure dâ€™effectuer des types dâ€™analyse similaires que vous vous attendez Ã  trouver dans un logiciel SIG tel quâ€™ArcGIS. Il existe de nombreux modules contenant de nombreux sous-modules dont peuvent effectuer plusieurs types dâ€™analyses.
<br/>

Ã€ lâ€™aide du module arcgis.features, importez le sous-module use_proximity ```from arcgis.features import use_proximity```. Ce sous-module nous permet de '.create_buffers' - zones de distance Ã©gale par rapport aux entitÃ©s. Ici, nous spÃ©cifions la couche que nous voulons utiliser, la distance, les unitÃ©s et le nom en sortie (vous pouvez Ã©galement spÃ©cifier dâ€™autres caractÃ©ristiques telles que le champ, le type dâ€™anneau, le type dâ€™extrÃ©mitÃ© et autres). En spÃ©cifiant un nom en sortie, aprÃ¨s avoir exÃ©cutÃ© la commande de zone tampon, une nouvelle couche sera automatiquement tÃ©lÃ©chargÃ©e dans le portail GEO DAaaS contenant la nouvelle fonctionnalitÃ© que vous venez de crÃ©er.
<br/>

```python
buffer_lyr = use_proximity.create_buffers(item1, distances=[1], 
                                          units = "Kilometers", 
                                          output_name='item1_buffer')

display(item1_buffer)
```

Certains utilisateurs prÃ©fÃ¨rent travailler avec des packages Open Source.  La traduction dâ€™ArcGIS vers spatial Dataframes est simple.
```python
# create a Spatially Enabled DataFrame object
sdf = pd.DataFrame.spatial.from_layer(feature_layer)
```

<hr>

### Mettre Ã  jour les Ã©lÃ©ments
En obtenant lâ€™Ã©lÃ©ment comme nous lâ€™avons fait similaire Ã  lâ€™exemple ci-dessus, nous pouvons utiliser la fonction Â«Â .updateÂ Â» pour mettre Ã  jour lâ€™Ã©lÃ©ment existant dans le portail DAaaS GEO. Nous pouvons mettre Ã  jour les propriÃ©tÃ©s des Ã©lÃ©ments, les donnÃ©es, les vignettes et les mÃ©tadonnÃ©es.
```python
item1_buffer = gis.content.get('c60c7e57bdb846dnbd7c8226c80414d2')
item1_buffer.update(item_properties={'title': 'Enter Title'
									 'tags': 'tag1, tag2, tag3, tag4',
                                     'description': 'Enter description of item'}
```

<hr>

### Visualisez vos donnÃ©es sur une carte interactive

**Exemple : BibliothÃ¨que MatplotLib**
Dans le code ci-dessous, nous crÃ©ons un objet ax, qui est un tracÃ© de style carte. Nous traÃ§ons ensuite notre colonne de changement de donnÃ©es (Â«Â Changement de populationÂ Â») sur les axes
```python
import matplotlib.pyplot as plt
ax = sdf.boundary.plot(figsize=(10, 5))
shape.plot(ax=ax, column='Population Change', legend=True)
plt.show()
```

**Exemple : bibliothÃ¨que ipyleaflet**
Dans cet exemple, nous utiliserons la bibliothÃ¨que 'ipyleaflet' pour crÃ©er une carte interactive. Cette carte sera centrÃ©e autour de Toronto, en Ontario. Les donnÃ©es utilisÃ©es seront dÃ©crites ci-dessous.
Commencez par coller ```conda install -c conda-forge ipyleaflet``` vous permettant dâ€™installer des bibliothÃ¨ques ipyleaflet dans lâ€™environnement Python.
<br/>
Importez les bibliothÃ¨ques nÃ©cessaires.
```python
import ipyleaflet 
from ipyleaflet import *
```
Maintenant que nous avons importÃ© le module ipyleaflet, nous pouvons crÃ©er une carte simple en spÃ©cifiant la latitude et la longitude de lâ€™emplacement que nous voulons, le niveau de zoom et le fond de carte [(plus de fonds de carte)](https://ipyleaflet.readthedocs.io/en/latest/map_and_basemaps/basemaps.html). Des contrÃ´les supplÃ©mentaires ont Ã©tÃ© ajoutÃ©s, tels que des couches et des mises Ã  lâ€™Ã©chelle.
```python
toronto_map = Map(center=[43.69, -79.35], zoom=11, basemap=basemaps.Esri.WorldStreetMap)

toronto_map.add_control(LayersControl(position='topright'))
toronto_map.add_control(ScaleControl(position='bottomleft'))
toronto_map
```
<br/>

##Learn En savoir plus sur ArcGIS API for Python
[La documentation complÃ¨te de lâ€™API ArGIS peut Ãªtre trouvÃ©e ici] (https://developers.arcgis.com/python/)

##Learn En savoir plus sur lâ€™environnement analytique gÃ©ospatial (EGA) et les services du DAS
[Guide dâ€™aide du GAE] (https://statcan.github.io/daaas-dads-geo/)