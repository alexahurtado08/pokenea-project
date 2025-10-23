import random

POKENEAS = [
    {
        "id": 1,
        "nombre": "Arequipeon",
        "altura": 1.2,
        "habilidad": "Dulzura letal",
        "imagen": "https://<tu-bucket>.s3.amazonaws.com/arequipeon.png",
        "frase": "El amor se cocina a fuego lento, como un buen arequipe."
    },
    {
        "id": 2,
        "nombre": "Montañaurio",
        "altura": 2.1,
        "habilidad": "Resistencia paisa",
        "imagen": "https://<tu-bucket>.s3.amazonaws.com/montanaurio.png",
        "frase": "Sube la montaña y verás la vida desde arriba."
    },
    {
        "id": 3,
        "nombre": "Cafesaurio",
        "altura": 1.4,
        "habilidad": "Energía infinita",
        "imagen": "https://<tu-bucket>.s3.amazonaws.com/cafesaurio.png",
        "frase": "El café es la chispa que enciende mis mañanas."
    },
    {
        "id": 4,
        "nombre": "Guarabeast",
        "altura": 1.7,
        "habilidad": "Sabrosura mágica",
        "imagen": "https://<tu-bucket>.s3.amazonaws.com/guarabeast.png",
        "frase": "Con un buen guaro, hasta los problemas bailan."
    },
    {
        "id": 5,
        "nombre": "Sombrerónix",
        "altura": 1.5,
        "habilidad": "Estilo ancestral",
        "imagen": "https://<tu-bucket>.s3.amazonaws.com/sombreronix.png",
        "frase": "Donde va el sombrerón, va la elegancia paisa."
    },
    {
        "id": 6,
        "nombre": "Silletron",
        "altura": 1.8,
        "habilidad": "Fuerza floral",
        "imagen": "https://<tu-bucket>.s3.amazonaws.com/silletron.png",
        "frase": "Llevar flores es un arte que pesa, pero enorgullece."
    },
    {
        "id": 7,
        "nombre": "Arepachu",
        "altura": 0.8,
        "habilidad": "Transformación dorada",
        "imagen": "https://<tu-bucket>.s3.amazonaws.com/arepachu.png",
        "frase": "Nadie se resiste a una arepita caliente."
    },
    {
        "id": 8,
        "nombre": "Cocornix",
        "altura": 1.1,
        "habilidad": "Camuflaje montañero",
        "imagen": "https://<tu-bucket>.s3.amazonaws.com/cocornix.png",
        "frase": "Donde hay niebla, hay misterio."
    },
    {
        "id": 9,
        "nombre": "Tamalion",
        "altura": 1.3,
        "habilidad": "Protección envolvente",
        "imagen": "https://<tu-bucket>.s3.amazonaws.com/tamalion.png",
        "frase": "No hay problema que un buen tamal no envuelva."
    },
    {
        "id": 10,
        "nombre": "Antioquemon",
        "altura": 2.0,
        "habilidad": "Orgullo paisa",
        "imagen": "https://<tu-bucket>.s3.amazonaws.com/antioquemon.png",
        "frase": "Soy de Antioquia, tierra de gente verraca."
    }
]

def random_pokenea():
    return random.choice(POKENEAS)