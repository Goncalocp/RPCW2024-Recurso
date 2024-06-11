import json
import ast

f = open("dataset.json")
bd = json.load(f)
f.close()

def parse_name(name):
    return name.replace('(', "_").replace(')', "_").replace(' ', "_").replace("'","").replace('"',"")

ttl_parts = ['''@prefix : <http://rpcw.di.uminho.pt/2024/untitled-ontology-34/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/untitled-ontology-34/> .

<http://rpcw.di.uminho.pt/2024/untitled-ontology-34> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#hasAuthor
:hasAuthor rdf:type owl:ObjectProperty ;
           rdfs:domain :Book ;
           rdfs:range :Author .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#hasAward
:hasAward rdf:type owl:ObjectProperty ;
          rdfs:domain :Book ;
          rdfs:range :Award .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#hasCharacter
:hasCharacter rdf:type owl:ObjectProperty ;
              rdfs:domain :Book ;
              rdfs:range :Character .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#hasGenre
:hasGenre rdf:type owl:ObjectProperty ;
          rdfs:domain :Book ;
          rdfs:range :Genre .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#hasPublisher
:hasPublisher rdf:type owl:ObjectProperty ;
              rdfs:domain :Book ;
              rdfs:range :Publisher .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#hasRating
:hasRating rdf:type owl:ObjectProperty ;
           rdfs:domain :Book ;
           rdfs:range :Rating .


#################################################################
#    Data properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#bbeScore
:bbeScore rdf:type owl:DatatypeProperty ;
          rdfs:domain :Book ;
          rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#bbeVotes
:bbeVotes rdf:type owl:DatatypeProperty ;
          rdfs:domain :Book ;
          rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#bookId
:bookId rdf:type owl:DatatypeProperty ;
        rdfs:domain :Book ;
        rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#bookformat
:bookformat rdf:type owl:DatatypeProperty ;
            rdfs:domain :Book ;
            rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#coverImg
:coverImg rdf:type owl:DatatypeProperty ;
          rdfs:domain :Book ;
          rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#description
:description rdf:type owl:DatatypeProperty ;
             rdfs:domain :Book ;
             rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#firstPublishDate
:firstPublishDate rdf:type owl:DatatypeProperty ;
                  rdfs:domain :Book ;
                  rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#fiveStarRating
:fiveStarRating rdf:type owl:DatatypeProperty ;
                rdfs:domain :Rating ;
                rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#fourStarRating
:fourStarRating rdf:type owl:DatatypeProperty ;
                rdfs:domain :Rating ;
                rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#isbn
:isbn rdf:type owl:DatatypeProperty ;
      rdfs:domain :Book ;
      rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#language
:language rdf:type owl:DatatypeProperty ;
          rdfs:domain :Book ;
          rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#likedPercent
:likedPercent rdf:type owl:DatatypeProperty ;
              rdfs:domain :Book ;
              rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#nameAuthor
:nameAuthor rdf:type owl:DatatypeProperty ;
            rdfs:domain :Author ;
            rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#nameAward
:nameAward rdf:type owl:DatatypeProperty ;
           rdfs:domain :Award ;
           rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#nameCharacter
:nameCharacter rdf:type owl:DatatypeProperty ;
               rdfs:domain :Character ;
               rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#nameGenre
:nameGenre rdf:type owl:DatatypeProperty ;
           rdfs:domain :Genre ;
           rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#namePublisher
:namePublisher rdf:type owl:DatatypeProperty ;
               rdfs:domain :Publisher ;
               rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#numRatings
:numRatings rdf:type owl:DatatypeProperty ;
            rdfs:domain :Book ;
            rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#oneStarRating
:oneStarRating rdf:type owl:DatatypeProperty ;
               rdfs:domain :Rating ;
               rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#pages
:pages rdf:type owl:DatatypeProperty ;
       rdfs:domain :Book ;
       rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#price
:price rdf:type owl:DatatypeProperty ;
       rdfs:domain :Book ;
       rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#publishDate
:publishDate rdf:type owl:DatatypeProperty ;
             rdfs:domain :Book ;
             rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#rating
:rating rdf:type owl:DatatypeProperty ;
        rdfs:domain :Book ;
        rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#ratingStarValue
:ratingStarValue rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Rating ;
                 rdfs:range xsd:int .



###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#threeStarRating
:threeStarRating rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Rating ;
                 rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#title
:title rdf:type owl:DatatypeProperty ;
       rdfs:domain :Book ;
       rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#twoStarRating
:twoStarRating rdf:type owl:DatatypeProperty ;
               rdfs:domain :Rating ;
               rdfs:range xsd:int .


#################################################################
#    Classes
#################################################################

###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#Author
:Author rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#Award
:Award rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#Book
:Book rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#Character
:Character rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#Genre
:Genre rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#Publisher
:Publisher rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#Rating
:Rating rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################'''
]

