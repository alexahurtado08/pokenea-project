import random

POKENEAS = [
    {
        "id": 1,
        "nombre": "Arequipeon",
        "altura": 1.2,
        "habilidad": "Dulzura letal",
        "imagen": "https://pokenea-alexa-2025.s3.us-east-1.amazonaws.com/arequipon.png",
        "frase": "El amor se cocina a fuego lento, como un buen arequipe."
    },
    {
        "id": 2,
        "nombre": "Montañaurio",
        "altura": 2.1,
        "habilidad": "Resistencia paisa",
        "imagen": "https://pokenea-alexa-2025.s3.us-east-1.amazonaws.com/monta%C3%B1aurio.png",
        "frase": "Sube la montaña y verás la vida desde arriba."
    },
    {
        "id": 3,
        "nombre": "Cafesaurio",
        "altura": 1.4,
        "habilidad": "Energía infinita",
        "imagen": "https://pokenea-alexa-2025.s3.us-east-1.amazonaws.com/cafesaurio.png",
        "frase": "El café es la chispa que enciende mis mañanas."
    },
    {
        "id": 4,
        "nombre": "Guarabeast",
        "altura": 1.7,
        "habilidad": "Sabrosura mágica",
        "imagen": "https://pokenea-alexa-2025.s3.us-east-1.amazonaws.com/guarobeast.png",
        "frase": "Con un buen guaro, hasta los problemas bailan."
    },
    {
        "id": 5,
        "nombre": "Sombrerónix",
        "altura": 1.5,
        "habilidad": "Estilo ancestral",
        "imagen": "https://pokenea-alexa-2025.s3.us-east-1.amazonaws.com/sombreronix.png",
        "frase": "Donde va el sombrerón, va la elegancia paisa."
    },
    {
        "id": 6,
        "nombre": "Silletron",
        "altura": 1.8,
        "habilidad": "Fuerza floral",
        "imagen": "https://pokenea-alexa-2025.s3.us-east-1.amazonaws.com/silletron.png",
        "frase": "Llevar flores es un arte que pesa, pero enorgullece."
    },
    {
        "id": 7,
        "nombre": "Arepachu",
        "altura": 0.8,
        "habilidad": "Transformación dorada",
        "imagen": "https://pokenea-alexa-2025.s3.us-east-1.amazonaws.com/arepachu.png",
        "frase": "Nadie se resiste a una arepita caliente."
    },
    {
        "id": 8,
        "nombre": "Cocornix",
        "altura": 1.1,
        "habilidad": "Camuflaje montañero",
        "imagen": "https://pokenea-alexa-2025.s3.us-east-1.amazonaws.com/cocornix.png",
        "frase": "Donde hay niebla, hay misterio."
    },
    {
        "id": 9,
        "nombre": "Tamalion",
        "altura": 1.3,
        "habilidad": "Protección envolvente",
        "imagen": "https://pokenea-alexa-2025.s3.us-east-1.amazonaws.com/tamalion.jpg",
        "frase": "No hay problema que un buen tamal no envuelva."
    },
    {
        "id": 10,
        "nombre": "Antioquemon",
        "altura": 2.0,
        "habilidad": "Orgullo paisa",
        "imagen": "https://pokenea-alexa-2025.s3.us-east-1.amazonaws.com/antioquemon.png",
        "frase": "Soy de Antioquia, tierra de gente verraca."
    }
]

def random_pokenea():
    return random.choice(POKENEAS)