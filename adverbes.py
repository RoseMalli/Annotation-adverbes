import sys
import re
import nltk

phrases_tmp = []

def split_(fichier):
    with open(fichier, 'r') as fichier_txt:
        lignes = fichier_txt.readlines()
        for ligne in lignes:
            res = re.split("(?<=[.!?])+\s+(?=[A-Z])", ligne)
            for i in res:
                phrases_tmp.append(i)
    fichier_txt.close()

autres_adverbes = []
with open('autres_adverbes.txt', 'r') as fichier_adv:
    lignes = fichier_adv.readlines()
    for ligne in lignes:
        autres_adverbes.append(ligne[:-1])
        autres_adverbes.append(ligne[:1].upper() + ligne[1:-1])
        autres_adverbes.append(ligne[:-1].upper())


tmp_ = ["le", "la", "les", 
	    "un", "une", "des", 
        "mon", "ma", "mes", 
        "ton", "ta", "tes", 
        "son", "sa", "ses", 
        "notre", "nos",
        "votre", "vos",
        "leur", "leurs", 
        "ce", "cette", "ces", "cet",
        "aucun", "aucuns", "aucune", "aucunes", 
        "certain", "certains", "certaine", "certaines", 
        "autre", "autres", 
        "de", "du",
        "en", "au", "aux",
        "avec", "qui", "’"]

tmp1_ = ["je", "tu", "il", "elle", "on", "nous", "vous", "ils", "elles"]

determinants_adjectifs_prepositions = []
pronoms = []

for x in tmp_:
    determinants_adjectifs_prepositions.append(x)
    determinants_adjectifs_prepositions.append(x[:1].upper() + x[1:])
    determinants_adjectifs_prepositions.append(x.upper())

for x in tmp1_:
    pronoms.append(x)
    pronoms.append(x[:1].upper() + x[1:])
    pronoms.append(x.upper())


adverbes_terminaisons = ["ement", "emment", "ément", "amment", "iment", "ument", "ûment"]

def adverbes_(phrase):
    for i in range(len(phrase)):
        for j in range(len(adverbes_terminaisons)):
            if phrase[i].endswith(adverbes_terminaisons[j]) and phrase[i-1] not in determinants_adjectifs_prepositions and phrase[i-1] not in pronoms and not (phrase[i].startswith(tuple([x for x in ["L'", "l'", "D'", "d'"]]))):
                phrase[i] = "<adverbe>" + phrase[i] + "</adverbe>"
        for autre_adverbe in autres_adverbes:
            if autre_adverbe == phrase[i]:
                phrase[i] = "<adverbe>" + phrase[i] + "</adverbe>"
    return ' '.join(phrase)

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Réssayer à nouveau")
    fichier = sys.argv[1]
    split_(fichier)
    phrases = []
    nouvelles_phrases = []
    for i in phrases_tmp:
        if i != '\n':
            phrases.append(i)
    for phrase in phrases:
        res = nltk.word_tokenize(phrase)
        nouvelles_phrases.append(adverbes_(res))
    with open(fichier[0:-3] + "xml", 'w') as fichier_xml:
        fichier_xml.write("<?xml version = \"1.0\" encoding = \"UTF-8\" ?>\n<?xml-stylesheet href = \" " + fichier[0:-3] + "xsl\"")
        fichier_xml.write(" type = \"text/xsl\"?>\n\n")
        fichier_xml.write("<phrases>\n")
        for i in nouvelles_phrases:
            fichier_xml.write("\n<phrase>" + str(i) + "</phrase>\n")
        fichier_xml.write("</phrases>\n")
    fichier_xml.close()

    with open(fichier[0:-3] + "xsl", "w") as fichier_xsl:
        fichier_xsl.write("<?xml version = \"1.0\" encoding = \"UTF-8\"?>\n<xsl:stylesheet version = \"1.0\" xmlns:xsl = \"http://www.w3.org/1999/XSL/Transform\">\n<xsl:output method = \"html\" version = \"4.01\" encoding = \"UTF-8\" doctype-public = \"-//W3C//DTD HTML 4.01//EN\" doctype-system = \"http://www.w3.org/TR/html4/strict.dtd\"/>")
        fichier_xsl.write("\n\n<xsl:template match =\"/\"> \n<html lang = \"fr\">\n<head>\n<title> Projet : Annotation les adverbes </title> \n</head>\n<body>\n<h2>Voici les adverbes présents dans \"" + fichier[0:-4].replace("_", " ") + "\"</h2>\n")
        fichier_xsl.write("<h4><p> Il y a <xsl:value-of select = \"count(//adverbe)\"/> adverbes. Voici ces adverbes : </p></h4>\n<xsl:for-each select = \"//adverbe\">\n<ul> <xsl:value-of select = \".\"/> </ul>\n</xsl:for-each>\n</body>\n</html>\n</xsl:template>\n</xsl:stylesheet>")
    fichier_xsl.close()