idClassificacao = 1
genres = set()
authors = set()
publishers = set()
awards = set()

for book in bd:
    bookCharacters = []
    bookGenres = []
    ratings = []
    bookAwards = []

    for character in ast.literal_eval(book['characters']):
        character_name = parse_name(character.replace("'",""))
        bookCharacters.append(character_name)
        if character not in genres:
            genres.add(character)
            ttl_parts.append(f'''
                ###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#{character_name}
                :{character_name} rdf:type owl:NamedIndividual ,
                                        :Character ;
                                :nameCharacter "{character}" .
            ''')

    if book['publisher'] not in publishers:
        publishers.add(book['publisher'])
        ttl_parts.append(f'''
            ###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#{parse_name(book['publisher'])}
            :{parse_name(book['publisher'])} rdf:type owl:NamedIndividual ,
                                            :Publisher ;
                                    :namePublisher "{book['publisher']}" .
        ''')

    if book['author'].replace(",","") not in authors:
        authors.add(book['author'].replace(",",""))
        ttl_parts.append(f'''
            ###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#{parse_name(book['author'])}
            :{parse_name(book['author'])} rdf:type owl:NamedIndividual ,
                                            :Author ;
                                    :nameAuthor "{book['author'].replace(",","")}" .
        ''')

    for genre in ast.literal_eval(book['genres']):
        genre_name = parse_name(genre.replace("'",""))
        bookGenres.append(genre_name)
        if genre.replace("'","") not in genres:
            genres.add(genre.replace("'",""))
            ttl_parts.append(f'''
                ###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#{genre_name}
                :{genre_name} rdf:type owl:NamedIndividual ,
                                :Genre ;
                        :nameGenre "{genre}" .
            ''')

    for rating in ast.literal_eval(book['ratingsByStars']):
        ratings.append(rating)

    for award in ast.literal_eval(book['awards']):
        award_name = parse_name(award.replace("'",""))
        bookAwards.append(award_name)
        if award.replace("'","") not in publishers:
            awards.add(award.replace("'",""))
            ttl_parts.append(f'''
                ###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#{award_name}
                <http://rpcw.di.uminho.pt/2024/untitled-ontology-34#{award_name}> rdf:type owl:NamedIndividual ,
                                                                                           :Award ;
                                                                                  :nameAward "{award}" .
            ''')

    ttl_parts.append(f'''
        ###  http://rpcw.di.uminho.pt/2024/untitled-ontology-34#{book['bookId']}
        <http://rpcw.di.uminho.pt/2024/untitled-ontology-34#{book['bookId']}> rdf:type owl:NamedIndividual ,
                                                                                   :Book ;
                                                                          :hasAuthor :{parse_name(book["author"].replace(",",""))} ;         
                                                                          :hasPublisher :{parse_name(book["publisher"])} ;
                                                                          :hasRating :classificacao{idClassificacao} ;
                                                                          :bbeScore "{book["bbeScore"]}"^^xsd:int ;
                                                                          :bbeVotes "{book["bbeVotes"]}"^^xsd:int ;
                                                                          :bookId "{book["bookId"]}" ;
                                                                          :bookformat "{book["bookFormat"]}" ;
                                                                          :coverImg "{book["coverImg"]}" ;
                                                                          :description "{book["description"].replace('(','').replace(')','').replace("'","").replace('"',"")}" ;
                                                                          :firstPublishDate "{book["firstPublishDate"]}" ;
                                                                          :isbn "{book["isbn"]}" ;
                                                                          :language "{book["language"]}" ;
                                                                          :likedPercent "{book["likedPercent"]}"^^xsd:int ;
                                                                          :numRatings "{book["numRatings"]}"^^xsd:int ;
                                                                          :pages "{book["pages"]}"^^xsd:int ;
                                                                          :price "{book["price"]}" ;
                                                                          :publishDate "{book["publishDate"]}" ;
                                                                          :title "{book["title"]}" ;
                                                                          :hasAward 
    ''')

    for award in bookAwards:
        ttl_parts.append(f'<http://rpcw.di.uminho.pt/2024/untitled-ontology-34#{award}> ,\n')

    ttl_parts = ttl_parts[:-2]
    ttl_parts.append(';\n:hasGenre ')


    for genre in bookGenres:
        ttl_parts.append(f':{genre} ,\n')
    
 
    ttl_parts = ttl_parts[:-2]
    ttl_parts.append(';\n:hasCharacter ')

    for character in bookCharacters:
        name = character.replace('"',"").replace("'","")
        ttl_parts.append(f':{name} ,\n')
    ttl_parts = ttl_parts[:-2]
    ttl_parts.append('.\n')
    idClassificacao += 1

ttl = "\n".join(ttl_parts)
print(ttl)
