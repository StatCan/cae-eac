# R-Shiny à partir de RStudio
Le document décrit comment accéder à R-Shiny à partir de l'application Rstudio.

## Commencer

Veuillez s'il vous plaît envoyer un message [Slack](https://cae-eac.slack.com) à l'équipe CAE pour activer RStudio dans le cluster de databricks afin d'utiliser R-Shiny.

**Avertissement**: 
Les clusters R-Shiny s'eteignent tous les jours à 19h. Pour faire des économies, veuillez s'il vous plaît arrêter vos clusters R-Shiny lorsque vous ne les utilisez pas.

## Accès à R-Shiny

1.	À partir du portail Azure, Lancer l'espace de travail Databricks créé pour vous.
2.	Cliquez sur **Clusters**.
 

3. À partir de la liste de clusters disponibles, selectionnez le cluster sur lequel RStudio a été installé.

 
    **Note:** Le cluster doit être actif pour pouvoir acceder à l'application RStudio. Consulter la [section Databricks](../DataBricks/DataBricks.md) pour plus de détails sur comment démarrer un cluster.


4.	Selectionnez l'onglet **Apps**.



5.	Cliquez sur **Set up RStudio**.
 

    **Note**: Un **mot de passe à usage unique** est généré pour vous, cliquez sur **show** pour l'afficher et le copier. Vous devez vous connecter en utilisant le nom d'utilisateur et le mot de passe fournis.
 
6.	Cliquez sur **Open RStudio**.

 
7.	Une nouvelle fenêtre s'ouvre, entrez le nom d'utilisateur et le mot de passe fournis dans le formulaire de connexion afin de démarrer RStudio.
 

 
8.	À partir de l'interface RStudio, entrez la commande **library(shiny)** dans la console afin d'importer la librarie Shiny.


## Exemple d'une application R-Shiny

Nous utiliserons l'exemple **Hello Shiny** pour explorer la structure d'une application Shiny.

1. Lancer l'application à partir de votre session RStudio en entrant les commandes:

    library(shiny)

    runExample("01_hello")

2.	Votre application devrait correspondre à l'image ci-dessous. 


