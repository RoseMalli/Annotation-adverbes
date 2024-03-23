<?xml version = "1.0" encoding = "UTF-8"?>
<xsl:stylesheet version = "1.0" xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">
<xsl:output method = "html" version = "4.01" encoding = "UTF-8" doctype-public = "-//W3C//DTD HTML 4.01//EN" doctype-system = "http://www.w3.org/TR/html4/strict.dtd"/>

<xsl:template match ="/"> 
<html lang = "fr">
<head>
<title> Projet : Annotation les adverbes </title> 
</head>
<body>
<h2>Voici les adverbes présents dans "Cendrillon"</h2>
<h4><p> Il y a <xsl:value-of select = "count(//adverbe)"/> adverbes. Voici ces adverbes : </p></h4>
<xsl:for-each select = "//adverbe">
<ul> <xsl:value-of select = "."/> </ul>
</xsl:for-each>
</body>
</html>
</xsl:template>
</xsl:stylesheet>